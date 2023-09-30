!pip install seaborn
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as  sns
#step2
data=pd.read_csv('1000_Companies.csv')

data.head()
data.tail()
data.info()

data.describe()
data.columns
data.isna()
data.isna().sum()
##############
sns.heatmap(data.corr(),annot=True)
##########
plt.scatter( x=data['R&D Spend'], y=data['Profit'])
sns.scatterplot(x=data['Administration'],y=data['Profit'])
sns.scatterplot(x=data['Marketing Spend'],y=data['Profit'])

sns.barplot(x=data['State'],y=data['Profit'])
sns.boxplot(x=data['State'],y=data['Profit'])
############################
















