import streamlit as st

# Import Libraries

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# from wordcloud import WordCloud, STOPWORDS

@st.cache(allow_output_mutation=True)
def read_data():
    df= pd.read_excel("data_final.xlsx")
    return df

#creating containers for each section
header = st.container()
Education= st.container()
Industries= st.container()
Skills= st.container()

with header: 
    st.title("Analyzing LinkedIn Profiles")
    data_final= read_data()

with Education: 
    st.header('Percentage of different degree level among the sample data ')
    degree= ['Bachelor', 'Master','PhD', 'Diploma', 'Baccalaureate', 'School', 'bachelorette', 'baccalaureate', 'Professional', 'Sessions','Program' ]
    data_final['bachelor_degree']= data_final['degree_name'].str.contains(degree[0])
    data_final['master_degree']= data_final['degree_name'].str.contains(degree[1])
    data_final['phd_degree']= data_final['degree_name'].str.contains(degree[2])
    data_final['other_degree']= data_final['degree_name'].str.contains(degree[3])
    data_final['other_degree']= data_final['degree_name'].str.contains(degree[4])
    data_final['other_degree']= data_final['degree_name'].str.contains(degree[5])
    data_final['other_degree']= data_final['degree_name'].str.contains(degree[6])
    data_final['other_degree']= data_final['degree_name'].str.contains(degree[7])
    data_final['other_degree']= data_final['degree_name'].str.contains(degree[8])
    data_final['other_degree']= data_final['degree_name'].str.contains(degree[9])
    # print(d[['degree_name','bachelor_degree']])
    cb= data_final['bachelor_degree'].sum()
    cm= data_final['master_degree'].sum()
    cp= data_final['phd_degree'].sum()
    co= data_final['other_degree'].sum()
    # plt.pie([cb, cm, cp, co], labels= ['bachelor_degree', 'master_degree', 'phd_degree','other_degree'], autopct='%1.1f%%')
    fig= go.Figure(data=[go.Pie(labels=['bachelor', 'master', 'phd', 'other'], values=[cb, cm, cp,co], title='Degree Distribution')])
    st.plotly_chart(fig)

    st.header('Distribution of Students Among Universities')
    fig1=plt.figure(figsize=(10,5))
    sns.countplot(data_final['school_name'])
    # total = float(len(data_education))
    plt.xticks(rotation= 90)
    plt.title('Distribution of profiles among universities')
    st.pyplot(fig1)

    st.header('Education Location')
    fig9= plt.figure(figsize=(10,5))
    sns.countplot(data_final.education_location_name)
    plt.xticks(rotation= 90)
    plt.title("Education Location among users (as a percentage)")
    plt.show()
    st.pyplot(fig9)

    st.header('Field of Study as per degree name')
    st.subheader('Bachelor Degree')
    degree_list= ['bachelor_degree', 'master_degree','phd_degree']
    degree= st.selectbox('Choose the degree:', options= degree_list)

    fig2=plt.figure(figsize=(10,5))
    sns.countplot(data_final['fieldOfStudy'][(data_final[degree]==True)])
    plt.xticks(rotation= 90)
    plt.title(f'Majors in {degree}')
    plt.show()
    st.pyplot(fig2)

with Industries: 
    st.header('Industries among Profiles')
    fig3=plt.figure(figsize=(10,5))
    sns.countplot(data_final['industries'])
    plt.xticks(rotation= 90)

    plt.title('Industry Types among user')
    plt.show()
    st.pyplot(fig3)

    st.header('Top 10 Industries among our dataset')
    fig5=plt.figure(figsize=(10,5))
    
    df_no_ind= data_final.copy()
    df_no_ind= df_no_ind[df_no_ind['industries']!= 'no industries']
    df_no_ind.industries.value_counts()[:10].sort_values().plot(kind = 'barh', color=['slateblue', 'mediumpurple', 'indigo', 'plum', 'purple'])
    # df_no_ind.industries.value_counts()[:10].sort_values().plot(kind = 'barh')
    plt.title('Top 10 Industries among users')
    plt.show()
    st.pyplot(fig5)
    st.header('Company Names Among Selected Top Industries')

    fig10= plt.figure(figsize=(10,5))
    industry1li= ['Higher Education', 'Computer Software','Banking', 'International Affairs', 'Civic & Social Organization', 'Information Technology and Services', 'Marketing and Advertising', 'Logistics and Supply Chain']

    industry1= st.selectbox('Choose the industry:', options= industry1li)
    data_final[(data_final.industries==industry1)].companyName.value_counts().sort_values().plot(kind = 'barh', color= ['lightsteelblue', 'cornflowerblue', 'midnightblue', 'navy', 'mediumblue', 'blue'])
    # data_final[(data_final.industries==industry1)].companyName.value_counts().sort_values().plot(kind = 'barh')
    plt.title(f'Top companies by {industry1} Industry')
    plt.show()
    st.pyplot(fig10)

   
    
with Skills: 
    st.header('Skill Types among users')
    from PIL import Image
    image = Image.open("wordcloud.png")

    st.image(image, caption='skills types among users')

    # st.header('Top Skills among top selected Industries')
    # edu= data_final[['industries', 'skill_name']][(data_final['industries']=='Higher Education')]
    # fig7= plt.figure(figsize=(10,5))
    # edu.skill_name.value_counts()[:10].sort_values().plot(kind = 'barh', color= ['forestgreen', 'limegreen', 'darkgreen', 'springgreen', 'mediumspringgreen', 'mediumaquamarine'])
    # # edu.skill_name.value_counts()[:10].sort_values().plot(kind = 'barh')
    # plt.title('Top Skills in Higher Education')
    # plt.show()
    # st.pyplot(fig7)


    st.header('Top Skills among top selected Industries')
    industry_list= ['Higher Education', 'Computer Software','Banking', 'International Affairs', 'Civic & Social Organization', 'Information Technology and Services', 'Marketing and Advertising', 'Management Consulting', 'Logistics and Supply Chain']
    industry= st.selectbox('Choose the industry:', options= industry_list)

    fig8=plt.figure(figsize=(10,5))
    edu= data_final[['industries', 'skill_name']][(data_final['industries']== industry)]
    edu.skill_name.value_counts()[:10].sort_values().plot(kind = 'barh', color= ['peru', 'chocolate', 'bisque', 'olive', 'darkgoldenrod', 'khaki'])
    # edu.skill_name.value_counts()[:10].sort_values().plot(kind = 'barh')

    plt.title(f'Top Skills in {industry}')
    plt.show()
    
    st.pyplot(fig8)

    st.header('Recruitment Seasons')
    fig4= plt.figure(figsize=(10,5))
    df= data_final.copy()
    df= df[df['start_month']!= 'no month avaialble']
    df.start_month.value_counts().sort_values().plot(kind = 'barh', color=['aqua', 'cyan', 'cadetblue', 'lightskyblue', 'steelblue'])
    # data_final.start_month.value_counts().sort_values().plot(kind = 'barh')

    plt.title('Recruitment Season Month')
    plt.show()
    st.pyplot(fig4)

  
