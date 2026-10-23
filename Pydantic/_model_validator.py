from pydantic import BaseModel,EmailStr, AnyUrl,model_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name : str
    age: int
    email : EmailStr         
    linkdin_url: AnyUrl     
    weight : float 
    married:  bool 
    allergies: List[str] 
    contact_details: Dict[str,str]


    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError('Patient older than 60 must have emergency contact')
        else:
            return model
     
def upadte_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print("data get updated into database") 

patient_info = {'name':'Aryan', 'age': 68,'email' : 'Aryankakade@hdfc.com', 'linkdin_url': 'http://aryan_linkdin.com/2111','weight':70.45,'married': True,'allergies':{'Dust'},'contact_details':{'address':'Pune','mobile_No': '9156125100','emergency':'8788192823'}}

# if age < 60 then its working but age >= 60 then emergency contact should be provided 

patient1 = Patient(**patient_info)


upadte_patient_data(patient1)


