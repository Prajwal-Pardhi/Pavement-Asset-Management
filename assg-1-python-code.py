# Question - 2----------------------------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Rutting data provided
sections = [1, 2, 3, 4, 5]
rutting_data = [10.79, 13.94, 12.69, 8.63, 11.25]

# Calculating the mean and standard deviation
mean_rutting = np.mean(rutting_data)
std_rutting = np.std(rutting_data, ddof=1)
acceptance_criterion = 1.25

# Print the key statistics
print(f"Mean Rutting Measurement: {mean_rutting:.2f} mm")
print(f"Standard Deviation of Rutting: {std_rutting:.2f} mm")

# Check if the standard deviation meets the agency's acceptance criterion
if std_rutting <= acceptance_criterion:
    print("The measurement method meets the precision acceptance criterion (Standard deviation ≤ 1.25 mm).")
else:
    print("The measurement method does NOT meet the precision acceptance criterion (Standard deviation > 1.25 mm).")

# 1. Bar plot of rutting measurements
plt.figure(figsize=(8, 6))
plt.bar(sections, rutting_data, color='lightgreen')
plt.xlabel('Section')
plt.ylabel('Rutting Measurement (mm)')
plt.title('Rutting Measurements per Section')
plt.grid(True)
plt.show()

# 2. Standard deviation plot with mean and ±1.25 mm range
plt.figure(figsize=(8, 6))
plt.axhline(mean_rutting, color='red', linestyle='--', label=f'Mean: {mean_rutting:.2f} mm')
plt.axhline(mean_rutting + acceptance_criterion, color='blue', linestyle='--', label=f'Mean + {acceptance_criterion} mm')
plt.axhline(mean_rutting - acceptance_criterion, color='green', linestyle='--', label=f'Mean - {acceptance_criterion} mm')
plt.plot(sections, rutting_data, marker='o', linestyle='-', color='black', label='Rutting Measurements')
plt.xlabel('Section')
plt.ylabel('Rutting Measurement (mm)')
plt.title('Rutting Measurement with ±1.25 mm Range')
plt.legend()
plt.grid(True)
plt.show()





# Question-1 --------------------------------------------------------------------------------------------------------

# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# from scipy import stats

# # Data from the IRI (International Roughness Index) of both agency and vendor is manually added
# data_dict = {
#     'SrNO': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
#     'IRI_agency': [1.6, 6.4, 8.0, 3.2, 4.1, 3.4, 3.4, 2.2, 5.0, 4.6, 2.4, 5.6, 4.1, 2.0, 3.1, 4.6, 2.8, 4.9, 5.0],
#     'IRI_vendor': [1.4, 6.5, 7.9, 3.3, 4.4, 3.7, 3.6, 2.6, 5.0, 4.6, 2.6, 5.4, 4.1, 2.0, 3.4, 4.6, 3.1, 5.1, 5.1]
# }

# # Converting the dictionary into a DataFrame for easy handling
# data = pd.DataFrame(data_dict)

# # Display the first few rows of the data
# print(data.head())

# # Step 1: Conduct a paired t-test to compare IRI values between agency and vendor
# t_stat, p_value = stats.ttest_rel(data['IRI_vendor'], data['IRI_agency'])
# print(f"Paired t-test results: \n t-statistic = {t_stat}, p-value = {p_value}")

# # Determine if the p-value indicates a significant difference (using alpha = 0.05 for 95% confidence)
# if p_value < 0.05:
#     print("At a 95% confidence level, there is a significant difference between the agency and vendor measurements.")
# else:
#     print("At a 95% confidence level, there is no significant difference between the agency and vendor measurements.")

# # Step 2: Calculate the bias (difference between the two sets of measurements)
# bias = data['IRI_vendor'] - data['IRI_agency']
# mean_bias = np.mean(bias)
# print(f"Mean bias between vendor and agency IRI: {mean_bias}")
# if mean_bias > 0:
#     print("The vendor tends to overestimate the IRI values.")
# elif mean_bias < 0:
#     print("The vendor tends to underestimate the IRI values.")
# else:
#     print("No consistent bias detected.")

# # Step 3: Check if the vendor's measurements fall within ±5% accuracy of the agency's reference
# accuracy_check = np.abs(bias / data['IRI_agency']) <= 0.05
# accuracy_percent = accuracy_check.mean() * 100
# print(f"Percentage of data within ±5% accuracy: {accuracy_percent}%")
# if accuracy_percent >= 95:
#     print("The automated equipment meets the accuracy requirement.")
# else:
#     print("The automated equipment does not meet the accuracy requirement.")

# # Visualizing the data

# # Plot 1: Vendor vs Agency scatter plot
# plt.figure(figsize=(10, 6))
# plt.scatter(data['IRI_agency'], data['IRI_vendor'], color='black', label='Vendor IRI')
# plt.plot([data['IRI_agency'].min(), data['IRI_agency'].max()],
#          [data['IRI_agency'].min(), data['IRI_agency'].max()],
#          color='red', linestyle='--', label='Perfect Match Line (Vendor = Agency)')
# plt.title('Comparison of Vendor and Agency IRI Measurements')
# plt.xlabel('Agency IRI (m/km)')
# plt.ylabel('Vendor IRI (m/km)')
# plt.legend()
# plt.grid(True)
# plt.show()

# # Plot 2: Visualizing the bias between vendor and agency measurements
# plt.figure(figsize=(10, 6))
# plt.plot(data.index, bias, marker='o', color='blue', label='Vendor - Agency Bias')
# plt.axhline(0, color='red', linestyle='--', label='No Bias Line')
# plt.title('Bias Between Vendor and Agency IRI Measurements')
# plt.xlabel('Sample Number')
# plt.ylabel('Bias (m/km)')
# plt.legend()
# plt.grid(True)
# plt.show()

# # Plot 3: Checking accuracy of the vendor measurements (±5% of the agency reference)
# plt.figure(figsize=(10, 6))
# plt.plot(data.index, accuracy_check, marker='o', color='blue', label='Within ±5% Accuracy')
# plt.axhline(1, color='black', linestyle='--', label='Accuracy Threshold')
# plt.title('Accuracy of Vendor Measurements (±5% of Agency Reference)')
# plt.xlabel('Sample Number')
# plt.ylabel('Accuracy (1 = Within Threshold, 0 = Outside)')
# plt.legend()
# plt.grid(True)
# plt.show()

# # Plot 4: Histogram showing the distribution of bias
# plt.figure(figsize=(10, 6))
# sns.histplot(bias, kde=True, bins=20, color='red')
# plt.axvline(mean_bias, color='black', linestyle='--', label=f'Mean Bias = {mean_bias:.3f}')
# plt.title('Distribution of Bias (Vendor - Agency)')
# plt.xlabel('Bias (m/km)')
# plt.ylabel('Frequency')
# plt.legend()
# plt.grid(True)
# plt.show()
