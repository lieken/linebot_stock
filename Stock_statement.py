# -*- coding: utf-8 -*-
"""
Created on Thu May 28 15:51:44 2020

@author: zang
"""
# 1 . import package
import requests
import pandas as pd
from io import StringIO
import datetime

def FinancialStatements(Stock):
    #時間
    now = datetime.datetime.now()
    year = now.year
    l_year = year-1
    data=pd.DataFrame()
    # 爬取目標網站
    url = 'https://mops.twse.com.tw/server-java/t164sb01?step=1&CO_ID='+str(Stock)+'&SYEAR=2019&SSEASON=4&REPORT_ID=C#BalanceSheet'
    headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36"}
    r = requests.get(url, headers=headers)
    r.encoding = 'big5'
    # 2 . 資產負債表
    BalanceSheet_df = pd.read_html(StringIO(r.text), encoding='big-5',header=1,index_col=0)[0].dropna(axis=0,how='any')
    BalanceSheet_df.columns = [0,l_year,l_year-1]
    for i in range(l_year, l_year-2,-1):
        BalanceSheet_df[i]=BalanceSheet_df[i].replace({'\(': '-', ',': '','\)': '',}, regex=True).astype(str)
        
    #綜合損益表
    StatementOfComprehensiveIncome_df = pd.read_html(StringIO(r.text), encoding='big-5',header=1,index_col=0)[1].dropna(axis=0,how='any')
    StatementOfComprehensiveIncome_df.columns = [0,l_year,l_year-1]
    for i in range(l_year, l_year-2,-1):
           StatementOfComprehensiveIncome_df[i]=StatementOfComprehensiveIncome_df[i].replace({'\(': '-', ',': '','\)': '',}, regex=True).astype(str)
            
    #現金流量表
    CashFlows_df = pd.read_html(StringIO(r.text), encoding='big-5',header=1,index_col=0)[2].dropna(axis=0,how='any')
    CashFlows_df.columns = [0,l_year,l_year-1]
    len(CashFlows_df.columns)
    for i in range(l_year, l_year-2,-1):
        CashFlows_df[i]=CashFlows_df[i].replace({'\(': '-', ',': '','\)': '',}, regex=True).astype(str).astype(int)
                
    # 3 . 資產負債表_資產總額,負債總額,股東權益總額
    df_1=pd.concat([BalanceSheet_df.loc['1XXX'],BalanceSheet_df.loc['2XXX'],BalanceSheet_df.loc['3XXX']], axis=1,names="資產負債表")
    for i in range(1, len(df_1.columns)+1,1):
        data[i] = i 
    df_1.columns = [data]
    data=pd.DataFrame()
    df_2=pd.concat([StatementOfComprehensiveIncome_df.loc[8200],StatementOfComprehensiveIncome_df.loc[5000],StatementOfComprehensiveIncome_df.loc[5950],StatementOfComprehensiveIncome_df.loc[6000],StatementOfComprehensiveIncome_df.loc[7000],StatementOfComprehensiveIncome_df.loc[6900],StatementOfComprehensiveIncome_df.loc[9750]
], axis=1,names="綜合損益表")
    for i in range(1, len(df_2.columns)+1,1):
        data[i] = i 
    df_2.columns = [data]
    data=pd.DataFrame()

    df_3=pd.concat([CashFlows_df.loc['AAAA'],CashFlows_df.loc['BBBB'],CashFlows_df.loc['CCCC']], axis=1,names="現金流量表")
    for i in range(1, len(df_3.columns)+1,1):
        data[i] = i 
    df_3.columns = [data]
    #清理多於內存
    del year,Stock,data,i,l_year,now,url,headers
    FinancialStatements = [df_1,df_2,df_3]
    return FinancialStatements
