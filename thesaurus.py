import json
from difflib import get_close_matches

data = json.load(open("JSON+Data+Inside/data.json"))

def meaning(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input( "Did you mean '%s' instead? Enter Y for yes and n for No." % get_close_matches(w, data.keys())[0])
        if yn == 'Y':
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == 'N':
            return "The word doexn't exist. Please double check it. "
        else:
            return "Please double chevk your input. "
    else:
        print("The word doesn't exist. Please double check it. ")

word = input("Enter a word: ")

output = meaning(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)