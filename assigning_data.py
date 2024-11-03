import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

df = pd.read_csv('training.csv')

empty_cabin_mask = df['Cabin'].isna()
#The list of possible cabin labels to choose from
cabin_labels =[f'{letter}{number}' for letter in 'ABCDE' for number in range(1, 101)]
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
m = len(df)
df['Cabin location'] = np.random.choice(["Upper", "Middle", "Lower"], size=m, p=[0.3, 0.4, 0.3])


empty_age_mask = df['Age'].isna()
age_labels = [int(number) for number in range(1, 80)]
random_ages = np.random.choice(age_labels , size=empty_age_mask.sum(), replace=True)
df.loc[empty_age_mask, 'Age'] = random_ages 

# Add new boolean column 'can_survive' with random 0 or 1 values
n = len(df)
df['Can swim'] = np.random.choice([0, 1], size=n, p=[0.6, 0.4])


# Function to determine survival based on the rules
def calculate_survival_probability(row):
    # Base survival probability
    survival_prob = 0.4
    
    # Adjust based on swimming ability
    if row['Can swim'] == 1:
        survival_prob += 0.3  # Swimmers get +20% chance
    
    # Adjust based on cabin location
    if row['Cabin location'] == "Upper":
        survival_prob += 0.4
    elif row['Cabin location'] == "Middle":
        survival_prob += 0.2
    elif row['Cabin location'] == "Lower":
        survival_prob -= 0.1  # Lower decks have a penalty
    
    # Adjust based on age
    if row['Age'] < 10 or row['Age'] > 70:
        survival_prob -= 0.15  # Young children have a lower chance
    elif row['Age'] > 20 or row['Age'] < 40:
        survival_prob += 0.10  # Older individuals have a lower chance   
    
    return survival_prob

df['Survival Probability'] = df.apply(calculate_survival_probability, axis=1)
df['Survive'] = df['Survival Probability'].apply(lambda x: 1 if x >= 0.8 else 0)


df.to_csv('training_modified.csv', index=False)

train_df, test_df = train_test_split(df, test_size=0.2, stratify=df['Survive'], random_state=42)

# Save the training and test sets to CSV files if needed
train_df.to_csv('training_set.csv', index=False)
test_df.to_csv('test_set.csv', index=False)