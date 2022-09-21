import tkinter
canvas = tkinter.Canvas(width=500,height=400)# vytvorenie platna
canvas.pack()
canvas.focus_set() #zaostry na hlavne okno
y=20
subor = open('vytazenie autobusovej linky_kremnicky','r')#otvorenie suboru z moznostou citania 
vytazenie = 0 # vytvorrenie premennych
stanice = []
cestujuci = 0
for riadok in subor: # for cyklus na citanie suboru
    if vytazenie == 0:
        vytazenie = int(riadok)
    else:
        cast = riadok.split()
        cestujuci += int(cast [0]) #precita prvy udaj
        cestujuci -= int(cast [1])#precitadruhy udaj
        stanice.append(cestujuci)#prida k stanici cestujucich
        canvas.create_text(50,y,text=' '.join(cast[2:]))
        y+=20
subor.close()
y=20
def klick(event): # definovanie funkcie klick
    global y # globalna premenna y
    if len(stanice)>0:
        canvas.create_rectangle(100,y+2,200,y+18)
        vytazenie = stanice.pop(0)
        if cestujuci>vytazenie: # podmienka na vyfarbenie riadkov
            farba='red'
        else:
            farba='green'
        canvas.create_rectangle(100,y+2,100+100*cestujuci/vytazenie,y+18,fill= farba)
        y+=20

canvas.bind('<Key>' ,klick)#nabindovanie tlacitka na spustenie programu    
                
            
