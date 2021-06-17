''' DEPENDS ON: Data/Frog_lemmatized.csv '''


# Load from url
url = 'http://127.0.0.1:8080/frog/sentiment/output/Frog_data.csv.xml'

def wordsToLemma(url):
    import folia.main as folia    
    import re    
    # translate url to folia doc    
    doc = folia.Document(file=url)
        # get full text     
    full_text = doc.text()
        # get words from file     
    word_index = list(doc.index)
    word_dict = {}

    for w in word_index:
        word = doc[w]
        try:
            text = word.text()
            if ((re.match(r'[A-z]{1}',text)) and (len(text)>2)):
                try:
                    word_dict[text] = word.lemma()
                except:
                    continue     
            else:
                continue        
        except:
            continue    
    return word_dict
  
word_dict = wordsToLemma(url)

import pandas as pd

comments_df = pd.read_csv('./Data/Frog_data.csv', sep=';')
comments_df['comment_lemma'] = comments_df['clean_comments']
for w in list(word_dict):
    comments_df['comment_lemma'] = comments_df['comment_lemma'].\
        str.replace('\\b{}\\b'.format(w),word_dict[w])

comments_df.head()         
comments_df.to_csv("./Data/Frog_lemmatized.csv")