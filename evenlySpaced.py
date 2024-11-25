# Given three ints, a b c, one of them is small, one is medium and one is large. 
# Return true if the three values are evenly spaced, so the difference between small and medium is the same as the difference between medium and large.

# evenlySpaced(2, 4, 6) → true
# evenlySpaced(4, 6, 2) → true
# evenlySpaced(4, 6, 3) → false

# first we need to define small, medium and large. Small can be initializd to the first element
# We can itr through the loop, for e/itr we can set small to the min between small and the current, medium which will be the max between medium and small, and large which will be the max between large and medium
# Then we can have an if condition to check diff of small/medium and equal to medium/large. If it is return true. Return false outside the if.

def evenlySpaced(a, b, c):
    sortedArr = sorted([a,b,c])
    small, medium, large = sortedArr
    if medium-small == large-medium:
        return True;

    return False;

print(evenlySpaced(2,3,6))
  