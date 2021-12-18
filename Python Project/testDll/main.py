import clr

# Add Reference to the library/dll
# Option -1 :Add the dll into project folder
clr.AddReference("dlls/CalcProject")

# Option -2: Add the dll path into the system path
# dll_path = r"C:\SMK\Desktop\test\CalcTest\CalcTest\bin\Debug"
# import sys
# sys.path.append(assembly_path)

# From NameSpace_Name import class_Name
from CalcProject import calculate

# Create object of the Class
obj = calculate()

# Call the function with class object (The function from dll that you want to access)
print(obj.Add(1, 2))