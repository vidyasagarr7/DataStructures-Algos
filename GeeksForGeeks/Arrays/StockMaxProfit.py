

"""
Stock Buy Sell to Maximize Profit

The cost of a stock on each day is given in an array, find the max profit that you can make by buying and
 selling in those days. For example, if the given array is {100, 180, 260, 310, 40, 535, 695},
 the maximum profit can earned by buying on day 0, selling on day 3. Again buy on day 4 and sell on day 6.
 If the given array of prices is sorted in decreasing order, then profit cannot be earned at all.



"""

def max_profit(input_list):
    if not input_list :
        return 0
    else :
        total_profit = 0
        profit = 0
        start = 0
        max_prof = 0
        for i in range(1,len(input_list)):
            profit = input_list[i] - input_list[start]
            if profit >= max_prof and i < len(input_list)-1:
                max_prof = profit

            else :
                total_profit += max_prof
                if i == len(input_list)-1 :
                    print('buy at {} and sell at {}'.format(start,i))
                else :
                    print('buy at {} and sell at {}'.format(start, i-1))
                start = i

        return total_profit

if __name__=='__main__':
    test = [100, 180, 260, 310, 40, 535, 695]
    print(max_profit(test))