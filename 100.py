import random

numbers = list(range(1, 101))
filtered_numbers = numbers[:]

to_remove = random.randint(0, 100)  # 22
for _ in range(to_remove):
    delete_index = random.randint(0, len(filtered_numbers))    # Initially 100
    filtered_numbers.remove(filtered_numbers[delete_index])

removed_numbers = []
for num in numbers:
    if num not in filtered_numbers:
        removed_numbers.append(num)
removed = len(removed_numbers)

print("original list={}".format(numbers))
print("list after removal of elements={}".format(filtered_numbers))
print("total numbers of elements removed={}".format(removed))
print("list of removed elements={}".format(removed_numbers))


# import time
# import timeit


# def heavy_tasks():
#     for i in range(0, 100):
#         print('Say hello to', 10**i)

#         time.sleep(0.1)


# def time_heavy_task():
#     starttime = timeit.default_timer()
#     heavy_tasks()
#     print('Time taken: ', timeit.default_timer()-starttime)


# time_heavy_task()
