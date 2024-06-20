import time

def usingWhile():
    i = 0
    while i < 50001:
        i = i + 1
        print(i)

def usingFor():
    for i in range(1,50001):
        print(i)

# init = time.time()
# usingWhile()
# t1 = (time.time() - init)
# init = time.time()
# usingFor()
# print(time.time() - init)
# print(t1)

# print(1)
# time.sleep(3)
# print("Print after 3 seconds")

# t = time.localtime()
# formated_time = time.strftime("%y-%m-%d %H:%M:%S",t)

# print(formated_time)


# current_time = time.time()
# formatted_time = time.ctime(current_time)
# print(formatted_time)


# start_time = time.perf_counter()

# Do something that takes time
# time.sleep(2)

# end_time = time.perf_counter()
# elapsed_time = end_time - start_time
# print(f"Elapsed time: {elapsed_time} seconds")

current_time = time.time()
# utc_time = time.gmtime(current_time)
# local_time = time.localtime(current_time)

# print(f"UTC time: {utc_time}")
# print(f"Local time: {local_time}")

print(time.localtime(current_time))

