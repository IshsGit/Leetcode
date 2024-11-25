# Given a list of non-negative integers, return a list of those numbers multiplied by 2, omitting any of the resulting numbers that end in 2.

# two2([1, 2, 3]) → [4, 6]
# two2([2, 6, 11]) → [4]
# two2([0]) → [0]

def two2(nums):
    if nums == [0]:
        return [0];
    result=[]
    for num in nums:
        if '2' not in str(num*2):
            result.append(num*2)
    
    return result;

print(two2([0]))
