# Create a pie chart for Key Metrics Distribution
import matplotlib.pyplot as plt

# Data for the pie chart
metrics = [
    "User Engagement",
    "Health Outcomes",
    "Retention Rates",
    "Crisis Management",
    "Community Engagement",
    "Scalability"
]
percentages = [25, 20, 15, 10, 15, 15]  # Hypothetical percentage distribution

# Plotting the pie chart
fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(percentages, labels=metrics, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)

# Adding a title
ax.set_title("Key Metrics Impact Distribution", fontsize=14)

# Display the pie chart
plt.tight_layout()
plt.show()
