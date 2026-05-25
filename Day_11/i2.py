import json
data = '{"City": "Ahmedabad", "State": "Gujarat"}'

result = json.loads(data)
print(result)
print(result["City"])