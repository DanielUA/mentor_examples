from adress_book import AdressBook
from my_logger import input_error_loger, logging

def parse_input(user_input):
    cmd, *args = user_input.strip().split(" ")
    return cmd, args

@input_error_loger
def add_user(args, adress_book):
    name, phone = args
    adress_book.update({name: phone})
    logging.info(f"User added {name, phone}") 
    print("User added")
 

def main():
    adress_book = AdressBook()
    while True:
        user_input = input("enter command: ")
        command, args = parse_input(user_input)

        if command == 'add':
            add_user(args, adress_book)           
        elif command == 'all':
            print(adress_book)
        
        elif command == 'exit':
            print("Good bye")
            break

if __name__ == "__main__":
    main()

        
