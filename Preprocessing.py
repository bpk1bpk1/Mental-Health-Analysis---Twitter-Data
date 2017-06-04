import string
import csv
import collections
import warnings
import pandas as pd
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import statsmodels.api as sm

#Preprocessing the data -- Need to add to access only twitter
rawData = pd.read_csv('Initialdataset.csv')
rawData.to_csv('First.csv',sep = ',')
with open('First.csv') as file:
    reader = csv.reader(file)
    with open('Preprocessed.csv','w',newline = '') as output_file:
        writer = csv.writer(output_file, delimiter = ',')
        for rows in reader:
            line = rows[10]
            line = line.translate(str.maketrans('', '', string.punctuation))
            line = line.translate(str.maketrans('', '', string.digits))
            rows[10] = line
            writer.writerow(rows)







