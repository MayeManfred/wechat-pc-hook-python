#coding=utf-8
"""
运行前，安装
python -m pip install --upgrade pip
pip install apscheduler

"""
import os,time
#导入apscheduler线程模块
from apscheduler.schedulers.background import BackgroundScheduler
"""
从read.txt中获取到实时数据信息
判断是否是自己需要的内容
是自己需要的内容就一条一条的写入到web爆料中去
"""
def tick_go_read_to_webBaoLiao():
    print('tick_go_read_to_webBaoLiao!')


"""
实时读取webxx地区信息
判断是否有新信息条目
有新就一条一条的发送到微信和写入到web爆料中
"""
def tick_go_webDiQu_to_wx_and_webBaoLiao():
    print('tick_go_webDiQu_to_wx_and_webBaoLiao!')

#运行
if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    # 间隔3秒钟执行一次
    scheduler.add_job(tick_go_read_to_webBaoLiao, 'interval', seconds=3)
    # 这里的调度任务是独立的一个线程
    scheduler.start()
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
    try:
        # 其他任务是独立的线程执行
        while True:
            time.sleep(2)
            print('sleep!')
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
        print('Exit The Job!')