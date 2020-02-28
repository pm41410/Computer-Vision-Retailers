import sys
import argparse
import numpy as np
import cv2
import os
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
print(cv2.__version__)

from moviepy.video.io.VideoFileClip import VideoFileClip
#

def extractimage(t1 = 0, t2 = 40):
    pathIn = os.getcwd()
    os.chdir(pathIn)
    video_list = os.listdir('video')
    os.makedirs('output')
    os.chdir('output')
    for video in video_list:
        object_name = video.split(".")[0]
        ffmpeg_extract_subclip(pathIn + '\\video\\' + video, t1, t2, targetname=object_name + '_subclip.mp4')
    # Current wd: cropped videos

    video_list_changed = os.listdir()
    os.chdir(pathIn) # Back to the pathIn
    os.makedirs("image_output") # Make iamge output folder
    for video_subclip in video_list_changed:
        count = 0
        os.chdir(pathIn + '\image_output')
        object_name = video_subclip.split("_")[0]
        os.makedirs(object_name)
        # Change directory to output video to process image
        os.chdir(pathIn + '\output')
        vidcap = cv2.VideoCapture(video_subclip)
        success = True
        while success:
            vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*999))    # added this line
            success,image = vidcap.read()
            if success == False:
                break
            cv2.imwrite(pathIn + '\image_output\\' + '\\%s\\' % object_name + object_name + "_%d.jpg" % count, image)     # save frame as JPEG file
            count = count + 1
        vidcap.release()
    cv2.destroyAllWindows()
