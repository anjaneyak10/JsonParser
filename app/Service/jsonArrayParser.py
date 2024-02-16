from app import app

from app.Service.parsingService import jsonParser


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
