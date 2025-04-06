import platform
import psutil

def system_info():
    print("System Information:")
    print("-------------------")
    print(f"Operating System: {platform.system()} {platform.release()}")
    print(f"Version: {platform.version()}")
    print(f"Platform: {platform.platform()}")
    print(f"Machine: {platform.machine()}")
    print(f"Processor: {platform.processor()}")
    print(f"Python Version: {platform.python_version()}")

    print("\nMemory Information:")
    mem = psutil.virtual_memory()
    print(f"Total Memory: {mem.total / (1024 ** 3):.2f} GB")
    print(f"Used Memory: {mem.used / (1024 ** 3):.2f} GB")
    print(f"Available Memory: {mem.available / (1024 ** 3):.2f} GB")
    print(f"Memory Usage: {mem.percent}%")
    
    print("\nDisk Information:")
    disk = psutil.disk_usage('/')
    print(f"Total Disk: {disk.total / (1024 ** 3):.2f} GB")
    print(f"Used Disk: {disk.used / (1024 ** 3):.2f} GB")
    print(f"Free Disk: {disk.free / (1024 ** 3):.2f} GB")
    print(f"Disk Usage: {disk.percent}%")
    
    print("\nCPU Information:")
    print(f"CPU Usage: {psutil.cpu_percent(interval=1)}%")
    print(f"Physical CPU Cores: {psutil.cpu_count(logical=False)}")
    print(f"Logical CPU Cores: {psutil.cpu_count(logical=True)}")

if __name__ == "__main__":
    system_info()
