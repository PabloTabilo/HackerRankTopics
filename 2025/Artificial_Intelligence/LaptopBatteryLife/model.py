import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

import matplotlib.pyplot as plt

def read_data() -> pd.DataFrame:
    row_data = []
    with open("train.txt", "r") as f:
        for line in f:
            line = list(map(float, line.split(",")))
            row_data.append(line)
    return pd.DataFrame(row_data, columns=["x", "y"])

if __name__ == "__main__":
    df = read_data()
    print(df.head(6))
    
    plt.scatter(x = df["x"], y = df["y"], alpha=0.7)
    plt.xlabel("Charging Time")
    plt.ylabel("Battery Life")
    plt.title("Charging Time vs. Battery Life")
    plt.savefig('scatter.png')
    
    break_point = 4.1
    df_before_break_point = df.loc[df.x <= break_point,:]
    df_after_break_point = df.loc[df.x > break_point,:]
    
    y_bbp = df_before_break_point.loc[:,"y"].to_numpy()
    X_bbp = df_before_break_point.loc[:,"x"].to_numpy()
    X_bbp = X_bbp.reshape(-1,1)
    reg_bbp = LinearRegression().fit(X_bbp, y_bbp)
    print(f"reg_bbp.coef = {reg_bbp.coef_[0]}")
    print(f"reg_bbp.intercept = {reg_bbp.intercept_}")
    
    y_abp = df_after_break_point.loc[:,"y"].to_numpy()
    X_abp = df_after_break_point.loc[:,"x"].to_numpy()
    X_abp = X_abp.reshape(-1,1)
    reg_abp = LinearRegression().fit(X_abp, y_abp)
    print(f"reg_abp.coef = {reg_abp.coef_[0]}")
    print(f"reg_abp.intercept = {reg_abp.intercept_}")
    
    
    # reg_bbp.coef = 1.9999999999999993
    # reg_bbp.intercept = 1.7763568394002505e-15
    # reg_abp.coef = -0.0
    # reg_abp.intercept = 8.0