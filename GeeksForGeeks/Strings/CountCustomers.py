

"""
Function to find Number of customers who could not get a computer
Write a function “runCustomerSimulation” that takes following two inputs
a) An integer ‘n’: total number of computers in a cafe and a string:
b) A sequence of uppercase letters ‘seq’: Letters in the sequence occur in pairs. The first occurrence indicates the arrival of a customer; the second indicates the departure of that same customer.

A customer will be serviced if there is an unoccupied computer. No letter will occur more than two times.
Customers who leave without using a computer always depart before customers who are currently using the computers. There are at most 20 computers per cafe.

For each set of input the function should output a number telling how many customers, if any walked away without using a computer. Return 0 if all the customers were able to use a computer.

runCustomerSimulation (2, “ABBAJJKZKZ”) should return 0

runCustomerSimulation (3, “GACCBDDBAGEE”) should return 1 as ‘D’ was not able to get any computer

runCustomerSimulation (3, “GACCBGDDBAEE”) should return 0

runCustomerSimulation (1, “ABCBCA”) should return 2 as ‘B’ and ‘C’ were not able to get any computer.

runCustomerSimulation(1, “ABCBCADEED”) should return 3 as ‘B’, ‘C’ and ‘E’ were not able to get any computer.

"""

def count_customers(input_string,k):
    if not input_string or k <= 0 :
        return 0
    else :
        count = 0
        in_use = {}
        in_wait = {}
        for i in range(len(input_string)) :
            if input_string[i] not in in_use and len(in_use) < k :
                in_use[input_string[i]] = 1
            elif input_string[i] in in_use :
                del in_use[input_string[i]]
            else :
                if input_string[i] not in in_wait :
                    in_wait[input_string[i]] = 1
                    count += 1
                else :
                    del in_wait[input_string[i]]
        return count

if __name__=='__main__':
    test = list('ABBAJJKZKZ')
    print(count_customers(test,2))

    test = list('GACCBDDBAGEE')
    print(count_customers(test,3))

    test = list('GACCBGDDBAEE')
    print(count_customers(test,3))

    test = list('ABCBCA')
    print(count_customers(test,1))

    test = list('ABCBCADEED')
    print(count_customers(test,1))