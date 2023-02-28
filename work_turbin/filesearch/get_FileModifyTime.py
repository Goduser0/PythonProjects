import time
import os


def TimeStampToTime(timestamp):
    timestruct = time.localtime(timestamp)
    return time.strftime('%Y-%m-%d %H:%M:%S', timestruct)


def get_fileModifyTime(filepath):
    t = os.path.getmtime(filepath)
    return TimeStampToTime(t)
