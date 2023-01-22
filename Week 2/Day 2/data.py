import json
dict = {"id":1,"name":"Sudhir","age":24}
print("Writing JSON data in a file  with keys sorted")

with open("data.json","w") as write_file:
    json.dump(dict,write_file,indent=4,sort_keys=True)
print("JSON writing done, please check output file")