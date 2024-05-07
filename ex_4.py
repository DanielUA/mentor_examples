import numpy as np

from collections import Counter
from threading import Thread

def parts(file):
    data = []
    with open(file, "r") as fh:
        lines = fh.readline().split(" ")
    for line in lines:
        data.append(int(line))
     
    sublists = [list(x) for x in np.array_split(data, 3)]
    return sublists


def counts(lst, index):
    res = Counter(lst[index])
    print(res)


def main():
    data = parts("text_2.txt")
    th1 = Thread(target=counts(data, 0))
    th2 = Thread(target=counts(data, 1))
    th3 = Thread(target=counts, args=(data, 2))
    
    th1.start()
    th2.start()
    th3.start()

    th1.join()
    th2.join()
    th3.join()

if __name__ == "__main__":
    main()