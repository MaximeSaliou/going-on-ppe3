import argparse
#Definition des parametre du parser
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

#affiche les parametre qu'on a demander avec leurs pourcentage
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

#Ecrit par Gregory David
class appendTypeQuantity(argparse.Action):
    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        if nargs == 2:
            super(appendTypeQuantity, self).__init__(option_strings, dest, nargs=nargs, **kwargs)
        else:
            logging.error("Option %s must have 2 arguments in its definition" % option_strings)
    def __call__(self, parser, namespace, values, option_string=None):
        try:
            quantity = abs(int(values[1]))
        except ValueError:
            logging.warning("Quantity Input value is Not A Number (NaN): '" + values[1] + "'. Using None instead, and apply rules (see man page)")
            values[1] = None
        else:
            values[1] = quantity if quantity <= 100 else None 

        current_dest_value = getattr(namespace, self.dest)
        if type(current_dest_value) is list:
            current_dest_value.append(values)
            setattr(namespace, self.dest, current_dest_value)
        else:
            logging.debug(values)
            setattr(namespace, self.dest, [values])
