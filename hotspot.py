file = open("hotspot-database.txt","a")
while True : 
    Answer = input ('Input new Hotspot User (Yes/No)')
    print('*'*40)
    if Answer == 'yes' :
        Username = input ('Hotspot Username : ')
        Password = input ('Hotspot Password : ')
        print('*'*40)
        file.write('Hotspot Username : ' +Username+'\n' 
        'Hotspot Password : '+Password)
    else:
        file = open ("hotspot-database.txt","r")
        for item in file :
            item=item.strip()
            print(item)
        file.close()
        break
file.close()