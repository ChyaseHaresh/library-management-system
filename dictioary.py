import json
from difflib import get_close_matches


data=json.load(open("data.json"))

cae=True
while cae==True:
    def return_meaning(sabda):
        sabda=sabda.lower()
        if sabda in data:
            return (data[sabda])

        elif len(get_close_matches(sabda,data.keys()))>0:
            yn=input("\nDid you mean %s instead ?? Y for yes n for no: " %get_close_matches(sabda,data.keys())[0])
            yn=yn.lower()
            if yn=='y':
                return (data[get_close_matches(sabda,data.keys())[0]])
            elif yn=='n':
                return ('Please make sure you type the word correctly')
            else:
                return ('\nWhat the heck is this ??')

        else:
            return (sabda+' doesnt exist')


    word=input('Input Word: ')
    output=return_meaning(word)

    if type(output)==list:
        for item in output:
            print(item)

    else:
            print(output)
    # choice=input('\n\nDo you wanna coninue ?? y/n: ')
    # choice=choice.lower()
    # if choice=='n':
    #     cae=False
    # else:
    #     cae=True
    #
