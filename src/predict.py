import pickle
import numpy as np

model = pickle.load(open("models/churn_model.pkl","rb"))

sample = np.array([[600,40,5,10000,2,1,1,50000,0,1,1]])

prediction = model.predict(sample)

print("Prediction:",prediction)