This program is designed to calculate the area and perimeter (or circumference) of shapes detected in an image. It uses a combination of Python libraries: Pillow (PIL) for image handling and OpenCV for image processing.

Here is a step-by-step description of what the program does:

1. Open Image: The program starts by opening an image file using the Pillow library to extract the image's DPI (dots per inch) information, if available. This information is used to calculate the scale factor from pixels to centimeters, assuming that DPI is the same in both horizontal and vertical directions.
2. DPI Handling: If the DPI information is found, the program uses it to calculate the scale (conversion from pixels to centimeters). If the DPI is not found, it defaults to a predefined scale of 0.1 cm per pixel.
3. Image Processing with OpenCV: With the scale determined, the program reads the image using OpenCV, converts it to grayscale, and applies a Gaussian blur to smooth the image. This is in preparation for edge detection.
4. Edge Detection: The program uses the Canny edge detector to find edges in the image.
5. Contour Detection: The contours of the shapes are then detected using the findContours function from OpenCV. Each detected contour represents a potential shape in the image.
6. Area and Perimeter Calculation: For each contour, the program calculates the area in pixels and then converts it to square centimeters using the scale factor. It also checks if the contour is an approximate circle by comparing the area of the enclosing circle to the contour's area. If they are similar (within a 10% error margin), it calculates the circumference; otherwise, it calculates the perimeter.
7. Side Lengths for Polygons: If the contour is not a circle, the program approximates the contour to a simpler polygon and then calculates the length of each side in centimeters.
8. Output: The calculated area and the perimeter (or circumference) of each shape, along with the length of each side for polygons, are printed to the console.
The program can be used to analyze various shapes in images, such as squares, rectangles, stars, triangles, and circles, as indicated by the commented list of image paths at the end of the script. Users can specify the path to the image they want to analyze, and the program will output the geometric properties of the shapes found within that image.
