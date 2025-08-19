def check_age_category(age):
    if age < 18:
        return "Minor"
    elif 18 <= age < 60:
        return "Adult"
    elif age >= 60:
        return "Senior Citizen"
    else:
        return "Invalid age"
print(check_age_category(15))   
print(check_age_category(30))   
print(check_age_category(65))  
