CONNECTION_STRING = "C:\\Users\\Thanh NVan\\Desktop\\MSE\\1st-sem\\pythons\\exercise-5\\exercise-5-1.db"
INSERT_DOCTOR_QUERY = "INSERT INTO doctor (firstName, lastName, joiningDate, salary, address) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}')"
SELECT_SINGLE_DOCTOR_QUERY = "SELECT * FROM doctor WHERE id = {0}"
SELECT_ALL_DOCTORS_QUERY = "SELECT * FROM doctor"
UPDATE_DOCTOR_FIRST_LASTNAME_QUERY = "UPDATE doctor SET firstName = '{0}', lastName = '{1}' WHERE id = {2}"
UPDATE_DOCTOR_SALARY_QUERY = "UPDATE doctor SET salary = '{0}' WHERE id = {1}"
UPDATE_DOCTOR_ADDRESS_QUERY = "UPDATE doctor SET address = '{0}' WHERE id = {1}"
DELETE_DOCTOR_ADDRESS_QUERY = "DELETE FROM doctor WHERE id = {0}"
