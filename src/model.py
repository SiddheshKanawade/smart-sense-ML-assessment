from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score  

class TestingModels():
    def __init__(self, model):
        self.model=model
    
    def train_test_split(self,features,labels):
        train_data, test_data, train_labels, test_labels = train_test_split(features, labels, test_size=0.2, random_state=42)  
        return train_data, test_data, train_labels, test_labels
    
    def fit(self, train_data, train_labels):
        trained_model=self.model.fit(train_data,train_labels)
        return trained_model
    
    def predict(self, test_data):
        predictions=self.model.predict(test_data)
        return predictions
    
    def evaluate(self, test_labels, predictions):
        score=r2_score(test_labels,predictions)
        return score
    
    