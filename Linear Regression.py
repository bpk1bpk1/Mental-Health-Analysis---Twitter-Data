import csv
import collections
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from statsmodels.stats.anova import anova_lm
from pylab import *
import statsmodels.formula.api as smf
import statsmodels.api as sm

#To find the most frequent location
locations = collections.Counter()
with open('Sentiment_data.csv') as input_file:
    reader = csv.reader(input_file)
    for row in reader:
        locations[row[7]] += 1
locationcount = pd.DataFrame.from_dict(locations, orient='index').reset_index()
locationcount = locationcount.rename(columns={'index':'Name of the Location', 0:'Location-count'})


#Performing Linear Regression
data_lr = pd.read_csv('Sentiment_data.csv',encoding = "ISO-8859-1")
data_lr = data_lr.rename(columns={'Fav Count': 'Favorite' ,'Retweet Count' :'Retweet'})
result = smf.ols(formula="pscore ~ Favorite + Retweet", data= data_lr).fit()
print (result.summary())

favorite_plot = data_lr['Favorite']
retweet_plot = data_lr['Retweet']
pscore_plot = data_lr['pscore']
#Plotting the graph
#Multiple linear regression
plot1 = scatter(retweet_plot,pscore_plot)
(m,b) = polyfit(retweet_plot,favorite_plot,1)
yp = polyval([m,b],pscore_plot)
plot(yp,retweet_plot)
scatter(yp,retweet_plot)
plt.show()

#http://nullege.com/codes/search/statsmodels.api.graphics.plot_regress_exog
#Only using retweet count
fig = plt.figure(figsize=(12,8))
fig = sm.graphics.plot_regress_exog(result,'Retweet',fig=fig)

plt.show()