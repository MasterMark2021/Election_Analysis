from types import prepare_class


Introduction = ["P N Okeke wrote Physics"]
Another = ["His wife also a Physics Professor"]
print(Introduction +  Another)
print(Another)




countries_dict = {}
print(countries_dict)
counties = ["Arapahoe","Denver","Jefferson"]
countries_dict ["Arapahoe"] = 422829
countries_dict ["Denver"] = 463353
countries_dict ["Jefferson"] = 432438
print(countries_dict)
len(countries_dict)
print(len(countries_dict))
voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
print(voting_data)


counties = ["Arapahoe","Denver","Jefferson"]
if counties[0] =='Arapahoe':
    print(counties[0])


    counties = ["Arapahoe","Denver","Jefferson"] 
    if "England" in counties: print("True") 
    else: print("False")



if "Arapahoe" in counties and "El Paso" not in counties:
   print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")




voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)
