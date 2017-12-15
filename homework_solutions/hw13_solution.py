from __future__ import print_function

import pandas as pd
import matplotlib.pyplot as plt

# ========== HW13 SOLUTION [Python2/3] ========== #

# read in data
df_aapl = pd.read_csv('AAPL.csv', na_values='null', index_col='Date')
df_msft = pd.read_csv('MSFT.csv', na_values='null', index_col='Date')
df_pg = pd.read_csv('PG.csv', na_values='null', index_col='Date')
# convert index to datetime type (for plotting)
df_aapl.index = df_aapl.index.astype('datetime64')
df_msft.index = df_msft.index.astype('datetime64')
df_pg.index = df_pg.index.astype('datetime64')

# calculate Range (abs not necessary since High >= Low can be assumed)
df_aapl['Range'] = abs(df_aapl['High'] - df_aapl['Low'])
df_msft['Range'] = abs(df_msft['High'] - df_msft['Low'])
df_pg['Range'] = abs(df_pg['High'] - df_pg['Low'])

# write output files
df_aapl.to_csv('AAPL_range.csv')
df_msft.to_csv('MSFT_range.csv')
df_pg.to_csv('PG_range.csv')

# print summary statistics
print(df_aapl.Range.describe())
print(df_msft.Range.describe())
print(df_pg.Range.describe())

# subset Close prices between 2008-2009 (for year 2008)
close_aapl = df_aapl['Close'].loc['2008']
close_msft = df_msft['Close'].loc['2008']
close_pg = df_pg['Close'].loc['2008']

# plot
plt.figure()
plt.plot(close_aapl.index, close_aapl, label='AAPL')
plt.plot(close_msft.index, close_msft, label='MSFT')
plt.plot(close_pg.index, close_pg, label='PG')
plt.legend()
plt.xticks(rotation=30)
plt.show()
