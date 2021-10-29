class DateTime:
    
    date_cmd = ["date", "+%Y/%m/%d %H:%M:%S"]
    date_time = list()
    
    def __init__(self):
        import subprocess
        self.date_time = subprocess.check_output(self.date_cmd)
        self.date_time = self.date_time.decode()
        self.date_time = self.date_time.split(' ')
        self.date_time[1] = self.date_time[1].rstrip('\n')

    
    def get_date_time(self):
        return self.date_time

    def get_date(self):
        return self.date_time[0]

    def get_time(self):
        return self.date_time[1]

