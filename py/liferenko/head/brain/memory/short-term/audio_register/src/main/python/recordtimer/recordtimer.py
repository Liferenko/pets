import datetime
import time
rec_time_limit = input("What duration of each record do you want?")
rec_time_limit = int(rec_time_limit)
if rec_time_limit is None:
    rec_time_limit = 5 # seconds

class Timer(rec_time_limit):
    def to_set_start_time(self):
        start_time = int( time.time() )
        return srart_time

    def to_set_stop_time(self):
        stop_time = int( time.time() )
        return stop_time
    
    def to_find_start_stop_delta(self):
        timedelta = stop_time - start_time
        return timedelta
    
    def to_stop_working_process_by_time(self):
        is_it_time_to_stop = False
        if timedelta >= rec_time_limit:
            is_it_time_to_stop = True
            return is_it_time_to_stop
    
