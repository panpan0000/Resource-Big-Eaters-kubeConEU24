import os

import time
#Create file descriptor
#for i in range(10000):
i=0

while True:
    try:
        i=i+1;
        fd = os.open("/tmp/test_file_" + str(i), os.O_CREAT)
        print(f"File descriptor {fd} created for file test_file_{i}")
        if i > 65500:
            time.sleep(0.1)
    except Exception as e:
        print("catch error: ", e)
        break;
