#!/usr/bin/python

print("Ievadiet skaitli ")
# a=2**2000000

#te ir tris darbibas - vertibas sagaidisana, vertibas parveidosana, pieskirsana
#argument = input()
#int(argument)
#a = int(argument)

#pildod int(input()) "bez izmeginajuma programma var vienkarsi izpildit ....
#tapec lai "nelidotu" mes izmantosim try ... except ... finaly konstrukcija

pazime = False
while not pazime:
#whle pazima = False:
#while paziime !=True: 

    try:
        a=int(input())
        pazime = True 
    except:
        print("Diemzel, cienijamais lietotaj, to kas ir ievadits nevar parveidot")
        print("Ludzu ievadi skaitli (0,1,2,3,4,5,6,7,8,9) velreiz")

#if (a == int): print ("a**100)
#ja loti gribas, tad var salidzinas type(a) == int -> rezultats bus True

if (a == 5):
    print(a**100)
    print("Aprekins ir gatavs")
print("Sis teksts atrodas arpus bloka - pierakstits bez"
      "atstarpem prieksa, tapec tas paradisies jebkura gadijuma")
