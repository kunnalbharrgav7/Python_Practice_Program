# class employee:
#     no_of_leaves = 20
#     pass

# harry = employee()
# rohan = employee()

# harry.name = "harry"
# harry.salary = 234
# harry.role = "instructor"

# rohan.name = "rohan"
# rohan.salary = 999
# rohan.role = "student"

# print(rohan.name)
# print(rohan.no_of_leaves)
# print(harry.no_of_leaves)
# print(employee.no_of_leaves)

# employee.no_of_leaves=10
# print(employee.no_of_leaves)

# rohan.no_of_leaves=9
# print(rohan.__dict__)









class employee:
    no_of_leaves = 20
    
    def printdetails(self):
        return f"name is {self.name} . salary is {self.salary} and role is {self.role}"

harry = employee()
rohan = employee()

harry.name = "harry"
harry.salary = 234
harry.role = "instructor"

rohan.name = "rohan"
rohan.salary = 999
rohan.role = "student"

print(rohan.name)
print(rohan.no_of_leaves)
print(harry.no_of_leaves)
print(employee.no_of_leaves)

employee.no_of_leaves=10
print(employee.no_of_leaves)

rohan.no_of_leaves=9
print(rohan.__dict__)

print(rohan.printdetails())