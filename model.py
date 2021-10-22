
import json

#To load data

def load_data():
    with open("product.json") as f:
        return json.load(f)


#to add data
def save_data():
    with open("product.json",'w') as f:
        return json.dump(db,f)

db=load_data()