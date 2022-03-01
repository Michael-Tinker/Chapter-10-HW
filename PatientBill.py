#write a program that will create a patient instances as shown below:
#Patient ID | Name | Address | Phone | Veteran Status
#1 | Matt Jones | 123 Main St., Waco, Tx 76706 | 254-444-4444 | TRUE

import PatientClass as pc
import ProcedureClass as dr

def main():
    #Initializing the patient class
    generic_patient = pc.Patient(1, "Matt Jones", "123 Main St., Waco, Tx 76706", "254-555-7415", True)

    #Initializing three instances of the procedure class
    procedure_exam = dr.Procedure("Physical Exam", "2/15/2022", "Dr. Irvine", 250, 1)
    procedure_mri = dr.Procedure("MRI", "2/15/2022", "Dr. Hamilton", 1500, 1)
    procedure_ct = dr.Procedure("CT Scan", "2/17/2022", "Dr. Drey", 1200, 2)

    print("*** Patient Bill ***")
    print("Name:", generic_patient.get_name())
    print("Address:", generic_patient.get_address())
    print("Phone:", generic_patient.get_phone())
    print()
    
    total_cost = 0
    procedure_list = [procedure_exam, procedure_mri, procedure_ct]
    for procedure in procedure_list:
        if procedure.get_patient_id() == generic_patient.get_id():
            print("Procedure:", procedure.get_name())
            print("Date:", procedure.get_date())
            print("Practitioner:", procedure.get_practitioner())
            print("Charge:", procedure.get_charge())
            total_cost += procedure.get_charge()
            print()
    
    if generic_patient.get_veteran_status() == True:
        total_cost = total_cost * .6

    total_cost_format = format(total_cost, ",")
    print("Total Charges: $" + str(total_cost_format))

main()