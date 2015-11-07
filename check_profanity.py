import urllib
def read_text():
    quotes = open(".txt file location in your computer")
    contents_of_file = quotes.read()
    #print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+text_to_check) #I use wdly.com in this operation.It's so useful for suchlike project.
    output = connection.read()
    if "true" in output: #Actually you dont have to use if-else statment, but in this way our project will become better.
        print("Profanity Alert!!!")
    elif "false" in output:
        print("This document has no curve word.")
    else:
        print("Sorry.Couldn't scan the document probaly")
    connection.close()

read_text()
