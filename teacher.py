# -*- coding: utf-8 -*-
#-----(3) teacher data analysis -----

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

df = pd.read_csv ('/home/jeet/Desktop/[C]-teacher.csv',encoding="cp1252")

print("\n------- output data :-----------\n")
print("School data analysis:")
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

# 0 --> Year
year1 = df['Year']
year = np.arange(0,15)


# Question - 1A : Primary Schools - Total
# Question - 1B :Primary Schools - Women

primary = df['Primary Schools - Total'].replace(np.nan,0)
primary_women = df['Primary Schools - Women'].replace(np.nan,0)

for i in range(0,15):
    print(year1[i],"---> Total = ",primary[i],
            "---> Women = ",primary_women[i])
            
plt.title('[1] Number of Primary Teachers (2000-01) to (2015-16) : ')
plt.xlabel("year sl. no.--- >")
plt.ylabel("Number of teachers --- >")
    
plt.plot(primary,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="[1] Primary Schools - Total ")

                   
plt.plot(primary_women,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="[2] Primary Schools - Women")
            
plt.legend()
plt.show()


# Question - 2A : Upper Primary Schools - Total
# Question - 2B : Upper Primary Schools - Women

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

df = pd.read_csv ('/home/jeet/Desktop/[C]-teacher.csv',encoding="cp1252")

# 0 --> Year
year1 = df['Year']
year = np.arange(0,15)

upper_primary = df['Upper Primary Schools - Total'].replace(np.nan,0)
upper_primary_women = df['Upper Primary Schools - Women'].replace(np.nan,0)

for i in range(0,15):
    print(year1[i],"---> Total = ",upper_primary[i],
            "---> Women = ",upper_primary_women[i])

plt.title('[2] Number of Upper Primary Teachers (2000-01) to (2015-16) : ')
plt.xlabel("year sl. no. --- >")
plt.ylabel("Number of teachers --- >")
    
plt.plot(upper_primary,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="[1] Upper Primary Schools - Total ")

                   
plt.plot(upper_primary_women,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="[2] Upper Primary Schools - Women")
            
plt.legend()
plt.show()

# Question - 3A : Secondary Schools - Total
# Question - 3B : Secondary Schools - Women

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

df = pd.read_csv ('/home/jeet/Desktop/[C]-teacher.csv',encoding="cp1252")

# 0 --> Year
year1 = df['Year']
year = np.arange(0,15)

secondary = df['Secondary Schools - Total'].replace(np.nan,0)
secondary_women = df['Secondary Schools - Women'].replace(np.nan,0)

for i in range(0,15):
    print(year1[i],"---> Total = ",secondary[i],
            "---> Women = ",secondary_women[i])

plt.title('[3] Number of Secondary Teachers (2000-01) to (2015-16) : ')
plt.xlabel("year sl. no. --- >")
plt.ylabel("Number of teachers --- >")
    
plt.plot(secondary,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="[1] Secondary Schools - Total ")

                   
plt.plot(secondary_women,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="[2] Secondary Schools - Women")
            
plt.legend()
plt.show()

# Question - 4A : Senior Secondary Schools - Total
# Question - 4B : Senior Secondary Schools - Women

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

df = pd.read_csv ('/home/jeet/Desktop/[C]-teacher.csv',encoding="cp1252")

# 0 --> Year
year1 = df['Year']
year = np.arange(0,15)

senior_secondary = df['Senior Secondary Schools - Total'].replace(np.nan,0)
senior_secondary_women = df['Senior Secondary Schools - Women'].replace(np.nan,0)

for i in range(0,15):
    print(year1[i],"---> Total = ",senior_secondary[i],
            "---> Women = ",senior_secondary_women[i])

plt.title('[4] Number of Senior Secondary Teachers (2000-01) to (2015-16) : ')
plt.xlabel("year sl. no. --- >")
plt.ylabel("Number of teachers --- >")
    
plt.plot(senior_secondary,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="[1] Senior Secondary Schools - Total")

                   
plt.plot(senior_secondary_women,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="[2] senior Secondary Schools - Women")
            
plt.legend()
plt.show()

# Question - 5A : Total Teacher - Total
# Question - 5B : Total Teacher - Women

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

df = pd.read_csv ('/home/jeet/Desktop/[C]-teacher.csv',encoding="cp1252")

# 0 --> Year
year1 = df['Year']
year = np.arange(0,15)

total = df['Total Teacher - Total'].replace(np.nan,0)
total_women = df['Total Teacher - Women'].replace(np.nan,0)

for i in range(0,15):
    print(year1[i],"---> Total = ",total[i],"---> Women = ",total_women[i])

plt.title('[5] Number of Total Teachers (2000-01) to (2015-16) : ')
plt.xlabel("year sl. no. --- >")
plt.ylabel("Number of teachers --- >")
    
plt.plot(total,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="[1] Total Teachers")

                   
plt.plot(total_women,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="[2] Total teachers - Women")
            
plt.legend()
plt.show()


# Question - 6A : UTD
# Question - 6B: AC

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

df = pd.read_csv ('/home/jeet/Desktop/[C]-teacher.csv',encoding="cp1252")

# 0 --> Year
year1 = df['Year']
year = np.arange(0,15)

utd = df['UTD'].replace(np.nan,0)
ac = df['AC'].replace(np.nan,0)

for i in range(0,15):
    print(year1[i],"---> UTD = ",utd[i],"---> AC = ",ac[i])

plt.title('[6] UTD & AC (2000-01) to (2015-16) : ')
plt.xlabel("year sl. no. --- >")
plt.ylabel("Number of teachers --- >")
    
plt.plot(utd,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="[1] UTD")

                   
plt.plot(ac,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="[2] AC")
            
plt.legend()
plt.show()


# Question - 7 : Total No. of Teacher in all Universities & Affiliated Colleges

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

df = pd.read_csv ('/home/jeet/Desktop/[C]-teacher.csv',encoding="cp1252")

# 0 --> Year
year1 = df['Year']
year = np.arange(0,15)

college = df['Total No. of Teacher in all Universities & Affiliated Colleges'].replace(np.nan,0)

for i in range(0,15):
    print(year1[i],"--->",college[i])

plt.title('[7] Total No. of Teacher recruitment in all Universities & Affiliated Colleges (2000-01) to (2015-16) : ')
plt.xlabel("year sl. no. --- >")
plt.ylabel("Number of teachers --- >")
    
plt.plot(college,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="[1] Total No. of Teacher in all Universities & Affiliated Colleges")
 
plt.legend()
plt.show()