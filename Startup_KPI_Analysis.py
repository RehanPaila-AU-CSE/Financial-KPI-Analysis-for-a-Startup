
import pandas as pd

# Simulate the cleaned version of your startup financial dataset (like your Excel work)
data = {
    "Month": ["January", "February", "March", "April", "May", "June"],
    "Revenue": [120000, 150000, 180000, 200000, 220000, 250000],
    "Expenses": [200000, 210000, 190000, 230000, 240000, 250000],
    "Marketing Spend": [40000, 35000, 45000, 46000, 48000, 47000],
    "Customers Acquired": [100, 90, 120, 130, 125, 135]
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate derived KPIs
df["Burn Rate"] = df["Expenses"] - df["Revenue"]
df["CAC"] = df["Marketing Spend"] / df["Customers Acquired"]
df["Revenue per Customer"] = df["Revenue"] / df["Customers Acquired"]
df["LTV"] = df["Revenue per Customer"] * 12
df["LTV to CAC Ratio"] = df["LTV"] / df["CAC"]

# Calculate overall metrics
total_revenue = df["Revenue"].sum()
average_burn_rate = df["Burn Rate"].mean()
average_ltv_cac = df["LTV to CAC Ratio"].mean()
runway_months = 1000000 / average_burn_rate  # assuming ₹10 lakh runway cash

# Print results
print("Cleaned KPI Table:\n", df)
print("\nSummary:")
print("Total Revenue: ₹", total_revenue)
print("Average Burn Rate: ₹", round(average_burn_rate, 2))
print("Average LTV:CAC Ratio:", round(average_ltv_cac, 2))
print("Estimated Runway (in months):", round(runway_months, 2))

# Save cleaned data to CSV
df.to_csv("Cleaned_Startup_KPI_Analysis.csv", index=False)
