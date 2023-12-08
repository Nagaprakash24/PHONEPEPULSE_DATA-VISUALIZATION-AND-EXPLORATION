import os     #This package is to access files in local system
import json
from tkinter import OptionMenu    
import pandas as pd
import psycopg2
import git
import requests
import plotly.express as px
import numpy as np
import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu
import PIL



#sql to dataframe,aggre_trans
mydb=psycopg2.connect(host='localhost',user='postgres',password='PRAKASH',database='phonepe_data',port=5432)
cursor=mydb.cursor()

query1='''select * from aggregated_transaction'''
cursor.execute(query1)
mydb.commit()
d1=cursor.fetchall()
agre_tran=pd.DataFrame(d1,columns=("States",
                        "Years",
                        'Quarter',
                        'Transaction_type',
                        'Transaction_count',
                        'Transaction_amount'))

#REPLACE THE SPELLING FOR MAP AND FOR OTHER VISUALISATION
agre_tran.States=agre_tran.States.str.title()
agre_tran['States']=agre_tran['States'].replace(['Andaman-&-Nicobar-Islands'],'Andaman & Nicobar')
agre_tran['States']=agre_tran['States'].replace(['Dadra-&-Nagar-Haveli-&-Daman-&-Diu'],'Dadra and Nagar Haveli and Daman and Diu')
agre_tran['States']=agre_tran['States'].str.replace('-',' ')


#sql to dataframe-2,aggre_user
mydb=psycopg2.connect(host='localhost',user='postgres',password='PRAKASH',database='phonepe_data',port=5432)
cursor=mydb.cursor()

query2='''select * from aggregated_user'''
cursor.execute(query2)
mydb.commit()
d2=cursor.fetchall()
agre_use=pd.DataFrame(d2,columns=("States",
                                  "Years",
                                  'Quarter',
                                  'Brands',
                                  'Transaction_count',
                                  'Percentage'))


agre_use.States=agre_use.States.str.title()
agre_use['States']=agre_use['States'].replace(['Andaman-&-Nicobar-Islands'],'Andaman & Nicobar')
agre_use['States']=agre_use['States'].replace(['Dadra-&-Nagar-Haveli-&-Daman-&-Diu'],'Dadra and Nagar Haveli and Daman and Diu')
agre_use['States']=agre_use['States'].str.replace('-',' ')

#sql to dataframe-3,map transaction
mydb=psycopg2.connect(host='localhost',user='postgres',password='PRAKASH',database='phonepe_data',port=5432)
cursor=mydb.cursor()

query3='''select * from map_transaction'''
cursor.execute(query3)
mydb.commit()
d3=cursor.fetchall()
map_tran=pd.DataFrame(d3,columns=("States",
                                  "Years",
                                  'Quarter',
                                  'Districts',
                                  'Transaction_count',
                                  'Transaction_amount'))

map_tran.States=map_tran.States.str.title()
map_tran['States']=map_tran['States'].replace(['Andaman-&-Nicobar-Islands'],'Andaman & Nicobar')
map_tran['States']=map_tran['States'].replace(['Dadra-&-Nagar-Haveli-&-Daman-&-Diu'],'Dadra and Nagar Haveli and Daman and Diu')
map_tran['States']=map_tran['States'].str.replace('-',' ')


#sql to dataframe-4,map_user
mydb=psycopg2.connect(host='localhost',user='postgres',password='PRAKASH',database='phonepe_data',port=5432)
cursor=mydb.cursor()

query4='''select * from map_user'''
cursor.execute(query4)
mydb.commit()
d4=cursor.fetchall()
map_user=pd.DataFrame(d4,columns=("States",
                                  "Years",
                                  'Quarter',
                                  'Districts',
                                  'RegisteredUsers',
                                  'AppOpens'))


map_user.States=map_user.States.str.title()
map_user['States']=map_user['States'].replace(['Andaman-&-Nicobar-Islands'],'Andaman & Nicobar')
map_user['States']=map_user['States'].replace(['Dadra-&-Nagar-Haveli-&-Daman-&-Diu'],'Dadra and Nagar Haveli and Daman and Diu')
map_user['States']=map_user['States'].str.replace('-',' ')

#sql to dataframe-5,top transaction
mydb=psycopg2.connect(host='localhost',user='postgres',password='PRAKASH',database='phonepe_data',port=5432)
cursor=mydb.cursor()

query5='''select * from top_transaction'''
cursor.execute(query5)
mydb.commit()
d5=cursor.fetchall()
top_tran=pd.DataFrame(d5,columns=("States",
                                  "Years",
                                  'Quarter',
                                  'Pincodes',
                                  'Transaction_Count',
                                  'Transaction_amount'))


top_tran.States=top_tran.States.str.title()
top_tran['States']=top_tran['States'].replace(['Andaman-&-Nicobar-Islands'],'Andaman & Nicobar')
top_tran['States']=top_tran['States'].replace(['Dadra-&-Nagar-Haveli-&-Daman-&-Diu'],'Dadra and Nagar Haveli and Daman and Diu')
top_tran['States']=top_tran['States'].str.replace('-',' ')

#sql to dataframe-6,top user
mydb=psycopg2.connect(host='localhost',user='postgres',password='PRAKASH',database='phonepe_data',port=5432)
cursor=mydb.cursor()

query6='''select * from top_user'''
cursor.execute(query6)
mydb.commit()
d6=cursor.fetchall()
top_userr=pd.DataFrame(d6,columns=("States",
                                  "Years",
                                  'Quarter',
                                  'Pincodes',
                                  'RegisteredUser'))

top_userr.States=top_userr.States.str.title()
top_userr['States']=top_userr['States'].replace(['Andaman-&-Nicobar-Islands'],'Andaman & Nicobar')
top_userr['States']=top_userr['States'].replace(['Dadra-&-Nagar-Haveli-&-Daman-&-Diu'],'Dadra and Nagar Haveli and Daman and Diu')
top_userr['States']=top_userr['States'].str.replace('-',' ')

#INDIA MAP PLOTTING
def geo_map1():
    url = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
    response=requests.get(url)
    Gdata1=json.loads(response.content)

    fig = px.choropleth(
                    agre_tran,
                    geojson=Gdata1,
                    locations="States",
                    featureidkey="properties.ST_NM",
                    color="Transaction_amount",
                    color_continuous_scale="Sunsetdark",
                    range_color=(0,3000000),
                    title="TRANSACTION AMOUNT",
                    hover_name="States",
                    animation_frame="Years",
                    animation_group="Quarter")

    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(height=600,width=800)
    return st.plotly_chart(fig)

#BAR PLOT FOR TRANSACTION COUNT
def transaction_count():
    agcn=agre_tran[["Transaction_type","Transaction_count"]]
    agcn1=agcn.groupby('Transaction_type')['Transaction_count'].sum()
    dfagcn=pd.DataFrame(agcn1).reset_index()
    fig_ty=px.bar(dfagcn,x='Transaction_type',y='Transaction_count',title="TRANSACTION count",color_discrete_sequence=px.colors.sequential.Greens_r)
    fig_ty.update_layout(width=800,height=500)
    return st.plotly_chart(fig_ty)


def geo_map2():
    url="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
    response=requests.get(url)
    Gdata1=json.loads(response.content)

    agre_tran.States=agre_tran.States.str.title()
    agre_tran['States']=agre_tran['States'].replace(['Andaman-&-Nicobar-Islands'],'Andaman & Nicobar')
    agre_tran['States']=agre_tran['States'].replace(['Dadra-&-Nagar-Haveli-&-Daman-&-Diu'],'Dadra and Nagar Haveli and Daman and Diu')
    agre_tran['States']=agre_tran['States'].str.replace('-',' ')

    map2=agre_tran[['States','Transaction_count','Quarter','Years']]

    fig = px.choropleth(
                    map2,
                    geojson=Gdata1,
                    locations="States",
                    featureidkey="properties.ST_NM",
                    color="Transaction_count",
                    color_continuous_scale="solar",
                    range_color= (0,3000000),
                    title="TRANSACTION COUNT",
                    hover_name="States",
                    animation_frame="Years",
                    animation_group="Quarter")

    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(height=600,width=800)
    return st.plotly_chart(fig)

#BAR PLOT FOR TRANSACTION AMOUNT

def transaction_amount():
    agty=agre_tran[["Transaction_type","Transaction_amount"]]
    agty1=agty.groupby('Transaction_type')['Transaction_amount'].sum()
    dfagty=pd.DataFrame(agty1).reset_index()
    fig_ty=px.bar(dfagty,x='Transaction_type',y='Transaction_amount',title="TRANSACTION TYPE",color_discrete_sequence=px.colors.sequential.Reds_r)
    fig_ty.update_layout(width=800,height=500)
    return st.plotly_chart(fig_ty)

def trans_amnt_yr(yrs):

    url="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
    response=requests.get(url)
    data1=json.loads(response.content)
    state_name_tran=[feature["properties"]['ST_NM']for feature in data1['features']]
    state_name_tran.sort()

    agre_tran.States=agre_tran.States.str.title()
    agre_tran['States']=agre_tran['States'].replace(['Andaman-&-Nicobar-Islands'],'Andaman & Nicobar')
    agre_tran['States']=agre_tran['States'].replace(['Dadra-&-Nagar-Haveli-&-Daman-&-Diu'],'Dadra and Nagar Haveli and Daman and Diu')
    agre_tran['States']=agre_tran['States'].str.replace('-',' ')


    year=int(yrs)
    yr1= agre_tran[["States","Years","Transaction_amount"]]
    yr2=yr1.loc[(agre_tran["Years"]==year)]
    yr3=yr2.groupby("States")["Transaction_amount"].sum()
    yrby=pd.DataFrame(yr3).reset_index()

    
    fig_yr= px.choropleth(yrby, geojson= data1, locations= "States", featureidkey= "properties.ST_NM",
                            color= "Transaction_amount", color_continuous_scale="RdBu", range_color=(0,800000000000),
                            title="TRANSACTION AMOUNT BY YEAR", hover_name= "States")

    fig_yr.update_geos(fitbounds="locations",visible=False)
    fig_yr.update_layout(width=900,height=700)
    return st.plotly_chart(fig_yr)


def trans_countby_yr(yrs):
    year= int(yrs)
    cu1= agre_tran[["Transaction_type", "Years", "Transaction_count"]]
    cu2= cu1.loc[(agre_tran["Years"]==year)]
    cu3= cu2.groupby("Transaction_type")["Transaction_count"].sum()
    cuyr= pd.DataFrame(cu3).reset_index()

    fig_cuyr= px.bar(cuyr,x= "Transaction_type", y= "Transaction_count", title= "TRANSACTION COUNT BY TYPE",
                    color_discrete_sequence=px.colors.sequential.Greens_r)
    fig_cuyr.update_layout(width=600, height=500)
    return st.plotly_chart(fig_cuyr)



def trans_cont_yr(yrs):
    url= "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
    response= requests.get(url)
    data1= json.loads(response.content)

    agre_tran.States=agre_tran.States.str.title()
    agre_tran['States']=agre_tran['States'].replace(['Andaman-&-Nicobar-Islands'],'Andaman & Nicobar')
    agre_tran['States']=agre_tran['States'].replace(['Dadra-&-Nagar-Haveli-&-Daman-&-Diu'],'Dadra and Nagar Haveli and Daman and Diu')
    agre_tran['States']=agre_tran['States'].str.replace('-',' ')
    
    year= int(yrs)
    yr1= agre_tran[["States","Years","Transaction_count"]]
    yr2= yr1.loc[(agre_tran["Years"]==year)]
    yr3= yr2.groupby("States")["Transaction_count"].sum()
    yrby= pd.DataFrame(yr3).reset_index()

    fig_yr= px.choropleth(yrby, geojson= data1, locations= "States", featureidkey= "properties.ST_NM",
                            color= "Transaction_count", color_continuous_scale="RdBu", range_color=(0,800000000000),
                            title="TRANSACTION COUNT BY YEAR", hover_name= "States")

    fig_yr.update_geos(fitbounds= "locations", visible= False)
    fig_yr.update_layout(width=900,height=700)
    return st.plotly_chart(fig_yr)

def trans_amtby_yr(yrs):
    year= int(yrs)
    cu1= agre_tran[["Years", "Transaction_type", "Transaction_amount"]]
    cu2= cu1.loc[(agre_tran["Years"]==year)]
    cu3= cu2.groupby("Transaction_type")["Transaction_amount"].sum()
    cuyr= pd.DataFrame(cu3).reset_index()

    fig_cuyr= px.bar(cuyr,x= "Transaction_type", y= "Transaction_amount", title= "TRANSACTION COUNT BY TYPE",
                    color_discrete_sequence=px.colors.sequential.Rainbow_r)
    fig_cuyr.update_layout(width=600, height=500)
    return st.plotly_chart(fig_cuyr)

#QUESTIONS FOR THIS PROJECT
def ques1():
    brand= agre_use[["Brands","Transaction_count"]]
    brand1= brand.groupby("Brands")["Transaction_count"].sum().sort_values(ascending=False)
    brand2= pd.DataFrame(brand1).reset_index()

    fig_brd= px.pie(brand2, values= "Transaction_count", names= "Brands", color_discrete_sequence=px.colors.sequential.Bluyl_r,
                       title= "Top Mobile Brands and Transaction_count")
    return st.plotly_chart(fig_brd)
    

def ques2():
    lowt= agre_tran[["States","Transaction_amount"]]
    lowt1= lowt.groupby("States")["Transaction_amount"].sum().sort_values(ascending=True)
    lowt2= pd.DataFrame(lowt1).reset_index().head(15)

    fig_lt= px.bar(lowt2, x= "States", y= "Transaction_amount", title= "LOWEST TRANSACTION and STATES",
                color_discrete_sequence=px.colors.sequential.Purples_r)
    fig_lt.update_layout(width= 1000, height= 500)
    return st.plotly_chart(fig_lt)
    
def ques3():
    brand= map_tran[["Districts","Transaction_amount"]]
    brand1= brand.groupby("Districts")["Transaction_amount"].sum().sort_values(ascending=False)
    brand2= pd.DataFrame(brand1).reset_index().head(10)

    fig_brd= px.pie(brand2, values= "Transaction_amount", names= "Districts", color_discrete_sequence=px.colors.sequential.Bluered_r,
                       title= "TOP 10 DISTRICTS OF HIGHEST TRANSACTION")
    return st.plotly_chart(fig_brd)
    
def ques4():
    brand= map_tran[["Districts","Transaction_amount"]]
    brand1= brand.groupby("Districts")["Transaction_amount"].sum().sort_values(ascending=True)
    brand2= pd.DataFrame(brand1).reset_index().head(10)

    fig_brd= px.pie(brand2, values= "Transaction_amount", names= "Districts", color_discrete_sequence=px.colors.sequential.Bluered_r,
                       title= "TOP 10 DISTRICTS OF LOWEST TRANSACTION")
    return st.plotly_chart(fig_brd)
    
def ques5():
    lowt= agre_tran[["States","Transaction_amount"]]
    lowt1= lowt.groupby("States")["Transaction_amount"].sum().sort_values(ascending=False)
    lowt2= pd.DataFrame(lowt1).reset_index().head(15)

    fig_lt= px.bar(lowt2, x= "States", y= "Transaction_amount", title= "HIGHTEST TRANSACTION AND STATES",
                color_discrete_sequence=px.colors.sequential.Cividis_r)
    fig_lt.update_layout(width= 1000, height= 500)
    return st.plotly_chart(fig_lt)

def ques6():
    lowt= map_user[["States","AppOpens"]]
    lowt1= lowt.groupby("States")["AppOpens"].sum().sort_values(ascending=True)
    lowt2= pd.DataFrame(lowt1).reset_index().head(10)

    fig_lt= px.bar(lowt2, x= "States", y= "AppOpens", title= "LOWEST STATES WITH APPOPENS",
                color_discrete_sequence=px.colors.sequential.Redor_r)
    fig_lt.update_layout(width= 1000, height= 500)
    return st.plotly_chart(fig_lt)
    
def ques7():
    lowt= map_user[["States","AppOpens"]]
    lowt1= lowt.groupby("States")["AppOpens"].sum().sort_values(ascending=False)
    lowt2= pd.DataFrame(lowt1).reset_index().head(10)

    fig_lt= px.bar(lowt2, x= "States", y= "AppOpens", title= "HIGHTEST STATES WITH APPOPENS",
                color_discrete_sequence=px.colors.sequential.Bluered_r)
    fig_lt.update_layout(width= 1000, height= 500)
    return st.plotly_chart(fig_lt)
    
def ques8():
    lowt= agre_tran[["States","Transaction_count"]]
    lowt1= lowt.groupby("States")["Transaction_count"].sum().sort_values(ascending=True)
    lowt2= pd.DataFrame(lowt1).reset_index()

    fig_lt= px.bar(lowt2, x= "States", y= "Transaction_count", title= "LOWEST COUNT AND STATES",
                color_discrete_sequence=px.colors.sequential.Bluered_r)
    fig_lt.update_layout(width= 1000, height= 500)
    return st.plotly_chart(fig_lt)
    
def ques9():
    lowt= agre_tran[["States","Transaction_count"]]
    lowt1= lowt.groupby("States")["Transaction_count"].sum().sort_values(ascending=False)
    lowt2= pd.DataFrame(lowt1).reset_index()

    fig_lt= px.bar(lowt2, x= "States", y= "Transaction_count", title= "HIGHEST COUNT AND STATES",
                color_discrete_sequence=px.colors.sequential.Blues_r)
    fig_lt.update_layout(width= 1000, height= 500)
    return st.plotly_chart(fig_lt)
    
def ques10():
    brand= map_tran[["Districts","Transaction_amount"]]
    brand1= brand.groupby("Districts")["Transaction_amount"].sum().sort_values(ascending=True)
    brand2= pd.DataFrame(brand1).reset_index().head(20)

    fig_brd= px.bar(brand2, x= "Districts", y= "Transaction_amount", color_discrete_sequence=px.colors.sequential.Pinkyl_r,
                       title= "DISTRICTS TO LOWEST TRANSACTION")
    return st.plotly_chart(fig_brd)



st.set_page_config(layout="wide", page_title='phonepe pulse', page_icon= ':star:')
st.header(":violet[PHONEPE DATA VISUALIZATION AND EXPLORAION]")
st.caption(":violet[India's Leading Digital Payment And Banking Service Provider]")
tab1,tab2,tab3=st.tabs(["***HOME***","***DATA VISUALIZATION 📊***","***TOP DATA***"])
  


with tab1:
    cl1,cl2,cl3=st.columns(3)

    with cl1:
        on=st.toggle(":violet[ABOUT]")
        if on:
            st.write('''The narrative of Indian digital payments has definitely captivated the world's attention. From the greatest cities to the most distant villages, mobile phone and data penetration is driving a payments revolution''')
            st.write(""
                     "")
            st.write('''When PhonePe first launched five years ago, we were continuously on the lookout for authoritative data sources on digital payments in India. We were looking for answers to queries such,How are consumers truly using digital payments? What are the most notable cases? Is the penetration of QR codes giving kiranas in Tier 2 and 3 a facelift?
We resolved to demystify the what, why, and how of digital payments in India this year, as we became India's largest digital payments platform with a 46% UPI market share.''')
    
    with cl2:
        on=st.toggle(":violet[FEATURE]")
        if on:
            st.selectbox(
                    "",
                    ("Easy Interface", "Payment To Merchant", "Fund Transfer","Recharge and Bill Payments",
                        "Buy & Sell Gold","PhonePe ATM"),
                    index=None,
                    placeholder="Explore The Feature"
                    )

    with st.container():
        videofile=open(r"C:\Users\prakash\Documents\Project-2\video\PHONEPEPULSE.mp4",'rb')
        vid=videofile.read()
        st.video(vid)

with tab2:
    yr1=st.selectbox(":violet[SELECT THE DESIRED OPTION ⬇️]",
                    ("ALL","2018","2019","2020","2021","2022","2023"),index=None,placeholder="SELECT THE YEAR")
    if yr1=="ALL":
        cl1,cl2=st.columns(2)
        with cl1:
            geo_map1()
            transaction_count()
            geo_map2()
            transaction_amount()
        with cl2:
            st.write(" ")
    elif yr1=="2018":
        cl1,cl2=st.columns(2)
        with cl1:
            trans_amnt_yr(yr1)
            trans_cont_yr(yr1)
        with cl2:
            st.write(" ")
    elif yr1=="2019":
        cl1,cl2=st.columns(2)
        with cl1:
            trans_amnt_yr(yr1)
            trans_cont_yr(yr1)
        with cl2:
            st.write(" ")
    elif yr1=="2020":
        cl1,cl2=st.columns(2)
        with cl1:
            trans_amnt_yr(yr1)
            trans_amnt_yr(yr1)
        with cl2:
            st.write(" ")
    elif yr1=="2021":
        cl1,cl2=st.columns(2)
        with cl1:
            trans_amnt_yr(yr1)
            trans_cont_yr(yr1)
        with cl2:
            st.write(" ")
    elif yr1=="2022":
        cl1,cl2=st.columns(2)
        with cl1:
            trans_amnt_yr(yr1)
            trans_cont_yr(yr1)
        with cl2:
            st.write(" ")
    elif yr1=="2023":
        cl1,cl2=st.columns(2)
        with cl1:
            trans_amnt_yr(yr1)
            trans_cont_yr(yr1)
        with cl2:
            st.write(" ")

with tab3:
    on=st.toggle("TOP 10 DISTRICTS AND THIER TRANSACTION AMOUNT")
    if on:
        ques1()
        ques2()

    on1=st.toggle("STATES BY TRANSACTION AMOUNT")
    if on1:
        ques3()
        ques4()

    on2=st.toggle("STATES BY APP OPENING")
    if on2:
        ques5()
        ques6()
    on3=st.toggle("STATES BY TRANSACTION COUNT")
    if on3:
        ques7()
        ques8()
    on4=st.toggle("DISTRICTS HAVING LOWEST TRANSACTION AMOUNT")
    if on4:
        ques9()
    on5=st.toggle("TOP MOBILE AND THIER TRANSACTION")
    if on5:
        ques10()
        


              


