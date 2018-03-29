# -*- coding: utf8 -*-

"""
Goal:
to see dice game, check if combinations exists and send data to counter

Mainteiner: Liferenko Pavel

use - https://github.com/madmaze/pytesseract
"""

try:
	import Image
except ImportError:
	from PIL import Image
import pytesseract


# pytesseract.pytesseract.tesseract_cmd = '<full_path_to_your_tesseract_executable>'
# Include the above line, if you don't have tesseract executable in your PATH
# Example tesseract_cmd: 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract'

# Simple image to string
print(pytesseract.image_to_string(Image.open('drommel.jpg')))

# French text image to string
print(pytesseract.image_to_string(Image.open('test-european.jpg'), lang='fra'))

# Get bounding box estimates
print(pytesseract.image_to_boxes(Image.open('drommel.jpg')))

# Get verbose data including boxes, confidences, line and page numbers
# print(pytesseract.image_to_data(Image.open('drommel.jpg'))
