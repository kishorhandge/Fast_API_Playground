from pydantic import BaseModel,EmailStr, AnyUrl,computed_field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name : str
    age: int
    email : EmailStr         
    linkdin_url: AnyUrl     
    weight : float # kg
    height: float # mtr
    married:  bool 
    allergies: List[str] 
    contact_details: Dict[str,str]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight / (self.height**2),2)
        return bmi

     
def upadte_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.height)
    print(patient.married)
    print(patient.allergies)
    print('BMI',patient.bmi)
    print(patient.contact_details)
    print("data get updated into database") 

patient_info = {'name':'Aryan', 'age': 68,'email' : 'Aryankakade@hdfc.com', 'linkdin_url': 'http://aryan_linkdin.com/2111','weight':70.45,'height':2.5,'married': True,'allergies':{'Dust'},'contact_details':{'address':'Pune','mobile_No': '9156125100','emergency':'8788192823'}}

# if age < 60 then its working but age >= 60 then emergency contact should be provided 

patient1 = Patient(**patient_info)


upadte_patient_data(patient1)


