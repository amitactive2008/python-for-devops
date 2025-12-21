import psutil 
import humanize

def check_disk():
    for disk in psutil.disk_partitions():
        mp = disk.mountpoint
        print(f'{mp} : {humanize.naturalsize(psutil.disk_usage(mp).used)}')

def check_mem():
    print(f'Mem Percent used : {psutil.virtual_memory().percent} %')
def check_cpu():
    cpu_percent= psutil.cpu_percent(interval=1)
    print(f"CPU Percent : {cpu_percent}")
    print(f"1 min Load Avg : {psutil.getloadavg()[0]}")

check_disk()
check_mem()
check_cpu()
