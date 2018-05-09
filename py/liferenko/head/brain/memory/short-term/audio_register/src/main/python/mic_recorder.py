# -*-coding: utf-8 -*-
"""
NAME:

DESCRIPTION:

AUTHOR:
Pavel Liferenko (https://t.me/Liferenko)

SOURCE 
source code as example from https://python-sounddevice.readthedocs.io/en/0.3.10/examples.html

"""
import sounddevice
import soundfile
import argparse
import tempfile
import datetime
import logging
import queue
import time
import sys



def int_or_str(text):
    """Helper function for argument parsing."""
    try:
        return int(text)
    except ValueError:
        return text

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument( 
    '-t', '--time', default=6000, 
    help='choose duration of record' )

parser.add_argument(
    '-l', '--list-devices', action='store_true',
    help='show list of audio devices and exit')
parser.add_argument(
    '-d', '--device', type=int_or_str,
    help='input device (numeric ID or substring)')
parser.add_argument(
    '-r', '--samplerate', type=int, help='sampling rate')
parser.add_argument(
    '-c', '--channels', type=int, default=1, help='number of input channels')
parser.add_argument(
    'filename', nargs='?', metavar='FILENAME',
    help='audio file to store recording to')
parser.add_argument(
    '-s', '--subtype', type=str, help='sound file subtype (e.g. "PCM_24")')
args = parser.parse_args()

        

# device list
if args.list_devices:
    print( sounddevice.query_devices() )
    parser.exit(0)
# END device list



# define filename
if args.filename is None:
    args.filename = tempfile.mktemp( prefix='rec_', suffix='.wav', dir='result/' )   
    # TODO find how to rec on .mp3 or another less-size-format
# END define filename




q = queue.Queue() # FIFO (wanna test with LIFO)

# ...for each audioblock
def callback( indata, frames, time, status ):
    if status:
        print( status, file=sys.stderr )
    q.put( indata.copy() )
# END ...for each audioblock



# file saver ('with...as' promises that file will close)
def file_recorder():
    with soundfile.SoundFile( args.filename, mode='x', 
                              samplerate=44100, channels=2 ) as file:
        with sounddevice.InputStream( device=args.device, callback=callback ):
            print( '--/' * 11 )
            print( 'Press Ctrl+C to stop the rec' )
            rec_time_limit = 10
            end_time = time.time()
            timedelta = rec_time_limit + 1
            print(rec_time_limit)
            while timedelta > rec_time_limit:
                start_time = time.time()
                timedelta = timedelta - start_time
                print(int(timedelta))
                file.write( q.get() )                   
# END file saver



# Setting record time limit
start_time = time.time()
end_time = time.time()
timedelta = end_time - start_time
rec_time_limit = 900000
# END setting record time limit



# security
# END security

# logging 
class Logger(object):
    logging.basicConfig(filename='audio_events_logging.log', 
                        filemode='w',
                        level=logging.INFO,
                        format='%(asctime)s [%(levelname)s] %(message)s')
# END logging


if __name__ == '__main__':
    logging.info( "Start bit of record" )
    file_recorder()
    print('start - ', start_time,'end - ', end_time)
    end_time = time.time()
    logging.info( "Stop and save current bit // File name - %s" % (filename) )    
