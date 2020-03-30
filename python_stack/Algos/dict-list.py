# Update Values in Dictionaries and Lists
students=[
    {
    "firstname": "Reena",
    "city":"Chicago",
    "language":"Java"
},
{
    "firstname": "Tom",
    "city":"Seattle",
    "language":"NodeJS"
}]

def display(students):
    for student in students:
        # print(students[key])
        display_string=""
        for key in student:
            display_string+=f"{key}-{student[key]}, "
        display_string = display_string[:len(display_string)-2]
        print(display_string)
        display_string=""

display(students)

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printinfo(dojo):
    for key in dojo:
        count=0
        print(f"Total {key} are {len(dojo[key])}")
        for itm in dojo[key]:
            count+=1
            print (itm)
       
printinfo(dojo)