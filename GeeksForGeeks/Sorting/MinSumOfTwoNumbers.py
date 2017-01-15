

def min_sum_two_numbers(input_list):
    input_list.sort()
    summation=0
    first_non_zero = 0
    for i in range(len(input_list)):
        if input_list[i] != 0:
            first_non_zero=i
            break
    input_list = input_list[first_non_zero:]
    for i in range(0,len(input_list) if len(input_list)%2==0 else len(input_list)-1,2):
        summation = summation*10 + (input_list[i]+input_list[i+1])

    return summation




if __name__=="__main__":
    test_odd_input = [5,3,0,7,4]
    test_even_input= [6,8,4,5,2,3]
    print(min_sum_two_numbers(test_even_input))
    print(min_sum_two_numbers(test_odd_input))
