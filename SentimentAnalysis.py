import pandas as pd
from afinn import Afinn

# Cleaning the data and finding the sentiment score for each tweet in the dataset.

df= pd.read_csv('Preprocessed.csv',index_col=0)
length=df.__len__()
#print length

df=df.dropna()

afinn = Afinn()
pscore = []

#This gives the sentiment score for every tweet
for text in df['Text']:
    pscore.append(afinn.score(text))
df['pscore']= pscore
#print df.__len__()
df.to_csv('Sentiment_data.csv', delimiter = ',')

# Grouping the score and disorder basing on the location and storing it in a new csv file.
data = df.groupby(["Location","Disorder","pscore"])["Location"].agg("count")
data.to_csv('Location_data.csv', delimiter = ',')

#print len(data)
