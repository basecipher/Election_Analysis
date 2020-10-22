x = 3
while x <= 5:
    print(x)
    x = x + 1

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]


for i in range(len(voting_data)):

      print(voting_data[i])

#Nested for loop

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

for county_dict in voting_data:

     print(county_dict['registered_voters'])

for county_dict in voting_data:

     print(county_dict['county'])

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)