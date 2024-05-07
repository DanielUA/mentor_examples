from threading import Thread

def read_file(file):
    data = []
    with open(file, "r") as fh:
        lines = fh.readline().split(" ")
        for line in lines:
            data.append(int(line))
    return data

def sort_file(data):
    data.remove(min(data))
    data.remove(max(data))
    print(data) 
    

def main():
    file_1 = "text_1.txt"
    file_2 = "text_2.txt"
    data_1 = read_file(file=file_1)
    data_2 = read_file(file=file_2)

    sort_file(data = data_1)

    th1 = Thread(target=sort_file(data_1))
    th2 = Thread(target=sort_file(data_2))

    th1.start()
    th2.start()

    th1.join()
    th2.join()


if __name__ == "__main__":
    main()