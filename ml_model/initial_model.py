from sklearn.tree import DecisionTreeClassifier
import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Create the dataset
data = {
    'Age': [25, 45, 35, 50, 23, 40, 60, 30, 48, 33],
    'Gender': ['Female', 'Female', 'Male', 'Male', 'Female', 'Female', 'Male', 'Female', 'Male', 'Female'],
    'Sick': ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'No', 'Yes', 'Yes', 'No'],
    'Went_to_Lifeboat': ['Yes', 'No', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'No', 'Yes', 'No'],
    'Survives': ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'No', 'Yes', 'Yes', 'Yes']
}

# Convert to a DataFrame
df = pd.DataFrame(data)

# Map categorical features to numeric values for the decision tree
df['Gender'] = df['Gender'].map({'Female': 0, 'Male': 1})
df['Sick'] = df['Sick'].map({'No': 0, 'Yes': 1})
df['Went_to_Lifeboat'] = df['Went_to_Lifeboat'].map({'No': 0, 'Yes': 1})
df['Survives'] = df['Survives'].map({'No': 0, 'Yes': 1})

# Define features and target variable
X = df[['Age', 'Gender', 'Sick', 'Went_to_Lifeboat']]
y = df['Survives']

# # Split data into training and test sets
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# # Create and train the decision tree classifier
# clf = DecisionTreeClassifier()
# clf.fit(X_train, y_train)

# # Make predictions and evaluate accuracy
# y_pred = clf.predict(X_test)
# accuracy = accuracy_score(y_test, y_pred)

# Train a Decision Tree Classifier
clf = DecisionTreeClassifier(random_state=0)
clf.fit(X, y)

# Save the model as a pkl file
filename = 'ml_model/initial_model.pkl'
pickle.dump(clf, open(filename, 'wb'))