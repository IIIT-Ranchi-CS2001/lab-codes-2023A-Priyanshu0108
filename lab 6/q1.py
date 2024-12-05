import matplotlib.pyplot as plt

# Data for Madhya Pradesh and Rajasthan assembly elections
mp_data = {"BJP": 163, "INC": 66, "BSP": 0, "Others": 1}
raj_data = {"BJP": 115, "INC": 69, "BSP": 2, "Others": 13}

# Calculate percentage shares for pie charts
mp_total = sum(mp_data.values())
raj_total = sum(raj_data.values())
mp_percentages = {party: (seats / mp_total) * 100 for party, seats in mp_data.items()}
raj_percentages = {party: (seats / raj_total) * 100 for party, seats in raj_data.items()}

# Prepare pie chart data
mp_labels = list(mp_data.keys())
raj_labels = list(raj_data.keys())
mp_sizes = list(mp_percentages.values())
raj_sizes = list(raj_percentages.values())

# Highlight the party with the highest percentage
mp_explode = [0.1 if seats == max(mp_sizes) else 0 for seats in mp_sizes]
raj_explode = [0.1 if seats == max(raj_sizes) else 0 for seats in raj_sizes]

# Plot pie charts
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# Madhya Pradesh pie chart
axes[0].pie(mp_sizes, labels=mp_labels, autopct='%1.1f%%', explode=mp_explode, startangle=90, colors=plt.cm.tab20c.colors)
axes[0].set_title("Madhya Pradesh Assembly Elections 2023")

# Rajasthan pie chart
axes[1].pie(raj_sizes, labels=raj_labels, autopct='%1.1f%%', explode=raj_explode, startangle=90, colors=plt.cm.tab20b.colors)
axes[1].set_title("Rajasthan Assembly Elections 2023")

# Bar chart for both states
fig, ax = plt.subplots(figsize=(10, 6))
x = range(len(mp_data))
width = 0.4

# Plotting bar charts
ax.bar([i - width / 2 for i in x], mp_data.values(), width, label='Madhya Pradesh', color='skyblue')
ax.bar([i + width / 2 for i in x], raj_data.values(), width, label='Rajasthan', color='orange')

# Adding labels and title
ax.set_xticks(x)
ax.set_xticklabels(mp_data.keys())
ax.set_ylabel('Seats Won')
ax.set_xlabel('Party')
ax.set_title('Assembly Elections 2023 Results')
ax.legend()

# Display plots
plt.tight_layout()
plt.show()
