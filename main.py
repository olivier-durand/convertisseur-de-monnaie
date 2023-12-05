from forex_python.converter import CurrencyRates
def convertir_devise():
    c = CurrencyRates()

    montant_euros = float(input("Veuillez saisir la valeur en euros : "))
    devise_cible = input("Veuillez saisir le code de la devise cible (par exemple, USD) : ")
    taux_change = c.get_rate('EUR', devise_cible)

    montant_converti = montant_euros * taux_change

    print(f"{montant_euros} Euros équivaut à {montant_converti} {devise_cible} (taux de change actuel : {taux_change})")

# Appel de la fonction
convertir_devise()