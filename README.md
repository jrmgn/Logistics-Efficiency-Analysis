Week 8 (Activity 2): Logistics Efficiency Analysis

This project builds a complete end-to-end data pipeline to track and visualize key logistics performance metrics for improved operational monitoring.

Key Deliverables

1. Data Processing: Python scripts to clean delivery logs and compute core KPIs (On-Time Delivery, Package Loss, Fuel Efficiency).
2. Database Integration: PostgreSQL database implementation storing structured delivery logs for scalable querying.
3. Interactive Dashboard: A live web-based dashboard using Streamlit and Plotly for real-time KPI monitoring and trend visualization.

How to Run

1. Ensure Python 3.x is installed with the required libraries: pandas, numpy, plotly, sqlalchemy, psycopg2-binary, streamlit.
2. Open Logistics Efficiency Analysis.ipynb in Jupyter Notebook and run the cells sequentially to clean data and generate the KPI summaries.
3. Ensure your local PostgreSQL server is running and accessible.
4. Open your terminal in the project folder and run:
  streamlit run dashboard.py
5. Open http://localhost:8501 in your browser to interact with the dashboard.
