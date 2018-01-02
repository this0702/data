#seaborn是在matplotlib上的封装
#正好需要用到facegrid
import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats
import matplotlib as mpl
import matplotlib.pyplot as plt
sns.set(style="ticks")
tips = sns.load_dataset("tips")
print(tips.head())
#以后细致的学习吧。2017/11/14