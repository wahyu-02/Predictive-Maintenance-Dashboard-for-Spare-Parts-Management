
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Processed Data
data = pd.read_csv("processed_maintenance_data.csv")

# Title
st.title("Predictive Maintenance Dashboard")

# Show Dataset
st.header("Dataset Overview")
st.dataframe(data.head())

# Plot 1: Distribution of Predicted Replacement Time
st.header("Distribution of Predicted Replacement Time")
fig1, ax1 = plt.subplots()
sns.histplot(data['Predicted Replacement Time (Months)'], bins=15, kde=True, ax=ax1, color='blue')
ax1.set_title('Distribution of Predicted Replacement Time')
ax1.set_xlabel('Replacement Time (Months)')
ax1.set_ylabel('Frequency')
st.pyplot(fig1)

# Plot 2: Count of Urgency Levels
st.header("Count of Replacement Urgency Levels")
fig2, ax2 = plt.subplots()
sns.countplot(x=data['Replacement Urgency'], palette='viridis', ax=ax2)
ax2.set_title('Count of Replacement Urgency Levels')
ax2.set_xlabel('Urgency Level')
ax2.set_ylabel('Count')
st.pyplot(fig2)

# Interactive Section: Predict Urgency
st.header("Predict Replacement Urgency")
st.write("Input details to predict if a part replacement is urgent.")
usage_frequency = st.number_input("Usage Frequency (Per Month)", min_value=0, value=5)
current_stock = st.number_input("Current Stock Level", min_value=0, value=10)
min_nos = st.number_input("Min Nos", min_value=0, value=1)
max_nos = st.number_input("Max Nos", min_value=0, value=5)

predicted_time = current_stock / (usage_frequency if usage_frequency > 0 else 1)
urgency = "Urgent" if predicted_time < 2 else "Normal"

st.write(f"Predicted Replacement Time (Months): {predicted_time:.2f}")
st.write(f"Replacement Urgency: {urgency}")
