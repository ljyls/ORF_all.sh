#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
import argparse

parser=argparse.ArgumentParser(description="Merge duplicate sequences and output sequences with 20 or more amino acids")  
parser.add_argument("--file", dest="input_file", type=str, default="", required=True, help="input_file")
parser.add_argument("--sep", dest="sep", type=str, default="", required=True, help="input_file")
args=parser.parse_args()

#Merge duplicate sequences
df=pd.read_csv(args.input_file, header=None, sep='\t')
df=df.groupby(by=1).apply(lambda x:args.sep.join(x[0])).reset_index()

#output sequences with 20 or more amino acids
df=df[df[1].apply(lambda x: len(str(x))>=20)].reset_index(drop=True)
df.to_csv(f'filtered_{args.input_file}', index=False, header=None, columns=[0,1], sep='\t')

print('done ++++++++++++++++++sequnce_filter.py ++++++++++++++++++')
