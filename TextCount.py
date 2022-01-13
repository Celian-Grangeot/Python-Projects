#---------- LONGEST SENTENCE WORD COUNT ----------

WordsCount=[] #List that will contain the number of word for each sentence
Sentence=[] #List that will contain the sentences (for final print message)
    
def TextCount(TextToCheck):
    """This function will return the number of words in the longest sentence in a given text"""
       
    phrase=TextToCheck.replace('!','.').replace('?','.').split(".")   #Let's replace all punction for a point. Then splitting our text base on "points"

    for i in range(len(phrase)): #For each sentence
        new_phrase=phrase[i].replace(' ','.').replace(',','.').replace("'",'.').split(".") #splitting each words
        words = [x for x in new_phrase if x != '']   #Deleting empty string in the list since we don't want to count them
        WordsCount.append(len(words)) #Adding the number of words of THIS (i) sentence to WordsCount
        Sentence.append(words) #Adding the according sentence to the Sentence list

    indexLongueur = WordsCount.index(max(WordsCount)) #Calculating the index of the maximum value of WordsCount (the index of the longest sentence)
    JoinedSentence=' '.join(Sentence[indexLongueur]) #Converting the list (the one corresponding to the index we just calculated) to a string 
    print("\nThe longest sentence is {num} words long. There are {num} words in the sentence : '\x1B[3m{sent}\x1B[0m'".format(num=max(WordsCount), sent=JoinedSentence))



TextCount(input("Please enter the text you'd like to test : "))
