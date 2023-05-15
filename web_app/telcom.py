import joblib
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
 

rf = joblib.load('randomforest.pkl')

import numpy as np

def telecom_fnc(features_list):
					new_data = pd.DataFrame([features_list], columns=['customerID', 'gender', 'SeniorCitizen', 'Partner', 'Dependents',
					       'tenure', 'PhoneService', 'MultipleLines', 'InternetService',
					       'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport',
					       'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling',
					       'PaymentMethod', 'MonthlyCharges', 'TotalCharges'])
					print(new_data)
					new_data = pd.concat([new_data] * 1000, ignore_index=True)
					print(new_data.head())
					# Apply the same PCA transformation to the new input data
					pca = PCA(n_components=4) # use the same PCA parameters as before
					new_data_transformed = pca.fit_transform(new_data)


					# Make predictions on the transformed data using your trained model
					predictions = rf.predict(new_data_transformed)   
					print(predictions[0])   
					return predictions[0]          
                

