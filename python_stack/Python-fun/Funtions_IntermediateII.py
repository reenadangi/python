# Assignment: Functions Intermediate II
x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x[1][0]=15
print(x)

# Change the last_name of the first student from 'Jordan' to 'Bryant'
dict(name="John", age=36)
students[0]["last_name"]="Bryant"
print(students)

# In the sports_directory, change 'Messi' to 'Andres' ????????
sports_directory['soccer'][0]="Andres"
print(f"Sports :{sports_directory}")

# print(sports_directory[{0}])

# Change the value 20 in z to 30
z[0]["y"]=30
print(z)


def iterateDictionary1(students):
    for itm in students:
        # first_name -Michael, last_name - Jordan
        str=""
        for key in itm.keys():
            #  display_str = display_str[:len(display_str) - 2]
            # print(f"{key}-{itm[key]},",end =" ")
            str+=f"{key}-{itm[key]}, "
           
            # print(f"{key}-{itm[key]}")
        print(str[:-1])    
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterateDictionary1(students)

# Create a function iterateDictionary(some_list) that,
#  given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value. For example, given the following list:
def iterateDictionary2(last_name,students):
    for itm in students:
        for key in itm.keys():
            if(key==last_name):
                print(key, itm[key])


iterateDictionary2("last_name",students)

# Iterate Through a Dictionary with List Values
# Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size 
# of its list, and then prints the associated values within each key's list.
def iterateDictionary3(students):
    for key in students.keys():
        keycount=len(students[key])
        print (f"Items in {key} are {keycount}")
        for itm in students[key]:
            keycount=keycount+1
            print(itm)
           
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
iterateDictionary3(dojo)