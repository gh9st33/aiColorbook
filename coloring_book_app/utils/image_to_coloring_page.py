```python
from PIL import Image, ImageOps
import cv2
import numpy as np
from fpdf import FPDF

def convert_image_to_grayscale(image_path):
    image = Image.open(image_path)
    grayscale_image = ImageOps.grayscale(image)
    return grayscale_image

def apply_edge_detection(grayscale_image):
    image_array = np.array(grayscale_image)
    edges = cv2.Canny(image_array, 30, 100)
    return edges

def convert_edges_to_image(edges):
    edge_image = Image.fromarray(edges)
    return edge_image

def convert_image_to_pdf(image, output_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.image(image, x = 0, y = 0, w = 210, h = 297)
    pdf.output(output_path, "F")

def convert_image_to_coloring_page(image_path, output_path):
    grayscale_image = convert_image_to_grayscale(image_path)
    edges = apply_edge_detection(grayscale_image)
    edge_image = convert_edges_to_image(edges)
    edge_image.save("temp.jpg")
    convert_image_to_pdf("temp.jpg", output_path)
```
