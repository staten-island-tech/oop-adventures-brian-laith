import json
import random

test = open("data.json", encoding="utf8")
data = json.load(test)

testList = []
testList.append(data[2]['hp'])
print(testList)