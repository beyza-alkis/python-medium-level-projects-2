from json import loads, dumps

data = '{"firstName":"Ethan" , "lastName":"Hunt"}'
y = loads(data)

print(y["firstName"])
print(y["lastName"])

customer = {
        "firstName":"Ethan"
}

customerJson = dumps(customer)

