import math
#set constants for meat, bread variables
packhotdogmeat = 10
packbuns = 8

#prompt user to enter how many ppl are attending
numpplattending = int(input("How many people are attending this cookout?: \n"))

#prompt user to enter how many hotdogs each person is eating
numhotdogsperperson = int(input("How many hot dogs will each person have?: \n"))

#calc the total hotdogs required by multiplying people attending by how many hotdogs
#each person is eating
total_hotdogs_required = (numpplattending*numhotdogsperperson)

#print statements, using f strings, indicate how many are required
print(f"You will need {total_hotdogs_required} hot dogs total")

#rounding up, how mayn hotdogs are required
packtotal_hotdogmeat_required = math.ceil(total_hotdogs_required/packhotdogmeat)
print(f"You will need {packtotal_hotdogmeat_required} packages of hotdogs")

#rounding up, how many buns are required
packbuns_required = math.ceil(total_hotdogs_required/packbuns)
print(f"You will need {packbuns_required} packages of buns")

#leftover meat=however many is purchased minus how many is used
hotdogs_leftover = (packtotal_hotdogmeat_required*packhotdogmeat)-total_hotdogs_required
print(f"You will have {hotdogs_leftover} hot dogs left over")
#leftover buns=however many is purchased minus how many is used
buns_leftover = (packbuns_required*packbuns)-total_hotdogs_required
print(f"You will have {buns_leftover} buns left over")


