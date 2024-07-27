import os
from PIL import Image
from PySide6.QtWidgets import QApplication, QFileDialog, QMessageBox


class FrameExtractor:
    def __init__(self, ui):
        self.ui = ui
        self.setup_connections()

    def setup_connections(self):

        self.ui.browseInput1.clicked.connect(self.select_gif)
        self.ui.browseOutput1.clicked.connect(self.select_output_folder)
        self.ui.extractor_button.clicked.connect(self.extract_frames)

    def select_gif(self):
        file_path, _ = QFileDialog.getOpenFileName(None, "Select GIF", "", "Image files (*.gif *.webp)")
        if file_path:
            self.ui.fileInput1.setText(file_path)

    def select_output_folder(self):
        folder_path = QFileDialog.getExistingDirectory(None, "Select Output Folder")
        if folder_path:
            self.ui.output_folder_entry.setText(folder_path)

    def extract_frames(self):
        gif_path = self.ui.fileInput1.text()
        output_folder = self.ui.output_folder_entry.text()
        file_type = self.ui.saveAsFormat.currentText().lower()
        generate_frame_info = self.ui.generate_infocheckBox.isChecked()

        if not gif_path or not output_folder:
            QMessageBox.critical(None, "Error", "Please select both GIF file and output folder.")
            return

        if not os.path.exists(output_folder):
            try:
                os.makedirs(output_folder)
            except OSError as e:
                QMessageBox.critical(None, "Error", f"Failed to create output folder: {e}")
                return

        existing_files = [f for f in os.listdir(output_folder) if f.startswith('frame_') and f.endswith(f'.{file_type}')]
        filecount = len(existing_files)
        if filecount > 0:
            overwrite = QMessageBox.question(None, "Overwrite Existing Files", 
                f"The output folder already contains {filecount} existing files with the same name.\n\nDo you want to overwrite these files?",
                QMessageBox.Yes | QMessageBox.No)
            if overwrite == QMessageBox.No:
                return

        try:
            with Image.open(gif_path) as img:
                self.ui.progressBar.setMaximum(img.n_frames)
                frame_info = []
                total_duration = 0

                for i in range(img.n_frames):
                    img.seek(i)
                    duration = img.info.get('duration', 0) / 1000
                    total_duration += duration
                    frame_info.append((i, duration, total_duration))

                    frame_filename = f"frame_{i:03d}_{duration:.3f}s.{file_type}"
                    frame_path = os.path.join(output_folder, frame_filename)

                    if file_type == 'gif':
                        single_frame = Image.new('RGBA', img.size)
                        single_frame.paste(img)
                        single_frame.info = img.info
                        single_frame.save(frame_path, format='GIF', save_all=True, append_images=[], duration=duration, loop=1)
                    else:
                        img.save(frame_path)

                    self.ui.progressBar.setValue(i + 1)
                    self.ui.statusbar.showMessage(f"Extracting frame {i+1} of {img.n_frames}")
                    QApplication.processEvents()

                if generate_frame_info:
                    self.generate_frame_info_file(output_folder, frame_info)

            self.ui.statusbar.showMessage("Frames extracted successfully!")
            QMessageBox.information(None, "Success", "Frames extracted successfully!")
        except Exception as e:
            self.ui.statusbar.showMessage(f"Error: {str(e)}")
            QMessageBox.critical(None, "Error", f"An error occurred: {str(e)}")
        finally:
            self.ui.progressBar.setValue(0)

    def generate_frame_info_file(self, output_folder, frame_info):
        info_file_path = os.path.join(output_folder, "frame_info.txt")
        with open(info_file_path, 'w') as f:
            f.write("Frame Information:\n")
            f.write("------------------\n")
            total_time = frame_info[-1][2]
            fps = len(frame_info) / total_time
            f.write(f"FPS: {fps:.2f}\n\n")
            for frame, duration, total_time in frame_info:
                f.write(f"Frame {frame:03d}: Duration = {duration:.3f}s, Total Time = {total_time:.3f}s\n")
