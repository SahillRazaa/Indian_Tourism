import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import cleaning  # Ensure this module is compatible with Streamlit

def visualize_tourism_data_by_country():
    st.subheader("Visualize Tourism Data by Country")
    
    initialData = pd.read_csv('Country Quater Wise Visitors.csv')
    initialData = cleaning.cleanDataQuarter(initialData)

    countryNames = list(initialData['Country of Nationality'])
    
    st.write("Below are the available Countries Data for visualization:")
    st.write(countryNames)

    currCountry = st.selectbox("Select a country:", countryNames)

    if currCountry:
        currCountryData = initialData[initialData['Country of Nationality'] == currCountry]
        tempData = list(currCountryData.values)
        finalCountryData = np.array(tempData)[0, 1:]

        tempYearlyData = pd.read_csv('Country Wise Yearly VIsitors.csv')
        countryYearlyData = tempYearlyData[tempYearlyData['Country'] == currCountry]
        finalCountryYearly = np.array(countryYearlyData)[0, 1:]

        finalTouristData = []
        index = 0

        for item in finalCountryYearly:
            for i in range(4):
                currTourist = (finalCountryData[index] * item) // 100
                finalTouristData.append(currTourist)
                index += 1

        quarters = [
            '2014 Q1', '2014 Q2', '2014 Q3', '2014 Q4',
            '2015 Q1', '2015 Q2', '2015 Q3', '2015 Q4',
            '2016 Q1', '2016 Q2', '2016 Q3', '2016 Q4',
            '2017 Q1', '2017 Q2', '2017 Q3', '2017 Q4',
            '2018 Q1', '2018 Q2', '2018 Q3', '2018 Q4',
            '2019 Q1', '2019 Q2', '2019 Q3', '2019 Q4',
            '2020 Q1', '2020 Q2', '2020 Q3', '2020 Q4'
        ]

        plt.figure(figsize=(10, 5))
        sns.barplot(x=quarters, y=finalTouristData, palette="viridis", legend=False)
        plt.title(f'Number of Tourists vs. Quarters in {currCountry} (2014 - 2020)')
        plt.xlabel('Quarters')
        plt.ylabel('Number of Tourists')
        plt.xticks(rotation=45)
        st.pyplot(plt)

def visualize_tourism_data_by_quarter():
    st.subheader("Visualize Tourism Data by Quarter")
    
    initialData = pd.read_csv('Country Quater Wise Visitors.csv')
    uniqueQuarters = ['Q1', 'Q2', 'Q3', 'Q4']
    
    st.write("Below are the available Quarters Data for visualization:")
    st.write(uniqueQuarters)
    
    currQuarter = st.selectbox("Select a quarter:", uniqueQuarters)
    
    if currQuarter:
        # Transpose the data for easier manipulation
        transposeInitial = initialData.T
        allCountries = list(transposeInitial.iloc[0])

        # Extract data for the selected quarter
        if currQuarter == 'Q1':
            data_2014 = transposeInitial.iloc[1]
            data_2015 = transposeInitial.iloc[5]
            data_2016 = transposeInitial.iloc[9]
            data_2017 = transposeInitial.iloc[13]
            data_2018 = transposeInitial.iloc[17]
            data_2019 = transposeInitial.iloc[21]
            data_2020 = transposeInitial.iloc[25]
        elif currQuarter == 'Q2':
            data_2014 = transposeInitial.iloc[2]
            data_2015 = transposeInitial.iloc[6]
            data_2016 = transposeInitial.iloc[10]
            data_2017 = transposeInitial.iloc[14]
            data_2018 = transposeInitial.iloc[18]
            data_2019 = transposeInitial.iloc[22]
            data_2020 = transposeInitial.iloc[26]
        elif currQuarter == 'Q3':
            data_2014 = transposeInitial.iloc[3]
            data_2015 = transposeInitial.iloc[7]
            data_2016 = transposeInitial.iloc[11]
            data_2017 = transposeInitial.iloc[15]
            data_2018 = transposeInitial.iloc[19]
            data_2019 = transposeInitial.iloc[23]
            data_2020 = transposeInitial.iloc[27]
        elif currQuarter == 'Q4':
            data_2014 = transposeInitial.iloc[4]
            data_2015 = transposeInitial.iloc[8]
            data_2016 = transposeInitial.iloc[12]
            data_2017 = transposeInitial.iloc[16]
            data_2018 = transposeInitial.iloc[20]
            data_2019 = transposeInitial.iloc[24]
            data_2020 = transposeInitial.iloc[28]

        currYear = st.number_input("Enter the Year (2014 - 2020):", min_value=2014, max_value=2020)

        finalYearData = []

        if currYear == 2014:
            finalYearData = data_2014
        elif currYear == 2015:
            finalYearData = data_2015
        elif currYear == 2016:
            finalYearData = data_2016
        elif currYear == 2017:
            finalYearData = data_2017
        elif currYear == 2018:
            finalYearData = data_2018
        elif currYear == 2019:
            finalYearData = data_2019
        elif currYear == 2020:
            finalYearData = data_2020

        plt.figure(figsize=(13, 5))
        sns.barplot(x=allCountries, y=finalYearData, palette="viridis", legend=False)
        plt.title(f'Number of Tourists vs. Countries in {currQuarter} {currYear}')
        plt.xlabel('Countries')
        plt.ylabel('Number of Tourists')
        plt.xticks(rotation=45)
        st.pyplot(plt)