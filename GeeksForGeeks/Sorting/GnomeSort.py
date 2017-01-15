

def gnome_sort(input_list):
    """
    Gnome Sort / Stupid Sort
    :param input_list:
    :return:
    """
    i=1
    while True:
        if i < len(input_list)-1:
            if input_list[i] >= input_list[i - 1]:
                i += 1
            if input_list[i] < input_list[i-1]:
                input_list[i],input_list[i-1]=input_list[i-1],input_list[i]
                i-=1
        if i==0:
            i+=1
        if i==len(input_list)-1:
            break
    return input_list

if __name__=="__main__":
    test_input=[2,5,3,7,8,1,4,7]
    print(gnome_sort(test_input))

