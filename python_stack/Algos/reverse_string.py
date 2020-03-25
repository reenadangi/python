def reverse(str):
     final_string=""
     s=str.split()
     print (s)
     for string in s:
        final_string += string[::-1] + " "
     print(final_string)
            
        
             

         
   
reverse("hello world is going crazy")