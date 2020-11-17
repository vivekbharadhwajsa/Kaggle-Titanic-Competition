import matplotlib
import pandas as pd

class Titanic():
    
    def __init__(self):
        self.train_csv = pd.read_csv("train.csv")
        self.test_csv = pd.read_csv("test.csv")
        self.gender_sub = pd.read_csv("gender_submission.csv")
        
    def read_data(self):
        print(self.train_csv.head(5))
        print(self.test_csv.head(5))
        print(self.gender_sub.head(5))

if __name__ == '__main__':

    tit = Titanic()
    tit.read_data()