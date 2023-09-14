# decodes the coded word as long as the correct seed is selected
def decoder(seed):
    print('Please enter the word to decode')
    codeword = input()
    word = []
    baseword = []
    for i, letter in enumerate(codeword):
        if (i % 2) == 0:
            baseword += chr(ord(codeword[i]) + (int(seed) * 3))
        elif (i % 2) != 0:
            baseword += chr(ord(codeword[i]) + (int(seed) // 2))

    for i, letter in enumerate(baseword):
        newletter = chr(ord(baseword[i]) + int(seed))
        word.append(newletter)
    worded = ' '.join(word).replace(" ", "")
    print(worded)
