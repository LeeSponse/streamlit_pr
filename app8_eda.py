import streamlit as st
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
data = datasets.load_diabetes()

# iris.csv 파일 읽어와서
# 여러 칼럼들 선택 가능토록 하여,
# 선택한 컬럼들만 화면에 보여주고,
# 상관계수도 보여주도록 개발.

def run_eda() :
    st.subheader('EDA 화면')
    df = pd.read_csv('./data/iris.csv')

    st.dataframe(df)

    column_list = df.columns

    choice_list = st.multiselect('컬럼을 선택하기', column_list)

    print(choice_list)

    if choice_list != [] :

        st.dataframe( df[ choice_list ] )

        st.dataframe( df[choice_list].corr(numeric_only= True) ) # numerice_only= True : 숫자만 계산하게 하기


    
    
