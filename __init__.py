# importing necessary functions/classes

import input_word, decode_word, cypher, random_ass, cypher_list

# opening files which contain the last seed set

f = open("seed", "r")


# reading the current count of lines in saved file, if nothing saved setting count to 1

count = cypher_list.count()
count +=1

# reading the last set month for the seed

month = (f.read())
f.close()

# setting seed using selected month

seed = random_ass.random_seeded(month)

# giving the user some choices for what they would like the programme to do

while True:
    print("Make a selection from the following choices")
    print("1. Encode a word")
    print("2. Decode a previously encoded word")
    print("3. Set a key using your Month of birth, current seed is " + str(month))
    print("4. Retrieve previously saved list of cyphers")
    print("5. Exit programme")

    # using a try block to try to catch any exceptions from invalid selections

    try:
        choice = int(input())

        # Takes a word from the user, encodes it and gives the user the option to store it in a list

        if choice ==1:
            word = input_word.inputted()
            codeworder = cypher.Cypher(word)
            codeworder.set_codeword(word, seed)
            codeword = codeworder.get_codeword()
            print(codeword)
            print("Would you like to add this to a stored list??(Y/N)")
            dec = input()
            if dec == 'Y' or dec == 'y':
                cypher_list.addtolist(codeword, word, month, count)
                count = int(count) + 1


        # Takes a coded word and attempts to decode it

        elif choice ==2:
            decode_word.decoder(seed)

        # allows the user to amend the month used to generate the seed

        elif choice ==3:
            print("Please enter your Month of birth as an integer (1-12)")
            month = input()
            file = open("seed", "w")
            file.write(str(month))
            seed = random_ass.random_seeded(month)
            file.close()

        # shows the list of stored code words and the words they were generated from and the month used

        elif choice ==4:
            cypher_list.fetchlist()

        # closes the programme

        elif choice ==5:
            break

        # if the user inputs an integer not covered by the above they will be prompted to try again

        else:
            print("unexpected value, please try again")

    # if the user enters an invalid option, they will be asked to try again

    except:
        print("unexpected value, please try again")


