import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import Image
import os
from tkinter import filedialog, messagebox

version = "0.1.0-DEV"

class extractFrames(ttk.Window):
    def __init__(self):
        super().__init__(themename="darkly")
        self.title("extractFrames v{}".format(version))
        self.geometry("600x350")
        self.resizable(False, False)
    # set window icon
        #self.iconbitmap("icon.ico")

        self.create_widgets()

    def create_widgets(self):
        main_frame = ttk.Frame(self, padding="20 20 20 20")
        main_frame.pack(fill=BOTH, expand=YES)

        # GIF selection
        gif_frame = ttk.Frame(main_frame)
        gif_frame.pack(fill=X, pady=10)
        ttk.Label(gif_frame, text="Select GIF:").pack(side=LEFT)
        self.gif_path_entry = ttk.Entry(gif_frame, width=50)
        self.gif_path_entry.pack(side=LEFT, expand=YES, padx=(10, 0))
        ttk.Button(gif_frame, text="Browse", command=self.select_gif, style='info.TButton').pack(side=LEFT, padx=(10, 0))

        # Output folder selection
        output_frame = ttk.Frame(main_frame)
        output_frame.pack(fill=X, pady=10)
        ttk.Label(output_frame, text="Output Folder:").pack(side=LEFT)
        self.output_folder_entry = ttk.Entry(output_frame, width=50)
        self.output_folder_entry.pack(side=LEFT, expand=YES, padx=(10, 0))
        ttk.Button(output_frame, text="Browse", command=self.select_output_folder, style='info.TButton').pack(side=LEFT, padx=(10, 0))

        # File type selection
        file_type_frame = ttk.Frame(main_frame)
        file_type_frame.pack(fill=X, pady=10)
        ttk.Label(file_type_frame, text="Save as:").pack(side=LEFT)
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

    def select_gif(self):
        file_path = filedialog.askopenfilename(filetypes=[("GIF files", "*.gif")])
        if file_path:
            self.gif_path_entry.delete(0, END)
            self.gif_path_entry.insert(0, file_path)

    def select_output_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.output_folder_entry.delete(0, END)
            self.output_folder_entry.insert(0, folder_path)

    def extract_frames(self):
        gif_path = self.gif_path_entry.get()
        output_folder = self.output_folder_entry.get()
        file_type = self.file_type_var.get().lower()

        if not gif_path or not output_folder:
            messagebox.showerror("Error", "Please select both GIF file and output folder.")
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
            for frame, duration, total_time in frame_info:
                f.write(f"Frame {frame:03d}: Duration = {duration:.3f}s, Total Time = {total_time:.3f}s\n")

if __name__ == "__main__":
    app = extractFrames()
    app.mainloop()