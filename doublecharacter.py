def double(string):
    newWord = ''
    for i in string:
        newWord += i*multiplier
        print(newWord)
    print()
    print(newWord)

word = input('What is the word?\n')
multiplier = int(input('Double? Triple? Enter the number of letters to multiply the letters\n'))
double(word)
