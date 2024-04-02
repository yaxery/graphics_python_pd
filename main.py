import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoami':lst})
data.head()


# Create a new dataframe to store the one-hot encoded values
one_hot_data = pd.DataFrame()

# Get unique values from the 'whoami' column
unique_values = data['whoami'].unique()

# Iterate through the unique values and create a new column in the one-hot data for each value
for unique_value in unique_values:
    # Create a new column with the name as the unique value
    one_hot_data[unique_value] = (data['whoami'] == unique_value).astype(int)

one_hot_data.head()