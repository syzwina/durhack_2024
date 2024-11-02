import pandas as pd
import numpy as np

df = pd.read_csv('training.csv')

empty_cabin_mask = df['Cabin'].isna()

cabin_labels =[f'{letter}{number}' for letter in 'ABC' for number in range(1, 101)]
random_cabins = np.random.choice(cabin_labels, size=empty_cabin_mask.sum(), replace=True)

df.loc[empty_cabin_mask, 'Cabin'] = random_cabins 

df.to_csv('training_modified.csv', index=False)

print(np.__version__)
print(pd.__version__)
print("Empty cabins filled with random values")