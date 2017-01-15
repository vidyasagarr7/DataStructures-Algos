

"""
The Stock Span Problem

The stock span problem is a financial problem where we have a series of n daily price quotes for a stock
and we need to calculate span of stock’s price for all n days.

The span Si of the stock’s price on a given day i is defined as the maximum number of consecutive days
just before the given day, for which the price of the stock on the current day is less than or equal to its
 price on the given day.

For example, if an array of 7 days prices is given as {100, 80, 60, 70, 60, 75, 85}, then the span values
for corresponding 7 days are {1, 1, 1, 2, 1, 4, 6}

"""

def stock_span(input_list):
    if not input_list :
        return
    else :
        stac = []

        stac.append(0)
        arr = [1]*len(input_list)

        for i in range(1,len(input_list)):

            while len(stac) >= 0 and input_list[stac[-1]] <= input_list[i] :
                stac.pop()

            if len(stac) == 0 :
                arr[i] = i+1
            else :
                arr[i] = i - stac[-1]

            stac.append(i)
        return arr


def span(input_list):
    if not input_list :
        return
    else :
        array = [1]*len(input_list)
        stac = [0]

        for i in range(1,len(input_list)) :

            while len(stac) >= 0 and input_list[stac[-1]] <= input_list[i] :
                stac.pop()

            if len(stac) == 0 :
                array[i] = i+1
            else :
                array[i] = i - stac[-1]

            stac.append(i)
        return array



if __name__=='__main__':
    test = [100, 80, 60, 70, 60, 75, 85]
    print(stock_span(test))

    print(span(test))