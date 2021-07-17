name1 = "line"
name2 = "longline"
name3 = "biglongline"
street = [name1, name2]
street.append(name3)
print(street)
victim = street[-1]
print(victim)
street[0] = "newline"
print(street)
street[-1] = "verybiglongline"
print(street)
contact = ("+380970979665", "name1")
print(contact[1])
print(type(street), type(contact))
print(dir(street))
print(dir(contact))