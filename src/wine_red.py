import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
import missingno as msno
import pandas_profiling
from joblib import dump, load
import pickle

import sqlalchemy as db
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm import sessionmaker
import os

from sklearn.model_selection import KFold
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import LinearSVC, SVC
from sklearn.linear_model import Perceptron
from sklearn.naive_bayes import GaussianNB

from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
from sklearn.metrics import precision_score, recall_score, roc_curve
%matplotlib inline
# Customise plots
mpl.rcParams['font.sans-serif'] = "Arial"
mpl.rcParams['font.family'] = "sans-serif"
mpl.rcParams['xtick.labelsize'] = 12
mpl.rcParams['ytick.labelsize'] = 12
mpl.rcParams['axes.titlesize'] = 16
mpl.rcParams['axes.labelsize'] = 12

# Load MYSql connector 
SQL_USR, SQL_PSW= os.environ['SQL_USR'], os.environ['SQL_PSW']
mysql_str = 'mysql+mysqlconnector://'+SQL_USR+':'+SQL_PSW+'@localhost:3306/'
engine = db.create_engine(mysql_str+'Wine')

# Load database diamonds
df = pd.read_sql('SELECT * from wine_red', engine).drop('index', axis=1)
df.head()


# Check missing data
print('\nMissing values:')
print('-'*30)
for col in df.columns:
    is_null = df[col].isnull()
    n_null = df.loc[is_null, col].sum()
    print('{0}: {1} null values'.format(col, n_null))

# Generate Auto profiling
#profile = df.profile_report(title='Red wines Profiling Report')
#profile.to_file(output_file="../report/wine_red.html")

# Check duplicates
print('\nDuplicate data:')
print('-'*30)
df[df.duplicated(keep=False)].head()
df = df.drop_duplicates()

# Check correlation with the target
df.corr()['quality'].sort_values(ascending=False)

# Correlation
# Correlation between numerical values and target
print('\nCorrelation:')
print('-'*30)
corr = df.corr(method='pearson')
plt.figure(figsize=(8, 4))
ax = sns.heatmap(
    corr, 
    vmin=-1, vmax=1, center=0,
    cmap=sns.diverging_palette(20, 220, n=200),
    square=True,
    annot=True,\
    fmt='.1g'
)
ax.set_xticklabels(
    ax.get_xticklabels(),
    rotation=45,
    horizontalalignment='right'
)
plt.savefig('../images/correlation.png', dpi=300)
plt.show()

print('\nCorrelation with the target:')
print('-'*30)
print(df.corr()['converted'].sort_values(ascending=False))

# Target distribution
plt.figure()
sns.countplot(df['quality'])
plt.title('Quality distribution')
plt.show()

