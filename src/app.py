from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import GradientBoostingRegressor  

from datapreprocessing import DataProcesser
from model import TestingModels

# Data Preprocessing
processor = DataProcesser()
features, labels=processor.data_preprocessing()

# Model Training
decision_tree=DecisionTreeRegressor()
gradient_boosting=GradientBoostingRegressor()
models=[decision_tree, gradient_boosting]

for model in models:
    model_parser=TestingModels(model)
    train_data, test_data, train_labels, test_labels=model_parser.train_test_split(features, labels)
    trained_model=model_parser.fit(train_data, train_labels)
    predictions=model_parser.predict(test_data)
    score=model_parser.evaluate(test_labels, predictions)
    print(f"Model: {model} \nScore: {score} \n\n")