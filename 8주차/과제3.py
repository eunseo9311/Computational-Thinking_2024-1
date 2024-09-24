import time
i = 0
while i < 20:
    i += 1
    if i % 3 == 0:
        print("clap")
        time.sleep(0.5)
    else:
        print(i)
        time.sleep(0.5)
