#write a class named Procedure that represents a medical procedure 
#that has been performed on a patient. The Procedure class should have the 
#following attributes - Name of the procedure, Date of the procedure, 
#Name of the practitioner who performed the procedure, Charges for the 
#procedure and patient ID. The Procedure class’s __init__ method should 
#accept an argument for each attribute. The Procedure class should have 
#accessor methods only for each attribute.

#Three Instances Need to be initialized with the following data

#name | date | practitioner | charge | patient_id
#Physical Exam| 2/15/2022 | Dr. Irvine | 250 | 1
#MRI | 2/15/2022 | Dr. Hamilton | 1500 | 1
#CT Scan | 2/17/2022 | Dr. Drey | 1200 | 2

class Procedure:

    def __init__(self, name, date, practitioner, charge, patient_id):
        self.__name = name
        self.__date = date
        self.__practitioner = practitioner
        self.__charge = charge
        self.__patient_id = patient_id

    def get_name(self):
        return self.__name

    def get_date(self):
        return self.__date

    def get_practitioner(self):
        return self.__practitioner

    def get_charge(self):
        return self.__charge

    def get_patient_id(self):
        return self.__patient_id