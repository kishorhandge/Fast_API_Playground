from pydantic import BaseModel,EmailStr, AnyUrl, Field  
from typing import List, Dict, Optional, Annotated

###################################################################################
# 
#   Using Filed, Annotated we can add metadata
#   Field => this function is also used to attach metadata
#   Using filed we are doing=> Custom data validation, metadata, default value
#
#
#
#
#
###################################################################################

class Patient(BaseModel):
    name : Annotated[str, Field(max_length=50, title='Name of Patient',description='Give the name of patient in 50 character',examples=['Aryan','Kishor'])]
    age: int
    email : EmailStr        #for data validation
    linkdin_url: AnyUrl     #for data validation
    weight : float = Field(gt=0, lt=120) # Use Cases
    married: Annotated[bool, Field(default=None,  description='Is the patient married or not')]
    allergies: Optional[List[str]] = None
    contact_details: Dict[str,str]

def insert_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print("data get inserted into database") 

patient_info = {'name':'Aryan', 'age': 22,'email' : 'Aryankakade@gmail.com', 'linkdin_url': 'http://aryan_linkdin.com/2111','weight':70.45,'married': True,'allergies':{'Dust'},'contact_details':{'address':'Pune','mobile_No': '9156125100'}}

patient1 = Patient(**patient_info)


insert_patient_data(patient1)


