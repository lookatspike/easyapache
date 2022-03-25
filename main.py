from curses import echo
import os

print("Installare apahe non è mai stato così facile!")
print("Questo programma creerà un file bash in base alle tue scelte. Ti basterà cliccarlo per instalalre il web server.")
apache = input("Installare apache? [y/n]: ")
f = open("clickMe.txt","a")
if apache == "y":
    f.write("""
    sudo apt-get update
    sudo apt-get upgrade
    sudo apt install apache2 -y
    """)   
elif apache =="no":
    print("ok")
else:
    print("Questa opzione non esiste")

#install php
php = input("Installare php?: [y,n] ")
if php  == "y":
    f.write("""
    sudo apt install php7.3 php7.3-mbstring php7.3-mysql php7.3-curl php7.3-gd php7.3-zip -y
    """) 
elif php == "n":
       
    print( "ok")
else: 
    print("Questa opzione non esiste")


#install mysql
sql = input("Installare sql?: [y,n] ")
if sql  == "y":
    f.write("""
    sudo apt install mariadb-server    
    sudo mysql_secure_installation
    sudo apt install php-mysql
    """) 
    go = input("""
    Quando installerai il server, ti verranno poste delle domande, ti consigliamo di rispondere 'y' a tutte le domande a fine
    di migliorare la sicurezza dei tuoi database. [premi invio per continuare]
     """)
elif sql == "n":
       
    print( "ok")

print("La configurazione è finita qui. Grazie per aver usato EZAPACHE. Ora ti basterà aprire il file bash che si sarà creato nella stessa cartella.")
print("")
old_name = 'clickMe.txt'
new_name = 'clickMe.sh'
os.rename(old_name, new_name)


