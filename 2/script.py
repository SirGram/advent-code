with open("C:/Users/PC/Desktop/adventcode/2/a.txt", 'r') as data_file:
    stringData = data_file.read().splitlines() 
    


numberChars = {"sevenine":"79", "eighthree":"83","eightwo":"82", "zerone":"01", "oneight":"18", "twone":"21","threeight":"38", "fiveight":"58", "nineight":"98" ,"zero":"0","one":"1","two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9",}
validData = ["0","1","2","3","4","5","6","7","8","9"]
newStringData=[]

for index, string in enumerate(stringData):
    for key, value in numberChars.items():
        string = string.replace(key, value)
    stringData[index] = string

                
for index, string in enumerate(stringData):
    for char in string:
        if char not in validData:            
            string=string.replace(char, "")
    newStringData.append(string)



for index, string in enumerate(newStringData):
    if len(string)>2:
        newString = string[0] + string[-1]
        newStringData[index]= newString
    elif len(string)==1:
        newString = string[0] + string[0]        
        newStringData[index]= newString
sum=0
print(newStringData)
for string in newStringData:
    sum+= int(string)
     
print(sum)

numbers = [
    "zero",
     "one",
    "two",
    "three",
     "four",
    "five",
   "six",
    "seven",
    "eight",
   "nine",
]


for number in numbers:
    firstDigit = number
    for number2 in numbers:
        secondDigit = number2
        if firstDigit[-1] == secondDigit[0]:
            print (firstDigit,secondDigit)

