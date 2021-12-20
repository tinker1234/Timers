# Timers
a class that allows setInterval and setTimeout 


# Example


```py
timer = Time()
timer.setTimeout("test", 3, print, "#" * 80)
timer.setInterval("test2", 2, print, "#" * 80)
while True:
  timer.run()
```
