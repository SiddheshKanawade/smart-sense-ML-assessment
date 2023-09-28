import pandas as pd
from sklearn.preprocessing import OneHotEncoder 
from sklearn.preprocessing import MinMaxScaler  

from config import DATASET_PATH

class DataProcesser:
    
    def get_data(self, path):
        return pd.read_csv(path)


    def data_sanitation(self, data):
        data.drop(['min_price','max_price','district_name','state_name','date'],axis=1,inplace=True)
        data=data.dropna()
        return data

    def one_hot_encoding(self,data): 
        data = pd.get_dummies(data, columns=['APMC',"Commodity","Month"], prefix = ['APMC',"commodity","month"])
        return data

    def get_features(self,data):
        features=data.loc[:, data.columns !='modal_price']
        return features

    def get_labels(self,data):
        labels=data['modal_price']
        return labels

    def scaling_data(self,features):
        scaler=MinMaxScaler()
        features=scaler.fit_transform(features)
        return features

    def data_preprocessing(self):
        data=DataProcesser.get_data(self, DATASET_PATH)
        data=DataProcesser.data_sanitation(self, data)
        data=DataProcesser.one_hot_encoding(self, data)
        features=DataProcesser.get_features(self, data)
        labels=DataProcesser.get_labels(self, data)
        features=DataProcesser.scaling_data(self, features)

        return features,labels
        