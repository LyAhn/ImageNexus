import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import Image
import os
from tkinter import filedialog, messagebox

class GifFrameExtractor(ttk.Window):
    version = "0.1.0-beta"
    def __init__(self):
        super().__init__(themename="darkly")
        self.title("GIF Frame Extractor {version}".format(version=self.version))
        self.geometry("600x300")
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

        if not gif_path or not output_folder:
            messagebox.showerror("Error", "Please select both GIF file and output folder.")
            return

        try:
            with Image.open(gif_path) as img:
                self.progress['maximum'] = img.n_frames
                for i in range(img.n_frames):
                    img.seek(i)
                    img.save(os.path.join(output_folder, f"frame_{i:03d}.png"))
                    self.progress['value'] = i + 1
                    self.status_label['text'] = f"Extracting frame {i+1} of {img.n_frames}"
                    self.update_idletasks()

            self.status_label['text'] = "Frames extracted successfully!"
            messagebox.showinfo("Success", "Frames extracted successfully!")
        except Exception as e:
            self.status_label['text'] = f"Error: {str(e)}"
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
        finally:
            self.progress['value'] = 0

if __name__ == "__main__":
    app = GifFrameExtractor()
    app.mainloop()