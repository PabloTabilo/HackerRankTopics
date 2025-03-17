# Enter your code here. Read input from STDIN. Print output to STDOUT
import pandas as pd
def read_from_stdin() -> tuple[pd.DataFrame]:
    first_line = input().strip().split()
    F = int(first_line[0])
    row_list = []
    N = int(first_line[1])
    for _ in range(N):
        line = input().strip().split()
        line = [*map(float, line)]
        row_list.append(line)
    df = pd.DataFrame(row_list, columns=[f"col_{i}" for i in range(1,F+2)])
    #print(df.head())
    M = int(input().strip().split()[0])
    row_list_miss = []
    for _ in range(M):
        line = input().strip().split()
        line = [*map(float, line)]
        row_list_miss.append(line)
    missing = pd.DataFrame(row_list_miss, columns=[f"col_{i}" for i in range(1,F+1)])
    #print(missing.head())
    return (df, missing)
df, missing = read_from_stdin()

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

Y_name = df.columns[-1]
y = df[Y_name].to_numpy()
X = df.loc[:, ~df.columns.isin([Y_name])].to_numpy()
# Poly 1
#reg = LinearRegression().fit(X, y)
# Poly 2
#poly2 = PolynomialFeatures(2)
#X2 = poly2.fit_transform(X)
#reg2 = LinearRegression().fit(X2, y)
# Poly 3
poly3 = PolynomialFeatures(3)
X3 = poly3.fit_transform(X)
reg3 = LinearRegression().fit(X3, y)

X_test = missing.to_numpy()
#print("reg1: ")
#print(reg.predict(X_test))
#print("reg2: ")
#print(reg2.predict(poly2.fit_transform(X_test)))
#print("reg3: ")
#print(reg3.predict(poly3.fit_transform(X_test)))

res = reg3.predict(poly3.fit_transform(X_test))
for score in res:
    print(round(score, 3))



