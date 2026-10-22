from pydantic import BaseModel,EmailStr, AnyUrl, Field, field_validator
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

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):

        valid_domain = ['hdfc.com','icici.com']

        # ABC@gmail.com

        domain_name = value.split('@')[-1]

        if domain_name not in valid_domain:
            raise ValueError('Not a valid domain')

        return value

    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.upper()

    
    @field_validator('age' ,mode='before') # mode='after' its by default 
    @classmethod
    def  validate_age(cls, value):

        if 0 < value < 100:
            return value

        else:
            raise ValueError('age should be in between 0 and 100')
    
def upadte_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print("data get updated into database") 

patient_info = {'name':'Aryan', 'age': 22,'email' : 'Aryankakade@hdfc.com', 'linkdin_url': 'http://aryan_linkdin.com/2111','weight':70.45,'married': True,'allergies':{'Dust'},'contact_details':{'address':'Pune','mobile_No': '9156125100'}}

# For normal Aryankakade@gmail.com it should not work <====> but for Aryankakade@hdfc.com it should work

patient1 = Patient(**patient_info)


upadte_patient_data(patient1)


