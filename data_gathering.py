from data import search
import json

data = search("sneakers")

#format of the json file
d = {
    "sneakers" : data
}


with open ("data_gathered.json", "w") as output: 
    json.dump(d, output)