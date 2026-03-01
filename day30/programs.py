#Write a program to check whether a character is a vowel or consonant. If it is a vowel, check whether it is uppercase or lowercase.
ch=input("Enter character :")
if ch in "aeiouAEIOU":
    print("ch is vowel")
    if ch.islower():
        print("lowercase")
    else:
        print("uppercase")
else:
    print("consonant")