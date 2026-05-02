import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

# Load dataset
df = pd.read_csv("netflix_titles.csv")

# Basic information
print("Original Shape:", df.shape)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Fill missing values
df['director'].fillna('Unknown', inplace=True)
df['cast'].fillna('Not Available', inplace=True)
df['country'].fillna('Unknown', inplace=True)
df['rating'].fillna('Not Rated', inplace=True)
df['date_added'].fillna('Unknown', inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

print("\nShape After Cleaning:", df.shape)

# Verify missing values
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())
# Count Movies vs TV Shows
print("\nContent Type Distribution:")
print(df['type'].value_counts())

# Visualization
plt.figure(figsize=(8,5))
sns.countplot(x='type', data=df)

plt.title('Distribution of Movies and TV Shows on Netflix')
plt.xlabel('Content Type')
plt.ylabel('Count')

plt.show()
# Convert date_added to datetime
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

# Extract year
df['year_added'] = df['date_added'].dt.year

# Plot content additions over years
plt.figure(figsize=(12,6))
df['year_added'].value_counts().sort_index().plot(kind='bar')

plt.title('Content Added to Netflix Over the Years')
plt.xlabel('Year')
plt.ylabel('Number of Titles Added')

plt.show()
print("\nStep 4 completed successfully!")
print("Year Added column created.")
# Top 10 countries producing Netflix content
top_countries = df['country'].value_counts().head(10)

plt.figure(figsize=(12,6))
top_countries.plot(kind='bar')

plt.title('Top 10 Countries Producing Netflix Content')
plt.xlabel('Country')
plt.ylabel('Number of Titles')
plt.savefig('chart_name.png')

plt.show()

print("\nTop 10 Countries Analysis Completed!")
