'''write a python program to detect whether a comment is spam or not. a comment shoukd be treated as spam if it contains any of these keywords: "make a lot of money","buy now","subscribe this",or"click this".'''

cmnt = input("Enter a comment: ")
if "make a lot of money" in cmnt or "buy now" in cmnt or "subscribe this" in cmnt or "click this" in cmnt:
    print("This comment is a spam.")
else:
    print("This comment is not spam.")