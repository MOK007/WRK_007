# -*- coding: utf-8 -*-
#from __future__ import print_function

import numpy as np # Numpy library for arrays
import pandas as pd
import codecs
import string

import hashlib
import base64

from pandas import set_option
set_option("display.max_rows", 40) #Allows to control how Pandas displays the result
set_option("display.max_columns", 80) #Allows to control how Pandas displays the result


## n;ceh;pc;tp;dog;login;s;db;de;s1;s2;s3;dsb;dse
# A           B            C        D      E              F            G       H        I         J     K      L                                              M                                  P
#crk  & 7101000000010010 & 205.75 & CASH & Готівка & 15/06/2018 & 18/06/2018 & 3 & ???? 10023 & Платеж & & oshad_80D-317^^ПАТ "Ощадбанк"  № 80D115-317/17 &

print string.uppercase
print string.punctuation
print string.whitespace
print string.letters
print string.upper("марія".decode("cp1251")).encode("cp866","replace")
print u'asdfg'.upper().encode("cp1251")

text="маріїєя"
c = codecs.lookup('cp1251');
print c.decode(text)[0].upper().encode("cp866","replace");



with codecs.open('examples/11_.txt','rb','cp1251') as f:
   df = pd.read_csv(f, sep="\t",  header=None, names=list('ABCDEFGHIJKLM'), converters={"A":str,"B":str},
     index_col=False )

#df['E'] = pd.to_datetime(df['E'], format='dd.mm.yyyy')
df['F'] = pd.to_datetime(df['F'])
df['F'] = pd.to_datetime(df['F'])

print df
print df.dtypes

#exit()


'''
print df["A"]
print df["B"]
print df["M"]
print df["F"]

print "|--> " +df["L"][0].decode('utf-8','ignore')
issues = pd.DataFrame(df, columns=['B', 'C', 'F', 'G', 'L'])                                                          
print issues
'''



'''
df.set_index(["B"])
print df
print df.dtypes
print df["A"]
print df["B"]

## df['date'] = pd.to_datetime(df['date'], format='%d%b%Y')
# "E": pd.to_datetime('13000101', format='%Y%m%d', errors='coerce')}, 
#  "E": pd.to_datetime(): date_parser=lambda x: pd.to_datetime(x, format='%d/%m/%Y'),

exit()
'''

#df=pd.read_clipboard(engine="python")
#print df

converters = {col: str for col in ("A","B", "C")}

xlsx = pd.ExcelFile('examples/162_Rep.xlsx')
df = pd.read_excel(xlsx, sheet_name=0, skiprows=[0,], header=None, names=list('ABCDEFGHIJKLMNOPQR'),
       converters= converters,
       index_col=False )
df["I"] = pd.to_datetime(df["I"])
df["J"] = pd.to_datetime(df["J"])

print df.dtypes
#df.A =  map(lambda x: str(x) if len(str(x))==6 else "0" + str(x) , df.A)
df.A =  map(lambda x: string.rjust(str(x),6,"0") , df.A)
df.C =  map(lambda x: string.rjust(str(x),16,"0") , df.C)
print df.dtypes


issues = pd.DataFrame(df, columns=['A','C',"I","J"])
print issues
print df.A
print df.C
print df.D
#print df.describe()
print df[['A','C']][3:4]
for r in  df.C:
   print str(r) +"\t;;;" 

#df2 = pd.DataFrame({'col1': [1, 2, 2],'col_right':[2, 2, 2]})
dfr=pd.DataFrame({'C':['0501003470001602','0501003470001612'],"mrk":["1","1"]} )

print pd.merge(df[['A','C','K']], dfr, on='C', how='left', indicator=True)
## ??print df[['A','C','K']].join(dfr)

exit()

#df = pd.read_excel(xlsx, sheet_name=0, names=("ZZZ","XXX"), usecols="A:B", dtype={"ZZZ":str,"XXX":str}, engine="xlrd" )

#df = pd.read_excel(xlsx, sheet_name=0,   engine="xlrd" , index_col=[0])



#df = pd.read_excel(xlsx, sheet_name[0,],    index_col=False )


#df["I"] = pd.to_datetime(df["I"])

#print df

#issues = pd.DataFrame(df, columns=['qw', 'zx'])
issues = df                                                         
print issues



#print df["FS"]


#print df[("Логін договору".decode("cp1251")),("Телефон",decode("cp1251"))]

#df["ОР клієнта".decode("cp1251")]=str(df["ОР клієнта".decode("cp1251")])

#print df["ОР клієнта".decode("cp1251")].loc[2:3]
