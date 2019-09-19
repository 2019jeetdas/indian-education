# -*- coding: utf-8 -*-
#-----(1) school data analysis -----

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

df = pd.read_csv ('/home/jeet/Desktop/[A]-school.csv',encoding="cp1252")

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

# Question-01 : Board of Intermediate Secondary Education

board = df['Board of Intermediate Secondary Education']

plt.title("Question-01 : Board of Intermediate Secondary Education")
plt.xlabel("States sl. no. ---->")
plt.ylabel("No. for board of intermediate secondary education --->  ")
plt.plot(board)
plt.show()

# Question-02 : ISCED-3 - Pre-Degree Junior Colleges/ Higher Sec. Schools
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

df = pd.read_csv ('/home/jeet/Desktop/[A]-school.csv',encoding="cp1252")

pre = df['ISCED-3 - Pre-Degree Junior Colleges/ Higher Sec. Schools']

plt.title("Question-02 : ISCED-3 - Pre-Degree Junior Colleges/ Higher Sec. Schools")
plt.xlabel("States sl. no. ---->")
plt.ylabel("No. for ISCED-3 - Pre-Degree Junior Colleges/ Higher Sec. Schools --->  ")
plt.plot(pre)
plt.show()

# Question-03 : ISCED-3 - High/Post Basic Schools
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

df = pd.read_csv ('/home/jeet/Desktop/[A]-school.csv',encoding="cp1252")

pre = df['ISCED-3 - High/Post Basic Schools']

plt.title("Question-03 : ISCED-3 - High/Post Basic Schools")
plt.xlabel("States sl. no. ---->")
plt.ylabel("No. for ISCED-3 - High/Post Basic Schools --->  ")
plt.plot(pre)
plt.show()

# Question-04 : ISCED-2 - Middle / Sr Basic Schools
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

df = pd.read_csv ('/home/jeet/Desktop/[A]-school.csv',encoding="cp1252")

pre = df['ISCED-2 - Middle / Sr Basic Schools']

plt.title("Question-04 : ISCED-2 - Middle / Sr Basic Schools")
plt.xlabel("States sl. no. ---->")
plt.ylabel("No. for ISCED-2 - Middle / Sr Basic Schools --->  ")
plt.plot(pre)
plt.show()


# Question-05 : ISCED-1 - Primary/Jr Basic Schools
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

df = pd.read_csv ('/home/jeet/Desktop/[A]-school.csv',encoding="cp1252")

pre = df['ISCED-1 - Primary/Jr Basic Schools']

plt.title("Question-05 : ISCED-1 - Primary/Jr Basic Schools")
plt.xlabel("States sl. no. ---->")
plt.ylabel("No. for ISCED-1 - Primary/Jr Basic Schools --->  ")
plt.plot(pre)
plt.show()


# Question-06 : ISCED-1 - EGS Centers
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

df = pd.read_csv ('/home/jeet/Desktop/[A]-school.csv',encoding="cp1252")

pre = df['ISCED-1 - EGS Centers']

plt.title("Question-06 : ISCED-1 - EGS Centers")
plt.xlabel("States sl. no. ---->")
plt.ylabel("No. for ISCED-1 - EGS Centers --->  ")
plt.plot(pre)
plt.show()

# Question-07 : ISCED-0 - Pre-Primary/ Pre Basic Schools*
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

df = pd.read_csv ('/home/jeet/Desktop/[A]-school.csv',encoding="cp1252")

pre = df['ISCED-0 - Pre-Primary/ Pre Basic Schools*']

plt.title("Question-07 : ISCED-0 - Pre-Primary/ Pre Basic Schools*")
plt.xlabel("States sl. no. ---->")
plt.ylabel("No. for ISCED-0 - Pre-Primary/ Pre Basic Schools* --->  ")
plt.plot(pre)
plt.show()

# Question-08 :ISCED-0 - Institutions imparting pre-school education under ICDS
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

df = pd.read_csv ('/home/jeet/Desktop/[A]-school.csv',encoding="cp1252")

pre = df['ISCED-0 - Institutions imparting pre-school education under ICDS']

plt.title("Question-08 :ISCED-0 - Institutions imparting pre-school education under ICDS")
plt.xlabel("States sl. no. ---->")
plt.ylabel("No. for ISCED-0 - Institutions imparting pre-school education under ICDS --->  ")
plt.plot(pre)
plt.show()


