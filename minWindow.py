def minWindow(s, t):
    from collections import Counter
    if not s or not t:
        return ""
    t_count, s_count = Counter(t), Counter()
    required, formed = len(t_count), 0
    left, right = 0, 0
    window = float("inf"), None, None
    while right < len(s):
        char = s[right]
        s_count[char] += 1
        if char in t_count and s_count[char] == t_count[char]:
            formed += 1
        while left <= right and formed == required:
            char = s[left]
            if right - left + 1 < window[0]:
                window = right - left + 1, left, right
            s_count[char] -= 1
            if char in t_count and s_count[char] < t_count[char]:
                formed -= 1
            left += 1
        right += 1
    return s[window[1]:window[2] + 1] if window[0] != float("inf") else ""

