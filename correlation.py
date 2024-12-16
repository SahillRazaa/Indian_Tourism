import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

def plot_correlation_heatmap():
    st.subheader("Correlation Heatmap of Monthly Tourist Numbers")
    
    # Load the data
    tourist_data = pd.read_csv('Month Wise FFA.csv')
    tourist_data_monthly = tourist_data.drop(columns=["year"])

    # Calculate the correlation matrix
    correlation_matrix = tourist_data_monthly.corr()

    # Create the heatmap
    plt.figure(figsize=(12, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
    plt.title("Correlation Heatmap of Monthly Tourist Numbers")

    # Display the plot in Streamlit
    st.pyplot(plt)

    # Conclusion text
    conclusion_text = (
        "### Conclusion from Correlation Matrix:\n\n"
        "**High Positive Correlations:** Strong correlations are noticeable between months in the same season, "
        "like December and January, likely due to winter tourism peaks.\n\n"
        "**Moderate Seasonal Patterns:** Spring and summer months (March through July) display moderate correlations "
        "with each other, indicating a lesser but still noticeable seasonal effect.\n\n"
        "**Low to Negative Correlations:** Lower correlations or negative values indicate months that don’t share "
        "similar patterns, such as April and December, which may suggest a shift in tourist numbers due to seasonal "
        "or external factors."
    )

    # Display the conclusion text in Streamlit
    st.write(conclusion_text)