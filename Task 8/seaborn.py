import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    'A': np.random.randn(100),
    'B': np.random.randn(100)
}
df = pd.DataFrame(data)

sns.jointplot(x='A', y='B', data=df, kind='scatter')
plt.show()

sns.pairplot(df)
plt.show()
