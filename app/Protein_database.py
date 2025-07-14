#!/usr/bin/env python
# coding: utf-8


import numpy as np
import pandas as pd
import os

df_OS=pd.read_csv('./filtered_ORF_signal.table', header=None, sep='\t')

df_OS_split=df_OS.join(df_OS[0].str.split('|', expand=True).stack().reset_index(level=1, drop=True).rename("Accession"))
df_OS_split=df_OS_split["Accession"].str.split('_ORF\d+',expand=True)[0].str.strip()
df_OS_split.drop_duplicates

df_TA=pd.read_csv('../filtered_transcript_all.table', header=None, sep='\t')
df_TA_split=df_TA[0]
df_TA_split.drop_duplicates
df_list=set(df_TA_split).difference(set(df_OS_split))
df_list=pd.DataFrame(df_list)
df_TA=pd.merge(df_list,df_TA,how='left',on=0)

df=pd.concat([df_OS,df_TA], axis=0, join='outer')
df=df.reset_index(drop=True)
df.to_csv("./Search_file.table", index=False, header=None, sep='\t')

print('done ++++++++++++++++Protein_database.py++++++++++++++++++')