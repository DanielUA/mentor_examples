from threading import Thread


def read_file(file):
    data = []
    with open(file, "r") as fh:
        lines = fh.readline()
        lines = lines.split(" ")
    for line in lines:
        data.append(line)
    print(f"{data}")

def main():
    file_1 = "text_1.txt"
    file_2 = "text_2.txt"

    th1 = Thread(target=read_file(file_1))
    th2 = Thread(target=read_file(file_2))
    
    th1.start()
    th2.start()

    th1.join()
    th2.join()

    
if __name__=="__main__":
    main()