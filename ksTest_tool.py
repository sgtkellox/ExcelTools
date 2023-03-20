import pandas as pd
import numpy as np
from scipy import stats

pathTable = r"E:\Fuat\supp3short.xlsx"
table = pd.read_excel(pathTable)

for column in table.columns:
    if 'percentile' in column:
        array = table[[column]].to_numpy().ravel()
        loc, scale = stats.norm.fit(array)
        n = stats.norm(loc=loc, scale=scale)
        res = stats.kstest(array,n.cdf, alternative = 'less', method = 'exact')
        print(column + " :"+ res)
