# Given an input string, return the number of times that the string "code" appears anywhere in the string, except we'll accept any letter for the 'd', so "cope" and "cooe" count.

# count_code('aaacodebbb') → 1
# count_code('codexxcode') → 2
# count_code('cozexxcope') → 2

# define start and end pointers where start is 0 and end is 3, define count as 0
# loop from end to len(str)-1
# every itr, define sub as the str from start to end. 
# check if sub and 'co'+sub[2]+'e' are equal, then count+=1 else start+=1 and end+=1
# return count outside the loop
def count_code(s):
    if len(s) < 4:  # If the string length is less than 4, return 0 because "code" cannot fit in it.
        return 0
    count=0
    for i in range(len(s)-3):
        if s[i:i+2] == 'co' and s[i+3]=='e':
            count+=1
    
    return count;
print(count_code('aaacodebbb'))