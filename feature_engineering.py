
import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.impute import SimpleImputer

def fe_pipeline(df, categorical_cols, numerical_cols, scaler_type="standard"):
    df = df.copy()

    # Missing values
    num_imputer = SimpleImputer(strategy="median")
    df[numerical_cols] = num_imputer.fit_transform(df[numerical_cols])

    cat_imputer = SimpleImputer(strategy="most_frequent")
    df[categorical_cols] = cat_imputer.fit_transform(df[categorical_cols])

    # One-hot encoding
    df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

    # Scaling
    scaler = StandardScaler() if scaler_type == "standard" else MinMaxScaler()
    df[numerical_cols] = scaler.fit_transform(df[numerical_cols])

    return df
