#Creating a dictionary

onepiece = {'Main_Character' : 'Monkey.D.Luffy', 
'crew_name' : 'Strawhats' , 
'Age' : 19 , 'Power' : 'Rubber powers' , 
'Devil_Fruit' : 'Sun god Nika' ,
 'Specialmoves' : ['gomu-gomu fist','gum-gum pistol']
 }


print(onepiece['Main_Character'])
print('Firstname' in onepiece)
onepiece['Specialmoves'].append('gum-gum gattling')
print(onepiece.items())
keys = onepiece.keys()
print(keys)
print(len(onepiece))