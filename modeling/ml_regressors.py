import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.metrics import mean_squared_error,r2_score
from time import time as T
#Linear
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
#Nearest Neighbors
from sklearn.neighbors import KNeighborsRegressor
#Svm regressors
from sklearn.svm import LinearSVR
#Tree-based regressors
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from xgboost import XGBRegressor
import warnings
warnings.filterwarnings("ignore")

#Linear
reg_linear = LinearRegression()
reg_ridge = Ridge(alpha=0.5)
reg_lasso = Lasso(alpha=0.5)
#Nearest Neighbors
reg_knn = KNeighborsRegressor()
#Svm regressors
reg_lsvr = LinearSVR()
#Tree-based regressors
reg_dtr = DecisionTreeRegressor(random_state=42)
reg_rfr = RandomForestRegressor(random_state=42)
reg_gbr = GradientBoostingRegressor(random_state=42)
reg_xgb = XGBRegressor(random_state=42)

###read dataset
df = pd.read_csv('features.csv')
X = df.drop('vehicle_list_price',axis =1)
y = df.vehicle_list_price

### Train test splits
X_train, X_test, y_train, y_test = train_test_split(
X, y, test_size=0.2, random_state=42)

#For regressors that needs standarlization
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("-"*100)
print("Linear regression...")
start = T()
reg_linear.fit(X_train,y_train)
y_pred = reg_linear.predict(X_test)
print(f"R2: {r2_score(y_test,y_pred): .2f}")
print(f"RMSE: {np.sqrt(mean_squared_error(y_test,y_pred)):.2f}")
print(f"Finished in {T()- start: .2f} seconds")

print("-"*100)
print("Ridge regression...")
start = T()
reg_ridge.fit(X_train_scaled,y_train)
y_pred = reg_ridge.predict(X_test_scaled)
print(f"R2: {r2_score(y_test,y_pred): .2f}")
print(f"RMSE: {np.sqrt(mean_squared_error(y_test,y_pred)):.2f}")
print(f"Finished in {T()- start: .2f} seconds")

print("-"*100)
print("Lasso regression...")
start = T()
reg_lasso.fit(X_train_scaled,y_train)
y_pred = reg_lasso.predict(X_test_scaled)
print(f"R2: {r2_score(y_test,y_pred): .2f}")
print(f"RMSE: {np.sqrt(mean_squared_error(y_test,y_pred)):.2f}")
print(f"Finished in {T()- start: .2f} seconds")

print("-"*100)
print("KNN regression...")
start = T()
reg_knn.fit(X_train_scaled,y_train)
y_pred = reg_knn.predict(X_test_scaled)
print(f"R2: {r2_score(y_test,y_pred): .2f}")
print(f"RMSE: {np.sqrt(mean_squared_error(y_test,y_pred)):.2f}")
print(f"Finished in {T()- start: .2f} seconds")

print("-"*100)
print("SVM linear kernal regression...")
start = T()
reg_lsvr.fit(X_train_scaled,y_train)
y_pred = reg_lsvr.predict(X_test_scaled)
print(f"R2: {r2_score(y_test,y_pred): .2f}")
print(f"RMSE: {np.sqrt(mean_squared_error(y_test,y_pred)):.2f}")
print(f"Finished in {T()- start: .2f} seconds")

print("-"*100)
print("Decision tree regression...")
start = T()
reg_dtr.fit(X_train,y_train)
y_pred = reg_dtr.predict(X_test)
print(f"R2: {r2_score(y_test,y_pred): .2f}")
print(f"RMSE: {np.sqrt(mean_squared_error(y_test,y_pred)):.2f}")
print(f"Finished in {T()- start: .2f} seconds")

print("-"*100)
print("Random forest regression...")
start = T()
reg_rfr.fit(X_train,y_train)
y_pred = reg_rfr.predict(X_test)
print(f"R2: {r2_score(y_test,y_pred): .2f}")
print(f"RMSE: {np.sqrt(mean_squared_error(y_test,y_pred)):.2f}")
print(f"Finished in {T()- start: .2f} seconds")

print("-"*100)
print("Gradient Boosting regression...")
start = T()
reg_gbr.fit(X_train,y_train)
y_pred = reg_gbr.predict(X_test)
print(f"R2: {r2_score(y_test,y_pred): .2f}")
print(f"RMSE: {np.sqrt(mean_squared_error(y_test,y_pred)):.2f}")
print(f"Finished in {T()- start : .2f} seconds")

print("-"*100)
print("XGboost regression...")
start = T()
reg_xgb.fit(X_train,y_train)
y_pred = reg_xgb.predict(X_test)
print(f"R2: {r2_score(y_test,y_pred): .2f}")
print(f"RMSE: {np.sqrt(mean_squared_error(y_test,y_pred)):.2f}")
print(f"Finished in {T()- start : .2f} seconds")