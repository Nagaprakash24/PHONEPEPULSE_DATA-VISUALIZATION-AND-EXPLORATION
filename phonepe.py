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


#STREAMLIT PART

st.set_page_config(layout="wide", page_title='PHONEPE DATA VISUALIZATION AND EXPLORATION', page_icon= ':star:')

st.image('banner1.png', caption=None, width=None, use_column_width=True, clamp=False, channels="RGB", output_format="auto")


selected = option_menu(None, ["HOME",'FEATURES','QUERIES','DATA VISUALIZATION','CONTACT INFORMATION'], 
    icons=['house-door','alt', 'database-check','bar-chart-line-fill','envelope-at-fill'], 
    menu_icon="cast", default_index=0, orientation="horizontal",
       styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "darkviolet", "font-size": "15px"}, 
        "nav-link": {"font-size": "15px", "text-align": "left", "margin":"1px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "grey"},
    })

def local_css(file_name):
    with open(file_name)as f:
        st.markdown(f"<style>{f.read()},</style>",unsafe_allow_html=True)
local_css("style/style.css")

def load_image(image_path):
    return Image.open(image_path)


with st.sidebar:
    
    image=load_image("C:/Users/prakash/Documents/Project-2/phonepelogo.png")
    st.sidebar.image(image,width=170,caption=None)
    image=load_image("C:/Users/prakash/Documents/Project-2/pulselogo.gif")
    st.sidebar.image(image,width=150,caption="Welcome")
    
    st.header("ABOUT")
    st.markdown('''The narrative of Indian digital payments has definitely captivated the world's attention. From the greatest cities to the most distant villages, mobile phone and data penetration is driving a payments revolution''')
    st.write('''When PhonePe first launched five years ago, we were continuously on the lookout for authoritative data sources on digital payments in India.We were looking for answers to queries such,How are consumers truly using digital payments? What are the most notable cases?Is the penetration of QR codes giving kiranas in Tier 2 and 3 a facelift?We resolved to demystify the what, why, and how of digital payments in India this year, as we became India's largest digital payments platform with a 46% UPI market share.''')    
    st.markdown("---")
    st.link_button("Learn more..." ,"https://www.phonepe.com/pulse/")
    
if selected == "HOME":
       
    st.header(":violet[PHONEPE DATA VISUALIZATION AND EXPLORATION]")
    st.caption(":darkviolet[India's Leading Digital Payment And Banking Service Provider]")
    st.markdown("---")
   
    VIDEO_DATA = open('PHONEPEPULSE.mp4','rb')
    video_bytes = VIDEO_DATA.read()
    
    text_column,video_column=st.columns((1,2))
    with video_column:
        st.video(video_bytes)
    with text_column:
         st.subheader("INTRODUCTION:")
         st.write("""I am excited to present our project on "PhonePe Data Visualization and Exploration." In the rapidly evolving landscape of digital transactions and financial technology, PhonePe stands as a prominent player, facilitating seamless and secure transactions for millions of users. """)
    
    VIDEO_DATA6 = open('map.mp4','rb')
    video_bytes6 = VIDEO_DATA6.read()
  
    vcol,tcol=st.columns((1,2))
    with vcol:
        st.video(video_bytes6,start_time=0,format="video/mp4")
    with tcol:    
      st.subheader("OBJECTIVE:")
      st.write("""The primary objective of our project is to delve into the rich dataset provided by PhonePe and extract valuable insights through advanced data visualization and exploration techniques. By leveraging the power of visual representation, we aim to bring forth patterns, trends, and actionable information that can contribute to strategic decision-making and enhance user experience.""")
    st.markdown("---")
    st.image('phone1.png',caption=None ,width=None,use_column_width=True,channels="RGB",output_format="auto")
    st.header("KEY COMPONENTS")
    st.subheader("Data Collection:")
    st.write("""We have collected and curated a comprehensive dataset from PhonePe, encompassing transactional data, user behavior, and other relevant metrics. This dataset serves as the foundation for our exploration. """)
    st.subheader("Data Cleaning and Preprocessing:")
    st.write("""To ensure the accuracy and reliability of our findings, we have invested significant effort in cleaning and preprocessing the data. This step involves handling missing values, standardizing formats, and addressing any anomalies that may impact the analysis.""")
    st.subheader("Visualization Techniques:")
    st.write("""Our project employs a variety of visualization techniques, including charts, graphs, and interactive dashboards. These visuals aim to present complex information in an easily understandable format, enabling stakeholders to grasp insights at a glance. """)
    st.subheader("Exploratory Data Analysis (EDA):")
    st.write("""Through exploratory data analysis, we delve deep into the dataset, uncovering relationships, correlations, and outliers. This process allows us to identify key factors influencing user behavior and transaction patterns. """)
    st.markdown("---")
    st.header("EXPECTED OUTCOMES")
    st.subheader("Insights into User Behavior:")
    st.write("""By visualizing user interactions with the PhonePe platform, we anticipate gaining a deeper understanding of user preferences, popular transaction types, and peak usage times. """)
    st.subheader("Transaction Trends:")
    st.write("""Our analysis will highlight transactional trends, enabling stakeholders to identify areas for improvement, optimize services, and capitalize on emerging opportunities. """)
    st.markdown("---")
    st.header("CONCLUSION:")
    st.write("""-In conclusion, our PhonePe Data Visualization and Exploration project are poised to provide actionable insights that can drive strategic decisions, enhance user satisfaction, and contribute to the continued success of PhonePe in the dynamic digital payment landscape.
                Let's dive into the details and explore the visual journey our data has to offer. Thank you. """ )
    
    st.image('banner.png', caption=None, width=None, use_column_width=True, clamp=False, channels="RGB", output_format="auto")
    
with st.container():
    if selected == "FEATURES":
        VIDEO_DATA4 = open('pe1.mp4','rb')
        video_bytes4=VIDEO_DATA4.read()
        texcol,vicol=st.columns((1,2))
        with vicol:
            st.video(video_bytes4)
            st.markdown("---")
        st.image('banner.png', caption=None, width=None, use_column_width=True, clamp=False, channels="RGB", output_format="auto")    
        with texcol:
            st.markdown("---")
            st.write("Do you want to view the official features of phonepe..?")
            st.write("⬇️...just click the slider")
            on=st.toggle(":violet[FEATURE]")
        if on:
          yrm = st.selectbox(
                    "",
                    ("Easy Interface", "Payment To Merchant", "Fund Transfer","Recharge and Bill Payments",
                        "Buy & Sell Gold"),
                    index=None,
                    placeholder="Explore The Feature"
                    )  
       
          if yrm == "Easy Interface":
            st.subheader("EASY INTERFACE:")
            st.write("""The "Easy Interface" feature in the PhonePe Data Extraction project refers to the implementation of a user-friendly and intuitive interaction platform. It is designed to simplify the process of accessing, exploring, and interpreting the extracted data from PhonePe transactions. The primary goal is to enhance user experience and facilitate seamless engagement with the dataset through an uncomplicated and visually appealing interface.  """)  
            st.image('phone1.jpg',caption=None ,width=None,use_column_width=True,channels="RGB",output_format="auto")
            st.subheader("Streamlit Integration:")
            st.write("""The project incorporates the Streamlit framework to create a streamlined and responsive interface. Streamlit enables the development of dynamic and interactive web applications with minimal code, allowing users to effortlessly navigate through the extracted PhonePe data. """)
            st.subheader("Dynamic Selectors:")
            st.write(""": Users can interact with the data using dynamic selectors, sliders, and buttons. These elements empower users to customize their data exploration based on specific parameters such as timeframes, transaction types, or user segments.""")
            st.subheader("Intuitive Navigation:")
            st.write("""The interface is designed with a focus on simplicity and clarity. Users can easily navigate through different sections, select options, and visualize insights without encountering unnecessary complexity.""")
            st.subheader("User-Friendly Controls:")
            st.write(""" The controls and features are designed to be user-friendly, ensuring that individuals with varying levels of technical expertise can comfortably engage with the platform. This includes straightforward buttons, tooltips, and guidance prompts. """)
            st.image('phonepe1.jpg',caption=None ,width=400,use_column_width=False,channels="RGB",output_format="auto")
            st.write("---")
            st.link_button("For More Information...", "https://www.phonepe.com/")
            st.image('banner.png', caption=None, width=None, use_column_width=True, clamp=False, channels="RGB", output_format="auto")
          if yrm == "Payment To Merchant":
            st.image('paymenttomerchant1.jpg',caption=None ,width=600,use_column_width=False,channels="RGB",output_format="auto")
            st.subheader("Payment to Merchant:")
            st.write("""The "Payment to Merchant" feature in PhonePe Data Extraction pertains to the comprehensive analysis and extraction of data related to transactions involving payments made to merchants through the PhonePe platform. This segment of the project focuses on uncovering insights and patterns associated with user transactions specifically directed towards merchant services, contributing to a nuanced understanding of the platform's commercial dynamics. """)
            st.image('phone2.jpg',caption=None ,width=None,use_column_width=True,channels="RGB",output_format="auto")
            st.subheader("Transaction Categorization: ")
            st.write(""" The project categorizes and distinguishes transactions specifically designated as payments to merchants. This involves the identification of merchant-related transaction codes or attributes within the PhonePe dataset. """)
            st.subheader("Merchant Identification: ")
            st.write("""Utilizing available data fields, the project extracts and organizes information related to merchants, including merchant names, categories, and unique identifiers. This enables a detailed breakdown of payments based on the diverse range of merchants on the PhonePe platform. """)
            st.subheader("Transaction Frequency Analysis:")
            st.write("""The feature examines the frequency of payments to merchants over specified timeframes, allowing for the identification of popular merchants, peak transaction periods, and potential seasonal variations. """)
            st.subheader("Transaction Amounts and Trends: ")
            st.write(""" Analyzing the amounts involved in transactions with merchants provides insights into user spending behavior. The project explores trends in transaction amounts to understand variations, anomalies, and potential growth opportunities for both merchants and the PhonePe platform. """)
            st.subheader("Geospatial Analysis:")
            st.write(""" Incorporating geospatial data, the analysis extends to identifying the geographical distribution of merchant transactions. This helps in recognizing regional preferences, optimizing service offerings, and identifying areas for targeted business expansion. """)
            st.image('merchant.jpg',caption=None ,width=None,use_column_width=True,channels="RGB",output_format="auto")
            st.link_button("For More Information...", "https://www.phonepe.com/")
            st.image('banner.png', caption=None, width=None, use_column_width=True, clamp=False, channels="RGB", output_format="auto")
          if yrm == "Fund Transfer":
              
              VIDEO_DATA1 = open('fund3.mp4','rb')
              video_bytes1=VIDEO_DATA1.read()
    
              videocol,textcol=st.columns((1,2))
              with videocol:
                  st.video(video_bytes1)
              with textcol:    
                 st.subheader("Fund Transfer")
                 st.write("""The "Fund Transfer" component within PhonePe Data Extraction involves a thorough examination and extraction of data related to the transfer of funds between users on the PhonePe platform. This feature focuses on unraveling insights and patterns associated with peer-to-peer transactions, contributing to a comprehensive understanding of the platform's financial dynamics.  """)
              st.subheader("Transaction Identification:")
              st.write("""The project categorizes and isolates transactions specifically related to fund transfers. This involves the identification of transaction codes or attributes within the PhonePe dataset that signify peer-to-peer fund transfers. """)
              st.subheader("Sender and Receiver Analysis: ")
              st.write("""The extraction process involves organizing and analyzing data related to both the sender and receiver of funds. This includes user identifiers, account details, and transaction histories to comprehend the dynamics of fund flow between users.  """)
              st.image('fund1.png',caption=None ,width=800,use_column_width=False,channels="RGB",output_format="auto")
              st.subheader("Transaction Frequency and Volume:")
              st.write("""Analyzing the frequency and volume of fund transfer transactions provides insights into user behaviors and preferences. This analysis helps identify trends, peak transfer periods, and potential factors influencing the frequency of fund transfers. """)
              st.subheader("Amount Distribution:")
              st.write("""The feature explores the distribution of transfer amounts, examining average transfer values, outliers, and trends over specified timeframes. This aids in understanding the typical transaction size and identifying variations in fund transfer behaviors.  """)
              st.subheader("Geographical Patterns: ")
              st.write(""" Incorporating geospatial data, the analysis extends to identifying the geographical distribution of fund transfer transactions. This geographic insight helps recognize regional preferences and enables targeted strategies for promoting peer-to-peer transactions.  """)
              st.image('fund2.png',caption=None ,width=800,use_column_width=False,channels="RGB",output_format="auto")
              st.link_button("For More Information...", "https://www.phonepe.com/")
              st.image('banner.png', caption=None, width=None, use_column_width=True, clamp=False, channels="RGB", output_format="auto")
          if yrm == "Recharge and Bill Payments":
               VIDEO_DATA2 = open('recharge.mp4','rb')
               video_bytes2=VIDEO_DATA2.read()
               st.video(video_bytes2)
               st.markdown("---")
               st.subheader("Recharge and Bill Payments")
               st.write("""The "Recharge and Bill Payments" feature in PhonePe Data Extraction revolves around the comprehensive analysis and extraction of data related to mobile recharges, utility bill payments, and other financial transactions associated with services provided by various vendors. This component focuses on unraveling insights and patterns tied to user interactions with recharge and bill payment services on the PhonePe platform.""")
               st.link_button("For More Information...", "https://www.phonepe.com/")
               st.image('banner.png', caption=None, width=None, use_column_width=True, clamp=False, channels="RGB", output_format="auto")
          if yrm =="Buy & Sell Gold":
              st.image('gold1.jpg',caption=None ,width=950,use_column_width=False,channels="RGB",output_format="auto")  
              st.markdown("---")
              st.subheader("Buy and Sell Gold")
              st.write("""The "Buy and Sell Gold" feature in PhonePe Data Extraction involves the thorough analysis and extraction of data related to transactions associated with buying and selling gold on the PhonePe platform. This component focuses on unraveling insights and patterns tied to user interactions with gold transactions, contributing to a comprehensive understanding of the platform's financial and investment dynamics. """)  
              st.image('gold.png',caption=None ,width=950,use_column_width=False,channels="RGB",output_format="auto")  
              st.markdown("---")
              st.link_button("For More Information...", "https://www.phonepe.com/")
              st.image('banner.png', caption=None, width=None, use_column_width=True, clamp=False, channels="RGB", output_format="auto")
              
with st.container():
    if selected =="QUERIES":
        st.image('quer4.png',caption=None ,width=False,use_column_width=True,channels="RGB",output_format="auto") 
        st.header("TOP QUERIES...!")
        st.markdown("---")
        on=st.toggle("TOP MOBILE BRANDS AND THIER TRANSACTION COUNT")
        if on:
            ques1()

        on1=st.toggle("DISTRICTS BY TRANSACTION AMOUNT")
        if on1:
            ques3()
            ques4()

        on2=st.toggle("STATES BY APP OPENING")
        if on2:
            ques7()
            ques6()
        on3=st.toggle("STATES BY HIGHEST TRANSACTION COUNT")
        if on3:
            ques5()
            ques9()
        
        on4=st.toggle("STATES HAVING LOWEST TRANSACTION AMOUNT")
        if on4:
            ques8()
            ques2()
        on5=st.toggle("DISTRICTS WITH LOWEST TRANSACTION")
        if on5:
            ques10()
            
            

 
if selected == "DATA VISUALIZATION":           
    st.image('pe.png',caption="Explore the Data",width=False,use_column_width=True,channels="RGB",output_format="auto")
    st.subheader("You can view the data's of specified years or every years here...!")
    st.markdown("---")
    yrf = st.select_slider(
        'SELECT THE DESIRED OPTION ⬇️',
        options=['OFF','2018','2019','2020','2021','2022','2023'])
    
    if st.button("PRESS TO VIEW ALL YEARS"):
            cl1,cl2=st.columns(2)
            with cl1:
                geo_map1()
                transaction_count()
                geo_map2()
                transaction_amount()
            with cl2: 
                st.write(" ")

        
    
    elif yrf=="2018":
        cl1,cl2=st.columns(2)
        with cl1:
            trans_amnt_yr(yrf)
            trans_cont_yr(yrf)
        with cl2:
            st.write(" ")              
    elif yrf=="2019":
        cl1,cl2=st.columns(2)
        with cl1:
            trans_amnt_yr(yrf)
            trans_cont_yr(yrf)
        with cl2:
            st.write(" ")
    elif yrf=="2020":
        cl1,cl2=st.columns(2)
        with cl1:
            trans_amnt_yr(yrf)
            trans_amnt_yr(yrf)
        with cl2:
            st.write(" ")
    elif yrf=="2021":
        cl1,cl2=st.columns(2)
        with cl1:
            trans_amnt_yr(yrf)
            trans_cont_yr(yrf)
        with cl2:
            st.write(" ")
    elif yrf=="2022":
        cl1,cl2=st.columns(2)
        with cl1:
            trans_amnt_yr(yrf)
            trans_cont_yr(yrf)
        with cl2:
            st.write(" ")
    elif yrf=="2023":
        cl1,cl2=st.columns(2)
        with cl1:
            trans_amnt_yr(yrf)
            trans_cont_yr(yrf)
        with cl2:
            st.write(" ")
        

if selected == "CONTACT INFORMATION":

    st.image('contactus.png',caption=None ,width=False,use_column_width=True,channels="RGB",output_format="auto")
    st.subheader(":mailbox: Get In Touch With Me!!!")
    st.write("##")
    
    contact_form="""
    <form action="https://formsubmit.co/Nagaprakash48@gmail.com" method="POST">
         <input type="hidden" name="_captcha" value="false">
         <input type="text" name="name" placeholder="Your Name" required>
         <input type="email" name="email" placeholder="Your Email" required>
         <textarea name="message" placeholder="Your Message here"></textarea>
         <button type="submit">Send</button>    
    </form>
    """

    st.markdown(contact_form,unsafe_allow_html=True)
    st.markdown("---")
    st.link_button("Learn More", "https://www.phonepe.com/",use_container_width=True)
    st.link_button("Linkedin", "https://www.linkedin.com/in/naga-prakash-j-280aba1b9?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app",use_container_width=True)
    st.link_button("My github","github.com/Nagaprakash24",use_container_width=True)
    
   


