# ImageNexus formally extractFrames


ImageNexus is a powerful and user-friendly application originally designed to extract frames from GIF files. It allows you to easily convert your favorite animated GIFs into a series of individual image frames. Whether you're a designer, developer, or simply an enthusiast, ImageNexus provides a seamless experience for working with GIF animations. There are plans to continue adding to this project to make it into a whole suite of image tools.

## Installation

1. Clone the repository: `git clone https://github.com/lyahn/ImageNexus`
2. Navigate to the project directory: `cd ImageNexus`
3. Install dependencies: `pip install -r requirements.txt`

## Usage

1. Run the application: `python main.py`
2. Select the GIF file you want to extract frames from by clicking the "Browse" button next to the "Select GIF" field.
3. Choose the output folder where the extracted frames will be saved by clicking the "Browse" button next to the "Output Folder" field.
4. Click the "Extract Frames" button to start the extraction process.
5. The application will display a progress bar and status updates as it extracts the frames.
6. Once the extraction is complete, a success message will be displayed, and the extracted frames will be saved in the specified output folder with the naming convention "frame_001_0.120s.png", "frame_002_0.120s.png", and so on, where the numbers represent the duration of the frame in seconds.

## Contributing

If you'd like to contribute to the project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix: `git checkout -b my-new-feature`
3. Make your changes and commit them: `git commit -am 'Add some feature'`
4. Push your changes to your forked repository: `git push origin my-new-feature`
5. Create a new pull request.

## License

This project is yet have a licence attached...
































# ImageNexus

ImageNexus is a versatile Python application that provides two main functionalities: extracting frames from GIF files and converting image files between various formats. With its user-friendly graphical interface built using the ttkbootstrap library, ImageNexus offers a seamless experience for working with animated GIFs and image file conversions.

The Frame Extractor feature allows you to extract individual frames from a GIF file, saving them as separate image files (PNG or GIF) in a specified output folder. This can be useful for various purposes, such as creating frame-by-frame animations, analyzing individual frames, or converting GIFs to a different format.

The File Converter feature enables you to convert image files between various formats, including GIF, PNG, JPG, BMP, and TIFF. This functionality can be handy when you need to convert images to a specific format for compatibility or optimization purposes.

With its intuitive interface and efficient algorithms, ImageNexus simplifies the process of working with GIF animations and image file conversions, making it a valuable tool for designers, developers, and enthusiasts alike.