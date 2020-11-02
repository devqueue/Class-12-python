'''
Write a Python program to read a text file line by line and display the number of vowels/ consonants / upper case letters and lower case characters.
'''

vowels = ['a','e','i','o','u']
vowels_count = 0
consonat_count = 0
upper_count = 0
lower_count = 0


file = open('story.txt', 'r')
data = file.read()
print(data)
for ch in data:
    if str.isupper(ch):
        upper_count += 1
    elif str.islower(ch):
        lower_count += 1
    ch2 = str.lower(ch)
    if ch2 in vowels:
        vowels_count+=1
    elif ch2 not in vowels:
        consonat_count+=1

print(f"No. of vowels are {vowels_count}")
print(f"No. of vowels are {consonat_count}")
print(f"No. of vowels are {upper_count}")
print(f"No. of vowels are {lower_count}")
file.close()