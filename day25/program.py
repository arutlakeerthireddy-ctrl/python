#Write a program to check whether two strings are anagrams using a dictionary.
s1="listen"
s2="silent"
freq1={}
freq2={}
for ch in s1:
    freq1[ch]=freq1.get(ch,0)+1
for ch in s2:
    freq2[ch]=freq2.get(ch,0)+1
if freq1==freq2:
    print("strings are anagrams")
else:
    print("not anagrams")
#output:strings are anagrams


#Write a program to find duplicate elements in a list using a dictionary.
li=[1,2,2,3,4,4,3]
freq={}
for i in li:
    freq[i]=freq.get(i,0)+1
for key in freq:
    if freq[key]>1:
        print(key)
#2,3,4

#Write a program to find the element with the highest frequency in a list using a dictionary.
li=[1,2,2,3,4,4,4]
freq={}
for i in li:
    freq[i]=freq.get(i,0)+1
print(max(freq.items()))#(4, 3)
