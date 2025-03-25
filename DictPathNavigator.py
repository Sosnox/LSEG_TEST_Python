def passObject(obj, key):
    # Split key to loop value Object
    listkey = key.split("/")
    for i in listkey:
        obj = obj[i]
    return obj

def readFileJson(jsonFile):
    # Read File Json and return Object
    with open(jsonFile, "r") as f:
        jsonFile = f.read()
    return eval(jsonFile)

def main():
    pathData = "data-1.json"
    key = input("Enter key Format like : a/b/c ")
    ObjectList =  readFileJson(pathData)
    result = passObject(ObjectList, key)
    print("Result:", result)

main()
