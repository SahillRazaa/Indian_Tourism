import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import cleaning  # Ensure this module is compatible with Streamlit

def visualize_tourism_data_by_age_group():
    st.subheader("Visualize Tourism Data by Age Group")
    
    # Load the data
    dataAge = pd.read_csv('Country Wise Age Group.csv')
    cleanedDataAge = cleaning.cleanDataAge(dataAge)
    
    # Get user input for the year
    year = st.number_input("Enter the year [2014 - 2020] you want to visualize:", min_value=2014, max_value=2020, value=2014)
    
    age_groups = [f'{year} A1', f'{year} A2', f'{year} A3', f'{year} A4', f'{year} A5', f'{year} A6', f'{year} A7']
    data_year = cleanedDataAge[['Country of Nationality'] + age_groups]
    data_year = data_year.melt(id_vars='Country of Nationality', var_name='Age Group', value_name='Number of Tourists')
    
    ageMap = {
        'A1': '0-14',
        'A2': '15-24',
        'A3': '25-34',
        'A4': '35-44',
        'A5': '45-54',
        'A6': '55-64',
        'A7': '65+'
    }

    # Display the age map
    st.write("Age Group Mapping:")
    st.write(ageMap)

    # Create the bar plot
    plt.figure(figsize=(12, 6))
    sns.barplot(data=data_year, x='Age Group', y='Number of Tourists', hue='Country of Nationality')
    plt.title(f'Number of Tourists by Age Group in {year}')
    plt.xlabel('Age Group')
    plt.ylabel('Number of Tourists')
    plt.legend(title='Country', loc='upper right', bbox_to_anchor=(1.2, 1.1))
    
    # Display the plot in Streamlit
    st.pyplot(plt)