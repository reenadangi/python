# print all the values 
x = [ [5,2,3], [10,8,9] ]
for val in x:
    for value in val:
        print (value)

# print values in dict
students = [{'fname':'Reena','lname':'Dangi'},
            {'fname':'Aryana','lname':'Grande'},
            {'fname':'Nick', 'lname':'Jonas'}
            ]
for student in students:
    print (student['fname'],student['lname']) 
    print (student.keys())
   
def iterate_dictionary(some_list):
  for curr_dict in some_list:
    display_str = ''
    for curr_key in curr_dict.keys():
      display_str += f"{curr_key} - {curr_dict[curr_key]}, "
    # remove comma and extra space from display_str
    display_str = display_str[:len(display_str) - 2]
    print (display_str)


iterate_dictionary(students)

# # Create a function printInfo(some_dict) 
# that given a dictionary whose values are all lists, 
# prints the name of each key along with the size of its list,
#  and then prints the associated values within each key's list. 
# For example:

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def print_dojo(dojo):
  for key in dojo.keys():
    print(len(dojo[key]))
    for item in dojo[key]:
      print(item) 
 

    # print (len(dojo[key]))

print_dojo(dojo)

# ****************** Given a Dictionary. The task is to print the dictionary in the table format.
def print_users(users):
  print(f"NAME AGE COURSE")
  for key,value in users.items():
       name, age, course = value 
       print (f"{key}: {name}, {age}, {course}")
       
def print_usersII(users):
  for key in users.keys():
    print(f"{users[key][0]} {users[key][1]} {users[key][2]} ")
    # for item in users[key]:
    #   print (item)
dojo_users = {
1: ["Samuel", 21, "Data Structures"],
2: ["Richie", 20, "Machine Learning"],
3: ["Lauren", 21, "OOPS with java"],
}
print_users(dojo_users)
print_usersII(dojo_users)