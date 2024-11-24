# Given an array of scores sorted in increasing order, return true if the array contains 3 adjacent scores that differ from each other by at most 2, such as with [3, 4, 5] or [3, 5, 5]

# scoresClump([3, 4, 5]) → true
# scoresClump([3, 4, 6]) → false
# scoresClump([1, 3, 5, 5]) → true

# we can set 2 pointers, start is end-3 and end is len(scores)-1. The idea is every itr, we check if the diff between scores and start and scores at end is greater than 2, if it is then return false
# outside the loop return false
def scoresClump(scores):
    for i in range(len(scores)-2):
        if scores[i+2]-scores[i] <=2:
            return True;
    return False;

print(scoresClump([3, 4, 5]));