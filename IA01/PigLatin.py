import sys

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

j = 0
i = 0
argv_length = len(sys.argv)

for j in range(1,argv_length):
    word = sys.argv[j]
    new_word = ""

    if word[i] in vowels:
        if word[0].isupper():
            new_word = word[0] + word[1:] + 'way' + ' '
        else:
            new_word = word[0:] + 'way' + ' '
    else:
        if word[0].isupper():
            new_word = word[1].upper() + word[2:] + word[0].lower() + 'ay' + ' '
        else:
            new_word = word[1:] + word[0] + 'ay' + ' '

    print(new_word, end='')
