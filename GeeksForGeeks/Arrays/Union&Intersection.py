


"""
Union and Intersection of two sorted arrays
Given two sorted arrays, find their union and intersection.

For example, if the input arrays are:
arr1[] = {1, 3, 4, 5, 7}
arr2[] = {2, 3, 5, 6}
Then your program should print Union as {1, 2, 3, 4, 5, 6, 7} and Intersection as {3, 5}.

"""

def union_intersection(list1,list2):
    if not list1 :
        return list2
    if not list2 :
        return list1
    else :
        union = []
        inter = []
        first = 0
        second = 0
        while first < len(list1) and second < len(list2):
            if list1[first] == list2[second] :
                inter.append(list1[first])
                union.append(list1[first])
                first += 1
                second += 1
            elif list1[first] < list2[second] :
                union.append(list1[first])
                first += 1
            else :
                union.append(list2[second])
                second += 1
        while first < len(list1) :
            union.append(list1[first])
            first += 1

        while second < len(list2) :
            union.append(list2[second])
            second += 1

        return union,inter


if __name__=='__main__':
    list1 = [1, 3, 4, 5, 7]
    list2 = [2, 3, 5, 6]
    print(union_intersection(list1,list2))