import pandas as pd
#from openpyxl import load_workbook
import numpy as np
from scipy import stats
import scipy

pathTable1 = r"C:\Users\felix\Desktop\Neuro\Fuat\result.xlsx"
pathTable2 = r"C:\Users\felix\Desktop\Neuro\Fuat\Tabelle_Main.xlsx"

pathOut = r"C:\Users\felix\Desktop\Neuro\Fuat\resultMWU.xlsx"

table1 = pd.read_excel(pathTable1)
table2 = pd.read_excel(pathTable2)

final = pd.DataFrame(columns=['percentileName', 'statistics', 'pval'])

for column in table1.columns:
    if 'percentile' in column and not "median" in column:
        arrayA = table1[[column]].to_numpy().ravel()
        arrayB = table2[[column]].to_numpy().ravel()

        arrayACleaned = []
        arrayBCleaned = []

        for entry in arrayA:
            if entry >= 50:
                arrayACleaned.append(entry)
        for entry in arrayB:
            if entry >= 50:
                arrayBCleaned.append(entry)
        stat , p = scipy.stats.mannwhitneyu(arrayACleaned,arrayBCleaned,use_continuity=False, alternative='greater',nan_policy='raise')
        new_row = {'percentileName' : column ,  'statistics' : stat, 'pval': p}
        final = final.append(new_row,ignore_index=True)
final.to_excel(pathOut, index = False)
        