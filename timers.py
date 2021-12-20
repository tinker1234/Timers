import time


class Time:
    _timers = dict()
    _cancelled = list()
    def __init__(self, seconds: int = None, function: object = None, mode: str = None, *args, **kw) -> None:
        self.mode = mode
        self.secs = seconds
        self.function = function
        self.args = args
        self.kwargs = kw
        self.time = time.time()

    
    def setInterval(self, name: str, seconds: int, function: object, *args, **kw):
        """
        set a never ending timer to run x seconds

            @name: unique string to name timer object used to cancel
            @seconds: a number of secounds before timer runs
            @function: function to be called when seconds is hit

        """
        interval = Time(seconds, function, "interval", *args, **kw)
        if name not in self._timers:
            self._timers[name] = interval
        else:
            raise Exception(f"INTERVAL: {name} exists already")
    
    def setTimeout(self, name: str, seconds: int, function: object, *args, **kw):
        """
        set an ending timer to run at x seconds then stops
        
            @name: unique string to name timer object used to cancel
            @seconds: a number of secounds before timer runs
            @function: function to be called when seconds is hit
        """
        timeout = Time(seconds, function, "timeout", *args, **kw)
        if name not in self._timers:
            self._timers[name] = timeout
        else:
            raise Exception(f"TIMEOUT: {name} exists already")
    
    def cancel(self, name):
        """
        cancel the timer

            @name: the unique string you used to create the timer
        
        """
        if name not in self._cancelled:
            self._cancelled.append(name)

    def run(self):
        """
        call in a while loop runs timers and checks if cancelled
        """
        for key, value in iter(self._timers.items()):
            t = int((time.time() - value.time) % 60)
            if t >= value.secs:
                if value.mode == "timeout":
                    print(f"RUNNING: {key} MODE: {value.mode}")
                    value.function(*value.args, **value.kwargs)
                    self.cancel(key)
                else:
                    print(f"RUNNING: {key} MODE: {value.mode}")
                    value.function(*value.args, **value.kwargs)
                    value.time = time.time()

        for key in self._cancelled:
            del self._timers[key]
            print(f"CANCELLED: {key}")
        self._cancelled = list()

if __name__=="__main__":
  timer = Time()
  timer.setTimeout("test", 3, print, "#" * 80)
  timer.setInterval("test2", 2, print, "#" * 80)
  while True:
    timer.run()
