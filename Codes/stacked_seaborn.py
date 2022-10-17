# stacked bar graph with seaborn.

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# create a dataframe with 4 columns
df = pd.DataFrame({'x': np.arange(1, 11), 'y1': np.random.randn(10), 'y2': np.random.randn(10), 'y3': np.random.randn(10)})
print(df)

# create a stacked bar plot
sns.barplot(x='x', y='y1', data=df, color='b')
sns.barplot(x='x', y='y2', data=df, color='r', bottom=df['y1'])
sns.barplot(x='x', y='y3', data=df, color='g', bottom=df['y1']+df['y2'])

plt.show()

# stacked bar graph with seaborn with datetime index.

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# create a dataframe with 4 columns
df = pd.DataFrame({'y1': np.random.randn(10), 'y2': np.random.randn(10), 'y3': np.random.randn(10)}, index=pd.date_range('2018-01-01', periods=10))
print(df)

# create a stacked bar plot
sns.barplot(x=df.index, y='y1', data=df, color='b')
sns.barplot(x=df.index, y='y2', data=df, color='r', bottom=df['y1'])
sns.barplot(x=df.index, y='y3', data=df, color='g', bottom=df['y1']+df['y2'])

plt.show()


# formatting the datetime x-axis labels.

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.dates as mdates

# create a dataframe with 4 columns
df = pd.DataFrame({'y1': np.random.randn(10), 'y2': np.random.randn(10), 'y3': np.random.randn(10)}, index=pd.date_range('2018-01-01', periods=10))
print(df)

# create a stacked bar plot
#plot data
fig, ax = plt.subplots(figsize=(15,7))
sns.barplot(x=df.index, y='y1', data=df, color='b',ax=ax)
sns.barplot(x=df.index, y='y2', data=df, color='r', bottom=df['y1'],ax=ax)
sns.barplot(x=df.index, y='y3', data=df, color='g', bottom=df['y1']+df['y2'],ax=ax)

# format the x-axis labels
#plt.gcf().autofmt_xdate()
ax.xaxis.set_major_locator(mdates.DayLocator())
#set major ticks format
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))

plt.show()

# stacked bar graph with seaborn after grouping.

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# create a dataframe with 4 columns

df = pd.DataFrame({'x': np.arange(1, 11), 'y1': np.random.randn(10), 'y2': np.random.randn(10), 'y3': np.random.randn(10)})
print(df)

# group the data by x
df = df.groupby('x').sum()
print(df)

# create a stacked bar plot
sns.barplot(x=df.index, y='y1', data=df, color='b')
sns.barplot(x=df.index, y='y2', data=df, color='r', bottom=df['y1'])
sns.barplot(x=df.index, y='y3', data=df, color='g', bottom=df['y1']+df['y2'])

plt.show()


# stacked bar graph with seaborn after grouping with datetime index and formatting the datetime x-axis labels and several categories.

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.dates as mdates

# create a dataframe with 4 columns

df = pd.DataFrame({'y1': np.random.randn(10), 'y2': np.random.randn(10), 'y3': np.random.randn(10)}, index=pd.date_range('2018-01-01', periods=10))
print(df)

# group the data by x
df = df.groupby(pd.Grouper(freq='M')).sum()
print(df)

# create a stacked bar plot
#plot data
fig, ax = plt.subplots(figsize=(15,7))
sns.barplot(x=df.index, y='y1', data=df, color='b',ax=ax)
sns.barplot(x=df.index, y='y2', data=df, color='r', bottom=df['y1'],ax=ax)
sns.barplot(x=df.index, y='y3', data=df, color='g', bottom=df['y1']+df['y2'],ax=ax)

# format the x-axis labels
#plt.gcf().autofmt_xdate()
ax.xaxis.set_major_locator(mdates.DayLocator())
#set major ticks format
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))

plt.show()

















