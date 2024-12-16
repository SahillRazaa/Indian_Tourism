import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

def normalize_and_analyze_distribution():
    st.subheader("Distribution Analysis of Monthly Tourist Numbers")
    
    # Load the data
    tourist_data = pd.read_csv('Month Wise FFA.csv')
    
    # Flatten the monthly tourist numbers
    monthly_tourists = tourist_data.drop(columns=['year']).values.flatten()

    # Normalize the data
    normalized_data = (monthly_tourists - monthly_tourists.min()) / (monthly_tourists.max() - monthly_tourists.min())

    # Create the histogram
    plt.figure(figsize=(12, 6))
    sns.histplot(normalized_data, bins=30)
    plt.title("Distribution of Normalized Monthly Tourist Numbers")
    plt.xlabel("Normalized Number of Tourists")
    plt.ylabel("Frequency")
    
    # Display the plot in Streamlit
    st.pyplot(plt)

    # Conclusions text
    conclusion_text = (
        "### Conclusions from Distribution Analysis:\n\n"
        "1. **Right-Skewed Distribution:** Most months have lower to moderate tourist numbers, "
        "with fewer months experiencing higher numbers.\n\n"
        "2. **Peak Observations:** There’s a significant concentration of higher tourist numbers "
        "around 0.4–0.6, indicating specific high-tourism months.\n\n"
        "3. **Wide Spread of Values:** Tourist numbers vary significantly across months, "
        "suggesting seasonal trends with fluctuations throughout the year."
    )

    # Display the conclusions in Streamlit
    st.write(conclusion_text)