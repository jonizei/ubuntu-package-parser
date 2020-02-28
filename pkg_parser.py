
# Strings that are after description
after_desc = [
    "Original-Maintainer:",
    "Homepage:",
    "\n"
]

# Reads given file and split text with empty lines
# Creates package dictionaries from the lines
# Returns list of package dictionaries
def parse(filename):
    str_packages = open(filename, "r").read().split("\n\n")
    package_list = []

    for str in str_packages:
        if not str == "":
            package_list.append(create_package(str))

    for package in package_list:
        package["r_depends"] = get_reverse_dependencies(package, package_list)

    return package_list

# Creates package dictionary    
# Splits text with line breaks
# Finds "Package:" string from text and to dictionary
# Finds "Depends:" string from text and to dictionary
# Finds "Description:" string from text and to dictionary
# Returns package dictionary
def create_package(str_pkg):
    package = {}
    lines = str_pkg.split("\n")

    for i in range(len(lines)):
        if lines[i].find("Package:") >= 0:
            package["name"] = lines[i].split(":")[1].strip()
        elif lines[i].find("Depends:") >= 0:
            package["depends"] = get_dependencies(lines[i])
        elif lines[i].find("Description:") >= 0:
            package["description"] = get_description(i, lines)

    return package

# Gets index of the "Description:" line
# Gets lines after the "Description:" line
# Appends to string if line doesn't contain 
# specific strings
# Removes "Description:" from the string by
# spliting with ':' character
# Returns string
def get_description(i, lines):
    description = ""
    for j in range(i, len(lines)):
        if not contains_str(lines[j], after_desc):
            description += lines[j]

    return description.split(":")[1].strip()

# Removes "Depends:" from the string by
# splitting with ':' character
# Create list of dependencies by splitting
# with '|' or ',' character
# Removes version numbers from dependencies by
# splitting with space
# Appends item to the list
# Returns the list
def get_dependencies(str):
    str_dependencies = str.split(":")[1]
    list = str_dependencies.replace("|", ",").split(",")
    dependency_list = []

    for item in list:
        dependency_list.append(item.strip().split(" ")[0])

    return dependency_list

# Iterates through all the given packages
# and if given package's name appears in
# other package's depends list then it adds
# name of the package to the list
# Returns the list
def get_reverse_dependencies(package, package_list):
    dependency_list = []
    for pkg in package_list:
        if "depends" in pkg:
            if package["name"] in pkg["depends"]:
                dependency_list.append(pkg["name"])

    return dependency_list

# Checks if given string contains any of
# the strings from the given list
# Returns boolean                 
def contains_str(str, list):
    does_contain = False

    for item in list:
        if str.find(item) >= 0:
            does_contain = True
            break

    return does_contain


        

