import pandas as pd
import numpy as np

df = pd.read_csv('training.csv')

empty_cabin_mask = df['Cabin'].isna()
#The list of possible cabin labels to choose from
cabin_labels =[f'{letter}{number}' for letter in 'ABC' for number in range(1, 101)]
#This function call randomly selects elements from the cabin_labels list.
#empty_cabin_mask.sum() calculates the total number of empty cells in the Cabin column
#replace=True allows the same value to be selected multiple times
random_cabins = np.random.choice(cabin_labels, size=empty_cabin_mask.sum(), replace=True)
df.loc[empty_cabin_mask, 'Cabin'] = random_cabins 

# Function to keep only the first value in each 'Cabin' cell
def keep_first_cabin_value(cabin):
    if pd.isna(cabin):
        return cabin
    return cabin.split()[0]

# Apply the function to the 'Cabin' column
df['Cabin'] = df['Cabin'].apply(keep_first_cabin_value)
# Add new boolean column based on 'Cabin' values
df['Cabin flag'] = df['Cabin'].apply(lambda x: 0 if str(x).startswith(('A', 'B')) else 1)


empty_age_mask = df['Age'].isna()
age_labels = [float(number) for number in range(1, 90)]
random_ages = np.random.choice(age_labels , size=empty_age_mask.sum(), replace=True)
df.loc[empty_age_mask, 'Age'] = random_ages 

# Add new boolean column 'can_survive' with random 0 or 1 values
df['Can swim'] = np.random.randint(0, 2, size=len(df))
df['Can survive'] = df['Can swim'] & df['Cabin flag']

df.to_csv('training_modified.csv', index=False)

