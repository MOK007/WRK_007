# -*- coding: utf-8 -*-
#from __future__ import print_function

import numpy as np # Numpy library for arrays
import pandas as pd
import codecs
from collections import OrderedDict

import hashlib
import base64

from pandas import set_option
set_option("display.max_rows", 30) #Allows to control how Pandas displays the result


xlsx = pd.ExcelFile('examples/_162_Reps.xlsx')
#df = pd.read_excel(xlsx, [0,], skiprows=[0,], header=None, names=list('ABCDEFGHIJKLMNOPQR'), 
#       index_col=False )

#df = pd.read_excel(xlsx, [0], names=("ZZZ","XXX"), usecols="A:B", dtype={"ZZZ":str,"XXX":str}, engine="xlrd" )

df = pd.read_excel(xlsx, sheet_name=0,   engine="xlrd" , index_col=None,  na_values=['None'])
print df

print df.dtypes
#df=pd.DataFrame.from_dict(sales)
print df["zx"]
#data_dict = df.to_dict()
#print data_dict


#df = pd.read_excel(xlsx, ["sheet1",],    index_col=None )


#df["I"] = pd.to_datetime(df["I"])

#print pd.DataFrame(df,columns=["zx"])
#print df.dtypes
