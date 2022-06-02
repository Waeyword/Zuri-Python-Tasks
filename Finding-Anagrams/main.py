# Check if two words are anagrams
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] 
    
    #Removes all spaces between words and coverts them to lowercase
    w = word.replace(" ", "").lower()
    ana = anagram.replace(" ", "").lower()

    #Checks if both words are the same length
    if (len(w) == len(ana)):

        #sorts the letters in alphabetical order
        sorted_1 = sorted(w)
        sorted_2 = sorted(ana)

        if (sorted_1 == sorted_2):
            print ("\nTrue")
            #returns True
        else:
            print ("\nFalse")
            #returns False
    else:
        print("Invalid input.Try again")
        #if both words are not the same length, returns the above

find_anagram("hello", "check")
find_anagram("below", "elbow")


