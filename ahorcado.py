fallo=0
palabra=input("dime una palabra: ")

caso=" _ "*len(palabra)
print(caso)
print()
letras_correctas=[]
letras_incorrectas=[] 
fallo=0
aciertos=0
while fallo<5:
  
  letra=input("dime una letra: ")
  if letra in palabra:
    aciertos=aciertos+1
    letras_correctas.append(letra)
    #acierto=palabra.index(letra)
    #print("su letra está en la posición: "+ str(acierto+1) +" de la palabra.")
    
    caso="_"*len(palabra)
    for j in range(len(palabra)):
      if palabra[j] in letras_correctas:
        caso=caso[:j]+palabra[j]+caso[j+1:]
    
    
    for k in caso:
      print(k,end=" ")
    print() 
    
    
    if caso==palabra:
      print("Ganaste!!!, la palbra era " +palabra)
      break
      
  else:
    if letra in letras_incorrectas:
      print("Esta letra ya la has dicho antes, prueba con otra ")
    else:
      fallo=fallo+1
      print("lo siento has gastado " + str(fallo) + " fallo de 5")
      letras_incorrectas.append(letra)
    print()
  
    

print("Juego acabado")