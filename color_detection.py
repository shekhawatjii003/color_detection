# Import the necessary libraries
# OpenCV (cv2) is for computer vision tasks.
# NumPy (np) is for numerical operations, especially for working with arrays.
import cv2
import numpy as np

# Initialize the video capture object to access the default webcam (index 0).
cap = cv2.VideoCapture(0)

# Define a placeholder function for the trackbar.
# The trackbar requires a callback function that is executed when the slider position changes.
# Since we only need to read the value, this function does nothing.
def empty(a):
    pass

# Create a new window named 'HSV' to hold the trackbars.
cv2.namedWindow('HSV')
# Resize the 'HSV' window to a specific width and height.
cv2.resizeWindow('HSV', 640, 240)

# Create trackbars to control the HSV (Hue, Saturation, Value) threshold values.
# These sliders will allow you to dynamically select a color range.
# Hue: Represents the color (0-179 in OpenCV)
cv2.createTrackbar('hue-min', 'HSV', 0, 179, empty)
cv2.createTrackbar('hue-max', 'HSV', 179, 179, empty)
# Saturation: Represents the intensity/purity of the color (0-255)
cv2.createTrackbar('sat-min', 'HSV', 0, 255, empty)
cv2.createTrackbar('sat-max', 'HSV', 255, 255, empty)
# Value: Represents the brightness of the color (0-255)
cv2.createTrackbar('value-min', 'HSV', 0, 255, empty)
cv2.createTrackbar('value-max', 'HSV', 255, 255, empty)

# Start an infinite loop to process video frames continuously.
while True:
    # Read a single frame from the webcam.
    # 'success' is a boolean that is True if the frame was read successfully.
    # 'img' is the actual frame (an array of pixels).
    success, img = cap.read()
    if not success: # If a frame could not be read, break the loop.
        break

    # Convert the captured frame from the BGR color space to the HSV color space.
    # HSV is often better for color detection as it separates color (Hue) from brightness (Value).
    imghsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Get the current position of each trackbar from the 'HSV' window.
    hue_min = cv2.getTrackbarPos('hue-min', 'HSV')
    hue_max = cv2.getTrackbarPos('hue-max', 'HSV')
    sat_min = cv2.getTrackbarPos('sat-min', 'HSV')
    sat_max = cv2.getTrackbarPos('sat-max', 'HSV')
    value_min = cv2.getTrackbarPos('value-min', 'HSV')
    value_max = cv2.getTrackbarPos('value-max', 'HSV')

    # Create NumPy arrays for the lower and upper bounds of the color to be detected.
    lower = np.array([hue_min, sat_min, value_min])
    upper = np.array([hue_max, sat_max, value_max])

    # Create a binary mask.
    # Pixels in 'imghsv' that are within the 'lower' and 'upper' range will be white (255).
    # Pixels outside the range will be black (0).
    mask = cv2.inRange(imghsv, lower, upper)

    # Use the mask to extract the colored object from the original image.
    # The bitwise_and operation keeps only the pixels in the original 'img'
    # where the corresponding pixel in the 'mask' is white.
    result = cv2.bitwise_and(img, img, mask=mask)

    # --- IMPORTANT NOTE ON RESIZING ---
    # The following lines resize the images, but the result MUST be assigned to a variable.
    # cv2.resize is not an "in-place" function; it returns a new, resized image.
    result_resized = cv2.resize(result, (640, 240))
    imghsv_resized = cv2.resize(imghsv, (640, 240))
    mask_resized = cv2.resize(mask, (640, 240))

    # Display the different image windows.
    # 'imshow' takes the window name and the image to be displayed.
    cv2.imshow("Original Image", img)
    cv2.imshow("Mask", mask_resized)
    cv2.imshow("Result (Color Detected)", result_resized)

    # Wait for 1 millisecond for a key press.
    # The '& 0xFF' is a bitwise AND operation used for 64-bit machine compatibility.
    # If the key pressed is 'q' (ord('q') gets the ASCII value), the loop will break.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop ends, release the webcam resource.
cap.release()
# Destroy all the windows created by OpenCV.
cv2.destroyAllWindows()