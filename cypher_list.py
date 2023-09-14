# gives the user a way to save encrypted words to an attached file
def addtolist(cypher, word, month, count):
    file = open("cypherlist", "a")
    wrtten = ""
    writtn = str(count) + " [" + cypher + "] [" + word + "] [" + str(month) + "]"
    file.write(writtn)
    file.write("\n")
    file.close()

# reads the list back to the user
def fetchlist():
    f = open("cypherlist", "r")
    print(f.read())
    f.close()

# reads the saved list and finds the most up to date count

def count():
    f = open("cypherList", "r")
    count=0
    for line in f:
        count +=1
    f.close()
    return count




