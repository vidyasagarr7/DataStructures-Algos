

"""
Find Itinerary from a given list of tickets
Given a list of tickets, find itinerary in order using the given list.

Example:

Input:
"Chennai" -> "Banglore"
"Bombay" -> "Delhi"
"Goa"    -> "Chennai"
"Delhi"  -> "Goa"

Output:
Bombay->Delhi, Delhi->Goa, Goa->Chennai, Chennai->Banglore,
It may be assumed that the input list of tickets is not cyclic and there is one ticket from every city except
final destination.

"""

def find_itenary(input_dict):
    if not input_dict :
        return
    else:
        d2s_dict = {}

        for s,d in input_dict.items() :
            d2s_dict[d] = s

        source  = None
        dest = None

        for s,d in input_dict.items() :
            if s not in d2s_dict :
                source = s
        for d,s in d2s_dict.items() :
            if d not in input_dict :
                dest = d
        temp_d = source
        while True :
            print('{} -->'.format(temp_d),end='')
            temp_d = input_dict[temp_d]
            print(' {}'.format(temp_d))
            if temp_d is dest :
                break

if __name__=='__main__':
    input_dict = {'Chennai': 'Banglore', 'Bombay': 'Delhi', 'Goa': 'Chennai', 'Delhi': 'Goa'}
    find_itenary(input_dict)