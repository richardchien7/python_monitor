import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, LoggingEventHandler
from watchdog.observers.api import ObservedWatch


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path == r"C:\Users\Admin\Desktop\python monitor":
            print("log file %s changed!" % event.src_path)


if __name__ == "__main__":
    event_handler1 = MyHandler()
    observer = Observer()
    watch = observer.schedule(event_handler1, path='.', recursive=True)
    # 基礎設定
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

    event_handler2 = LoggingEventHandler()#標記標記~觸發事件顯示資訊
    observer.add_handler_for_watch(event_handler2, watch)  # 为watch新添加一个event handler
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:       #KeyboardInterrupt	引發當用戶按下中斷程序執行
        observer.stop()
    observer.join()