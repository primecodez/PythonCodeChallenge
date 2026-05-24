import json
data = '{"city": "Ahmedabad", "state": "Gujarat"}'

result = json.loads(data)
print(result)
print(result["city"])