from threading import Thread


def read_sort(file):
    data = []
    with open(file, "r") as fh:
        lines = fh.readline().split(" ")
    for line in lines:
        data.append(int(line))
    return(data)

def odd(data):
    res = [x for x in data if x%2 == 0]
    print(res)

def even(data):
    res = [x for x in data if x%2 != 0]
    print(res)


def main():
    data_list = read_sort("text_1.txt")
 
    th1 = Thread(target=odd(data_list))
    th2 = Thread(target=even(data_list))

    th1.start()
    th2.start()

    th1.join()
    th2.join()


if __name__=="__main__":
    main()