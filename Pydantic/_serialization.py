from pydantic import BaseModel


class Address(BaseModel):
    city: str
    state: str
    pin: str

class Patient(BaseModel):
    name: str
    gender: str
    age: int
    address : Address

address_dict = {'city':'Nashik','state':'MH','pin': '422210'}

address1 = Address(**address_dict)

Patient_dict = {'name':'Aryan','gender':'male','age':22,'address':address1}

Patient1 = Patient(**Patient_dict)

print(Patient1)
print(Patient1.name)
print(Patient1.address.city)
print(Patient1.address.pin)

Temp1 = Patient1.model_dump()

# If i want to include something or exclude
Temp1 = Patient1.model_dump(include=['name', 'gender'])
Temp1 = Patient1.model_dump(exclude={'address':['state']})

Temp2 = Patient1.model_dump_json()

print(Temp1)
print(type(Temp1))

print(Temp2)
print(type(Temp2))

# Better organization of related data 
# Reusability: Use Vitals in multiple records
# Readability : Easier for developers and API Consumers to understand
# Validation: Nested model are validated automatically - no exstra work needed