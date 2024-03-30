import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Load the CSV data into a DataFrame
data = pd.read_csv('result_data.csv')  # Replace 'result_data.csv' with your CSV file name

# Extract features (SSC Percentage) and labels (College Names)
X = data[['SSCPercentage']].values
y = data['CollegeName']

# Encode the college names to numerical values
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

# Create a decision tree classifier
clf = DecisionTreeClassifier()

# Fit the classifier to the training data
clf.fit(X_train, y_train)

# Prompt the student for their SSC percentage
ssc_percentage = float(input("Enter your SSC percentage: "))

# Filter colleges with cutoffs less than or equal to the entered percentage
matching_colleges = data[data['SSCPercentage'] <= ssc_percentage]

if matching_colleges.empty:
    print("No colleges found with a cutoff percentage less than or equal to your SSC percentage.")
else:
    # Display the list of colleges and branches that meet the student's criteria
    for index, row in matching_colleges.iterrows():
        print(f"College Name: {row['CollegeName']}")
        print(f"Branches Available: {row['Branches']}")
        print()
        