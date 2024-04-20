import utime

class Timer():

    def __init__(self, duration_seconds):
        self.duration_seconds = duration_seconds
        self.target_time = -1
        self.running = False
        self.suspended_time = -1

    def start(self):
        if not self.running:
            self.target_time = utime.time() + self.duration_seconds
            self.running = True

    def pause(self):
        if self.running:
            self.running = False
            self.suspended_time = self.target_time - utime.time()

    def resume(self):
        if not self.running:
            self.target_time = utime.time() + self.suspended_time
            self.suspended_time = -1
            self.running = True

    def reset(self):
        self.target_time = -1
        self.suspended_time = -1
        self.running = False

    def time_left(self):
        if self.running:
            return self.target_time - utime.time()
        else:
            return self.suspended_time

    def is_alarm(self):
        return self.running and utime.time() >= self.target_time   

