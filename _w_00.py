# -*- coding: utf-8 -*-
#from __future__ import print_function

import numpy as np # Numpy library for arrays
import pandas as pd
import codecs

import hashlib
import base64

from pandas import set_option
set_option("display.max_rows", 40) #Allows to control how Pandas displays the result
set_option("display.max_columns", 80) #Allows to control how Pandas displays the result


## n;ceh;pc;tp;dog;login;s;db;de;s1;s2;s3;dsb;dse
# A           B            C        D      E              F            G       H        I         J     K      L                                              M                                  P
#crk  & 7101000000010010 & 205.75 & CASH & Готівка & 15/06/2018 & 18/06/2018 & 3 & ???? 10023 & Платеж & & oshad_80D-317^^ПАТ "Ощадбанк"  № 80D115-317/17 &


with codecs.open('examples/11_.txt','rb','cp1251') as f:
   df = pd.read_csv(f, sep="\t",  header=None, names=list('ABCDEFGHIJKLM'), converters={"A":str,"B":str},
  index_col=False)

#df['E'] = pd.to_datetime(df['E'], format='dd.mm.yyyy')
df['F'] = pd.to_datetime(df['F'])
df['F'] = pd.to_datetime(df['F'])

print df
print df.dtypes

'''
print df["A"]
print df["B"]
print df["M"]
print df["F"]
'''
print df["L"]
issues = pd.DataFrame(df, columns=['B', 'C', 'F', 'G', 'L'])                                                          
print issues


'''
df.set_index(["B"])
print df
print df.dtypes
print df["A"]
print df["B"]

## df['date'] = pd.to_datetime(df['date'], format='%d%b%Y')
# "E": pd.to_datetime('13000101', format='%Y%m%d', errors='coerce')}, 
#  "E": pd.to_datetime(): date_parser=lambda x: pd.to_datetime(x, format='%d/%m/%Y'),
'''