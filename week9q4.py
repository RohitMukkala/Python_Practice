import threading

def delayed_function(milliseconds, func, *args, **kwargs):
    def wrapper():
        func(*args, **kwargs)
    
    timer = threading.Timer(milliseconds / 1000.0, wrapper)
    timer.start()


def my_function(message):
    print(f"Function invoked with message: {message}")

delayed_function(2000, my_function, "Hello after 2 seconds!")

