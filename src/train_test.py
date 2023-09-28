import pandas as pd

from config import TEST_DATA_PATH

class TestData():    
    def get_test_data():
        data=pd.read_csv(TEST_DATA_PATH)
        data.drop(['Type'],axis=1,inplace=True)
        data.drop(['Type','msp_filter'],axis=1,inplace=True)
        data['commodity'] = data['commodity'].apply(lambda x: x.lower() if isinstance(x, str) else x)
        return data
