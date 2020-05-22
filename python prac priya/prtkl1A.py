def inputnumber(message):
    while True:
        try:
            uerinput=int(input(message))
        except ValueError:
            print("not an integer try again")
            continue
        else:
            return userinput
            break
age=inputnumber("how old are you")
if(age>=18):
    print("you are old enough to vote")
else:
    print("you will be able to vote in"+str(18-age)+"year")
