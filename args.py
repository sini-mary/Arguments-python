def hello(*names):
    for name in names:print({name})
    
    
def student_attribute(**kwargs):
    for key,value in kwargs.items():
        print("{key}:{value}")


# default arguments
def my_country(country="Burundi"):
    print(f"my country is {country}")
     

 # A function named concatenate_args that takes any number of string arguments in positional arguments
 # format and concatenates them into a single string 
def concatenate_args(*string):
    answer= " "
    for s in string:
        answer+=s
    return answer

#A function named concatenate_kwargs that takes any number of string arguments in keyword arguments  
# format and concatenates them into a single string
def concatenate_kwargs(**string):
    empty= ""
    for key, value in string.items():
        empty+=(f"{key}{value}")
    return empty
    
    

        