import matplotlib.pyplot as plt

# Data for the graph
categories = [
    "Mental-Physical Integration",
    "Predictive Insights",
    "Gamified Mental Health",
    "Community Support",
    "Educational Content",
    "AR/VR Training",
    "User Personalization"
]
virtual_human_twin = [1, 1, 1, 1, 1, 1, 1]  # All features available
calm = [1, 0, 1, 0, 1, 0, 1]  # Features based on Calm's capabilities
fitbit = [0, 0, 0, 1, 0, 0, 1]  # Features based on Fitbit's capabilities
myfitnesspal = [0, 0, 0, 0, 0, 0, 1]  # Features based on MyFitnessPal's capabilities

# Set up the figure and bar width
fig, ax = plt.subplots(figsize=(10, 6))
bar_width = 0.2
x = range(len(categories))

# Plot the data
ax.bar(x, virtual_human_twin, bar_width, label="CoreInt", color="blue")
ax.bar([i + bar_width for i in x], calm, bar_width, label="Calm", color="green")
ax.bar([i + 2 * bar_width for i in x], fitbit, bar_width, label="Fitbit", color="orange")
ax.bar([i + 3 * bar_width for i in x], myfitnesspal, bar_width, label="MyFitnessPal", color="red")

# Add labels, title, and legend
ax.set_xlabel("Features", fontsize=12)
ax.set_ylabel("Availability (1 = Yes, 0 = No)", fontsize=12)
ax.set_title("Feature Comparison of CoreInt vs Competitors", fontsize=14)
ax.set_xticks([i + 1.5 * bar_width for i in x])
ax.set_xticklabels(categories, rotation=45, ha="right", fontsize=10)
ax.legend()

# Display the graph
plt.tight_layout()
plt.show()
