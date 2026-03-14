import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from preprocess import preprocess_data

print("Starting training...")

df = pd.read_csv("data/Churn_Modelling.csv")

print("Dataset loaded")
df = preprocess_data(df)

print("Preprocessing done")

X = df.drop("Exited", axis=1)
y = df["Exited"]

X_train, X_test, y_train, y_test = train_test_split(
    X,y,test_size=0.2,random_state=42
)

print("Training model...")

model = RandomForestClassifier()
model.fit(X_train,y_train)

print("Training finished")

pickle.dump(model, open("models/churn_model.pkl","wb"))

print("Model saved in models folder")