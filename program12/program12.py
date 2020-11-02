'''
write a Python program to find the most commonly occuring words in a text file or from sample of ten phising
'''
with open("email.txt", "r") as f:
    content = f.read()
    max = 0
    max_occuring_word = ""
    occurances_dict = {}
    words = content.split()
    for word in words:
        count = content.count(word)
        occurances_dict.update({word:count})
        if count>max:
            max=count
            max_occuring_word = word
    print(f"Most occuring word: {max_occuring_word}")
    print(f"Frequency of other words {occurances_dict}") 
