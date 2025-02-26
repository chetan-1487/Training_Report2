import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

data = {
    'Age': [25, 30, np.nan, 40, 35],  # Contains a missing value (NaN)
    'Salary': [50000, 54000, 60000, 58000, np.nan]  # Another NaN
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Handle Missing Values (Fill NaN with Column Mean)
new_df=df.fillna(df.mean())
print(new_df)
# Normalize Data (Scale between 0 and 1)
scaler = MinMaxScaler()
df[['Age', 'Salary']] = scaler.fit_transform(df[['Age', 'Salary']])

print(df)