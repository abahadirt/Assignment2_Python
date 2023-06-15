import sys
with open(sys.argv[1]) as f1:
    peopledict = {}
    for line in f1:
        strip = line.strip()
        line = strip
        line=line.replace(":", " ")
        line= line.split(" ")
        peopledict[line[0]] = line[1:]

with open(sys.argv[2]) as f2:
    commands = []
    for line2 in f2:
        strip2 = line2.strip()
        line2= strip2
        line2 = line2.split(" ")
        commands.append(line2)

file= open("output.txt","w")
file.write("Welcome to Assignment 3\n")
file.write("-------------------------------\n")


def ANU(x):
    if x in peopledict.keys():
        file.write("ERROR: Wrong input type! for 'ANU'!--This user already exists!!\n")
    else:
        file.write("User '")
        file.write(x)
        file.write("' has been added to the social network successfully\n")
        peopledict[x] = []
def DEU(x):
    if x in peopledict.keys():
        mesaj = "User '"+x+"' and his/her all relations have been deleted successfully\n"
        file.write(mesaj)
        peopledict.pop(x)
        for i in peopledict.keys():
            if x in peopledict[i]:
                tut = peopledict[i]
                tut.remove(x)
    else:
        mesaj = "ERROR: Wrong input type! for 'DEU'!--There is no user named '"+x+"'!!\n"
        file.write(mesaj)
def ANF(y,z):
    if y in peopledict.keys():
       if z in peopledict.keys():
            if z in peopledict[y]:
                mesaj= "ERROR: A relation between '"+y+"' and '"+z+"' already exists!!\n"               #zaten arkadaşlar
                file.write(mesaj)
            else:
                mesaj= "Relation between '"+y+"' and '"+z+"' has been added successfully\n"           #arkadaş ekle
                file.write(mesaj)
                a = []
                b = []
                a = peopledict[y]
                b = peopledict[z]
                a.append(z)
                b.append(y)
                peopledict[y] = a
                peopledict[z] = b
       else:
           mesaj = "ERROR: Wrong input type! for 'ANF'!--No user named '"+z+"' found!!\n"
           file.write(mesaj)
    else:
        if z in peopledict.keys():
            mesaj = "ERROR: Wrong input type! for 'ANF'!--No user named '" + y + "' found!!\n"
            file.write(mesaj)
        else:
            mesaj = "ERROR: Wrong input type! for 'ANF'!--No user named '"+y+"' and '"+z+"' found!\n"
            file.write(mesaj)

def DEF(y,z):               #arkadaşlıktan çıkarma
    if y in peopledict.keys():
        if z in peopledict.keys():
            if z in peopledict[y]:
                mesaj = "Relation between '"+y+"' and '"+z+"' has been deleted successfully\n"  # zaten arkadaşlar
                file.write(mesaj)
                a = []
                b = []
                a = peopledict[y]
                b = peopledict[z]
                a.remove(z)
                b.remove(y)
                peopledict[y] = a
                peopledict[z] = b
            else:
                mesaj = "ERROR: No relation between '"+y+"' and '"+z+"' found!!\n"
                file.write(mesaj)
        else:
            mesaj = "ERROR: Wrong input type! for 'DEF'!--No user named '" + z + "' found!!\n"
            file.write(mesaj)
    else:
        if z in peopledict.keys():
            mesaj = "ERROR: Wrong input type! for 'DEF'!--No user named '" + y + "' found!!\n"
            file.write(mesaj)
        else:
            mesaj = "ERROR: Wrong input type! for 'DEF'!--No user named '" + y + "' and '" + z + "' found!\n"
            file.write(mesaj)

def CF(x):
    if x in peopledict.keys():
        y= len(peopledict[x])
        mesaj = "User '" + x + "' has "+str(y)+" friends\n"
        file.write(mesaj)

    else:
        mesaj = "ERROR: Wrong input type! for 'CF'!--No user named '"+x+"' found!\n"
        file.write(mesaj)



def FPF(y,z):                                                                #sort YAPILACAK
    if y in peopledict.keys():
        myset = set()
        if z =="1":
            n = len(peopledict[y])
            mesaj1 = "User '" + y + "' has " + str(n) + " possible friends when maximum distance is " + z + "\n"
            file.write(mesaj1)
            for i in peopledict[y]:
                myset.add(i)
            list10 = list(myset)
            list10.sort()
            mesaj2 = "These possible friends: {{{}}}\n".format(str(list10)[1:-1])
            file.write(mesaj2)

        elif z =="2":
            for i in peopledict[y]:
                myset.add(i)
                for im in peopledict[i]:
                    myset.add(im)
            myset.remove(y)
            n= len(myset)
            mesaj1 = "User '" + y + "' has " + str(n) + " possible friends when maximum distance is " + z + "\n"
            file.write(mesaj1)
            list11 = list(myset)
            list11.sort()
            mesaj2 = "These possible friends: {{{}}}\n".format(str(list11)[1:-1])
            file.write(mesaj2)
        elif z =="3":
            for i in peopledict[y]:
                myset.add(i)
                for im in peopledict[i]:
                    myset.add(im)
                    for imm in peopledict[im]:
                        myset.add(imm)
            myset.remove(y)
            n = len(myset)
            mesaj1= "User '"+y+"' has "+str(n)+" possible friends when maximum distance is "+z+"\n"
            file.write(mesaj1)
            list12= list(myset)
            list12.sort()
            mesaj2 = "These possible friends: {{{}}}\n".format(str(list12)[1:-1])
            file.write(mesaj2)

        else:
            mesaj = "ERROR: Maximum distance is out of range!!\n"
            file.write(mesaj)
    else:
        mesaj= "ERROR: Wrong input type! for 'FPF'!--No user named '"+y+"' found!\n"
        file.write(mesaj)

def SF(y,z):
    if y in peopledict.keys():
        if z == "2":
            list2 = []
            list3 =[]
            dict3={}
            for i in peopledict[y]:
                for im in peopledict[i]:
                    if im != y:
                        list2.append(im)
            for i in list2:
                dict3[i]=list2.count(i)
            mesaj = "Suggestion List for '"+y+"' (when MD is 2):\n"
            file.write(mesaj)
            dict3= dict(sorted(dict3.items()))
            for i in dict3.keys():
                if dict3[i] == 2:
                    file.write("'{}' has 2 mutual friends with '{}'\n".format(y,i))
                    list3.append(i)
            for i in dict3.keys():
                if dict3[i] == 3:
                    file.write("'{}' has 3 mutual friends with '{}'\n".format(y, i))
                    list3.append(i)
            list3.sort()
            file.write("The suggested friends for '{}': {}\n".format(y, str(list3)[1:-1]))
        elif z =="3":
            list2 = []
            list3 =[]
            dict3={}
            for i in peopledict[y]:
                for im in peopledict[i]:
                    if im != y:
                        list2.append(im)
            for i in list2:
                dict3[i]=list2.count(i)
            mesaj = "Suggestion List for '" + y + "' (when MD is 3):\n"
            file.write(mesaj)
            dict3= dict(sorted(dict3.items()))
            for i in dict3.keys():
                if dict3[i] == 3:
                    file.write("'{}' has 3 mutual friends with '{}'\n".format(y, i))
                    list3.append(i)
            list3.sort()
            file.write("The suggested friends for '{}': {}\n".format(y, str(list3)[1:-1]))
        else:
            mesaj="Error: Mutually Degree cannot be less than 1 or greater than 4\n"
            file.write(mesaj)


    else:
        mesaj = "ERROR: Wrong input type! for 'SF'!--No user named '" + y + "' found!!\n"
        file.write(mesaj)



for i in commands:
    x = i[0]
    if x == "ANU":
        ANU(i[1])
    elif x == "DEU":
        DEU(i[1])
    elif x == "ANF":
        ANF(i[1],i[2])
    elif x == "DEF":
        DEF(i[1],i[2])
    elif x == "CF":
        CF(i[1])
    elif x == "FPF":
        FPF(i[1],i[2])
    elif x == "SF":
        SF(i[1],i[2])
    else:
        mesaj = "ERROR: Wrong input type!\n"
        file.write(mesaj)


file.close()

