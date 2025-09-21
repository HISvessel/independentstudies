#!/usr/bin/env python3
import cv2
from datetime import datetime

"""this is a camera parent class that takes a video source
from the online user and appends it for the camera to function."""

class VideoSource:
    #@classmethod
    def find_source():
        """this class method is a test to search algorithmically for a source
        to feed to the camera. The correct source is found by iterating through
        the list of valid arguments which are processed to the VideoCapture.isOpened()
        function for a smart way to find the feed without hardcoding it and changing
        the source code.
        
        The function should return a usable camera source for cv.VideoCapture to use,
        otherwise close the program if no valid source can be found."""
        ip_source = 'http://192.168.0.3:4747/video'
        video_capture = [0, 1, 2, ip_source]
        print(video_capture)
        try:
            for index, source in enumerate(video_capture):
                if source is True:
                    return video_capture[index]
                return
        except RuntimeError: #raising runtime error if a source is not found
            print('Could not find source.')
