# Importing header files
import numpy as np
import warnings
warnings.filterwarnings('ignore')
#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]
#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)
#print(np.shape(data))
#Code starts here
census=np.concatenate((data,new_record),axis=0)
##print(np.shape(census))
age=census[:,0]
#print(age)
max_age=age.max()
min_age=age.min()
age_mean=np.round(age.mean(),2)
age_std=np.round(np.std(age),2)
#print(max_age)
#print(min_age)
#print(age_mean)
#print(age_std)
race_0=census[:,2]
race_0=race_0[race_0<=0]
#print(race_0)
race_1=census[:,2]
race_1=race_1[race_1==1]
#print(race_1)
race_2=census[:,2]
race_2=race_2[race_2==2]
#print(race_2)
race_3=census[:,2]
race_3=race_3[race_3==3]
#print(race_3)
race_4=census[:,2]
race_4=race_4[race_4==4]
#print(race_4)
len_0=len(race_0)
print(len_0)
len_1=len(race_1)
print(len_1)
len_2=len(race_2)
print(len_2)
len_3=len(race_3)
print(len_3)
len_4=len(race_4)
print(len_4)
len_all=[len_0,len_1,len_2,len_3,len_4]
minority_race=len_all.index(min(len_all))
print(minority_race)
################
senior_citizens=census[census[:,0]>60]

#Calculating the sum of all the values of array
working_hours_sum=senior_citizens.sum(axis=0)[6]
print(working_hours_sum)
#Finding the length of the array
senior_citizens_len=len(senior_citizens)

#Finding the average working hours
avg_working_hours=working_hours_sum/senior_citizens_len

#Printing the average working hours
print((avg_working_hours))

#Creating an array based on 'education' column
high=census[census[:,1]>10]

#Finding the average pay
avg_pay_high=high[:,7].mean()

#Printing the average pay
print(avg_pay_high)

#Creating an array based on 'education' column
low=census[census[:,1]<=10]

#Finding the average pay
avg_pay_low=low[:,7].mean()

#Printing the average pay
print(avg_pay_low)





