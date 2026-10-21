def insert_patient_data(name: str, age: int):

    if type(name) == str and type(age) == int:

        if age < 0 :
            raise ValueError("age cant negative")
        else:

            print(name)
            print(age)
            print("data get inserted into database")

    else:
        raise TypeError("Incorrect datatype")

insert_patient_data("aryan",22)

def update_patient_data(name: str, age: int):

    if type(name) == str and type(age) == int:
        print(name)
        print(age)
        print("data get updated into database")

    else:
        raise TypeError("Incorrect datatype")

update_patient_data("aryan",23)