# coding=utf-8

import os
import cv2

# videos_src_path = "C:/Users/LYY/Desktop/VPData"
# video_formats = [".MP4", ".MOV"]
# frames_save_path = "C:/Users/LYY/Desktop/VPData"
#
# # capture = cv2.VideoCapture(videos_src_path + '1.mp4')   #读取视频数据
# # frame_count = capture.get(cv2.CAP_PEOP_FRAME_COUNT)     #读取视频帧数
# # frame_height1 = capture.get(cv2.CAP_PEOP_FRAME_HEIGHT)   #视频的高度
# # frame_width1 = capture.get(cv2.CAP_PEOP_FRAME_WIDTH)     #视频的宽度
#
#
#
# width = 640
# height = 368
# time_interval = 50
#
#
# def video2frame(video_src_path, formats, frame_save_path, frame_width, frame_height, interval):
#     """
#     将视频按固定间隔读取写入图片
#     :param video_src_path: 视频存放路径
#     :param formats:　包含的所有视频格式
#     :param frame_save_path:　保存路径
#     :param frame_width:　保存帧宽
#     :param frame_height:　保存帧高
#     :param interval:　保存帧间隔
#     :return:　帧图片
#     """
#     videos = os.listdir(video_src_path)
#
#     def filter_format(x, all_formats):
#
#         if x[-4:] in all_formats:
#             return True
#         else:
#             return False
#
#     videos = filter(lambda x: filter_format(x, formats), videos)
#
#     for each_video in videos:
#         print("正在读取视频：", each_video)
#
#     each_video_name = each_video[:-4]
#     os.mkdir(frame_save_path + each_video_name)
#     each_video_save_full_path = os.path.join(frame_save_path, each_video_name) + "/"
#
#     each_video_full_path = os.path.join(video_src_path, each_video)
#
#     cap = cv2.VideoCapture(each_video_full_path)
#     frame_index = 0
#     frame_count = 0
#     if cap.isOpened():
#         success = True
#     else:
#         success = False
#         print("读取失败!")
#
#     while (success):
#         success, frame = cap.read()
#         print("---> 正在读取第%d帧:" % frame_index, success)
#
#         if frame_index % interval == 0:
#             resize_frame = cv2.resize(frame, (frame_width, frame_height), interpolation=cv2.INTER_AREA)
#         # cv2.imwrite(each_video_save_full_path + each_video_name + "_%d.jpg" % frame_index, resize_frame)
#         cv2.imwrite(each_video_save_full_path + "%d.jpg" % frame_count, resize_frame)
#         frame_count += 1
#
#         frame_index += 1
#
#     cap.release()
#
#
# if __name__ == '__main__':
#     video2frame(videos_src_path, video_formats, frames_save_path, width, height, time_interval)


import cv2
import sys
import time
import re
from PyQt5.QtWidgets import (QDialog, QApplication,
                             QStyleFactory, QComboBox,
                             QLabel, QVBoxLayout)

def video2frame(videos_path, frames_save_path, time_interval):
    frames_save_path = 'C:/Users/LYY/Desktop/VPData'
    vidcap = cv2.VideoCapture(videos_path)
    success, image = vidcap.read()
    count = 0
    i = 1
    while success:
        success, image = vidcap.read()
        count += 1
        if count % time_interval == 0:
            cv2.imwrite(frames_save_path + '\\' + str(i) + '.jpg', image)
            i += 1
            print(i)
    print(i)


def progress_bar():
    for i in range(1, 101):
        print("\r", end="")
        print("progress: {}%: ".format(i), "▋" * (i // 2), end="")
        sys.stdout.flush()
        time.sleep(0.05)


if __name__ == '__main__':
    # videos_path = r'C:/Users/LYY/Desktop/VPData/1.mp4'
    # frames_save_path = r'C:/Users/LYY/Desktop/VPData'
    # time_interval = 10 #分帧间隔
    # video2frame(videos_path, frames_save_path, time_interval)
    # print(videos_path)
    # progress_bar()

    # videoFilePath = 'C:/Users/LYY/Desktop/VPData'
    # video_filename = os.listdir(videoFilePath)  # 拿到文件夹下的视频文件名称
    #
    #
    # videos_path = videoFilePath + str('/') + video_filename[0]  # 视频的路径+名称
    # print(videos_path)

    print(QStyleFactory.keys())
    print(os.path.abspath('.'))
    print(os.path.abspath(os.path.join(os.getcwd(), "..")))