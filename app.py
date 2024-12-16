import streamlit as st
import aggregation_1
import aggregation_2
import correlation
import normalization_distribution
import outliering
import define_hypothesis

def main():
    st.title("Sahil's Tourism Database")
    st.sidebar.title("Navigation")
    
    choice = st.sidebar.selectbox("Select an option", [
        "Get quarterly visualization of a specific country",
        "Get countries visualization for a specific quarter",
        "Get countries visualization for a specific Type of Tourist",
        "Get monthly correlation between number of tourists",
        "Get monthly normalized distribution analysis",
        "Get monthly outliers as number of tourists",
        "Get the hypothesis testing analysis",
        "EXIT"
    ])
    
    if choice == "Get quarterly visualization of a specific country":
        aggregation_1.visualize_tourism_data_by_country()
    elif choice == "Get countries visualization for a specific quarter":
        aggregation_1.visualize_tourism_data_by_quarter()
    elif choice == "Get countries visualization for a specific Type of Tourist":
        aggregation_2.visualize_tourism_data_by_age_group()
    elif choice == "Get monthly correlation between number of tourists":
        correlation.plot_correlation_heatmap()
    elif choice == "Get monthly normalized distribution analysis":
        normalization_distribution.normalize_and_analyze_distribution()
    elif choice == "Get monthly outliers as number of tourists":
        outliering.outliers_by_month()
    elif choice == "Get the hypothesis testing analysis":
        define_hypothesis.hypoTest()
    elif choice == "EXIT":
        st.write("Exiting... Goodbye!")

if __name__ == "__main__":
    main()