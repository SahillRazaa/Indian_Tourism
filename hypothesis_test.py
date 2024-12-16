import math
import streamlit as st

def oneLeftSided_comparetTest(size, mean1, sd1, mean2, sd2, alpha, degFree):
    t_star = 0
    if alpha == 5:
        if degFree == 11:
            t_star = -1.796
        elif degFree == 22:
            t_star = -1.717
    elif alpha == 1:
        if degFree == 11:
            t_star = -2.718
        elif degFree == 22:
            t_star = -2.508
    else:
        st.error("Wrong choice of significance level")
        return
    
    deno = math.sqrt((sd1**2 / size) + (sd2**2 / size))
    t_statistic = (mean1 - mean2) / deno
    
    # Display results in Streamlit
    st.write("\n**t_star:**", t_star)
    st.write("**t_statistic:**", t_statistic)
    
    if t_statistic < t_star:
        st.success("Rejecting the null hypothesis.")
        return True
    else:
        st.error("Failing to reject the null hypothesis.")
        return False
    
def oneRightSided_tTest(size, mean1, sd1, alpha, degFree, th):
    t_star = 0
    if alpha == 5:
        if degFree == 22:
            t_star = 1.717
    elif alpha == 1:
        if degFree == 22:
            t_star = 2.508
    else:
        st.error("Wrong choice of significance level")
        return
    
    deno = math.sqrt((sd1**2 / size))
    t_statistic = (th - mean1) / deno
    
    # Display results in Streamlit
    st.write("\n**t_star:**", t_star)
    st.write("**t_statistic:**", t_statistic)
    
    if t_statistic < t_star:
        st.success("Rejecting the null hypothesis.")
        return True
    else:
        st.error("Failing to reject the null hypothesis.")
        return False