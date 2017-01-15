import sys

def first_repeated(input_list):
	"""
	O(n^2) solution for finding the first repeated element
	"""	
	for i in range(len(input_list)):	
		for j in range(i+1,len(input_list)):
			if input_list[i]==input_list[j]:
				return input_list[i]

def _first_repeated(input_list):
    """
    O(n) algorithm using hashing.
    :param input_list:
    :return:
    """
    min_idx= sys.maxsize
    temp_dict = {}
    for i in range(len(input_list)-1,-1,-1):
        if input_list[i] in temp_dict:
            if i < min_idx:
                min_idx = i
        else :
            temp_dict[input_list[i]]= i

    return input_list[min_idx]


if __name__=="__main__":
    test = [3,1,2,4,2,2,5,3]
    print(first_repeated(test))

    print(_first_repeated(test))