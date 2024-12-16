import pandas as pd
import numpy as np
import streamlit as st

def cleanDataQuarter(data):
    quarters = [
        '2014 Q1', '2014 Q2', '2014 Q3', '2014 Q4',
        '2015 Q1', '2015 Q2', '2015 Q3', '2015 Q4',
        '2016 Q1', '2016 Q2', '2016 Q3', '2016 Q4',
        '2017 Q1', '2017 Q2', '2017 Q3', '2017 Q4',
        '2018 Q1', '2018 Q2', '2018 Q3', '2018 Q4',
        '2019 Q1', '2019 Q2', '2019 Q3', '2019 Q4',
        '2020 Q1', '2020 Q2', '2020 Q3', '2020 Q4'
    ]
    
    # Set the column names
    data.columns = ['Country of Nationality'] + quarters
    data.replace('', np.nan, inplace=True)

    # Convert columns to numeric
    for col in quarters:
        data[col] = pd.to_numeric(data[col], errors='coerce')

    # Drop rows with any NaN values
    data = data.dropna(how='any')
    
    # Log the cleaning process
    st.write("Data cleaned for quarters. Remaining rows:", data.shape[0])
    
    return data

def cleanDataAge(data):
    years = [
        '2014 A1', '2014 A2', '2014 A3', '2014 A4', '2014 A5', '2014 A6', '2014 A7',
        '2015 A1', '2015 A2', '2015 A3', '2015 A4', '2015 A5', '2015 A6', '2015 A7',
        '2016 A1', '2016 A2', '2016 A3', '2016 A4', '2016 A5', '2016 A6', '2016 A7',
        '2017 A1', '2017 A2', '2017 A3', '2017 A4', '2017 A5', '2017 A6', '2017 A7',
        '2018 A1', '2018 A2', '2018 A3', '2018 A4', '2018 A5', '2018 A6', '2018 A7',
        '2019 A1', '2019 A2', '2019 A3', '2019 A4', '2019 A5', '2019 A6', '2019 A7',
        '2020 A1', '2020 A2', '2020 A3', '2020 A4', '2020 A5', '2020 A6', '2020 A7',
    ]
    
    # Set the column names
    data.columns = ['Country of Nationality'] + years
    data.replace('', np.nan, inplace=True)

    # Convert columns to numeric
    for col in years:
        data[col] = pd.to_numeric(data[col], errors='coerce')

    # Drop rows with any NaN values
    data = data.dropna(how='any')
    
    # Log the cleaning process
    st.write("Data cleaned for age groups. Remaining rows:", data.shape[0])
    
    return data