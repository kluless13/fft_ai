import streamlit as st
from stat_test import choose_statistical_test
from posthoctest import choose_posthoc_test

def app():
    st.title("Statistical Test Chooser")

    data_type_1 = st.selectbox("Select the first type of data:", ["None", "numerical", "categorical"])
    data_type_2 = st.selectbox("Select the second type of data:", ["None", "numerical", "categorical"])
    sample_size = st.number_input("Enter the sample size:", min_value=1)
    independence = st.selectbox("Select the independence of the sample:", ["independent", "dependent"])
    test_type = st.selectbox("Select the type of test:", ["correlation", "difference"])

    if st.button("Choose Statistical Test"):
        result = choose_statistical_test(data_type_1, data_type_2, sample_size, independence, test_type)
        st.write(f"The suggested statistical test is: {result}")
        
    if st.button("Choose Post Hoc Test"):
        posthoc_result = choose_posthoc_test(data_type_1, data_type_2, sample_size, independence)
        st.write(f"The suggested post hoc test is: {posthoc_result}")



if __name__ == "__main__":
    app()