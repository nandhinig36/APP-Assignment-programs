import os
from datetime import datetime

def run():
    root = "task1/task2/task3"
    os.makedirs(root, exist_ok=True)
    sample = os.path.join(root, "sample.py")
    with open(sample, "w", encoding="utf-8") as file:
        file.write('print("Hello from sample.py")\n')
    print("Current directory:", os.getcwd())
    print("Directory exists:", os.path.isdir(root))
    total_size = 0
    for folder, dirs, files in os.walk("task1"):
        print("Directory:", folder)
        for name in files:
            path = os.path.join(folder, name)
            total_size += os.path.getsize(path)
            stat = os.stat(path)
            print(name, "accessed:", datetime.fromtimestamp(stat.st_atime))
            print(name, "modified:", datetime.fromtimestamp(stat.st_mtime))
    print("Total file size:", total_size, "bytes")
    print("Contents:", os.listdir("task1"))

if __name__ == "__main__":
    run()
