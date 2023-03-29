import pandas as pd
import numpy as np
from scipy import stats
import scipy
import itertools

pathTable = r"C:\Users\felix\Documents\41586_2022_5575_MOESM5_ESM.xlsx"
table = pd.read_excel(pathTable)
colsOfInterest = []

pathOut = r"C:\Users\felix\Desktop\fuatTest\result.xlsx"

final = pd.DataFrame(columns=['percentileName1', 'percentileName2', 'statistics', 'pval'])
for column in table.columns:
    if 'percentile' in column and not "median" in column:
        colsOfInterest.append(column)

for a, b in itertools.combinations(colsOfInterest, 2):
    arrayA = table[[a]].to_numpy().ravel()
    arrayB = table[[b]].to_numpy().ravel()
    res = scipy.stats.spearmanr(arrayA, arrayB, axis=1, nan_policy='propagate', alternative='two-sided')
    new_row = {'percentileName1' : a, 'percentileName2' : b, 'statistics' : res.statistic, 'pval': res.pvalue}
    final = final.append(new_row,ignore_index=True)
final.to_excel(pathOut, index = False)

-