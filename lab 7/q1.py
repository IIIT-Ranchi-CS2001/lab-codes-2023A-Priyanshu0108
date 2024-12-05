# Code reset. Re-importing necessary libraries and re-defining the solution.

import numpy as np
import matplotlib.pyplot as plt

# Dataset
covid_data = np.array([
    [1500, 2000, 1800, 1200, 900],  # Day 1 
    [1600, 2100, 1900, 1300, 950],  # Day 2 
    [1700, 2200, 2000, 1400, 1000],  # Day 3 
    [1650, 2150, 1950, 1350, 980],  # Day 4 
    [1750, 2250, 2050, 1450, 1020],  # Day 5 
    [1800, 2300, 2100, 1500, 1050],  # Day 6 
    [1900, 2400, 2200, 1600, 1100],  # Day 7 
])
countries = ["Country_A", "Country_B", "Country_C", "Country_D", "Country_E"]

# Task 1: Basic Statistics
total_cases_per_country = covid_data.sum(axis=0)
highest_cases_country_index = np.argmax(total_cases_per_country)
highest_cases_country = countries[highest_cases_country_index]

# Task 2: Daily Analysis
average_cases_per_day = covid_data.mean(axis=1)
highest_cases_day_index = np.argmax(covid_data.sum(axis=1))
highest_cases_day = highest_cases_day_index + 1

# Task 3: Trends
percentage_change = ((covid_data[-1, :] - covid_data[0, :]) / covid_data[0, :]) * 100
highest_increase_country_index = np.argmax(percentage_change)
highest_increase_country = countries[highest_increase_country_index]

# Task 4: Data Normalization
normalized_data = (covid_data - covid_data.min(axis=0)) / (covid_data.max(axis=0) - covid_data.min(axis=0))

# Task 5: Visualization
plt.figure(figsize=(12, 6))
days = np.arange(1, 8)

# Line chart
for i, country in enumerate(countries):
    plt.plot(days, covid_data[:, i], label=country)

# Highlight the day with the highest total cases
plt.axvline(x=highest_cases_day, color='red', linestyle='--', label=f"Highest Total Cases (Day {highest_cases_day})")
plt.annotate(f"Day {highest_cases_day}",
             xy=(highest_cases_day, covid_data.sum(axis=1)[highest_cases_day_index]),
             xytext=(highest_cases_day + 0.5, covid_data.sum(axis=1).max() - 500),
             arrowprops=dict(facecolor='black', arrowstyle="->"))

plt.title("Daily COVID-19 Cases per Country")
plt.xlabel("Day")
plt.ylabel("Number of Cases")
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()

# Outputs
(total_cases_per_country, highest_cases_country, average_cases_per_day, highest_cases_day, 
 percentage_change, highest_increase_country, normalized_data)
