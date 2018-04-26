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

# optional flags
def int_or_str(text):
    try:
        return int(text)
    except ValueError:
        return text

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument( 
    '-l', '--list-devices', action='store_true',
    help='show list of audio devices and exit'
 )
parser.add_argument( 
    'filename', nargs='?',
    metavar='FILENAME', 
    help='audio file to store recording to'
 )
args = parser.parse_args()
# END optional flags    
        
# device list
if args.list_devices:
    print( sounddevice.query_devices() )
    parser.exit(0)
# END device list
# define filename
if args.filename is None:
    args.filename = tempfile.mktemp( prefix='rec_', suffix='.wav', dir='result/' )
# END define filename

q = queue.Queue() # FIFO (wanna test with LIFO)

# ...for each audioblock
def callback( indata, frames, time, status ):
    if status:
        print( status, file=sys.stderr )
    q.put( indata.copy() )
# END ...for each audioblock

# 
# END 


# file saver ('with...as' promises that file will close)
with soundfile.SoundFile( args.filename, mode='x' ) as file:
    with sounddevice.InputStream( device=args.device, callback=callback ):
        print( '--/' * 11 )
        print( 'Press Ctrl+C to stop the rec' )
        print( '-FINISH-!!!' * 11 )
        while True:
            file.write( q.get() )
# END file saver
