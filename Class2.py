import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

cols = ['CreditScore', 'Geography', 'Gender', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'IsActiveMember', 'EstimatedSalary',
'Exited']
churn = pd.read_csv("Churn_Modelling.csv", usecols=cols)
churn.head()

#plt.figure(figsize=(8,5))
#plt.title("Number of Customers", fontsize=14)
#plt.bar(x=churn['Geography'].value_counts().index,
 #       height=churn.Geography.value_counts().values)

# plt.rcParams.get('figure.figsize')
# [6.0, 4.0]
# plt.rcParams['figure.figsize'] = (8,5)
# plt.rc('xtick', labelsize=12)
# plt.rc('ytick', labelsize=12)
# plt.hist(x=churn['Balance'])
# plt.show()


plt.hist(x=churn['Balance'], bins=12, color='darkgrey',
         range=(25000, 225000))
plt.title("Distribution on Balance (25000 - 225000)", fontsize=14)

plt.show()