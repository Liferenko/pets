# -*-coding: utf-8 -*-
"""
NAME:

DESCRIPTION:

AUTHOR:
Pavel Liferenko (https://t.me/Liferenko)

source code as example from https://python-sounddevice.readthedocs.io/en/0.3.10/examples.html

"""

import sounddevice
import soundfile
import argparse
import tempfile
import queue
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
    '-t', '--subtype', type=str, help='sound file subtype (e.g. "PCM_24")')
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
with soundfile.SoundFile( args.filename, mode='x', samplerate=44100, channels=2 ) as file:
    with sounddevice.InputStream( device=args.device, callback=callback ):
        print( '--/' * 11 )
        print( 'Press Ctrl+C to stop the rec' )
        print( '-FINISH-!!!' * 11 )
        while True:
            file.write( q.get() )
# END file saver
