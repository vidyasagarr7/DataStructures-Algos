

"""
Function to find Number of customers who could not get a computer

Write a function “runCustomerSimulation” that takes following two inputs
a) An integer ‘n’: total number of computers in a cafe and a string:
b) A sequence of uppercase letters ‘seq’: Letters in the sequence occur in pairs.
The first occurrence indicates the arrival of a customer; the second indicates the departure of that same customer.

A customer will be serviced if there is an unoccupied computer. No letter will occur more than two times.
Customers who leave without using a computer always depart before customers who are currently using the computers.
There are at most 20 computers per cafe.

For each set of input the function should output a number telling how many customers, if any walked away without
 using a computer. Return 0 if all the customers were able to use a computer.

runCustomerSimulation (2, “ABBAJJKZKZ”) should return 0

runCustomerSimulation (3, “GACCBDDBAGEE”) should return 1 as ‘D’ was not able to get any computer

runCustomerSimulation (3, “GACCBGDDBAEE”) should return 0

runCustomerSimulation (1, “ABCBCA”) should return 2 as ‘B’ and ‘C’ were not able to get any computer.

runCustomerSimulation(1, “ABCBCADEED”) should return 3 as ‘B’, ‘C’ and ‘E’ were not able to get any computer.

"""

def count_customers(input_string,k):
    if not input_string  :
        return
    else :
        num = k
        htable = {}
        count = 0
        inside = {}
        for char in input_string :
            if char in htable :
                del htable[char]
                if char in inside :
                    del inside[char]
                    num += 1
            else :
                if num > 0  :
                    htable[char] = 1
                    inside[char] = 1
                    num -= 1
                else :
                    htable[char] = 1
                    count += 1
        return count

if __name__=='__main__':
    print(count_customers('ABBAJJKZKZ',2))
    print(count_customers('GACCBDDBAGEE',3))
    print(count_customers('GACCBGDDBAEE',3))
    print(count_customers('ABCBCA',1))
    print(count_customers('ABCBCADEED',1))
