import pandas as pd
#from openpyxl import load_workbook

pathTable1 = r"D:\Fuat\Med_4_Probe.xlsx"
pathTable2 = r"D:\Fuat\Tabelle_Main.xlsx"

pathOut = r"C:\Users\felix\Desktop\fuatTest\result.xlsx"

table1 = pd.read_excel(pathTable1)
table2 = pd.read_excel(pathTable2)

#wb = load_workbook(filename = pathTable2)

#print(wb.sheetnames)
#print(table2['SITE_+/-7_AA'].values)

final = pd.DataFrame(columns=table2.columns)


#final.to_excel(pathOut, index = False)

for ind in table1.index:
    val1 = table1['peptide'][ind]
    #print("read val at" + str(ind)+ " "+ val1)
    concatVal = ""
    if val1.count("s")>1 or val1.count("t")>1:
        continue
    if "s" in val1: 
        val1Split = val1.split("s")
        valSplitLenFront = len(val1Split[1])
        valSplitLenBack = len(val1Split[0])
        if valSplitLenFront>6:
            subVal1 = val1Split[1][0:7]
          
            if valSplitLenBack > 6:
                subVal2 = val1Split[0][valSplitLenBack-7:valSplitLenBack]
                concatVal = subVal2+"S"+subVal1
            else:
                subVal2 = val1Split[0][0:valSplitLenBack]
                concatVal = subVal2+"S"+subVal1
        else:
            subVal1 = val1Split[1][0:valSplitLenFront]
            if valSplitLenBack > 6:
                subVal2 = val1Split[0][valSplitLenBack-7:valSplitLenBack]
                concatVal = subVal2+"S"+subVal1
            else:
                subVal2 = val1Split[0][0:valSplitLenBack]
                concatVal = subVal2+"S"+subVal1
    elif "t" in val1:
        val1Split = val1.split("t")
        valSplitLenFront = len(val1Split[1])
        valSplitLenBack = len(val1Split[0])
        if valSplitLenFront>6:
            subVal1 = val1Split[1][0:7]
            if valSplitLenBack > 6:
                subVal2 = val1Split[0][valSplitLenBack-7:valSplitLenBack]
                concatVal = subVal2+"T"+subVal1
            else:
                subVal2 = val1Split[0][0:valSplitLenBack]
                concatVal = subVal2+"T"+subVal1
        else:
            subVal1 = val1Split[1][0:valSplitLenFront]
            if valSplitLenBack > 6:
                subVal2 = val1Split[0][valSplitLenBack-7:valSplitLenBack]
                concatVal = subVal2+"T"+subVal1
            else:
                subVal2 = val1Split[0][0:valSplitLenBack]
                concatVal = subVal2+"T"+subVal1
    if not concatVal == "":
        #final.loc[len(final)] = table1.iloc[[ind]]
        for ind2 in table2.index:
            if table2['SITE_+/-7_AA'][ind2].strip("_") == concatVal:
                print(concatVal+ " index: "+ str(ind+2)+ " matched at "+ str(ind2+2))
                final = final.append(table2.iloc[[ind2]],ignore_index=True)
                break
                

final.to_excel(pathOut, index = False)
