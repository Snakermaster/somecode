import time

from fangall import app


@app.task
def show_msg(content):
    print(content)


@app.task
def foo(message):
    time.sleep(5)
    print(message)






