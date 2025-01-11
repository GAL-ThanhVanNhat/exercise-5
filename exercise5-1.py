from Doctor import Doctor;

#newDoctor = Doctor("Napoleon", "Doe", 100000, "123 Main St")
#id = newDoctor.insert()
#print(f"Doctor ID: {id}")

doctors = Doctor.get_all()
for doctor in doctors:
    print(doctor.__repr__())
    
secondDoctor: Doctor = doctors[1]
secondDoctorId: int = secondDoctor[0]

Doctor.update_doctor_first_lastname(secondDoctorId, "test", "demo")
Doctor.update_doctor_salary(secondDoctorId, 200000)
Doctor.update_doctor_address(secondDoctorId, "456 Main St")
print(secondDoctor.__repr__())

dbSecondDoctor = Doctor.get_doctor_by_id(secondDoctorId)
print(dbSecondDoctor.__repr__())


