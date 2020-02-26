#
# Python:   3.6.4
#
# Author:   Brian Hobbs
#
# Purpose: Python course class assignment


# def start():
#     print("Hello {}".format(get_name()))
#
#
# def get_name():
#     name = input("What is your name?: ")
#     return name


# def get_number():
#     number = 12
#     return number

def start():
    f_name = "Sarah"
    l_name = "Connor"
    age = 28
    gender = "female"
    get_info(f_name, l_name, age, gender)


def get_info(f_name, l_name, age, gender):
    print("My name is {} {}. I am {} yearold {} ".format(f_name, l_name, age, gender))


if __name__ == "__main__":
    start()
