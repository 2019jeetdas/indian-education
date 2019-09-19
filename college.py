# -*- coding: utf-8 -*-
#-----(2) college and University data analysis -----

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

df = pd.read_csv ('/home/jeet/Desktop/[B-2]-college-enrolment.csv',encoding="cp1252")

print("\n------- output data :-----------\n")
print("College data analysis:")
print("\n-----------------------------------\n")

# Question – A : get row and column numbers 

print('---------------------------------------------')
print("Dimension of the data frame = ",df.shape)
print('---------------------------------------------')

# Question – B : print column names :

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n")

year1 = df['Year']
year = np.arange(0,36)
print(year1)

# 0 --> Year
# 1 --> Universities
# 2 --> Institutions Deemed to be Universities
# 3 --> Colleges
# 4 --> Total Enrolment

uni = df['Universities'].replace(np.nan,0)
ins = df['Institutions Deemed to be Universities'].replace(np.nan,0)

for i in range(0,36):
     print([i],"-->",year1[i],"--- Universities : ",uni[i])

for i in range(0,36):
     print([i],"-->",year1[i],"--- Institutions Deemed to be Universities : ",ins[i])
      

plt.title('University & Institutions Deemed to be Universities Data (1976-77) to (2015-16) :')
plt.xlabel("year sl. no --- >")
plt.ylabel("Number --- >")

plt.plot(uni,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="[1] Universities ")


plt.plot(ins,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="[2] Institutions Deemed to be Universities")
            
plt.legend()
plt.show()

# Question -02 : college (1976-77) to (2015-16)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

df = pd.read_csv ('/home/jeet/Desktop/[B-2]-college-enrolment.csv',encoding="cp1252")

col = df['Colleges'].replace(np.nan,0)
year1 = df['Year']
year = np.arange(0,36)

for i in range(0,36):
     print([i],"-->",year1[i],"--- no. of colleges : ",col[i])

plt.title('Total college Data (1976-77) to (2015-16) :')
plt.xlabel("year sl. no --- >")
plt.ylabel("Number --- >")

plt.plot(col,
            marker='X',
            markersize=10,
            linestyle='dashed',
            label="[0] No. of colleges")
plt.legend()      
plt.show()                  


# Question -03 : Enrolment (1976-77) to (2015-16)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

df = pd.read_csv ('/home/jeet/Desktop/[B-2]-college-enrolment.csv',encoding="cp1252")

enrol = df['Total Enrolment'].replace(np.nan,0)
year1 = df['Year']
year = np.arange(0,36)

for i in range(0,36):
     print([i],"-->",year1[i],"--- Enrolment : ",enrol[i])

plt.title('[3] Total Enrolment Data (1976-77) to (2015-16) :')
plt.xlabel("year sl. no --- >")
plt.ylabel("Number --- >")

plt.plot(enrol,
            marker='X',
            markersize=10,
            linestyle='dashed',
            label="[0] Total Enrolment")
plt.legend()      
plt.show()                  




