import json
from difflib import get_close_matches
data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data: #if user entered "texas" this will check for "Texas" as well.
        return data[w.title()]
    elif len(get_close_matches(w,data.keys(),1,0.8)) > 0:
        yn = input("Did you mean %s instead? Enter Y for Yes, or N if no: " % get_close_matches(w,data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w,data.keys())[0]]
        else:
            return "The word does not exist. Please double check it"
    else:
        return "The word does not exist. Please double check it"

str = input("Enter word:  ")

output = translate(str)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)

