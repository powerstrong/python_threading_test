import threading
import subprocess
import time

class PythonThreadingTest:
    def main(self):
        self.is_generating = True

        thread1 = threading.Thread(target=self.crawl_something_periodically)
        thread1.start()
        for i in range(5):
            print('[main] loop {}'.format(i))
            self.run_subprocess()

        self.is_generating = False
        thread1.join()
        print('[main] finished!')

    # 한번 실행되면 한참동안 소식이 없어지는 서브프로세스
    def run_subprocess(self):
        subprocess.run(["python", "threesecsleeper.py"])

    # 주기적으로 뭔가 일을 뚝딱뚝딱..
    def crawl_something_periodically(self):
        while(self.is_generating):
            print(' [main] crawl_something_periodically()')
            time.sleep(1)
        pass


if __name__ == '__main__':
    PythonThreadingTest().main()