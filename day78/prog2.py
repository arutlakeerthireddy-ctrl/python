#Write a function is_palindrome(n) that takes an integer n as input and returns True 
# if the number is a palindrome, otherwise returns False.
def is_palindrome(n):
    s=str(n)
    if s==s[::-1]:
        return True
    else:
        return False
print(is_palindrome(121))