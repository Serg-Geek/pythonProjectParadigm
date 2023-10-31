
from time import time, sleep


class Timer:
    def __init__(self):
        self.reset()





    def start(self):
        self.is_running = True
        self.restart = time()

    def pause(self):
        if self.is_running and not self.is_paused:
            self.is_paused = True
            self.start_pause_time = time()





    def stop(self):
        if self.is_running or  self.is_paused:
            self.stop = True

    def resume(self):
        self.is_paused = False
        self.total_pause_time += time() - self.start_pause_time

    def reset(self):
        self.is_running = False
        self.is_paused = False
        self.stop = 0
        self.restart = None
        self.start_pause_time = 0
        self.total_pause_time = 0

    def print_result(self):
        print(f'time: {time() - self.restart - self.total_pause_time: 5f} seconds')



if __name__ == '__main__':
    t =Timer()
    t.start()
    sleep(5)
    t.print_result()
    t.pause()
    sleep(5)
    t.resume()
    t.print_result()


