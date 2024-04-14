# Importing the data, Pandas, Matplotlib.pyplot, and Numpy libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('CSE578_Project_Data.txt', sep=',', names=['Age', 'Work Class', 'fnlwgt', 'Education','Education Num','Marital Status','Occupation','Relationship','Race','Sex','Capital Gain', 'Capital Loss','Hours Per Week', 'Native
Country', 'Salary'])

# Cleaning the data to remove the "?"
data.replace(" ?", "Not Identified", inplace=True)
data.to_csv('CSE578_Project_Data.txt', index=False)
data = data[data['Salary'] != 'Salary']
grouped_count = data.groupby(['Education', 'Salary']).size().unstack(fill_value=0)
print(grouped_count.columns)
grouped_count.drop(grouped_count.tail(1).index, inplace=True)

# Add the correct column names as appear in your DataFrame
columns_to_keep = [' <=50K', ' >50K']
grouped_count = grouped_count[columns_to_keep]
print(grouped_count)

# Plotting
fig, ax = plt.subplots(figsize=(10, 6)) # Adjust figure size as needed

# Assuming 'grouped_count' is indexed by 'Education' with salary brackets as columns
grouped_count.plot(kind='bar', stacked=True, ax=ax)
ax.set_title('Number of Individuals by Education and Salary')
ax.set_xlabel('Education')
ax.set_ylabel('Count')
plt.xticks(rotation=65) # Rotate the x-axis labels for better readability
ax.legend(title='Salary')
plt.show()

# Visualization for User Story 2
# Ensure 'Age' is numeric, changing any errors to NaN
data['Age'] = pd.to_numeric(data['Age'], errors='coerce')

# Check for any NaN values that might indicate conversion issues
nan_count_age = data['Age'].isnull().sum()
print(f"NaN values in 'Age': {nan_count_age}")
age_bins = [0, 20, 30, 40, 50, 60, np.inf]
age_labels = ['<20', '20-30', '30-40', '40-50', '50-60', '60+']
data['Age Binned'] = pd.cut(data['Age'], bins=age_bins, labels=age_labels, include_lowest=True)
plt.figure(figsize=(10, 8))
sns.boxplot(x='Salary', y='Age Binned', hue='Education', data=data[data['Education'].isin(['
Bachelors', ' HS-grad', ' Masters'])])
plt.title('Age and Education Impact on Income')
plt.xlabel('Income')
plt.ylabel('Age')
plt.legend(title='Education', loc='upper right')
plt.show()

# Visualization for User Story 3
pd.crosstab(index=data['Occupation'], columns=data['Marital Status'], values=data['Salary'],
aggfunc=lambda x: np.mean(x== ' >50K'), normalize='index').plot(kind='bar', stacked=True,
figsize=(10, 7))
plt.title('Impact of Marital Status and Occupation on Income')
plt.xlabel('Occupation')
plt.ylabel('Percentage with >50K Salary')
plt.xticks(rotation=45)
plt.legend(title='Marital Status', loc='upper left', bbox_to_anchor=(1, 1))
plt.tight_layout()
plt.show()

# Visualization for User Story 4
sns.countplot(x='Salary', hue='Sex', data=data, palette='Set2')
plt.title('Income Distribution by Gender')
plt.xlabel('Income')
plt.ylabel('Count')
plt.show()
sns.countplot(x='Salary', hue='Race', data=data, palette='Set3')
plt.title('Income Distribution by Race')
plt.xlabel('Income')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

# Visualization for User Story 5
# Convert 'Capital Gain' to numeric, changing errors to NaN
data['Capital Gain'] = pd.to_numeric(data['Capital Gain'], errors='coerce')

# Define the bin edges
data['Capital Gain Category'] = pd.cut(data['Capital Gain'],
 bins=[-1, 0, 5000, 10000, 15000, 20000, 100000],
 labels=['0', '1-5000', '5001-10000', '10001-15000', '15001-20000', '>20000'])

# Convert 'Hours Per Week' to a numeric type, changin any errors to NaN
data['Hours Per Week'] = pd.to_numeric(data['Hours Per Week'], errors='coerce')

# Define the bin edges
bins = [0, 20, 40, 60, 80, 100]
labels = ['0-20', '21-40', '41-60', '61-80', '81-100']
data['Hours Per Week Binned'] = pd.cut(data['Hours Per Week'], bins=bins, labels=labels,
include_lowest=True)

# Using stripplot for a scatter-like plot with a categorical axis
plt.figure(figsize=(10, 7))
sns.stripplot(x='Capital Gain Category', y='Hours Per Week', hue='Salary', data=data, dodge=True,
alpha=0.5)
plt.title('Hours Per Week by Capital Gain Category and Income')
plt.xlabel('Capital Gain Category')
plt.ylabel('Hours Per Week')
plt.legend(title='Income', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
