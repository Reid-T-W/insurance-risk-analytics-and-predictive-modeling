import pandas as pd

def convert_txt_to_csv():
    # Load data from txt
    print("Starting data conversion")
    df = pd.read_csv("../data/raw/MachineLearningRating_v3.txt", delimiter="|")
    df.to_csv("../data/raw/MachineLearningRating_v3_csv.csv", index=False)
    print("Conversation from txt to csv successful")
        
if __name__ == "__main__":
    convert_txt_to_csv()