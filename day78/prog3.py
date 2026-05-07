#Function to Find Frequency of Each Character
def frequency_ch(name):
    freq={}
    for ch in name:
        if ch in freq:
            freq[ch]+=1
        else:
            freq[ch]=1
    return freq
print(frequency_ch("keerthi"))#{'k': 1, 'e': 2, 'r': 1, 't': 1, 'h': 1, 'i': 1}