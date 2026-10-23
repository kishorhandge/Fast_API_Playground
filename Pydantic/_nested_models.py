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

# Better organization of related data 
# Reusability: Use Vitals in multiple records
# Readability : Easier for developers and API Consumers to understand
# Validation: Nested model are validated automatically - no exstra work needed