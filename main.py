import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import Image
import os
from tkinter import filedialog, messagebox

version = "0.2.0-DEV"

class ImageNexus(ttk.Window):
    def __init__(self):
        super().__init__(themename="darkly")
        self.title("ImageNexus v{}".format(version))
        self.geometry("650x400")
        self.resizable(False, False)
        # set window icon
        #self.iconbitmap("icon.ico")

        self.create_widgets()

    def create_widgets(self):
        # Create notebook (tabbed interface)
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill=BOTH, expand=YES, padx=10, pady=10)

        # Create tabs
        self.extractor_tab = ttk.Frame(self.notebook)
        self.converter_tab = ttk.Frame(self.notebook)

        self.notebook.add(self.extractor_tab, text="Frame Extractor")
        self.notebook.add(self.converter_tab, text="File Converter")

        self.create_extractor_widgets()
        self.create_converter_widgets()

    def create_extractor_widgets(self):
        main_frame = ttk.Frame(self.extractor_tab, padding="20 20 20 20")
        main_frame.pack(fill=BOTH, expand=YES)

        # GIF selection
        self.create_labeled_entry(main_frame, "Select GIF:", self.select_gif, "gif_path_entry")

        # Output folder selection
        self.create_labeled_entry(main_frame, "Output Folder:", self.select_output_folder, "output_folder_entry")

        # File type selection
        file_type_frame = ttk.Frame(main_frame)
        file_type_frame.pack(fill=X, pady=10)
        ttk.Label(file_type_frame, text="Save as:", width=15).pack(side=LEFT)
        self.file_type_var = ttk.StringVar(value="PNG")
        file_type_combo = ttk.Combobox(file_type_frame, textvariable=self.file_type_var, values=["PNG", "GIF"], width=10, state="readonly")
        file_type_combo.pack(side=LEFT, padx=(10, 0))

        # Extract button
        ttk.Button(main_frame, text="Extract Frames", command=self.extract_frames, style='success.TButton').pack(pady=20)

        # Progress bar
        self.progress = ttk.Progressbar(main_frame, length=400, mode='determinate', style='info.Horizontal.TProgressbar')
        self.progress.pack(pady=10)

        # Status label
        self.status_label = ttk.Label(main_frame, text="", font=("TkDefaultFont", 10))
        self.status_label.pack(pady=10)

    def create_converter_widgets(self):
        main_frame = ttk.Frame(self.converter_tab, padding="20 20 20 20")
        main_frame.pack(fill=BOTH, expand=YES)

        # Input file selection
        self.create_labeled_entry(main_frame, "Select Input File:", self.select_input_file, "input_file_entry")

        # Output folder selection
        self.create_labeled_entry(main_frame, "Output Folder:", self.select_output_folder_converter, "output_folder_converter_entry")

        # Input and Output format selection
        formats = ["GIF", "PNG", "JPG", "BMP", "TIFF"]
        self.create_format_selection(main_frame, "Input Format:", "input_format_var", formats)
        self.create_format_selection(main_frame, "Output Format:", "output_format_var", formats)

        # Convert button
        ttk.Button(main_frame, text="Convert File", command=self.convert_file, style='success.TButton').pack(pady=20)

        # Converter status label
        self.converter_status_label = ttk.Label(main_frame, text="", font=("TkDefaultFont", 10))
        self.converter_status_label.pack(pady=10)

    def create_labeled_entry(self, parent, label_text, command, entry_name):
        frame = ttk.Frame(parent)
        frame.pack(fill=X, pady=10)
        ttk.Label(frame, text=label_text, width=15).pack(side=LEFT)
        entry = ttk.Entry(frame, width=50)
        entry.pack(side=LEFT, expand=YES, padx=(10, 0))
        setattr(self, entry_name, entry)
        ttk.Button(frame, text="Browse", command=command, style='info.TButton').pack(side=LEFT, padx=(10, 0))

    def create_format_selection(self, parent, label_text, var_name, values):
        frame = ttk.Frame(parent)
        frame.pack(fill=X, pady=10)
        ttk.Label(frame, text=label_text, width=15).pack(side=LEFT)
        var = ttk.StringVar(value=values[0])
        setattr(self, var_name, var)
        combo = ttk.Combobox(frame, textvariable=var, values=values, width=10, state="readonly")
        combo.pack(side=LEFT, padx=(10, 0))

    def select_gif(self):
        self.select_file(self.gif_path_entry, [("GIF files", "*.gif")])

    def select_input_file(self):
        self.select_file(self.input_file_entry, [("Image files", "*.gif;*.png;*.jpg;*.jpeg;*.bmp;*.tiff")])

    def select_output_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.output_folder_entry.delete(0, END)
            self.output_folder_entry.insert(0, folder_path)

    def select_output_folder_converter(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.output_folder_converter_entry.delete(0, END)
            self.output_folder_converter_entry.insert(0, folder_path)

    def select_file(self, entry_widget, filetypes):
        file_path = filedialog.askopenfilename(filetypes=filetypes)
        if file_path:
            entry_widget.delete(0, END)
            entry_widget.insert(0, file_path)

    def extract_frames(self):
        gif_path = self.gif_path_entry.get()
        output_folder = self.output_folder_entry.get()
        file_type = self.file_type_var.get().lower()

        if not gif_path or not output_folder:
            messagebox.showerror("Error", "Please select both GIF file and output folder.")
            return

        # Check if output folder contains already processed files
        existing_files = [f for f in os.listdir(output_folder) if f.startswith('frame_') and f.endswith(f'.{file_type}')]
        filecount = len(existing_files)
        if filecount > 0:
            overwrite = messagebox.askyesno("Overwrite Existing Files", f"The output folder already contains {filecount} existing files with the same name.\n\nDo you want to overwrite these files?")
            if not overwrite:
                return

        try:
            with Image.open(gif_path) as img:
                self.progress['maximum'] = img.n_frames
                frame_info = []
                total_duration = 0

                for i in range(img.n_frames):
                    img.seek(i)
                    duration = img.info.get('duration', 0) / 1000  # Convert to seconds
                    total_duration += duration
                    frame_info.append((i, duration, total_duration))

                    # Save frame with duration info in filename
                    frame_filename = f"frame_{i:03d}_{duration:.3f}s.{file_type}"
                    frame_path = os.path.join(output_folder, frame_filename)

                    if file_type == 'gif':
                        # For GIF, we need to create a new single-frame GIF
                        single_frame = Image.new('RGBA', img.size)
                        single_frame.paste(img)
                        single_frame.info = img.info
                        single_frame.save(frame_path, format='GIF', save_all=True, append_images=[], duration=duration, loop=1)
                    else:
                        img.save(frame_path)

                    self.progress['value'] = i + 1
                    self.status_label['text'] = f"Extracting frame {i+1} of {img.n_frames}"
                    self.update_idletasks()

                # Generate frame info text file
                self.generate_frame_info_file(output_folder, frame_info)

            self.status_label['text'] = "Frames extracted successfully!"
            messagebox.showinfo("Success", "Frames extracted successfully!")
        except Exception as e:
            self.status_label['text'] = f"Error: {str(e)}"
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
        finally:
            self.progress['value'] = 0

    def generate_frame_info_file(self, output_folder, frame_info):
        info_file_path = os.path.join(output_folder, "frame_info.txt")
        with open(info_file_path, 'w') as f:
            f.write("Frame Information:\n")
            f.write("------------------\n")
            total_time = frame_info[-1][2] # Get the total duration from the last frame
            fps = len(frame_info) / total_time
            f.write(f"FPS: {fps:.2f}\n\n")
            for frame, duration, total_time in frame_info:
                f.write(f"Frame {frame:03d}: Duration = {duration:.3f}s, Total Time = {total_time:.3f}s\n")

    def convert_file(self):
        input_path = self.input_file_entry.get()
        output_folder = self.output_folder_converter_entry.get()
        input_format = self.input_format_var.get().lower()
        output_format = self.output_format_var.get().lower()

        if not input_path or not output_folder:
            messagebox.showerror("Error", "Please select both input file and output folder.")
            return

        # generate output filename
        input_filename = os.path.basename(input_path)
        output_filename = os.path.splitext(input_filename)[0] + f".{output_format}"
        output_path = os.path.join(output_folder, output_filename)

        # Check if output file already exists
        if os.path.isfile(output_path):
            overwrite = messagebox.askyesno("Overwrite Existing File", f"An existing file with the same name already exists.\n\nDo you want to overwrite it?")
            if not overwrite:
                return

        try:
            with Image.open(input_path) as img:
                if input_format == 'gif' and output_format != 'gif':
                    # If converting from GIF to non-GIF, use only the first frame
                    img.seek(0)

                # Generate output filename
                input_filename = os.path.basename(input_path)
                output_filename = os.path.splitext(input_filename)[0] + f".{output_format}"
                output_path = os.path.join(output_folder, output_filename)

                img.save(output_path, format=output_format)

            self.converter_status_label['text'] = "File converted successfully!"
            messagebox.showinfo("Success", "File converted successfully!")
        except Exception as e:
            self.converter_status_label['text'] = f"Error: {str(e)}"
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    app = ImageNexus()
    app.mainloop()