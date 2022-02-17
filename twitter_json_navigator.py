from re import L

from markupsafe import re
import twitter2
import json

def get_data(twitter_acc):
    try:
        with open("twitter2.json", "w") as file:
            json.dump(twitter2.data_return(twitter_acc), file, indent = 4)
        with open("twitter2.json", "r") as file1:
            user_data = json.load(file1)
        return user_data
    except Exception:
        return None

def get_acc_name():
    acc_name = input("Please, enter user's name, for whom you want to generate data: ")
    return acc_name

def main_parser(data):
    if isinstance(data, dict):
        for key in data:
            print(key)
        try:
            key_of_choice = input("The object is dictionary, please enter the key: ")
            main_parser(data[key_of_choice])
        except KeyError:
            print("Sorry, no such key in dictionary")
            return None
    elif isinstance(data, list):
        index_of_choice = int(input(f"The current object is list of len {len(data)}, choose index of next element: "))
        try:
            main_parser(data[index_of_choice])
        except IndexError:
            print("Sorry, incorrect input")
            return None
    else:
        print(f"Here is your data: {data}")
        return None


if __name__=="__main__":
    data = get_data(get_acc_name())
    main_parser(data)
