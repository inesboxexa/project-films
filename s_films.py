# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import plotly.express as px
import numpy as np

o_netflix_df      = pd.read_csv("/home/ines/project-films/data/netflix_titles.csv")
o_rotten_1_df   = pd.read_csv("/home/ines/project-films/data/movie_info.tsv", sep='\t')
o_rotten_2_df   = pd.read_csv("/home/ines/project-films/data/reviews.tsv", sep='\t', encoding='latin1')

#%%

o_netflix_df.head()
o_netflix_df.tail()
o_netflix_df.describe(
o_netflix_df['director'].value_counts()

#%%

def f_hist_by_column(df):

    for coli in df.columns:
        print(df[coli].name)
        if (str(df[coli].dtype) == "object"):       
            if df[coli].unique().size < 300:
                print(df[coli].unique())
                fig = px.histogram(df, x=coli)
                fig.show()
                
#%%
                
f_hist_by_column(o_netflix_df)

#%%

rotten_1_df.id == rotten_2_df.loc[rotten_1_df.index].id