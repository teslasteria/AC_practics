import json

result_json = [{
       "target": "region1.host1.metric_name1",
                     "datapoints": [[123.2323232,1634083200]],    # value, timestamp
}]

result_data = {
    "timestamp": [],
    "host": [],
    "request_type": [],
    "value": []
}

for i in result_json:
    target_parts = i["target"].split(".")
    host = target_parts[1]
    request_type = target_parts[2]

    for j in i["datapoints"]:
        value, timestamp = j
        result_data["timestamp"].append(timestamp)
        result_data["host"].append(host)
        result_data["request_type"].append(request_type)
        result_data["value"].append(round(value, 3))


print(json.dumps(result_data, indent=4, sort_keys=False))

with open('data.json', 'w', encoding='utf-8') as file:
    json.dump(result_data, file, ensure_ascii=False, indent=4)
