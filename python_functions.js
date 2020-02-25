my_sentence = "loves the color"
color_list = ['red', 'blue', 'yellow', 'black', 'teal', 'purple', 'green']


def colorFunc(name):
    my_list = []
    for i in color_list:
        msg = "{} {} {}".format(name, my_sentence, i)
        my_list.append(msg)
    return my_list


my_list = colorFunc('Sally')
for i in my_list:
    print(i)