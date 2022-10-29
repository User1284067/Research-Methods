#Write program that gets input and solves for ohms law
#write loop that puts the first six presidents names into a list

var=input("Input V, I, or R to solve for.")

if var.upper()=='V':
    R=float(input("What is the Resistance?"))
    I=float(input("Whaat is the Current"))
    V=I*R
    print('The resistance is '+str(V))
elif var.upper()=='R':
    R=float(input("What is the Voltage?"))
    I=float(input("Whaat is the Current"))
    R=V/I
    print('The resistance is '+str(R))
elif var.upper()=='I':
    R=float(input("What is the Voltage?"))
    I=float(input("Whaat is the Resistance"))
    I=V/R
    print('The resistance is '+str(I)) 
else:
    print("youre an idiot, retry")



presidency_list=[]
presidency_dict={1:"George Washington",2:'John Adams',3:'Thomas Jefferson',4:'James Madison',5:'James Monroe',
6:'John Quincy Adams'}
for i in presidency_dict:
    presidency_list.append(presidency_dict[i])
print(presidency_list)