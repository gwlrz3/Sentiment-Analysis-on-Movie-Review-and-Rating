import pandas as pd 
from pandas import DataFrame, read_csv
import csv 
import numpy as np

Reviews=[]
Ratings=[]

file=open("/Users/tong/Desktop/scale_data/scaledata/Dennis+Schwartz/subj.Dennis+Schwartz",'r')
for line in file.readlines():
	line=line.strip()
	Reviews.append(line)

file=open("/Users/tong/Desktop/scale_data/scaledata/Dennis+Schwartz/rating.Dennis+Schwartz",'r')
for line in file.readlines():
	line=line.strip()
	Ratings.append(line)

file=open("/Users/tong/Desktop/scale_data/scaledata/James+Berardinelli/subj.James+Berardinelli",'r')
for line in file.readlines():
	line=line.strip()
	Reviews.append(line)

file=open("/Users/tong/Desktop/scale_data/scaledata/James+Berardinelli/rating.James+Berardinelli",'r')
for line in file.readlines():
	line=line.strip()
	Ratings.append(line)

file=open("/Users/tong/Desktop/scale_data/scaledata/Scott+Renshaw/subj.Scott+Renshaw",'r')
for line in file.readlines():
	line=line.strip()
	Reviews.append(line)

file=open("/Users/tong/Desktop/scale_data/scaledata/Scott+Renshaw/rating.Scott+Renshaw",'r')
for line in file.readlines():
	line=line.strip()
	Ratings.append(line)

file=open("/Users/tong/Desktop/scale_data/scaledata/Steve+Rhodes/subj.Steve+Rhodes",'r')
for line in file.readlines():
	line=line.strip()
	Reviews.append(line)

file=open("/Users/tong/Desktop/scale_data/scaledata/Steve+Rhodes/rating.Steve+Rhodes",'r')
for line in file.readlines():
	line=line.strip()
	Ratings.append(line)

Dataset = list(zip(Reviews,Ratings))

np.random.shuffle(Dataset)

TrainSet=Dataset[:(4*len(Dataset)/5)]

TestSet=Dataset[(4*len(Dataset)/5):]

df1 = pd.DataFrame(data = TrainSet, columns=['review', 'rating'])

df1.to_csv('TrainSet.csv', index=False, header=True)

df2 = pd.DataFrame(data = TestSet, columns=['review', 'rating'])

df2.to_csv('TestSet.csv', index=False, header=True)


