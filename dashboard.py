import streamlit as st
import pandas as pd
import plotly.express as px

deliveries = pd.read_csv(r"C:\Users\JERMAGNE\logistics-efficiency-analysis\deliveries.csv")
fuel_data = pd.read_csv(r"C:\Users\JERMAGNE\logistics-efficiency-analysis\fuel_logs.csv")

on_time_rate = (len(deliveries[deliveries['status'] == 'on_time']) / len(deliveries)) * 100
loss_rate = (len(deliveries[deliveries['status'] == 'lost']) / len(deliveries)) * 100
fuel_data['fuel_efficiency'] = fuel_data['distance_km'] / fuel_data['fuel_liters']
fuel_efficiency = fuel_data['distance_km'].sum() / fuel_data['fuel_liters'].sum()

st.title("Logistics KPI Dashboard")
st.metric("On-Time Delivery %", f"{on_time_rate:.2f}%")
st.metric("Package Loss %", f"{loss_rate:.2f}%")
st.metric("Fuel Efficiency (km/L)", f"{fuel_efficiency:.2f}")

st.plotly_chart(px.pie(deliveries, names='status', title='Delivery Status'))
st.plotly_chart(px.bar(fuel_data, x='vehicle_id', y='fuel_efficiency', title='Fuel Efficiency by Vehicle'))
