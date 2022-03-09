from random import randint
import numpy


# apply an function
def keygen():
    a = randint(1,10)
    b = a**3
    return [a,b]

# Arithmetic Curcuit 
def arth_cir(a,b):
    sym1 = a*a
    sym2 = a+b
    out = sym2 + 5
    return [sym1,sym2,out]

def mapping(a,b):
    [sym1, sym2, out] = arth_cir(a,b)
    return[1, a, out, sym1, b, sym2]

# R1CS
def verify_1(a,b):
    key = mapping(a,b)
    t = [1,key[1],0,key[3],0,0]
    v = [0,1,0,0,0,0]
    w = [0,1,0,0,0,0]
    k = [0,0,0,1,0,0]
    if numpy.dot(t,v) * numpy.dot(t,w) - numpy.dot(t,k) == 0:
        return verify_2(a,b)
    else:
        return False

def verify_2(a,b):
    key = mapping(a,b)
    t = [1,key[1],0,key[3],key[4],0]
    v = [0,0,0,1,0,0]
    w = [0,1,0,0,0,0]
    k = [0,0,0,0,1,0]
    if numpy.dot(t,v) * numpy.dot(t,w) - numpy.dot(t,k) == 0:
        return verify_3(a,b)
    else:
        return False

def verify_3(a,b):
    key = mapping(a,b)
    t = [1,key[1],0,key[3],key[4],key[5]]
    v = [0,1,0,0,1,0]
    w = [1,0,0,0,0,0]
    k = [0,0,0,0,0,1]
    if numpy.dot(t,v) * numpy.dot(t,w) - numpy.dot(t,k) == 0:
        return verify_4(a,b)
    else:
        return False

def verify_4(a,b):
    key = mapping(a,b)
    t = [1,key[1],key[2],key[3],key[4],key[5]]
    v = [5,0,0,0,0,1]
    w = [1,0,0,0,0,0]
    k = [0,0,1,0,0,0]
    if numpy.dot(t,v) * numpy.dot(t,w) - numpy.dot(t,k) == 0:
        return True
    else:
        return False

def verification(a,b):
    return verify_1(a,b)
    
if __name__ == "__main__":
    [x,y] = keygen()
    while True:
        o = input('Press "K" for Key-Gen, "V" for verifaction, "Q" for quit')
        if o == "Q":
            break
        elif o == "K":
            [k1,k2] = keygen()
            print("Your key(a,b) is : {},{}".format(k1,k2))
        elif o == "V":
            key = input("Please Enter your key(k1,k2): ")
            key = key.split(",")
            a = int(key[0])
            b = int(key[1])
            if verification(a,b):
                print("Approved")
            else:
                print("Rejected")
    
