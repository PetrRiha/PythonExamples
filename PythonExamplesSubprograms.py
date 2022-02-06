''' 
Example
def get_name():
    user_name = input("Input your  name")
    return user_name

def print_Msg(user_name):
    print("Hello", user_name)

def main():
    user_name = get_name()
    print_Msg(user_name)

main()
 
''' 

def ask_user():
    number = int(input("Insert a number "))
    return number

def count(number):
    start = 1
    while start <= number:
        start = start + 1
        print(start)
def main():
    number = ask_user()
    count(number)
    


main()



