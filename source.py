ip=str(input("Enter the IP Address :-  "))
l=list(ip.split(sep="."))
first=int(l[0])
if 0 <= first <= 127 :
    print("Class - A")
    print("Network ID - ",first)
    print("Host ID - ",str(l[1]) + str(".") + str(l[2]) + str(".") + str(l[3]))
elif 128 <= first <= 191 :
    print("Class - B")
    print("Network ID - ",str(first) +str(".") + str(l[1]))
    print("Host ID - ",str(l[2]) + str(".") + str(l[3]))

elif 192 <= first <= 223 :
    print("Class - C")
    print("Network ID - ",str(first) +str(".") + str(l[1])+str(".") + str(l[2]))
    print("Host ID - ",str(l[3]))

elif 224 <= first <= 239 :
     print("Class - D\nMulticast Address")

elif 240 <= first <= 255 :
    print("Class - E\nReserved")
else :
    print("Error !!!\nPlease Enter the IP in correct format")
