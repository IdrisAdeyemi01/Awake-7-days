def players_checker():
    names= []
    feet= []
    inches= []
    weight= []
    number_of_players= int(input('Write the number of players you want to checkout here: '))
    
    for i in  range(number_of_players):
        namer= input('Write the name of the player: ')
        names.append(namer)

        feet_input= float(input('Write the feet of the player: '))
        feet.append(feet_input)

        inch = int(input('How many inches is this player: '))
        inches.append(inch)

        weight_input= float(input('What is the weight of the player: '))
        weight.append(weight_input)

    #To print out the respective names, feet, inches and weight in the format provided 
    for i in range(len(names)):
        print(names[i])
        print(feet[i], inches[i], weight[i])
        
    height= [12*feet[i]+inches[i] for i in range(len(names))]
    
    #To calculate the average and then print it out
    average_height= sum(height)/len(height)
    average_weight= sum(weight)/len(weight)
    
    
    # To print out the averages to 2 decimal places
    print ('\n',
           'The average height is', average_height//12,'ft',round(average_height%12, 2),'inches','and the average weight is', round(average_weight, 2))

players_checker()
