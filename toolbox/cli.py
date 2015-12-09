import argparse
from option import appendTypeQuantity

parser = argparse.ArgumentParser(description='Création de la playlist.')
parser.add_argument('-g', "--genre", action = 'append', nargs = 2, help='Genre de musique que in veut écouter') 
parser.add_argument('-d', "--duration", action = 'append',type=int, required=True, help='Durée de la playlist' ) 
parser.add_argument('-s', "--sub_genre",action = 'append', nargs = 2, help='Sous genre de la musique') 
parser.add_argument('-b', "--band",action = 'append', nargs = 2, help='Nom du groupe de musique')
parser.add_argument('-a', "--album",action = 'append', nargs = 2, help='Nom de album')
parser.add_argument('-t', "--title",action = 'append', nargs = 2, help='Titre de la musique') 
parser.add_argument('-f', "--format",choices = ['m3u','xspf'], help='choix du format d écoute')
parser.add_argument('-n', "--nom", help='nom de la playliste')

args=parser.parse_args()

if args.genre:
	print("Genre :\n")
	for choix in args.genre:
        	print(choix[0] + " " + choix[1] + "%\n")

if args.band:
	print("Groupe :\n")
	for choix in args.band:
		print(choix[0] + " " + choix[1] + "%\n")

if args.title:
	print("Titre :\n")
	for choix in args.title:
		print(choix[0] + " " + choix[1] + "%\n")

if args.sub_genre:
	print("Sous-Genre :\n")
	for choix in args.sub_genre:
		print(choix[0] + " " + choix[1] + "%\n")

