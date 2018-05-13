# -*-coding: utf-8 -*-
"""
NAME:

DESCRIPTION:

AUTHOR:
Pavel Liferenko (https://t.me/Liferenko)

SOURCE 
source code as example from https://python-sounddevice.readthedocs.io/en/0.3.10/examples.html

"""
# import recordtimer.recordtimer
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
parser.add_argument( '-t', '--timer', type=int, help='recording part duration in seconds' )
    
args = parser.parse_args()
        

# device list
if args.list_devices:
    print( sounddevice.query_devices() )
    parser.exit(0)
# END device list


# define filename
if args.filename is None:
    filename_timestamp_prefix = str('rec_' + time.ctime())
    args.filename = tempfile.mktemp( prefix=filename_timestamp_prefix, suffix='.wav', dir='result/' )   
# TODO find how to rec on .mp3 or another less-size-format

# END define filename









q = queue.Queue() # FIFO (wanna test with LIFO)

# ...for each audioblock
def callback( indata, frames, time, status ):
    if status:
        print( status, file=sys.stderr )
    q.put( indata.copy() )
# END ...for each audioblock



# file recorder ('with...as' promises that file will close)
def file_recorder():
    with soundfile.SoundFile( args.filename, 
                              mode='x', 
                              samplerate=44100, 
                              channels=2 ) as file:
        with sounddevice.InputStream( device=args.device, callback=callback ):
            print( '--/' * 11 )
            print( 'Press Ctrl+C to stop the rec' )
            rec_time_limit = 5
            timedelta = 0
            end_time = int( time.time() )
                
            while True:
                start_time = int( time.time() )
                timedelta = start_time - end_time
                print(int(timedelta))
                if timedelta > rec_time_limit:
                    break
                file.write( q.get() )                   
                args.filename = tempfile.mktemp( prefix=filename_timestamp_prefix, suffix='.wav', dir='result/' )   


# END file recorder



# Setting record time limit
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
    while True:
        file_recorder()
    
    print("Stop successfully")

    logging.info( "Stop and save current bit -- File name - %s" % (args.filename) )    
