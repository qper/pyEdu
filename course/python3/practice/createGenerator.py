from tqdm import tqdm


def generator(n):
    count = 0
    while True:
        if count < n:
           yield count
           count += 1
        else:
            break


gen_instance = generator(10**6)

for i in tqdm(gen_instance):
    print(i)