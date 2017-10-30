import pandas as pd
import numpy as np

inputfilepath = "/Users/emadezzeldin/Dropbox/Networking/Ashfaq/Grants/"
inputfilename = "GrantMoney.csv"
inputfile     = inputfilepath +  inputfilename

Grants = pd.read_csv (inputfile)
print  (Grants.head())
def substiuteMoney (Money):
    Money = str (Money)
    Money = (float (Money [1:-1]) * 1000 if "K" in Money  else float(Money[1:-1]) * 1000000)
    return Money
print (substiuteMoney ("$8K"))
print (substiuteMoney ("$1.8M"))
try:
    Grants["Grants"] = Grants["Grants"].apply (lambda x : substiuteMoney (x))
except Exception as err:
    print (err)
print (Grants.head())
Grants.to_csv ("GrantsMoney_Clean.csv",index = False)
