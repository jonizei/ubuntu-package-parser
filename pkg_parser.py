
after_desc = [
    "Original-Maintainer:",
    "Homepage:",
    "\n"
]

def parse(filename):
    str_packages = open(filename, "r").read().split("\n\n")
    package_list = []

    for str in str_packages:
        if not str == "":
            package_list.append(create_package(str))

    for package in package_list:
        package["r_depends"] = get_reverse_dependencies(package, package_list)

    return package_list
    

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

def get_description(i, lines):
    description = ""
    for j in range(i, len(lines)):
        if not contains_str(lines[j], after_desc):
            description += lines[j]

    return description.split(":")[1].strip()

def get_dependencies(str):
    str_dependencies = str.split(":")[1]
    list = str_dependencies.replace("|", ",").split(",")
    dependency_list = []

    for item in list:
        dependency_list.append(item.strip().split(" ")[0])

    return dependency_list

def get_reverse_dependencies(package, package_list):
    dependency_list = []
    for pkg in package_list:
        if "depends" in pkg:
            if package["name"] in pkg["depends"]:
                dependency_list.append(pkg["name"])

    return dependency_list

                
def contains_str(str, list):
    does_contain = False

    for item in list:
        if str.find(item) >= 0:
            does_contain = True
            break

    return does_contain


        

