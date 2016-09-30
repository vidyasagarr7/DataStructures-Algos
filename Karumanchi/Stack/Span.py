
def find_span(input_list):
    """
    O(n^2) algorithm to find the span of numbers in a list
    :param input_list:
    :return:
    """
    temp = [None]*len(input_list)
    for i in range(len(input_list)):
        j=i
        while j>=0 and input_list[j] <= input_list[i]:
            j-=1
        temp[i]=i-j
    return temp

def _find_span(input_list):
    """
    O(n) solution
    :param input_list:
    :return:
    """
    stack = []
    stack.append(0)     # appending indices into the stack.
    output = [None]*len(input_list)
    output[0] = 1
    for i in range(1,len(input_list)):
        while len(stack)>0 and input_list[stack[0]]<=input_list[i] :
            stack.pop()
        output[i]= i+1 if len(stack)==0 else i-stack[0]
        stack.append(i)
    return output

if __name__=="__main__":
    test_input= [6,3,4,5,2]
    test_input1=[1,2,3,4,5,6,7,8]
    print(_find_span(test_input1))
    print(find_span(test_input1))
