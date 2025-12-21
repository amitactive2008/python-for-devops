import psutil
import humanize
import sys

def check_cpu_thresold():
    cpu_thresold = int(input('Please give cpu % : '))
    current_cpu = psutil.cpu_percent(interval=1)
    print(f'Current cpu % is {current_cpu}')
    if current_cpu > cpu_thresold:
        print('High CPU alert Send ....')
    else:
        print('CPU is good now')
check_cpu_thresold()


