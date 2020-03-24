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
   for item in key:
     print (item)

    # print (len(dojo[key]))

print_dojo(dojo)