
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# Set page config
st.set_page_config(
    page_title="African Economic Dashboard",
    page_icon="🌍",
    layout="wide"
)

# EMBED YOUR ACTUAL DATA HERE - Replace this with your cleaned dataframe
@st.cache_data
def load_data():
    """Load your African economic data"""
    # CREATE SAMPLE DATA (REPLACE WITH YOUR ACTUAL DATA)
    countries = ["Nigeria", "South Africa", "Kenya", "Ghana", "Ethiopia", "Egypt", 
                 "Tanzania", "Uganda", "Angola", "Morocco"]
    
    indicators = ["GDP Growth Rate", "Inflation Rate", "Budget Deficit/Surplus", 
                  "Government Debt", "Exports", "Imports"]
    
    years = list(range(2015, 2024))
    
    data = []
    for country in countries:
        for indicator in indicators:
            for year in years:
                if indicator == "GDP Growth Rate":
                    value = np.random.normal(4.5, 1.5)
                elif indicator == "Inflation Rate":
                    value = np.random.normal(8.0, 2.5)
                elif indicator == "Budget Deficit/Surplus":
                    value = np.random.normal(-120000, 40000)
                elif indicator == "Government Debt":
                    value = np.random.normal(500000, 150000)
                elif indicator == "Exports":
                    value = np.random.normal(600000, 200000)
                else:  # Imports
                    value = np.random.normal(700000, 250000)
                
                data.append({
                    "Country": country,
                    "Indicator": indicator,
                    "Year": year,
                    "Amount": value
                })
    
    return pd.DataFrame(data)

df = load_data()

# MAIN APP
def main():
    st.title("🌍 African Economic Dashboard")
    st.markdown("Interactive analysis of economic performance across Africa")
    
    # Sidebar filters
    st.sidebar.header("Filters")
    countries = st.sidebar.multiselect(
        "Select Countries:",
        options=df["Country"].unique(),
        default=df["Country"].unique()[:3]
    )
    
    # Filter data
    filtered_df = df[df["Country"].isin(countries)]
    
    # Display key metrics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        gdp_avg = filtered_df[filtered_df["Indicator"] == "GDP Growth Rate"]["Amount"].mean()
        st.metric("Average GDP Growth", f"{gdp_avg:.1f}%")
    
    with col2:
        inflation_avg = filtered_df[filtered_df["Indicator"] == "Inflation Rate"]["Amount"].mean()
        st.metric("Average Inflation", f"{inflation_avg:.1f}%")
    
    with col3:
        deficit_avg = filtered_df[filtered_df["Indicator"] == "Budget Deficit/Surplus"]["Amount"].mean()
        st.metric("Average Budget", f"{deficit_avg:,.0f}")
    
    # Charts
    tab1, tab2, tab3 = st.tabs(["GDP Growth", "Inflation", "Budget"])
    
    with tab1:
        gdp_data = filtered_df[filtered_df["Indicator"] == "GDP Growth Rate"]
        if not gdp_data.empty:
            fig = px.line(gdp_data, x="Year", y="Amount", color="Country", 
                         title="GDP Growth Trends")
            st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        inflation_data = filtered_df[filtered_df["Indicator"] == "Inflation Rate"]
        if not inflation_data.empty:
            fig = px.line(inflation_data, x="Year", y="Amount", color="Country",
                         title="Inflation Trends")
            st.plotly_chart(fig, use_container_width=True)
    
    with tab3:
        budget_data = filtered_df[filtered_df["Indicator"] == "Budget Deficit/Surplus"]
        if not budget_data.empty:
            fig = px.bar(budget_data, x="Year", y="Amount", color="Country",
                        title="Budget Positions")
            st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    main()
