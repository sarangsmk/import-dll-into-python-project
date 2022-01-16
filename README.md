# import-dll-into-python-project
Importing a custom dll built with C# into a Python Project and access the functions inside the dll with the help of [pythonnet](https://pypi.org/project/pythonnet/).

### Project Structure
* dll Project - Contains the C# Solution for the custom dll <br>
* Python Project - The Python project folder

### Dll Code
```C#
namespace CalcProject
{
    public class calculate
    {
        /// <summary>
        /// Simple Helper to add 2 Numbers and return the result
        /// </summary>
        /// <param name="a">Number 1</param>
        /// <param name="b">Number 2</param>
        /// <returns>Sum of 2 Numbers</returns>
        public int Add(int a, int b)
        {
            return a + b;
        }
    }
}
```

### Python Code
```python
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
```
