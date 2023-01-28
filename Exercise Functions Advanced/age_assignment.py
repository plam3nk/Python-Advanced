def age_assignment(*args, **kwargs):
    names_ages = {}
    for name in args:
        for k, v in kwargs.items():
            if k == name[0]:
                names_ages[name] = v
    sorted_data = sorted(names_ages.items())
    return "\n".join([f"{key} is {value} years old." for key, value in sorted_data])


print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))