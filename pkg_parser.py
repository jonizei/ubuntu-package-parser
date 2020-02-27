
after_desc = [
    "Original-Maintainer:",
    "Homepage:",
    "\n"
]

def parse(filename):
    file = open(filename, "r")
    content = file.read()

    str_packages = content.split("\n\n")
    packages = []

    for str in str_packages:
        if not str == "":
            packages.append(create_package(str))

    for package in packages:
        print(package)
        print("\n")
    

def create_package(str_pkg):
    package = {}
    lines = str_pkg.split("\n")

    for i in range(len(lines)):
        if lines[i].find("Package:") >= 0:
            package["Package"] = lines[i].split(":")[1].strip()
        elif lines[i].find("Depends:") >= 0:
            package["Depends"] = get_dependencies(lines[i])
        elif lines[i].find("Description:") >= 0:
            package["Description"] = get_description(i, lines)

    return package

def get_description(i, lines):
    description = ""
    for j in range(i, len(lines)):
        if not contains(lines[j], after_desc):
            description += lines[j]

    return description.split(":")[1].strip()

def get_dependencies(str):
    str_dependencies = str.split(":")[1]
    list = str_dependencies.replace("|", ",").split(",")
    dependency_list = []

    for item in list:
        dependency_list.append(item.strip().split(" ")[0])

    return dependency_list
    
                
def contains(str, list):
    does_contain = False

    for item in list:
        if str.find(item) >= 0:
            does_contain = True
            break

    return does_contain


        

