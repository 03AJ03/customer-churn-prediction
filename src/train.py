import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

print("Starting training...")

# load dataset
df = pd.read_csv("../data/Churn_Modelling.csv")

print("Dataset loaded")

# drop unnecessary columns
df = df.drop(["RowNumber","CustomerId","Surname"], axis=1)

# encode categorical variables
df = pd.get_dummies(df, columns=["Geography","Gender"], drop_first=True)

print("Preprocessing done")

# split features and target
X = df.drop("Exited", axis=1)
y = df["Exited"]

# train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X,y,test_size=0.2,random_state=42
)

print("Training model...")

# train model
model = RandomForestClassifier()
model.fit(X_train,y_train)

print("Training finished")

# save model
pickle.dump(model, open("../models/churn_model.pkl","wb"))

print("Model saved in models folder")