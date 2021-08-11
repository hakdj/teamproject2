import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

from sklearn import metrics
from sklearn import tree
from sklearn.ensemble import VotingClassifier, RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.metrics import accuracy_score
from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier
from xgboost import XGBClassifier


df = pd.read_excel('./goms_filtered_.xlsx',engine='openpyxl',header=0);
pd.set_option('display.max_columns', 15)
df.replace('', np.nan, inplace=True);   # ''을 np.nan으로 변경
df.fillna(0,inplace=True);


# print(df);
# print(df.head());
# print(df.info());
# print(df.columns);
print('---------------------------------------------------------------------------------------------------------')
ndf=df[['schoolType','graduY','age','internExp','toeicScore','tospGrade',
        'trainingHr','jobseekYN','certNum','mainJobCate']]

print(ndf.columns);
print('---------------------------------------------------------------------------------------------------------')

for i in range(0,len(ndf)):
        if ndf['mainJobCate'][i] != 0:
                ndf['mainJobCate'][i]=1;
        else:
                ndf['mainJobCate'][i]=0;
print(ndf['mainJobCate']);

print('---------------------------------------------------------------------------------------------------------')

X=ndf[['schoolType','graduY','age','internExp','toeicScore','tospGrade',
        'trainingHr','jobseekYN','certNum']]
Y=ndf['mainJobCate'];

print(ndf);

