import json
from datetime import datetime

class TimeUnit:
    def __init__(self):
        '''
        Variables for durations (by counting seconds)
        timedelta를 안 쓰는 이유 => 24시간이 넘을 경우 1 day로 바뀌어서 계산하는 데 불편
        '''
        self.duration_of_the_day = 0
        self.duration_this_month = 0
        self.duration_until_now = 0
        
        try: 
            with open('time_data.json', 'r') as file:
                time_data = json.load(file)
                    
        except FileNotFoundError: 
            pass
        
        else: 
            self.duration_of_the_day = time_data['record_of_the_day']
            self.duration_until_now = time_data['record_until_now']

            # Check if 'the current month' of 'the current year' exists in time data
            if datetime.now().strftime("%B").upper()[0:3] in time_data[datetime.now().strftime("%Y")]:
                self.duration_this_month = time_data[datetime.now().strftime("%Y")][datetime.now().strftime("%B").upper()[0:3]]
            
    # Convert seconds to HH:MM:SS
    def record_sec(self, seconds):
        return seconds % 60
    
    def record_min(self,seconds):
        return (seconds // 60) % 60
        
    def record_hour(self, seconds):
        return seconds // 60 // 60
    
    def record_formatting(self, seconds):
        if self.record_hour(seconds) > 99:
            return '{0}:{1:02d}:{2:02d}'.format(self.record_hour(seconds), self.record_min(seconds), self.record_sec(seconds))
        
        return '{0:02d}:{1:02d}:{2:02d}'.format(self.record_hour(seconds), self.record_min(seconds), self.record_sec(seconds))
