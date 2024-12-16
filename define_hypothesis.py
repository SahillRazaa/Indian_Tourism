import pandas as pd
import numpy as np
import streamlit as st
import hypothesis_test  # Ensure this module is compatible with Streamlit

def hypoTest():
    st.subheader("Hypothesis Testing")

    # Define hypotheses
    hypotheses = {
        1: "Number of tourists during COVID was decreased as compared to before COVID.",
        2: "The female gender ratio during COVID was greater than 50 percent.",
        3: "The ratio of age group between 25-34 was greater than 25 percent during COVID.",
        4: "Number of children tourists of age group between 0 - 14 was less during COVID than before COVID.",
        5: "Delhi airport has the tourist percentage greater than 50 during COVID."
    }

    # User selects a hypothesis
    choice = st.selectbox("Select a hypothesis to test:", list(hypotheses.keys()), format_func=lambda x: hypotheses[x])

    if choice:
        if choice == 1:
            currData = pd.read_csv('Month Wise FFA.csv')
            covidData = list(currData.iloc[6][1:13])
            preCovidData = list(currData.iloc[5][1:13])
            size = 12
            covidMean = np.mean(covidData)
            preCovidMean = np.mean(preCovidData)
            covidSD = np.std(covidData)
            preCovidSD = np.std(preCovidData)

            st.write("We define null and alternative hypothesis as below:")
            st.write("H0: Covid Mean = Pre Covid Mean")
            st.write("Ha: Covid Mean < Pre Covid Mean")

            alpha = st.selectbox("Select significance level:", [0.01, 0.05], format_func=lambda x: f"{x*100}%")
            flag = hypothesis_test.oneLeftSided_comparetTest(size, covidMean, covidSD, preCovidMean, preCovidSD, alpha, size - 1)

            if flag:
                st.success("Rejecting the null hypothesis. Hence, the claim is correct: Number of tourists during COVID decreased compared to before COVID.")
            else:
                st.error("Rejecting the alternative hypothesis. Hence, the claim is incorrect: Number of tourists during COVID increased compared to before COVID.")

        elif choice == 2:
            currData = pd.read_csv('Country Wise Gender.csv')
            covidData = currData['2020 Female']
            size = len(covidData) - 40
            covidMean = np.mean(covidData)
            covidSD = np.std(covidData)

            st.write("We define null and alternative hypothesis as below:")
            st.write("H0: Covid Female Mean = 50")
            st.write("Ha: Covid Female Mean > 50")

            alpha = st.selectbox("Select significance level:", [0.01, 0.05], format_func=lambda x: f"{x*100}%")
            flag = hypothesis_test.oneRightSided_tTest(size, covidMean, covidSD, alpha, size - 1, 50)

            if flag:
                st.success("Rejecting the null hypothesis. Hence, the claim is correct: The female gender ratio during COVID was greater than 50 percent.")
            else:
                st.error("Rejecting the alternative hypothesis. Hence, the claim is incorrect: The female gender ratio during COVID was less than 50 percent.")

        elif choice == 3:
            currData = pd.read_csv('Country Wise Age Group.csv')
            covidData = currData[' 2020 25-34']
            size = len(covidData) - 40
            covidMean = np.mean(covidData)
            covidSD = np.std(covidData)

            st.write("We define null and alternative hypothesis as below:")
            st.write("H0: Covid Age 25-34 Mean = 25")
            st.write("Ha: Covid Age 25-34 Mean > 25")

            alpha = st.selectbox("Select significance level:", [0.01, 0.05], format_func=lambda x: f"{x*100}%")
            flag = hypothesis_test.oneRightSided_tTest(size, covidMean, covidSD, alpha, size - 1, 25)

            if flag:
                st.success("Rejecting the null hypothesis. Hence, the claim is correct: The ratio of age group between 25-34 was greater than 25 percent during COVID.")
            else:
                st.error("Rejecting the alternative hypothesis. Hence, the claim is incorrect : The ratio of age group between 25-34 was less than 25 percent during COVID.")

        elif choice == 4:
            currData = pd.read_csv('Country Wise Age Group.csv')
            covidData = currData['2020 0-14']
            preCovidData = currData['2019 0-14']
            size = len(covidData) - 40
            covidMean = np.mean(covidData)
            covidSD = np.std(covidData)
            preCovidMean = np.mean(preCovidData)
            preCovidSD = np.std(preCovidData)

            st.write("We define null and alternative hypothesis as below:")
            st.write("H0: Covid Age 0-14 Mean = Pre Covid Age 0-14 Mean")
            st.write("Ha: Covid Age 0-14 Mean < Pre Covid Age 0-14 Mean")

            alpha = st.selectbox("Select significance level:", [0.01, 0.05], format_func=lambda x: f"{x*100}%")
            flag = hypothesis_test.oneLeftSided_comparetTest(size, covidMean, covidSD, preCovidMean, preCovidSD, alpha, size - 1)

            if flag:
                st.success("Rejecting the null hypothesis. Hence, the claim is correct: Number of children tourists of age group between 0 - 14 was less during COVID than before COVID.")
            else:
                st.error("Rejecting the alternative hypothesis. Hence, the claim is incorrect: Number of children tourists of age group between 0 - 14 was more during COVID than before COVID.")

        elif choice == 5:
            currData = pd.read_csv('Country Wise Airport.csv')
            covidData = currData['2020 Delhi (Airport)']
            size = len(covidData) - 40
            covidMean = np.mean(covidData)
            covidSD = np.std(covidData)

            st.write("We define null and alternative hypothesis as below:")
            st.write("H0: Covid Delhi Airport Mean = 50")
            st.write("Ha: Covid Delhi Airport Mean > 50")

            alpha = st.selectbox("Select significance level:", [0.01, 0.05], format_func=lambda x: f"{x*100}%")
            flag = hypothesis_test.oneRightSided_tTest(size, covidMean, covidSD, alpha, size - 1, 50)

            if flag:
                st.success("Rejecting the null hypothesis. Hence, the claim is correct: Delhi airport has the tourist percentage greater than 50 during COVID.")
            else:
                st.error("Rejecting the alternative hypothesis. Hence, the claim is incorrect: Delhi airport has the tourist percentage lesser than 50 during COVID.")

    if st.button("Exit"):
        st.write("Ending Hypothesis Testing...")