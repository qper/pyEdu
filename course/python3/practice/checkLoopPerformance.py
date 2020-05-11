from datetime import datetime
from tqdm import tqdm


def one(n):
    num_list = []
    start_time = datetime.now()
    for i in tqdm(range(10**n)):
        if i % 2 == 0:
            num_list.append(i)
    print(datetime.now() - start_time)
    return num_list


def two(n):
    start_time = datetime.now()
    num_list = [i for i in tqdm(range(10**n)) if i % 2 == 0]
    print(datetime.now() - start_time)
    return num_list


l1 = one(8)
l2 = two(8)
