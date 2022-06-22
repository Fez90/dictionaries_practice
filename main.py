person_0 = {
    'first_name': 'john',
    'last_name': 'evans',
    'age': '37',
    'city': 'new york',
    'job' : 'software genius',
    'salary' : '378 000$',
    'job experience' : '5 years',
}
print(person_0)
print(person_0['first_name'].title())
del person_0['first_name']
print(person_0)
person_0['first_name'] = 'chris'
print(person_0)
for k,v in person_0.items():
    print(f"\nKeys: {k}")
    print(f"{v}")
rivers_countries = {
    'nile' : 'Egypt',
    'missisipi' : 'USA',
    'hudson' : 'USA',
    }
for river,country in rivers_countries.items():
    print(f"The {river.title()} runs through {country.title()}")
print("Rivers list are:")
for river in rivers_countries.keys():
    print(river.title())
print("Countries list are:")
for country in set(rivers_countries.values()):
    print(country.title())
team_members = {
    'brad' : 'Python',
    'jerry' : 'C++',
    'Jess' : 'Ruby',
    }
other_members = {
    'luke' : 'Java',
    'sara' : 'Python',
    }
for name in team_members.keys():
    print(f"Hi {name.title()}, thank you for joining our club")
for member in other_members.keys():
    if member  not in team_members.keys():
        print(f"{member.title()} please join our class\n")
person_1 = {
    'first_name' : 'luke',
    'last_name' : 'hardy',
    'age' : '36',
    'city' : 'Boston'
    }
person_2 = {
    'first_name' : 'tom',
    'last_name' : 'larry',
    'age' : '35',
    'city' : 'san francisco'
    }
people = [person_0,person_1,person_2]
for person in people:
    print(f"\n{person}")

pet_0 = {
    'animal' : 'dog',
    'owner' : 'jessica',
    }
pet_1 = {
    'animal' : 'cat',
    'owner' : 'liza',
    }
pets = [pet_0,pet_1]
for pet in pets:
    print(pet)

favorite_places = {
    'canada' : 'louis', 
    'new zealand' : 'john',
    'iceland' : 'kimberly',
    }
for k,v in favorite_places.items():
    print(f"\t{v.title()} wants to visit {k.title()}\n")

favorite_numbers = {
    'p_1' : ['1','2'],
    'p_2' : ['2','3'],
    'p_3' : ['3','4'],
    'p_4' : ['4','5'],
    }
for k,v in favorite_numbers.items():
    print(f"\tPerson {k.title()}:")
    print(f"\tNumber{v}")

cities = {
    'new_york' : {
        'country' : 'USA',
        'population' : '8 mln',
        'fact' : 'Empire state'
        },
    'dc_washington' : {
        'country' : 'USA',
        'population' : '3 mln',
        'fact' : 'capital of US',
        },
    'boston' : {
        'country' : 'USA',
        'population' : '5 mln',
        'fact' : 'famous see food'
        } 
}
for cityname,city_info in cities.items():
    print(f"\nCity: {cityname}")
    population = city_info['population']
    print(f"Population of the city {population}")
    fact = city_info['fact']
    print(f"Fact about city: {fact}")