import sys
import os

def parse_input(user_input, len):
    """Parse the user input, arg: user input and length of list as user input reference"""
    try:
        user_input = int(user_input)
        assert user_input < len
    except AssertionError:
        print("Le numero fourni ne correspond à aucun des choix proposés")
        sys.exit()
    except ValueError:
        print("Veuilez fournir un chiffre valide")
        sys.exit()
    except:
        print("TYPE ERREUR INCONNU")
        sys.exit()

# ADD NEW SPIDERS TO THIS LIST (spiders need to have the same name as in their Scrapy classes)
spiders = list()
spiders.append("WelcomeToTheJungle")
spiders.append("JobTeaser")
spiders.append("LinkedIn")

# ADD NEW LANGUAGES TO PARSE TO THIS LIST
languages = list()
languages.append("Python")
languages.append("PHP")
languages.append("Javascript")

# prompt user for website to scrape -> retuns index of corresponding website
def get_user_input(spiders, languages):
    """Prompt user for input and parse it"""
    print ("Veuillez sélectionner un des sites suivant à scraper \n")
    for i, spider in enumerate(spiders):
        print(str(i) + " : " + spider + "\n")
    c_site = input("Choice : ")
    parse_input(c_site, len(spiders))
    print ("\nVeuillez un des langages suivants \n")
    for i, language in enumerate(languages):
        print(str(i) + " : " + language + "\n")
    c_language = input("Choice : ")
    parse_input(c_language, len(languages))

    return int(c_site), int(c_language)

# Get user inpu
user_choice = get_user_input(spiders, languages)

# Build scrapy crawl based on user input
scrapy_call = "scrapy crawl " + spiders[user_choice[0]] + " -a language=" + languages[user_choice[1]] + " -o " + spiders[user_choice[0]] + "_" + languages[user_choice[1]] + ".json -t json"
os.system(scrapy_call)