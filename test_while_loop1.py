counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

counties = ["Arapahoe","Denver","Jefferson"]

for county in counties_dict.keys():
    print(county)

for voters in counties_dict.values():
    print(voters)

for county in counties_dict:
        print(counties_dict[county])

for county in counties_dict:
        print(counties_dict.get(county))

for key, value in counties_dict.items():
    print(key,value)

for county, voters in counties_dict.items():
    print(county, voters)