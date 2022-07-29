import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# app1.py
def app():
    st.title('Welcome to data visualization dashboard!')
    # st.header('Header')
    # st.subheader('subheader')
    # st.caption('caption')
    # st.write('Welcome to data visualization dashboard!')

    st.subheader('Inventory vs Sold item per category')

    ################ case 1 ##########

    df_inventory = pd.read_csv(r'inv.csv')
    item_status = []

    for i in df_inventory.index:
        if pd.isna(df_inventory.iloc[i , 1]) == True:
            item_status.append('Inventory item')
        else:
            item_status.append('Sold item')

    df_inventory['item_status'] = item_status

    df_invitem = df_inventory[df_inventory['item_status'] == "Inventory item"]
    df_invitem = df_invitem.groupby(["product_category"])[['item_status']].count()

    df_solditem = df_inventory[df_inventory['item_status'] == "Sold item"]
    df_solditem = df_solditem.groupby(["product_category"])[['item_status']].count()
    df_allitem = df_inventory.groupby(["product_category"])[['product_category']].count()
    
    pd.DataFrame(df_allitem)
    df_allitem['inventory'] = df_invitem.loc[:,'item_status']
    df_allitem['sold'] = df_solditem.loc[:,'item_status']
    df_allitem = df_allitem.rename(columns ={'product_category':'total_item'})
    df_allitem = df_allitem.sort_values(by="total_item", ascending=False)

    df_allitem_plot = df_allitem.drop(columns=['total_item'])

    df_allitem_plot=df_allitem_plot.reset_index()

    fig, ax = plt.subplots(figsize=(10,6))
    # sns.barplot(data=df_allitem_plot,x='product_category',y=['inventory','sold'],ax=ax,orient='v', color='black')
    # plt.xticks(rotation=90)
    df_allitem_plot = df_allitem.drop(columns=['total_item'])
    df_allitem_plot.plot(kind='bar', ax=ax)

    ax.set_xlabel('product_category') 
    ax.set_ylabel('inventory, sold') 
    ax.set_title('inventory vs sold item') 

    st.pyplot(fig)

    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")


    ################# case 2 ###############

    st.subheader('The look rate of sales and returns by gender')

    dfgender_return = pd.read_csv(r'return_gender.csv')
    dfgender_return.head(5)

    selected = st.selectbox('Select category',['Female','Male'])
    if selected == "Female":
        selected = "F"
    else:
        selected = "M"

    dfreturn = dfgender_return[dfgender_return['gender'] == selected].groupby(["status"])[["num_of_item"]].sum()
    dfreturn = dfreturn.drop(['Cancelled','Processing'],axis = 0)

    fig1, ax1 = plt.subplots(figsize=(8,6))

    dfreturn.iloc[:,0].plot(kind='pie', ax=ax1, autopct='%1.1f%%', startangle=90, shadow=False)      

    ax1.set_title('Return Percentage')
    ax1.set_ylabel(' ')
    st.pyplot(fig1)
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")

    ############### case 3 ################

    st.subheader('Return percentage per product category')
    dfcategory_return = pd.read_csv(r'return_category.csv')
    dfcategory_return.head(5)

    dfcatret = dfcategory_return[dfcategory_return['status'] == "Returned"].groupby(["product_category"])[["product_category"]].count()
    allsum = dfcatret.loc[:,'product_category'].sum()
    for i in dfcatret.index:
        dfcatret.loc[i,'product_category'] = np.round(dfcatret.loc[i,'product_category']/allsum*100,2)

    dfcatret = dfcatret.rename(columns ={'product_category':'return_percentage'})
    dfcatret = dfcatret.sort_values(by='return_percentage', ascending=False)

    others = dfcatret.iloc[11:,0].sum()
    dfcatret_plot = dfcatret.copy()
    dfcatret_plot.iloc[11,0] = others
    dfcatret_plot = dfcatret_plot.rename(index={dfcatret_plot.index[11]: "Others (14 other categories)"})

    dfcatret_plot = dfcatret_plot.drop(dfcatret_plot.index[12:], axis=0 )
    
    fig2, ax2 = plt.subplots(figsize=(10,6))
    dfcatret_plot.loc[:,'return_percentage'].plot(kind='pie', figsize=(5, 6), autopct='%1.1f%%', startangle=90, shadow=False)      

    ax2.set_title('Return Percentage')
    ax2.set_ylabel(' ')

    st.pyplot(fig2)
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")

    ################# case 5 ########
    st.subheader('Shipping work load per distribution center')
    df_distribution = pd.read_csv(r'distribution_center.csv')
    df_distribution.head(5)
    df_selldist = df_distribution.groupby(["name"])[["country"]].count().sort_values(by='country', ascending=False)
    df_selldist = df_selldist.rename(columns ={'country':'total_shipping'})
    fig3, ax3 = plt.subplots(figsize=(10,6))
    df_selldist.loc[:,'total_shipping'].plot(kind='pie', ax = ax3, autopct='%1.1f%%', startangle=90, shadow=False)      

    ax3.set_title('Shipping Percentage')
    ax3.set_ylabel(' ')

    st.pyplot(fig3)

    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")

    ############# case 6  ##########
    st.subheader('List of countries handled by each distribution center')
    selected2 = st.selectbox('Select distribution center',df_distribution.name.unique())
    df_distribution['shipping_qty'] = df_distribution.loc[:,'country']
    df_countdistMT = df_distribution[df_distribution['name']== selected2].groupby(["country"])[["shipping_qty"]].count().sort_values(by='shipping_qty', ascending=False)
    #df_countdistMT = df_countdistMT.rename(columns ={'country':'shipping_qty'})
    

    others = df_countdistMT.iloc[8:,0].sum()
    df_countdistMT.iloc[8,0] = others
    df_countdistMT = df_countdistMT.rename(index={df_countdistMT.index[8]: "Other country"})
    

    df_countdistMT = df_countdistMT.drop(df_countdistMT.index[9:], axis=0 )

    fig4, ax4 = plt.subplots(figsize=(10,6))
    df_countdistMT.loc[:,'shipping_qty'].plot(kind='pie', ax = ax4, autopct='%1.1f%%', startangle=90, shadow=False)      

    ax4.set_title('Shipping Percentage')
    ax4.set_ylabel(' ')

    st.pyplot(fig4)
