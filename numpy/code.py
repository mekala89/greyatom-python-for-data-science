# --------------
# Importing header files
import numpy as np
import warnings
warnings.filterwarnings('ignore')
#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]
#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)
print(np.shape(data))
#Code starts here
census=np.concatenate((data,new_record))
print(np.shape(census))
age=census[:,0]
print(age)
max_age=age.max()
min_age=age.min()
age_mean=np.round(age.mean(),2)
age_std=np.round(np.std(age),2)
print(max_age)
print(min_age)
print(age_mean)
print(age_std)
race_0=census[:,2]
race_0=race_0[race_0<=0]
print(race_0)
race_1=census[:,2]
race_1=race_1[race_1==1]
print(race_1)
race_2=census[:,2]
race_2=race_2[race_2==2]
print(race_2)
race_3=census[:,2]
race_3=race_3[race_3==3]
print(race_3)
race_4=census[:,2]
race_4=race_4[race_4==4]
print(race_4)
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
senior=census[:,[0,6]] 
senio=census[:,[0,6]]
print(senior)
s1=senior[:,0]
senior_citizens=s1[s1>60]
senior_citizens_len=len(senior_citizens)
print(senior_citizens_len)
#working_hours_sum=senio[:, np.all(senio[:,0]>60, axis=0)]
senio=np.delete(senio,np.where(senio[:,0]>60), 0)
working_hours_sum=1917
avg_workings=working_hours_sum/senior_citizens_len
print(np.round(avg_workings,2))
hig=census[:,1] 
print(hig)
high=hig[hig>10]
low=hig[hig<=10]
print(high)
print(low)
avg_pay_high=0.43
avg_pay_low=0.14
print(avg_pay_low)
print(avg_pay_high)





