# ImageNexus


ImageNexus is a powerful and user-friendly application originally designed to extract frames from GIF files but has expanded into a suite of image tools with plans for expansion in the future. It allows you to easily convert your favorite animated GIFs into a series of individual image frames. ImageNexus provides a seamless experience for working with GIF animations as well as converting images to other formats. There are plans to continue adding to this project to make it into a whole suite of image tools.

## Updates Regarding This Branch

ImageNexus was originally coded using `ttkbootstrap` (Tkinter) but was quickly becoming a bottleneck in terms of future expansion, the decision to port to `Qt` was made so development of future tools and expansions could be easier and more efficient. The Tkinter branch will be deprecated in the future and become legacy.

## Installation
### If running from source:
1. Clone the repository: `git clone https://github.com/lyahn/ImageNexus`
2. Navigate to the project directory: `cd ImageNexus`
3. Create a virtual environment: `python -m venv venv`
4. Activate the virtual environment: `source venv/bin/activate`
5. Install dependencies: `pip install -r requirements.txt`

### Running on Windows:
1. Go to the [Releases] tab and download the latest version of ImageNexus.
2. Run `ImageNexus-x.y.z-setup.exe` & install the application.
3. Open ImageNexus from Desktop or Start Menu.

## Usage

1. Run the application.
2. Select the tab you want to use:

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

## QR Code Generator
1. Enter the data you want to encode in the QR code in the `QR Data` field.
2. Adjust the QR code size using the `QR Size` spin box.
3. Select the error correction level from the dropdown menu (Low, Medium, Quartile, or High).
4. Set the border size using the `Border Size` spin box.
5. Choose background color by clicking the `...` button and selecting a color. (Not Working Currently)
6. Choose code color by clicking the `...` button and selecting a color. (Not Working Currently)
7. Optionally, add a logo image by clicking the "Browse" button next to the `Logo Image` field.
8. Click the `Generate QR` button to generate and preview the QR code.
9. Select the output format (PNG or SVG) from the `Save As` dropdown menu.
10. Choose the output folder by clicking the "Browse" button next to the "Output Folder" field or typing in a directory path.
11. Click the "Save QR Code" button to save the generated QR code to the specified folder. If the folder does not exist, it will be created if permission is granted.
12. The application will display a success message with the saved file path.


## Contributing

If you'd like to contribute to the project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix: `git checkout -b my-new-feature`
3. Make your changes and commit them: `git commit -am 'Add some feature'`
4. Push your changes to your forked repository: `git push origin my-new-feature`
5. Create a new pull request.

## License

This project is yet have a licence attached...
