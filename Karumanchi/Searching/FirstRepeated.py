 
def first_repeated(input_list):
	"""
	O(n^2) solution for finding the first repeated element
	"""	
	for i in range(len(input_list)):	
		for j in range(i+1,len(input_list)):
			if input_list[i]==input_list[j]:
				return input_list[i]

### complete after learning hashing ####
def _first_repeated(input_list):
	"""
	Use hasing technique to find the first repeated element
	"""
	temp_dict = {}
	for i in range(len(input_list):
		if input_list[i] not in temp_dict:
		



 __name__=="__main__":
	test = [3,4,2,1,4,5,5,5,5]
	print(first_repeated(test))

