# ImageNexus formally extractFrames


ImageNexus is a powerful and user-friendly application originally designed to extract frames from GIF files. It allows you to easily convert your favorite animated GIFs into a series of individual image frames. Whether you're a designer, developer, or simply an enthusiast, ImageNexus provides a seamless experience for working with GIF animations. There are plans to continue adding to this project to make it into a whole suite of image tools.

## Installation

1. Clone the repository: `git clone https://github.com/lyahn/ImageNexus`
2. Navigate to the project directory: `cd ImageNexus`
3. Install dependencies: `pip install -r requirements.txt`

## Usage

1. Run the application: `python main.py`
2. Select the desired tab: "Frame Extractor", "Image Converter", or "Batch Converter".

### Frame Extractor
1. Select the GIF file you want to extract frames from by clicking the "Browse" button next to the "Select GIF" field.
2. Choose the output folder where the extracted frames will be saved by clicking the "Browse" button next to the "Output Folder" field.
3. Select the file format for the extracted frames (PNG or GIF) from the dropdown menu.
4. Optionally, check the "Generate frame info file" checkbox to create a text file with frame duration information.
5. Click the "Extract Frames" button to start the extraction process.
6. The application will display a progress bar and status updates as it extracts the frames.
7. Once the extraction is complete, a success message will be displayed, and the extracted frames will be saved in the specified output folder with the naming convention "frame_001_0.120s.png", "frame_002_0.120s.png", and so on, where the numbers represent the duration of the frame in seconds.

### Image Converter
1. Select the input image file by clicking the "Browse" button next to the "Select Input File" field.
2. Choose the output folder where the converted image will be saved by clicking the "Browse" button next to the "Output Folder" field.
3. Select the desired output format (GIF, PNG, JPEG, BMP, or TIFF) from the dropdown menu.
4. Click the "Convert File" button to start the conversion process.
5. The application will display a status update upon successful conversion.

### Batch Converter
1. Select the conversion type ("Files" or "Folder") from the dropdown menu.
2. If "Files" is selected, choose the input image files by clicking the "Browse" button next to the "Select Input" field.
3. If "Folder" is selected, choose the input folder containing the image files by clicking the "Browse" button next to the "Select Input" field.
4. Choose the output folder where the converted images will be saved by clicking the "Browse" button next to the "Output Folder" field.
5. Select the desired output format (GIF, PNG, JPEG, BMP, or TIFF) from the dropdown menu.
6. Click the "Convert Files" button to start the batch conversion process.
7. The application will display status updates as the files are being converted.
8. Once the conversion is complete, a success message will be displayed.

## Contributing

If you'd like to contribute to the project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix: `git checkout -b my-new-feature`
3. Make your changes and commit them: `git commit -am 'Add some feature'`
4. Push your changes to your forked repository: `git push origin my-new-feature`
5. Create a new pull request.

## License

This project is yet have a licence attached...
