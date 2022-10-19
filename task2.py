import json

file = open('phones.json')
phones = json.load(file)


def func1():
    for i in phones:
        print(phones[i]["number"][6:])


#func1()


def func2():
    for i in phones:
        code = phones[i]["number"][3:6]
        if code == '050':
            print(code, " Vodafone")
        elif code == '096':
            print(code, " Kyivstar")
        else:
            print(code," Life")


#func2()