# -*-coding: utf-8 -*-
"""
NAME:

DESCRIPTION:

AUTHOR:
Pavel Liferenko (https://t.me/Liferenko)

"""
import sounddevice as sd
duration = 5.5  # seconds

def callback(indata, outdata, frames, time, status):
    if status:
        print(status)
    outdata[:] = indata

        

if __name__ == '__main__':
    print('Start rec \n \n ---')
    with sd.Stream(channels=2, callback=callback):
        sd.sleep(int(duration * 300))
