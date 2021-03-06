# -*- coding: utf-8 -*-
"""Project_Titanic.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/thecodescholar/DA_Python_Jun_21/blob/main/Project_Titanic.ipynb

# Project_titanic
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

# %matplotlib inline

"""## Data Operations Task

#### Q. Import the Titianic Dataset and Display the Head of the Dataset
"""

df = pd.read_csv('https://raw.githubusercontent.com/thecodescholar/DA_Python_Jun_21/main/Dataset/titanicDataset.csv')





"""#### Q. Show the Statistics of dataframe"""



"""#### Q. Display last 3 columns"""

dtfrm=pd.read_csv('https://raw.githubusercontent.com/thecodescholar/DA_Python_Jun_21/main/Dataset/titanicDataset.csv') 
print (dtfrm.loc[[0,1,2,3,4],['Age','Fare','Embarked']])

"""#### Q. Show Unique values in Embarked"""

dtfrm=pd.read_csv('https://raw.githubusercontent.com/thecodescholar/DA_Python_Jun_21/main/Dataset/titanicDataset.csv') 
record = pd.read_csv(dtfrm)
print(record['Embarked'].unique())

"""## Visualization Task

#### Q. Draw histogram for Age, using Matplotlib
"""

plt.hist(data = df, x = 'Age')

"""#### Q. Draw countplot for Sex, using Seaborn"""

df = pd.read_csv('https://raw.githubusercontent.com/thecodescholar/DA_Python_Jun_21/main/Dataset/titanicDataset.csv')
sb.countplot(data =df , x = 'Sex')

"""#### Q. Make a Pie Chart of Corona Cases by taking numbers list as [500000, 1800000, 1200000] and labels list as ["Deaths", "Total Cases", "Cured"]"""

counts_ = [500000, 1800000, 1200000]
corona= ["Deaths", "Total Cases", "Cured"]
plt.pie(counts_, labels = corona);

"""### Great Job

## All the Best

# THE CODE SCHOLAR
"""