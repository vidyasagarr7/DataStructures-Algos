
"""
Find maximum depth of nested parenthesis in a string

We are given a string having parenthesis like below
     “( ((X)) (((Y))) )”
We need to find the maximum depth of balanced parenthesis, like 4 in above example.
Since ‘Y’ is surrounded by 4 balanced parenthesis.

If parenthesis are unbalanced then return -1.

More examples:

S = "( a(b) (c) (d(e(f)g)h) I (j(k)l)m)";
Output : 4

S = "( p((q)) ((s)t) )";
Output : 3

S = "";
Output : 0

S = "b) (c) ()";
Output : -1

S = "(b) ((c) ()"
Output : -1


"""

def max_depth(input_string):
    if not input_string :
        return 0
    else :
        if len(input_string) == 0 :
            return 0
        stac = []
        max_len = 0
        open_brace = '('
        close_brace = ')'
        for char in input_string :
            if char in open_brace :
                stac.append(char)
                if len(stac) > max_len :
                    max_len = len(stac)
            elif char in close_brace :
                if len(stac) ==0  :
                    return -1
                popped = stac.pop()
                if open_brace.index(popped) != close_brace.index(char) :
                    return -1
        if len(stac) > 0 :
            return -1
        return max_len

if __name__=='__main__':
    string = '( a(b) (c) (d(e(f)g)h) I (j(k)l)m)'
    print(max_depth(list(string)))

    string = '( p((q)) ((s)t) )'
    print(max_depth(list(string)))

    string = ''
    print(max_depth(list(string)))

    string = 'b) (c) ()'
    print(max_depth(list(string)))

    string = '(b) ((c) ()'
    print(max_depth(list(string)))




