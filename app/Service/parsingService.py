from app import app


def jsonParser(jsonString):
    jsonString= check_json(jsonString)
    if jsonString == "Invalid JSON":
        return "Invalid JSON"
    dic={}
    i =0
    while i < len(jsonString):
        while i<len(jsonString) and jsonString[i] != '"':
            i+=1
        if i==len(jsonString):
            break
        if jsonString[i] == '"':
            i+=1
            key = ""
            while jsonString[i] != '"':
                key+=jsonString[i]
                i+=1
            i+=1
            if jsonString[i] != ':':
                return "Invalid JSON"
            i+=1
            value = ""
            if jsonString[i]=="{":
                while jsonString[i] != "}":
                    value+=jsonString[i]
                    i+=1
                value+=jsonString[i]
                value=jsonParser(value)
            elif jsonString[i] == '"':
                i+=1
                while jsonString[i] != '"':
                    value+=jsonString[i]
                    i+=1
            elif jsonString[i] == "[":
                i+=1
                x="["
                while jsonString[i] != "]":
                    x+=jsonString[i]
                    i+=1
                x+=jsonString[i]
                i+=1
                value=jsonArrayParser(x)
            else:
                while i<len(jsonString) and jsonString[i] != ',':
                    value+=jsonString[i]
                    i+=1
                if value.isdigit():
                    value = int(value)
                elif value == "true":
                    value = True
                elif value == "false":
                    value = False
                elif value == "null":
                    value = None
                elif isFloat(value):
                    value = float(value)
            dic[key]=value
    return dic

def isFloat(s):
    try:
        float_val = float(s)
        return True
    except ValueError:
        return False

def check_json(jsonString):
    jsonString=jsonString.strip()
    if jsonString[0] == '{' and jsonString[-1] == '}':
        return jsonString[1:-1]
    else:
        return "Invalid JSON"

def jsonArrayParser(arrayString):
    if arrayString[0]!='[' or arrayString[-1]!=']':
        return "Invalid String"
    else:
        arrayString=arrayString[1:-1]
        arr = []
        arrayString=arrayParser(arrayString)
        for i in arrayString:
            arr.append(jsonParser(i))
    return arr

def arrayParser(jsonString):
    i = 0
    ans = []
    while i <len(jsonString):
        while jsonString[i]!='{':
            i+=1
        stack=[]
        stack.append(jsonString[i])
        x=jsonString[i]
        i+=1
        while i<len(jsonString) and stack:
            if jsonString[i]=="{":
                stack.append(jsonString[i])
            elif jsonString[i]=="}":
                stack.pop()
            x+=jsonString[i]
            i+=1
        if stack and i ==len(jsonString):
            return "Invalid Input"
        ans.append(x)
    return ans
