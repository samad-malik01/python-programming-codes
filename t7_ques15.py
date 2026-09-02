#take a sentence containing double spaces and unwanted spaces at the beginning or end. Clean the sentence
sen = input("Enter a sentence: ")
sen = sen.strip()
sen = sen.replace("  "," ")
print("Clean Sentence: ",sen)