import mysql.connector
from difflib import get_close_matches

con = mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"
)

cursor = con.cursor()

word=input("Enter the word: ")




def keyWord(cursor):
    #query = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression LIKE '%s'"  % word  )
    query = cursor.execute("SELECT Expression FROM Dictionary" )
    keys = [b[0] for b in cursor.fetchall()]
#keys = [b for b in cursor.fetchall()]
    return (keys)

def definition(cursor,word):
    query = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression LIKE '%s'"  % word )
    results = cursor.fetchall()
    return (results)

results_key=keyWord(cursor)
results_definition=definition(cursor,word)


if results_definition:
    for result in results_definition:
        print(result[0])
else:
    #print(results_key)
    if len(get_close_matches(word,results_key,cutoff=0.8))>0:  
        #print("did you mean rain???")
        matches=get_close_matches(word,results_key)
        for match_word in matches:
            yn=input("did u mean %s instead?Enter Y if yes,or N if no:" %match_word)
            if yn=="Y":
                result= definition(cursor,match_word)
                print(result)
                break
            else:
                print("The word doesn't exist.Please double check it.")
                break

    else:
        print(" not found")
