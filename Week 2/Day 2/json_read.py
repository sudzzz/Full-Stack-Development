import json
data_dictonary = {"key1":"Value1","key2":"Value2","key3":"Value3"}

json_data = json.dumps(data_dictonary)
print(json_data)

read_json_data = json.loads(json_data)
print(read_json_data["key2"])