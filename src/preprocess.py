import pandas as pd

def preprocess_data(df):

    # drop unnecessary columns
    df = df.drop(["RowNumber","CustomerId","Surname"], axis=1, errors="ignore")

    # encode gender
    df["Gender"] = df["Gender"].map({"Female":0,"Male":1})

    # encode geography
    df = pd.get_dummies(df, columns=["Geography"], drop_first=True)

    return df