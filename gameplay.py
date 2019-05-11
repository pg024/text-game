from sys import exit 
import random
from os.path import exists
import shamir

def dead():
 print("Mi dispiace, hai perso.")
 print("Vuoi continuare a giocare?")
 while True:
  scelta = input("Si/No> ")
  if scelta.lower() == 'si':
   return start()
  elif scelta.lower() == 'no':
   print("Arrivederci.")
   exit(0)
  else:
   print("Non ho capito, puoi ripetere?")

def bivio():
 print("Attraversi la porta. C'è un bivio. Dx o Sx?")
 scelta = input("> ")
 list=['dx','sx']
 if "dx" in scelta.lower():
  print("Incontri dei nazi, ti picchiano a morte")		
  dead()
 elif "sx" in scelta.lower():
  sacchetto = random.randint(1, 50)
  print(f"La strada è libera, per terra trovi un sacchetto con {sacchetto} scellini belgi")
  return nazi(sacchetto)
 else: 
  print("non ho capito la tua scelta, riprova")
  return bivio()

def last_step():
 print("Ce l'hai fatta, sei un campione\n")
 exit(0)

def morra():
 def morra():
 score_hero = 0
 score_nazi = 0
 print("\n")
 print("Ti sfido a carta pietra forbice lucertola spock!")
 print("Al meglio delle cinque, GO!\n")
		
 while score_hero < 5 and score_nazi < 5:
  print("Il tuo score è: ", score_hero)
  print("Lo score del nazi è: ", score_nazi, "\n")
  print("Scegli: [1]Carta [2]Forbice [3]Sasso [4]Lucertola [5]Spock")
  lista = ['carta', 'forbice', 'sasso', 'lucertola', 'spock']
  colpo = lista[int(input("> "))-1]
  colponazi = random.choice(lista)
  print("\n")
  print(f"il tuo avversario ha scelto {colponazi}\n")
 		
  if colpo == colponazi:
   print("pareggio, come on!\n")
  elif (colpo == 'carta' and colponazi == 'forbice') or (colpo == 'carta' and colponazi == 'lucertola') or (colpo == 'forbice' and colponazi == 'sasso') or (colpo == 'forbice' and colponazi == 'spock') or (colpo == 'sasso' and colponazi == 'carta') or (colpo == 'sasso' and colponazi == 'Spock') or (colpo == 'lucertola' and colponazi == 'forbice') or (colpo == 'lucertola' and colponazi == 'sasso') or (colpo == 'spock' and colponazi == 'paper') or (colpo == 'spock' and colponazi == 'lucertola'):
   print("argh!\n")
   score_nazi = score_nazi + 1
  else:
   print("un punto per noi!\n")
   score_hero = score_hero + 1

  if score_nazi == 5:
   print(f"Hai perso! Il nazi vince {score_nazi} a {score_hero} e ti picchia\n ")
   dead()
  elif score_hero == 5:
   print(f"Olè, VITTORIA, vinci {score_hero} a {score_nazi}!\n ")
   else:
   print("""Olè, VITTORIA!
Il bullo scappando droppa un pezzo di carta contenente una stringa alfanumerica
Lo raccogli?""")

   scelta = input(">Si/No")
   if scelta.lower() == 'si':
    f = open("hash1.txt", "w+")
    f.write("hash")
    f.close()
   else:
    
   return start()
		 
def nazi(s):
 print("""Un bullo ti sbarra la strada,
 Vuoi provare a corromperlo con il tuo tesoro?""")
 scelta = input("Yes/No ")
 if "yes" in scelta.lower():
  minimo = random.randint(1, 50)
  print(f"il bullo avrebbe accettato un'offerta minima di {minimo}")
  if minimo >= s:
   dead()
  else:
   print("Il bullo accetta i tuoi soldi e ti lascia passare, ben fatto!")
   return start(0)
   start()
 if "no" in scelta.lower():
  print("\n Ok allora lo sfidi a morra cinese \n ")
  morra()

def caverna 
 print("[1]Porta bivio")
 print("[2]Porta 
 print("[5]Porta di Shamir)")
  
 scelta = input("> ")
 if int(scelta) == 1:
  return caverna()
 elif int(scelta) == 2:
  return zaino()
 elif int(scelta) == 5:
  print("Vedi un'elaboratore, con due piccole fessure")
  exists1 = os.path.isfile('hash1.txt')
  exists2 = os.path.isfile('hash2.txt')
   if exists1 and exists2:
    #chiama shamir secret
   else: 

def start()
 print("Ti guardi attorno.")
 print("Cosa vuoi fare?\n")
 print("[1]Esplora la caverna")
 print("[2]Esamina il contenuto dello zaino")
 print("[3]")
 scelta = input("> ")
 if int(scelta) == 1:
  return caverna()
 elif int(scelta) == 2:
  return zaino()
 elif int(scelta) == 3:

print("Ciao Punk! Qual è il tuo nome?")
nome = input("> ")
print(f"Ok {nome}, ti sei svegliato in questa caverna")
print("hai con te uno zaino")
 
start()
