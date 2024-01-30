# 4. Write a python program to read a text fileaissce.txt & display the number of vowels,
#    consonants, uppercase, lowercase characters in the file.

filename = "fileaissce.txt"

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

vowels_count = 0
consonants_count = 0
uppercase_count = 0
lowercase_count = 0

with open(filename, 'r') as file:
    for char_data in file.read():
        if char_data.isalpha() == False:
            continue

        if char_data.isupper():
            uppercase_count += 1

        if char_data.islower():
            lowercase_count += 1

        # if char_data.lower() in vowels:
        if char_data in vowels:
            vowels_count += 1
        else:
            consonants_count += 1


print("vowels_count :", vowels_count)
print("consonants_count :", consonants_count)
print("uppercase_count :", uppercase_count)
print("lowercase_count :", lowercase_count)
