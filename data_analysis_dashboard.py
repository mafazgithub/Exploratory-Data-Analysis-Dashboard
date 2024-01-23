import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Generate dummy data for demonstration
data = pd.DataFrame({
    'Age': np.random.randint(18, 65, 100),
    'Income': np.random.randint(30000, 100000, 100),
    'SpendingScore': np.random.randint(1, 100, 100)
})

# Exploratory Data Analysis
summary_stats = data.describe()
correlation_matrix = data.corr()

# Plot a pair plot for important features
sns.pairplot(data[['Age', 'Income', 'SpendingScore']])
plt.suptitle('Pair Plot of Important Features', y=1.02)
plt.show()

# Plot a heatmap for the correlation matrix
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix')
plt.show()
