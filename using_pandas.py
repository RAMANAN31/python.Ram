import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pylab as plt
import seaborn as sns
plt.style.use('ggplot')
#pd.set_option('max_columns',150)
#pd.set_option('max_columns',150)
# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
        

df=pd.read_csv('/kaggle/input/students-performance/DATA (1).csv')

#df.shape
#df.head(5)               
df.columns  
'''df[['STUDENT ID', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
       '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23',
       '24', '25', '26', '27', '28', '29', '30', 'COURSE ID', 'GRADE']].copy()'''#.copy-new df and not a reference,easy while manupulation.
#df.drop([10],axis=1)# axis =1 tells us that we have to drop a column not row
#df.describe()
df.rename(columns={'COURSE ID':'course id'})#rename column
df['course id']= pd.to_numeric(df['course id'])#assigning datatype
df.isna()
df.isna().sum()
#particular duplicate
#df.query('course id'=='course name')
#(~df)-not option
#df.duplicated()#list of duplicated
#loc tells which one is duplicated
#df.loc[df.duplicated()]
#df.duplicated(subset=['col_name']
#df.loc[df.duplicated(subset=['col_name'])]#display rows duplicated with row number no.
df=df.loc[~df.duplicated(subset=['course id'])]\
    .reset_index(drop=True).copy()#drop removes reset index
ax=df['course id'].value_counts()\
    .head(10)
    .plot(kind='bar',title='courses')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
ax= df['GRADE'].plot(kind='list',bins=20,title='ranks')
    #display rows duplicated with row number no.
ax=df['course id']
    .plot(kind='scatterplot',title='courses',x='x',y='y')
plt.show()
# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All" 
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session
sns.scatterplot(---hue='')
sns.pairplot(df,vars=[columns],hue)
plt.show()
df[['columns']].dropna().corr() 
sns.heatmap(df_corr,amnot=True)
.groupby()
.agg(['',''])
.query('cond<>..')
.sort_values()[]#[]tells what value to plot
.plot
