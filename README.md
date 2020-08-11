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

#### Darbs ar mainīgājiem  

#!/bin/bash  

NAME="Zara Ali"  
echo $NAME  

Will give a result --->

Zara Ali  
---------------------------------  
Making a read-only:  

#!/bin/bash  

NAME="Zara Ali"  
readonly NAME  
NAME="Qadiri"  

Will give a result --->

NAME: readonly variable  
---------------------------------  
#### Darbs ar speciāliem mainīgājiem  

#!/bin/bash

echo "File Name: $0"
echo "First Parameter : $1"
echo "Second Parameter : $2"
echo "Quoted Values: $@"
echo "Quoted Values: $*"
echo "Total Number of Parameters : $#"

> ./test_variables_3.sh Stas Kursish  
File Name : ./test_variables_3.sh  
First Parameter : Stas  
Second Parameter : Kursish  
Quoted Values: Stas Kursish  
Quoted Values: Stas Kursish  
Total Number of Parameters : 2 

---------------------------------  
  
#### Darbs ar mainīgo masīvu

#!/bin/sh

NAME[0]="Vitjok"  
NAME[1]="Mashka"  
NAME[2]="Zajchik343"  
NAME[3]="Popka"  
NAME[4]="Juljchik"  
echo "First Index: ${NAME[*]}"  
echo "Second Index: ${NAME[@]}"  




