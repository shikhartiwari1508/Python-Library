# NUMPY PROGRAMME :

import numpy as np
arr=np.array([1,2,3])
print(arr)



# PANDAS PROGRAMME :

import pandas as pd
data = {
    "name": ["A","B"]
}
df = pd.DataFrame(data)
print(df)



#MATPLOTLIB PROGRAMME :

import matplotlib.pyplot as plt
x=[1,2,3]
y=[4,5,6]
plt.plot(x,y)
plt.show()


#SCIPY PROGRAMME :

from scipy import stats
data = [10,20,30,40,50]
print("Mean :",stats.tmean(data))
print("Varience :",stats.tvar(data))


#SEABORN PROGRAMME :

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.DataFrame({
    "Name":["Shikhar","Shivam","Saurabh","Shivansh","Suryansh","Shivesh"],
    "Marks":[80, 58, 68, 95, 74, 55],
    "Address":["Pratapgarh","Ballia","Kunda","Prayagraj","Allahabad","Rewa"]
})
sns.barplot(data=df,x="Name",y="Marks")
plt.show()