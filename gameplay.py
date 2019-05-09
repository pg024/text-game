from sys import exit
import random

def dead():
	print("Mi dispiace, hai perso.")
	exit(0)

def bivio():
	print("Ti trovi a un bivio. Dx o Sx?")
	scelta = input("> ")

	if "dx" in scelta.lower():
	 print("sei morto, dei nazi ti hanno picchiato a morte")		
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
 score_hero = 0
 score_nazi = 0
 print("Al meglio delle tre, GO!\n")
		
 while score_hero < 3 and score_nazi < 3:
  print("Il tuo score è: ", score_hero)
  print("Lo score del nazi è: ", score_nazi)
  print("Scegli: [1]Carta [2]Forbice [3]Sasso")
  lista = ['carta', 'forbice', 'sasso']
  colpo = lista[int(input("> "))-1]
  colponazi = random.choice(lista)
  print(f"il tuo avversario ha scelto {colponazi}\n")
 		
  if colpo == colponazi:
   print("pareggio, come on!\n")
  elif (colpo == 'carta' and colponazi == 'forbice') or (colpo == 'forbice' and colponazi == 'sasso') or (colpo == 'sasso' and colponazi == 'carta'):
   print("argh!\n")
   score_nazi = score_nazi + 1
  else:
   print("un punto per noi!\n")
   score_hero = score_hero + 1

  if score_nazi == 3:
   print("Hai perso! Il nazi ti picchia")
   return dead()
  else:
   print("Olè, VITTORIA!")
   return last_step()
	 	 
	
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
  last_step()
 if "no" in scelta.lower():
  print("\n Ok allora lo sfidi a morra cinese \n ")
  morra()
	 
bivio()
