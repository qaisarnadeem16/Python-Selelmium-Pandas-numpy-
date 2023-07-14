#File create, open and read
file_name = "harry.txt"
data = "Hi, I'm Harry"
with open(file_name, "w") as file:
    file.write(data)
with open(file_name, "r") as file:
    content = file.read()
print("File contents:", content)


#To find the list of modules in my laptop
import pkgutil
modules = list(pkgutil.iter_modules())
module_names = [module.name for module in modules]
print(module_names)

#Random Module
import random
random_number = random.randint(0, 10)
print("Random number:", random_number)
random_float = random.random()
print("Random float:", random_float)
persons = ["Harry", "Patrick", "Tyler"]
random_pers = random.choice(persons)
print("Random Persons:", random_pers)


#Time Module
import time
current_time = time.time()
print("Current time:", current_time)

print("Pausing for 2 seconds...")
time.sleep(2)
print("Resuming after 2 seconds")

formatted_time = time.ctime(current_time)
print("Formatted time:", formatted_time)

start_time = time.time()
end_time = time.time()

execution_time = end_time - start_time
print("Execution time:", execution_time, "seconds")