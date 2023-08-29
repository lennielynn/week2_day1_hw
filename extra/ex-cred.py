monster = 100
hero = 100

while hero >= 1 or monster >= 1:
  player = input("mele, shoot(-20hp), or special(-50hp) ")
  
  if player == "mele":
    print("monster -10hp")
    monster -= 10
  elif player == "shoot":
    print("monster -30hp" )
    monster -= 30
    player -= 20
  elif player == "special":
    print("monster -85hp")
    monster -= 85
    player -= 50
    break
print("Victory!")
    
    
    
   
   
   
   
   
   
    # return
    # print('monter: -10hp')
    # elif player == 'run':
    #   print('back to school')
    # elif player == 'monday':
    #   print('monday 2')
    # elif player == 'tuesday':
    #   print('working thru the week')
    # elif player == 'wednesday':
    #   print('hump day')