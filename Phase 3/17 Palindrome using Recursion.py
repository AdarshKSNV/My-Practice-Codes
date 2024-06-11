def palindrome(s):
    s = s.lower().replace(" ", "")
    if len(s) <= 1:
        return True
    else:
        if s[0] == s[-1]:
            return palindrome(s[1:-1])
        else:
            return False

input_string="Pragati"
if palindrome(input_string):
    print(input_string,"is palindrome")
else:
    print(input_string,"is not a palindrome")