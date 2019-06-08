
import sys 
import re 
import pandas as pd 

def prepare_data():
    men_women_pronouns = ['He', 'her']
    women_men_pronouns = ['She', 'him']

    data = []
    with open('./datasets.txt', 'r') as f:
        for i in f.readlines():
            first = i.replace('<1>', men_women_pronouns[0])
            first = first.replace('<2>', men_women_pronouns[1]).lower().strip()
            second = i.replace('<1>', women_men_pronouns[0])
            second = second.replace('<2>', women_men_pronouns[1]).lower().strip()
            data.append(first)
            data.append(second)

    

    df = pd.DataFrame(data)
    return(df)
