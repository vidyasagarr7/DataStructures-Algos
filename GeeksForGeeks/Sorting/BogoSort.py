
import random


def bogo_sort(input_list):
    """
    Randomly permutes the list till all the elements in the list are in sorted order
    :param input_list:
    :return:
    """
    while is_sorted(input_list) is False :
        shuffle(input_list)

    return input_list

def is_sorted(input_list):

    for i in range(len(input_list)-1):
        if input_list[i] > input_list[i+1]:
            return False
    return True


def shuffle(input_list):
    for i in range(len(input_list)):
        random_num = random.randint(i,len(input_list)-1)
        input_list[i],input_list[random_num]=input_list[random_num],input_list[i]

if __name__=="__main__":
    test_input = [3,5,7,9,2,54,65]
    print(bogo_sort(test_input))


