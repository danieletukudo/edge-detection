import cv2
import numpy as np
from typing import Tuple


class ImageProcessor:
    """
    ImageProcessor: A class for performing various image processing operations such as
    resizing, converting to grayscale, blurring, edge detection, dilation, and erosion
    using OpenCV. This class also provides functionality to display the processed images.
    """

    def __init__(self, image_path: str):
        """
        Initialize the ImageProcessor class with the path to the image.

        Args:
            image_path (str): Path to the image file.
        """
        self.image_path = image_path
        self.kernel = np.ones((5, 5), np.uint8)  # Kernel for morphological operations
        self.image = None
        self.processed_images = {}

    def load_image(self) -> None:
        """
        Load the image from the specified path.
        """
        self.image = cv2.imread(self.image_path)
        if self.image is None:
            raise FileNotFoundError(f"Image not found at the path: {self.image_path}")
        print(f"Image loaded from {self.image_path}")
        self.processed_images["Original Image"] =cv2.resize(self.image,(400,400))

    def resize_image(self, width: int = 200, height: int = 200) -> None:
        """
        Resize the image to the specified width and height.

        Args:
            width (int): The target width of the image. Default is 200.
            height (int): The target height of the image. Default is 200.
        """
        self.image = cv2.resize(self.image, (width, height))
        print(f"Image resized to {width}x{height}")

    def convert_to_grayscale(self) -> None:
        """
        Convert the loaded image to grayscale and store it in processed_images.
        """
        gray_img = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.processed_images["Gray Image"] = gray_img
        print("Image converted to grayscale")

    def apply_blur(self, kernel_size: Tuple[int, int] = (7, 7)) -> None:
        """
        Apply Gaussian blur to the grayscale image and store it in processed_images.

        Args:
            kernel_size (Tuple[int, int]): The size of the kernel for blurring. Default is (7, 7).
        """
        gray_img = self.processed_images.get("Gray Image")
        if gray_img is not None:
            blur_img = cv2.GaussianBlur(gray_img, kernel_size, 0)
            self.processed_images["Blur Image"] = blur_img
            print(f"Gaussian blur applied with kernel size {kernel_size}")
        else:
            print("Grayscale image not found. Please convert to grayscale first.")

    def detect_edges(self, threshold1: int = 100, threshold2: int = 200) -> None:
        """
        Detect edges in the blurred image using the Canny edge detector.

        Args:
            threshold1 (int): First threshold for the hysteresis procedure. Default is 100.
            threshold2 (int): Second threshold for the hysteresis procedure. Default is 200.
        """
        blur_img = self.processed_images.get("Blur Image")
        if blur_img is not None:
            edges = cv2.Canny(blur_img, threshold1, threshold2)
            self.processed_images["Edges"] = edges
            print(f"Edges detected using Canny with thresholds {threshold1} and {threshold2}")
        else:
            print("Blurred image not found. Please apply blur first.")

    def dilate_image(self, iterations: int = 1) -> None:
        """
        Dilate the edges to make them more prominent.

        Args:
            iterations (int): Number of dilation iterations. Default is 1.
        """
        edges = self.processed_images.get("Edges")
        if edges is not None:
            dilated = cv2.dilate(edges, self.kernel, iterations=iterations)
            self.processed_images["Dilated Image"] = dilated
            print(f"Image dilated with {iterations} iterations")
        else:
            print("Edge-detected image not found. Please detect edges first.")

    def erode_image(self, iterations: int = 1) -> None:
        """
        Erode the dilated image to refine the edges.

        Args:
            iterations (int): Number of erosion iterations. Default is 1.
        """
        dilated = self.processed_images.get("Dilated Image")
        if dilated is not None:
            eroded = cv2.erode(dilated, self.kernel, iterations=iterations)
            self.processed_images["Eroded Image"] = eroded
            print(f"Image eroded with {iterations} iterations")
        else:
            print("Dilated image not found. Please dilate the image first.")

    def display_images(self) -> None:
        """
        Display all processed images including the original image.
        """
        for title, image in self.processed_images.items():
            cv2.imshow(title, image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


if __name__ == "__main__":
    # Define the path to the image
    image_path = "test.png"

    # Create an ImageProcessor object
    processor = ImageProcessor(image_path)

    # Perform image processing steps
    processor.load_image()
    processor.resize_image(400, 400)
    processor.convert_to_grayscale()
    processor.apply_blur((7, 7))
    processor.detect_edges(100, 200)
    processor.dilate_image(1)
    processor.erode_image(1)

    # Display the results
    processor.display_images()

'''blur box or people
face recogniton
'''
