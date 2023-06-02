import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('bitconnect_price.csv')

#LineBar
df=df.set_index('Date')
df.iloc[[0.1],0:4].plot.bar()

#plot ofopen in all years
df=df.set_index('Date')
ax=df.iloc[:,0].plot.line(title="Bitcoin \n Open" , rot=90,grid=True)
ax.set_ylabel("Dollars")

#Plot of High in All Years
df = df.iloc[::-1]

ax=df.iloc[:,1].plot.line(title="Bitcoin \n High" , rot=90,grid=True,color='skyblue' )
ax.set_ylabel("Dollars")
ax.set_facecolor('black')

df=df.iloc[::-1]
df=df.set_index('Date')
ax=df.iloc[:,0:3].plot.line(title="Bitcoin \n High" , rot=90,grid=True )
ax.set_ylabel("Dollars")
ax.set_facecolor('black')

ax=df.iloc[:,2].plot.line(title="Bitcoin \n Low")
ax.set_ylabel("Dollars")

ax=df.iloc[:,3].plot.line(title="Bitcoin \n Close")
ax.set_ylabel("Dollars")

#Top 10 Entries
df1=df.sort_values('Open', ascending=False)
df1.iloc[0:10, 0].plot.barh(grid=True, title="Top 10 High")
df1.set_ylabel("Dollars")

#Least 10 Entries
df1=df.sort_values('Open')
df1.iloc[0:10, 0].plot.barh(grid=True, title="Least 10 High")
df1.set_ylabel("Dollars")


df=df.iloc[::-1]
x=input("ENTER STARTING DAY")
y=input("ENTER ENDING DATE")

df=df.set_index('Date')
df1=df.loc[x:y,:]
width=.40
ax=df1[['Low','High','Close','Open']].plot()
df1['Volume'].plot(secondary_y=True,kind='bar',color='blue')
ax.set_facecolor('lightgrey')