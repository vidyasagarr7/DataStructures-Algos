
def remove_adjacent_duplicates(input_string):
    stack=[]
    for char in input_string:
        if len(stack)==0:
            stack.append(char)
            continue
        if stack[-1] != char:
            stack.append(char)
        elif stack[-1]==char:
            stack.pop()
    return stack

if __name__=="__main__":
    test_string = 'careermonk'
    test_string1 = 'mississippi'
    print(remove_adjacent_duplicates(test_string))
    print(remove_adjacent_duplicates(test_string1))