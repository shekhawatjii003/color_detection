A simple and interactive Python application that uses a webcam to detect and isolate objects of a specific color in real-time using HSV color space thresholding.

This project is an excellent introduction to fundamental computer vision concepts, including color spaces, masking, and real-time video processing with OpenCV.

(This is a placeholder. You can record a GIF of your screen and upload it here to show the project in action!)

Features
Live Video Feed: Captures video directly from your webcam.

Interactive HSV Controls: Use intuitive sliders (trackbars) to adjust the Hue, Saturation, and Value ranges.

Real-Time Masking: Instantly see the binary mask that separates the target color from the rest of the view.

Object Isolation: View the final result where only the object of the selected color is visible.

Clean User Interface: All control sliders are grouped in a separate window, keeping the main display clean.

Technology Stack
Language: Python 3

Libraries:

OpenCV-Python: The core library for all computer vision tasks.

NumPy: Used for efficient array manipulation, especially for creating the color range boundaries and the final masked image.

Getting Started
Follow these instructions to get a copy of the project up and running on your local machine.

Prerequisites
You need to have Python and pip installed on your system. You can download Python from python.org.

Installation
Clone the repository:

Bash

git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
Install the required Python libraries:

Bash

pip install opencv-python numpy
How to Use
Run the script from your terminal:

Bash

python your_script_name.py
Two windows will appear:

HSV: This window contains the six sliders to control the color range.

Original | Mask | Result: This window shows the live webcam feed, the generated mask, and the final isolated color output.

Adjust the sliders in the HSV window to select the color you want to detect:

hue-min & hue-max: This is the most important slider. It selects the actual color (e.g., red, green, blue). Since Hue is a circle, you might need to select a range at the very beginning and end for colors like red.

sat-min & sat-max: This controls the "purity" or "richness" of the color. A low sat-min will include grays and less vibrant shades of your target color.

value-min & value-max: This controls the brightness. A low value-min will include darker shades of your color.

Observe the Mask and Result windows to see your selection applied in real-time.

Press the 'q' key on your keyboard while one of the OpenCV windows is active to quit the application.

Code Explanation
Initialization: The script starts by initializing the webcam, creating a named window for controls, and setting up the six HSV trackbars.

Main Loop: The while True: loop continuously reads frames from the webcam.

Color Conversion: Each frame is converted from the default BGR color space to HSV, which is more suitable for color-based segmentation.

Mask Creation: cv2.inRange() uses the lower and upper HSV values from the trackbars to create a binary mask. Pixels within the range are turned white, and all others are turned black.

Object Extraction: cv2.bitwise_and() performs a logical AND operation between the original image and itself, using the mask. This effectively "erases" everything that isn't part of the selected color range.

Display: The original image, the mask, and the final result are displayed using cv2.imshow().

License
This project is licensed under the MIT License - see the LICENSE.md file for details.
