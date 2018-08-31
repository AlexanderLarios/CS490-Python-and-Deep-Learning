file = open("phrase.txt", "r");
phrase = file.read();
print("Phrase: " + phrase + " Number of words: " + str(len(phrase.split())) + " Number of characters: " + str(len(phrase)))