

"""
Find number of Employees Under every Employee
Given a dictionary that contains mapping of employee and his manager as a number of (employee, manager) pairs
like below.

{ "A", "C" },
{ "B", "C" },
{ "C", "F" },
{ "D", "E" },
{ "E", "F" },
{ "F", "F" }

In this example C is manager of A,
C is also manager of B, F is manager
of C and so on.


Write a function to get no of employees under each manager in the hierarchy not just their direct reports.
It may be assumed that an employee directly reports to only one manager. In the above dictionary the root node/ceo is
listed as reporting to himself.

Output should be a Dictionary that contains following.

A - 0
B - 0
C - 2
D - 0
E - 1
F - 5

"""

# Assuming on there can only be a single manager for an employee
def find_no_emp(input_dict):
    if not input_dict :
        return
    else :

        manager_emp_dict = {}

        for e,m in input_dict.items() :
            if m not in manager_emp_dict :
                manager_emp_dict[m] = [e]
            else :
                manager_emp_dict[m].append(e)

        out_dict = {}

        for e,m in input_dict.items() :
            if e not in manager_emp_dict :
                out_dict[e] = 0
            else :
                count = 0
                for x in manager_emp_dict[e] :
                    if x is not e :
                        if x not in manager_emp_dict :
                            count += 1
                        else :
                            count += len(manager_emp_dict[x])+1

                out_dict[e] = count

        for e,count in out_dict.items() :
            print('employee : {} and count : {}'.format(e,count))

if __name__=='__main__':
    input_dict = {'a':'c','b':'c','c':'f','d':'e','e':'f','g':'f','f':'f'}
    find_no_emp(input_dict)




