import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def outliers_by_month():
    st.subheader("Outliers in Monthly Tourist Numbers")
    
    # Load the data
    data = pd.read_csv('Month Wise FFA.csv')

    # Transform the data to long format
    data_long = pd.melt(data, id_vars=['year'], var_name='month', value_name='tourists')

    # Display observations
    st.write("We can observe the outliers in the number of tourists:")
    st.write("The outliers below the box plot show the reduction of tourists during COVID times.")
    st.write("The outliers above the box plot show the peak tourist numbers in years before COVID, exceeding the limit.")

    # Create the boxplot
    plt.figure(figsize=(12, 6))
    colorful_palette = sns.color_palette("tab10", n_colors=12) 
    sns.boxplot(x='month', y='tourists', data=data_long, hue='month', palette=colorful_palette, legend=False)
    plt.title('Boxplot of Tourists by Month')
    plt.xlabel('Month')
    plt.ylabel('Number of Tourists')
    plt.xticks(rotation=45)

    # Display the plot in Streamlit
    st.pyplot(plt)