# creates a class called Cypher, used to generate the encrypted word

class Cypher:
    def __init__(self, word):
        self._codeword = word

    def get_codeword(self):
        return self._codeword

    def set_codeword(self, word, seed):
        firstpart = []
        codeword = []
        for i, letter in enumerate(word):
            newletter = chr(ord(word[i]) - seed)
            codeword.append(newletter)
        # print(codeword)
        for i, letter in enumerate(codeword):
            if (i % 2) == 0:
                firstpart += chr(ord(codeword[i]) - (seed * 3))
            elif (i % 2) != 0:
                firstpart += chr(ord(codeword[i]) - (seed // 2))

        finalcode = []

        for i, letter in enumerate(firstpart):
            finalcode.append(firstpart[i])

        self._codeword = ' '.join(finalcode).replace(" ", "")
