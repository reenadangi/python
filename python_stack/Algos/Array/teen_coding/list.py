
cars=["BMW","Audie","BMW","BMW8.5","Audie8","Lexus9","BMW","Audie8","Lexus9"]

print(cars[5])
# last value in list
print(cars[-1])
print(cars[-2])
print(cars[-9])
# start:end
print(cars[0:5])
# given index:end of the list
print(cars[2:])
print(cars[2:6])

len_cars=len(cars)



b="BMW"
count=0
# i=0 cars[i]="BMW" count=1 
# i=1 cars[i]="Audie" count=1 
# i=2 cars[i]="BMW" count=2 
for i in range(0,len_cars): 
    if cars[i]=="BMW":
        count=count+1
print(f"Total BMW's in my list are {count}")
   

















