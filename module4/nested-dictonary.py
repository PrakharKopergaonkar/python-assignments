people = {1:{'name':'john','age':'27','sex':'male'}, 2:{'name':'marie', 'age':'22', 'sex':'female'}}

print(people)
print(people[1]['name'])
print(people[1]['age'])
print(people[1]['sex'])
print(people[1])

people[3] = {}
people[3]['name'] = 'Luna'
people[3]['age'] = 'female'
people[3]['married'] = 'no'

people[4] = {'name':'jhon','age':'21','sex':'male', 'married':'yes'}

del people[3]['married']
del people[4]['married']
print(people[3])
print(people[4])

del people[3]
del people[4]
print(people)

for p_id, p_info in people.items():
    print("\nperson id:",p_id)
    for key in p_info:
        print(key + ':', p_info[key])
