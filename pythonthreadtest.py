import threading
import subprocess

def run_subprocess():
    subprocess.run(["python", "C:\\Users\\power\\Desktop\\threesecsleeper.py"])

def crawl_something_periodically():
    pass

for i in range(5):
    print('[main] loop {}'.format(i))
    run_subprocess()