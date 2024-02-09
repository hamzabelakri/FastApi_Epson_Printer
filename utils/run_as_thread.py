# This function uses the threading module to create a new thread and
# run the function in that thread. The @run_in_thread decorator syntax
# is a shortcut for calling the run_in_thread function and passing
# the result to the foo function as a decorator.
# You can use this function to run any function in a
# separate thread by adding the @run_in_thread decorator to the function definition.

import queue
import threading


def run_in_thread(function):
    def wrapper(*args, **kwargs):
        thread = threading.Thread(target=function, args=args, kwargs=kwargs)
        thread.start()
    return wrapper


##how to use it just add @run_in_thread  before the function
#@run_in_thread
#def foo(x, y):
#    print(x + y)


# This will run "foo" in a separate thread
#foo(1, 2)