# -*-coding: utf-8 -*-

"""
Sources:
Mainteiner: Pavel Liferenko

- 
- https://www.pyimagesearch.com/2017/07/10/using-tesseract-ocr-python/
"""

import PIL
import numpy as np
import cv2 # OpenCV
import pytesseract
import os
import argparse


class Visioneer:
        def to_open_frame(self):
                capture = cv2.VideoCapture(0)
                while(True):
                        ret, frame = capture.read()
                        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                        webcam = cv2.imshow('frame', frame)
                        gray_webcam = cv2.imshow('gray', gray)       
        
                        if cv2.waitKey(20) & 0xFF == ord('q'):
                                break

                # release the capture
                capture.release()
                cv2.destroyAllWindows()



def constructor():
        argument_parser = argparse.ArgumentParser()
        argument_parser.add_argument( "-i", "--image", required=True, help="path to input image to be OCR'd" )
        argument_parser.add_argument( "-p", "--preprocess", type=str, default="thresh", help="type of preprocessing to be done" )
        args = vars( argument_parser.parse_args() )

if __name__ == '__main__':
        constructor()
        visioneer = Visioneer()
        visioneer.to_open_frame()
