"""test python threading module"""

import threading
import subprocess
import time

class PythonThreadingTest:
    """main class"""

    def __init__(self):
        self.is_generating = True

        thread1 = threading.Thread(target=self.crawl_something_periodically)
        thread1.start()
        for i in range(5):
            print(f'[main] loop {i}')
            self.run_subprocess()

        self.is_generating = False
        thread1.join()
        print('[main] finished!')

    def run_subprocess(self):
        """한번 실행되면 한참동안 소식이 없어지는 서브프로세스"""
        subprocess.run(["python", "threesecsleeper.py"], check=False)

    def crawl_something_periodically(self):
        """주기적으로 뭔가 일을 뚝딱뚝딱.."""
        while self.is_generating:
            print(' [main] crawl_something_periodically()')
            time.sleep(1)

if __name__ == '__main__':
    PythonThreadingTest()