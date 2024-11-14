#### Fonction secondaire
"""class that display palyndroms"""

def ispalindrome(p):
    """module verifying if the string is a palyndrome"""
    # votre code ici
    p=p.lower()
    normal = str.maketrans("àâäéèêëîïôöùûüç", "aaaeeeeiioouuuc",  " !'()*,.:;?`- ")
    new_p = p.translate(normal)
    return bool(new_p == new_p[::-1])
### Fonction principale
def main():
    """module printing the word and telling if it is a palyndrome or not"""
    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
