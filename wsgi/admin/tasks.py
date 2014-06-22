from admin import wrk

@wrk.task()
def add_together(a, b):
    return a + b
