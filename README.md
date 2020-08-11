# EDIBO
EDIBO projekta elektroniskā klāde
## Day 01 - Day 02
### Topics:
- Terminal (hot-keys)
- Shell (basics)
- Git (basics)
- ASCII table

#### Terminal (hot-keys)
Ctrl+Alt+T - open **Terminal**  
Ctrl+Shift+T - open a new tab in **Terminal**  
Ctrl+Shift+Q or ALT+F4 - close **Terminal**  
Ctrl + - Zoom In **Terminal**  
Ctrl - - Zoom Out **Terminal**  
Arrow Up and Arrow Down - List last commands  
Tab - Continue a command  

#### Shell (basics)
PS1="$ " - Rename first line in Shell for $
> It will not be written with a full name of PC, for example "user@333k-34:~$"

echo - First command to show (tell me)  
echo Hello World - Shows a text "Hello world"
echo $a - Shows what is a=?  
echo $(($a+$b)) - Summing  
echo $0 - Shows a name of a console  
pwd - Shows where are we  
cd "name" - Change directory  
cd .. - Change directory going upper
cd /home - Change directory "home"  
ls - List directory contents  
ls -l - List of directories with a time  
ls -a - Show all, include hidden  
ls -lt - List of directories with a last update
mkdir - Make a new directory  
rmdir - Remove a directory  
cat, tail, less, more - Shows a.txt (if made)  
date - Shows a time  
cal - Shows a calendar
sh - Another shell (not bash now)  
whoami - Command shows us who are we now  
who - Shows when PC was enabled  
last - We can see who is close  
tree - Shows all directory content

#### ASCII Table

[ASCII table](http://www.ecowin.org/ascii.htm)

## Day 04  

### Topics:  

- Darbs ar mainīgājiem  
- Darbs ar speciāliem mainīgājiem  
- Darbs ar mainīgo masīvu
- Darbs ar operācijām
- Darbs ar nosacījumu operatoru
- Darbs ar cikliem  

#### Darbs ar mainīgājiem  

#!/bin/bash  

NAME="Zara Ali"  
echo $NAME  

#### RESULT:

>Zara Ali  
---------------------------------  
Making a read-only:  

#!/bin/bash  

NAME="Zara Ali"  
readonly NAME  
NAME="Qadiri"  

#### RESULT:

>NAME: readonly variable  
---------------------------------  
#### Darbs ar speciāliem mainīgājiem  

#!/bin/bash

echo "File Name: $0"  
echo "First Parameter : $1"  
echo "Second Parameter : $2"  
echo "Quoted Values: $@"  
echo "Quoted Values: $*"  
echo "Total Number of Parameters : $#"  

#### RESULT:
> ./test_variables_3.sh Stas Kursish  
File Name : ./test_variables_3.sh  
First Parameter : Stas  
Second Parameter : Kursish  
Quoted Values: Stas Kursish  
Quoted Values: Stas Kursish  
Total Number of Parameters : 2 

---------------------------------  
  
#### Darbs ar mainīgo masīvu

#!/bin/bash

NAME[0]="Vitjok"  
NAME[1]="Mashka"  
NAME[2]="Zajchik343"  
NAME[3]="Popka"  
NAME[4]="Juljchik"  
echo "First Index: ${NAME[*]}"  
echo "Second Index: ${NAME[@]}"  

#### RESULT:
>First Index: Vitjok Mashka Zajchik343 Popka Juljchik
Second Index: Vitjok Mashka Zajchik343 Popka Juljchik
--------------------------------

#### Darbs ar operācijām

#### Arithmetic Operators

a=10  
b=20  
c=10  

echo $[ $a == $b ]  would return false (0)  
echo $[ $c != $a ]  would return false (0)  
echo $[ $a == $c ]  would return true (1)  
echo $[ $c != $b ]  would return true (1)  

#### Relational Operators

-eq - equal or not [ $a -eq $b ] - is not true  
-ne - not equal or is [ $a -ne $b ] - is true  
-gt - is one greater or is not [ $a -gt $b ] - is not true  
-lt - first operand is less than second [ $a -lt $b ] - is true  
-ge - first operand is greater or equal to second [ $a -ge $b ] - is not true  
-le - first operand is less or equal to second [ $a -le $b ] - is true  

#### Boolean Operators

! - logical negation. This inverts a true condition into false [ !false ] - is true  
-o - this is logical **OR**. If one of the operands is true, than the condition becomes true [ $a -lt 20 -o $b -gt 100] is true  
-a - this is logical **AND**. If both the operands, then the condition becomes true otherwise false [ $a -lt 20 -a $b -gt 100] is false  


