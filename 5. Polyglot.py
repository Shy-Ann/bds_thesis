'''--- DEPENDS ON: Data/comment_overview_CLEAN.xlsx ,
Data/Extra analyse/comment_overview_CLEAN_ZT.xlsx --- '''

'''' ---- CREATES: Data/Prediction files/4. Polyglot Prediction.csv,
Data/Extra analyse/Prediction files/4. Polyglot Prediction_ZT.csv --- '''

import pandas as pd
import polyglot
from polyglot.text import Text, Word

'''Load in datafile with the comments. Noise has been removed but tokenization, 
stopword removal and lower casing is not yet done '''

comment_overview = pd.read_excel("./Data/comment_overview_CLEAN.xlsx")

# Strings to lower
comments_lower = []
for i in comment_overview["comment_lemma"]:
    comments_lower.append(i.lower())

comment_overview['comments_lower'] = comments_lower

'''Make a definition that turns the comment into a wordlist with Text and then
put the wordlist into the polarity function of polyglot to get the sentiment '''

def add_sentiment(comment):
    text = Text(comment, hint_language_code='NL')
    sentiment_score = text.polarity
    return sentiment_score

# Check if the function works
add_sentiment(comment_overview.comments_lower[8])

'''Loop over the dataframe and store result of sentiment function to list which is 
then added as new column in the dataframe. Sentiment  is measured from -1 (negative)
 to +1 (positive), with a value of 0 being neutral'''

sentiment_score = []
for i in comment_overview["comments_lower"]:
    sentiment_score.append(add_sentiment(i))

comment_overview['sentiment_score'] = sentiment_score

comment_overview.head()

''' Sentiment scores are now on a scale from -1 to +1. In order to compare these results
with the manual analysis, we need to onvert sentiment_scores to string containg either 
positive, negative or neutral. '''

sentiment_auto = []
for value in comment_overview['sentiment_score']:
    if value > 0:
        sentiment_auto.append('Positive')
    elif value < 0:
        sentiment_auto.append('Negative')
    else:
        sentiment_auto.append('Neutral')

comment_overview['sentiment_auto'] = sentiment_auto

# Check if it worked propery
comment_overview[0:10]

''' Now that we can compare the automated with the manual sentiment analysis, we can make
 a table to see the proportions that are classified correct'''

# Table with just the actual numbers per category
pd.crosstab(index = comment_overview['ma_sentiment'], 
            columns= comment_overview['sentiment_auto'])

# Tabe with proportions overall
pd.crosstab(index = comment_overview['ma_sentiment'], 
            columns= comment_overview['sentiment_auto'],
            normalize = 'all').round(2)
           
# Table with proportionns calculated per row
pd.crosstab(index = comment_overview['ma_sentiment'], 
            columns= comment_overview['sentiment_auto'],
            normalize = 'index').round(2)


# Write predictions to file
comment_overview.to_csv("./Data/Prediction files/4. Polyglot Prediction.csv")

''' ---------------------------------EXTRA ANALYSES-----------------------------------'''
''' ----------WITHOUT DEBATABLE COMMENTS--------------'''
'''Load in datafile with the comments. Noise has been removed but tokenization, 
stopword removal and lower casing is not yet done '''

comment_overview_ZT = pd.read_excel("./Data/Extra analyse/comment_overview_CLEAN_ZT.xlsx")

# Strings to lower
comments_lower_ZT = []
for i in comment_overview_ZT["comment_lemma"]:
    comments_lower_ZT.append(i.lower())

comment_overview_ZT['comments_lower'] = comments_lower_ZT

'''Loop over the dataframe and store result of sentiment function to list which is 
then added as new column in the dataframe. Sentiment  is measured from -1 (negative)
 to +1 (positive), with a value of 0 being neutral'''

sentiment_score_ZT = []
for i in comment_overview_ZT["comments_lower"]:
    sentiment_score_ZT.append(add_sentiment(i))

comment_overview_ZT['sentiment_score'] = sentiment_score_ZT

comment_overview_ZT.head()

''' Sentiment scores are now on a scale from -1 to +1. In order to compare these results
with the manual analysis, we need to onvert sentiment_scores to string containg either 
positive, negative or neutral. '''

sentiment_auto_ZT = []
for value in comment_overview_ZT['sentiment_score']:
    if value > 0:
        sentiment_auto_ZT.append('Positive')
    elif value < 0:
        sentiment_auto_ZT.append('Negative')
    else:
        sentiment_auto_ZT.append('Neutral')

comment_overview_ZT['sentiment_auto'] = sentiment_auto_ZT

# Check if it worked propery
comment_overview_ZT[0:10]

''' Now that we can compare the automated with the manual sentiment analysis, we can make 
a table to see the proportions that are classified correct'''

# Table with just the actual numbers per category
pd.crosstab(index = comment_overview_ZT['ma_sentiment'], 
            columns= comment_overview_ZT['sentiment_auto'])

# Tabe with proportions overall
pd.crosstab(index = comment_overview_ZT['ma_sentiment'], 
            columns= comment_overview_ZT['sentiment_auto'],
            normalize = 'all').round(2)
           
# Table with proportionns calculated per row
pd.crosstab(index = comment_overview_ZT['ma_sentiment'], 
            columns= comment_overview_ZT['sentiment_auto'],
            normalize = 'index').round(2)

# Write predictions to file
comment_overview_ZT.to_csv("./Data/Extra analyse/Prediction files/4. Polyglot Prediction_ZT.csv")

