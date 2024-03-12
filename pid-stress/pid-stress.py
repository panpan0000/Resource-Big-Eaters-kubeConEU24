import time
import os
import multiprocessing

def worker(counter):
    while True:
        try:
            pid = os.fork()
            if pid < 0:
                print("Failed to fork a child process")
                print("Error code: ", os.errno)
                time.sleep(0.5)
            elif pid == 0:
                # sub-sub-Process
                with counter.get_lock():
                    counter.value += 1
                if counter.value > 5000: 
                    time.sleep(0.01)
                print(f"This is the child process. Total processes: {counter.value}")
                exit(0)
        except Exception as e:
                print("Exception : ",e)
                time.sleep(1)

if __name__ == '__main__':
    counter = multiprocessing.Value('i', 0)
    
    # Create several sub-process
    processes = []
    for _ in range(5):
        p = multiprocessing.Process(target=worker, args=(counter,))
        p.start()
        processes.append(p)
    
    # wait for all sub-process
    for p in processes:
        p.join()
    
    print("All processes have finished. Total processes created: ", counter.value)
