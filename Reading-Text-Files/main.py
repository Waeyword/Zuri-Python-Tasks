# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!")
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment]
    with open(filename) as file:
        data_file = file.read()
    return data_file


def count_words():
    text = read_file_content("./story.txt")
    # [assignment]
    spl_text = text.split()
    textDict = {}
    for i in spl_text:
        if i in textDict:
            textDict[i] += 1
        else:
            textDict[i] = 1
    return textDict

    #w = text.split()
    #x = input("Word you would like to count in the text file: ")
    #y = w.count(x)
    #textDict = dict.fromkeys(w[x], y)
    # print(y)

    # return {"as": 10, "would": 20}


print(count_words())
