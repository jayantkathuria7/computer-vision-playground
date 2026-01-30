# Image Processing Playground (OpenCV)

## Description
This project was built to explore various basic image operations available in OpenCV such as rotation, Gaussian blur, cropping, Canny edge detection
Besides making it just a script i have turned it into a keyboard controlled interface 

## Features
This project takes an input image (file_path passed as a command-line argument) and supports the following operation:
- `r` --> Rotate image by 90° clockwise
- `b` --> Apply Gaussian Blur (kernel size = 10)
- `g` --> Convert image to grayscale 
- `c` --> Crop image (20 pixels from all four sides)
- `e` --> Perform Canny edge detection (threshold1=155, threshold2=255)
- `u` --> Undo last change
- `o` --> Revert to original image
- `s` --> Save the modified image
- `q` --> Quit the playground

## Tech Stack
- Python
- OpenCV

## How to Run
Run the project using the following command:
```bash
python img_playground.py <filepath>
```
Provide the file path of the image you want to process as the command-line argument.

## Project Purpose / Learning Outcomes
- Implemented keyboard-based interaction in an OpenCV application by mapping key inputs to image processing operations.
- Learned to manage image state explicitly, including maintaining the original image, applying transformations incrementally, and supporting undo/revert functionality.
- Improved understanding of how basic image processing operations (blurring, grayscale conversion, edge detection, cropping) behave when applied sequentially in an interactive workflow.

## Future Improvements
- Add trackbars to dynamically adjust parameters such as blur kernel size and Canny edge thresholds.
- Extend support to video files or webcam input for real-time image processing.
- Refactor the script into a modular structure to make it easier to add new image operations.
