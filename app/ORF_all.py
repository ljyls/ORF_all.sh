#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
import glob

df=pd.read_csv('../../filtered_transcript_all.table', header=None, sep='\t')
df.to_csv("0.seq", index=False, header=None, columns=[0,1], sep='\t')
df[1]=df[1].str.replace('^M','X', case=False, regex=True)
df[1]="M"+df[1].map(str)
df.to_csv("1.tmp", index=False, header=None, columns=[0,1], sep='\t')
df[1]=df[1].str.replace('M','-M', n=-1, case=False)
data=df[1].str.split('-',expand=True)
m=len(data.columns)

k=range(2,m,1)
for i in list(k):

    dfn=pd.read_csv(f'{i-1}.tmp', header=None, sep='\t')
    dfn[1]=dfn[1].str.replace('M','-M', case=False, n=2)   
    dfn[1]=dfn[1].str.split('-',expand=True)[2]
    dfn=dfn.dropna(axis=0)
    dfn.to_csv(f'{i}.tmp', index=False, header=None, sep='\t')
    dfn1=pd.read_csv(f'{i}.tmp', header=None, sep='\t')
    dfn1[0]=dfn1[0]+f'_ORF{i-1}'
    dfn1.to_csv(f'{i-1}.seq', index=False, header=None, columns=[0,1], sep='\t')

files = glob.glob("*.seq")
cols = [0, 1] 
dflist = [pd.read_csv(i, usecols=cols, header=None, sep='\t') for i in files]
df = pd.concat(dflist) 
df.to_csv("ORF_all.table", index=False, header=None, sep='\t')

print('done ++++++++++++++++++ORF_all.py++++++++++++++++++')
