#Write a program to count the frequency of each character in a given string using a dictionary.
s="keerthi"
freq={}
for ch in s:
    freq[ch]=freq.get(ch,0)+1
print(freq)#{'k': 1, 'e': 2, 'r': 1, 't': 1, 'h': 1, 'i': 1}



#Write a program to count the frequency of each word in a sentence using a dictionary.
s="hi hi iam keerthi"
s=list(s.split())
freq={}
for word in s:
    freq[word]=freq.get(word,0)+1
print(freq)#{'hi': 2, 'iam': 1, 'keerthi': 1}



#Write a program to find the first non-repeating character in a string using a dictionary.
s="keerthi"
freq={}
for ch in s:
    freq[ch]=freq.get(ch,0)+1
    if freq[ch]==1:
        print("first non repeating character:",ch)
        break
#first non repeating character: k

        





