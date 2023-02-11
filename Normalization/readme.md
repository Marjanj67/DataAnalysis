# How to normalize data for machine learning and othe purposes
## THe code
```
import numpy as np
import pandas as pd
from sklearn.preprocessing import normalize,MinMaxScaler,RobustScaler,StandardScaler
import matplotlib.pyplot as plt

#create dataset
data1 = np.random.normal(5,2,100)
data2 = np.random.randint(7,size=(100))
data2[53] = 25
data2[20] = 17
# x = np.linspace(data1.mean(), data1.max(), 1000)

fig , ax = plt.subplots(2,5)
fig.set_size_inches(10,7)
fig.suptitle('Different types of normalization for data')
ax[0,0].hist(data1,color = "skyblue")
ax[0,0].set_title('Original data')
ax[0,0].set_ylabel('Normal distribution data')
ax[1,0].hist(data2,color = "skyblue")
ax[1,0].set_ylabel('Random data')
# normalize
data1Norm = normalize([data1])
data2Norm = normalize([data2])
ax[0,1].hist(data1Norm[0],color = '#32a852')
ax[0,1].set_title('normalize')
ax[0,1].set_xlim(0,1)
ax[1,1].hist(data2Norm[0],color = '#32a852')
ax[1,1].set_xlim(0,1)
# MinMaxScaler
scaler = MinMaxScaler()
data1Norm = scaler.fit_transform(data1.reshape(-1,1))
data2Norm = scaler.fit_transform(data2.reshape(-1,1))
ax[0,2].hist(data1Norm,color = '#eddf3e')
ax[0,2].set_xlim(0,1)
ax[0,2].set_title('MinMaxScaler')
ax[1,2].hist(data2Norm,color = '#eddf3e')
ax[1,2].set_xlim(0,1)

# RobustScaler
scaler = RobustScaler()
data1Norm = scaler.fit_transform(data1.reshape(-1,1))
data2Norm = scaler.fit_transform(data2.reshape(-1,1))
ax[0,3].hist(data1Norm,color = '#d13232')
ax[0,3].set_title('RobustScaler')
ax[0,3].set_xlim(-5,5)
ax[1,3].hist(data2Norm,color = '#d13232')
ax[1,3].set_xlim(-5,5)
# StandardScaler
scaler = StandardScaler()
data1Norm = scaler.fit_transform(data1.reshape(-1,1))
data2Norm = scaler.fit_transform(data2.reshape(-1,1))
ax[0,4].hist(data1Norm,color = '#8f32d1')
ax[0,4].set_xlim(-5,5)
ax[0,4].set_title('StandardScaler')
ax[1,4].hist(data2Norm,color = '#8f32d1')
ax[1,4].set_xlim(-5,5)

fig.savefig("norm.png")
plt.show()


```
## The result
![](https://github.com/Marjanj67/DataAnalysis/blob/19ab349a6e8adea6817d25d812687c956f7c2856/Normalization/norm.png)

