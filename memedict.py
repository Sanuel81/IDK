meme_dict = {"XD": "Se usa cuando algo nos da gracia",
             "POSSER": "Se usa cuando alguien en fan de algo por moda",
             "DEAH": "Se usa cuando despues de decir algo que es mentira o de una manera sarcastica",
             "FANBOY": "Un fan ciego",
             "CHAMBA": "Trabajo"
}
for i in range(5):
    si = input("¿Que palabra quieres aprender?").upper()
    if si in meme_dict.keys():
        print(meme_dict[si])
    else: 
        print("Palabra no encontrada") 
    
