def solve(s):
    a_string = s.split(' ')
    ans = (' '.join((word.capitalize() for word in a_string)))
    return ans
