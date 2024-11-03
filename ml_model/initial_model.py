from sklearn.tree import DecisionTreeClassifier
import pickle
import pandas as pd

# Load the dataset
df = pd.read_csv('./training_modified.csv')

# Map categorical features to numeric values for the decision tree
df['Sex'] = df['Sex'].map({'female': 0, 'male': 1})
df['Cabin'] = df['Cabin'].astype('category').cat.codes
df['Cabin location'] = df['Cabin location'].astype('category').cat.codes

# Define features and target variable
X = df[['Age', 'Pclass', 'Sex', 'Can swim', 'Cabin', 'Cabin location']]
y = df['Survive']

# Train a Decision Tree Classifier
clf = DecisionTreeClassifier(random_state=0)
clf.fit(X, y)

# Save the model as a pkl file
filename = 'ml_model/initial_model.pkl'
pickle.dump(clf, open(filename, 'wb'))