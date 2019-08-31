class Room:
    def __init__(me,name,n,e,w,s,items):
        me.name=name
        me.n=n
        me.s=s
        me.e=e
        me.w=w
        me.items=list(items)

class Man:
    def __init__(me,room,items):
        me.room=room
        me.bag=list(items)

    def look(me):
        print('North: ',d[me.room].n)
        print('South: ',d[me.room].s)
        print('East : ',d[me.room].e)
        print('West : ',d[me.room].w)
        print()
        print('items in',me.room,': ',end='')
        print(*d[me.room].items,sep=', ')

    def move(me,di):
        di=di[0].lower()
        try:
            room=d[me.room].__getattribute__(di)
            if room==None:
                print('Sorry, but there is Nothing ahead !!')
            else:
                me.room=room
                print('Moved to',room)
        except:
            print("Please Enter one of the direction (N, E, W, S)")
            return

    def pick(me,item):
        if item not in d[me.room].items:
            print('There is no such item in the room.')
        else:
            me.bag.append(item)
            d[me.room].items.remove(item)
            print(item,'picked.')

    def drop(me,item):
        if item in me.bag:
            me.bag.remove(item)
            print(item,'droped')
            d[me.room].items.append(item)
        else:
            print(item,'not in bag')

    def showBag(me):
        print('Items in your bag: ',end='')
        print(*me.bag,sep=', ')

def save():
    f=open('home.txt','w')
    for room in rooms:
        f.write(','.join(d[room].items)+'\n')
    f.write(man.room+'\n')
    f.write(','.join(man.bag))
    f.close()


home=[ [0             , 'KITCHEN'    , 'DINING ROOM' , 0            ],  # Map of Home, home list not used in code.
       ['RON WASHROOM', 'RON BEDROOM', 'HALL'        , 'NN BEDROOM' ],
       [0             , 'GAME ROOM'  , 'DRAWING ROOM', 'NN WASHROOM'],
       [0             ,      0       ,   'ROAD'      , 0            ] ]
rooms=('road','kitchen','dining room','ron washroom','ron bedroom','hall','nn bedroom','game room','drawing room','nn washroom')
items=[('dog','grass'),('knife','apple'),('Plate','spoon','table','chair'),('soap','mug' ),('pillow','bed'),('photo','sofa'),
       ('shirt','gold'),('ludo','chess'),('photo',),('brush','paste')]

# Loading data from file - 'home.txt'
room='road'
bag=[]
try:
    f=open('home.txt')
    data=f.read()
    f.close()
    if data!='':
        ch=input('Do you want to load Data (y/s) : ')
        print()
        if ch=='y':
            #Loading data.
            data=data.split('\n')
            for i in range(len(items)):
                items[i]=tuple(data[i].split(','))
            room=data[i+1]
            bag=data[i+2].split(',')
            
except:
    pass
    
        
# Dictionary for linking room name to its object.        

d= { 'road'         :Room('road'        ,'drawing room' ,None           ,None           ,None           , items[0]   ),
     'kitchen'      :Room('kitchen'     ,None           ,'dining room'  ,None           ,'ron bedroom'  , items[1]   ),
     'dining room'  :Room('dining room' ,None           ,None           ,'kitchen'      ,'hall'         , items[2]   ),
     'ron washroom' :Room('ron washroom',None           ,'ron bedroom'  ,None           ,None           , items[3]   ),
     'ron bedroom'  :Room('ron bedroom' ,'kitchen'      ,'hall'         ,'ron washroom' ,'game room'    , items[4]   ),
     'hall'         :Room('hall'        ,'dining room'  ,'nn bedroom'   ,'ron bedroom'  ,'drawing room' , items[5]   ),
     'nn bedroom'   :Room('nn bedroom'  ,None           ,None           ,'hall'         ,'nn washroom'  , items[6]   ),
     'game room'    :Room('game room'   ,'ron bedroom'  ,'drawing room' ,None           ,None           , items[7]   ),
     'drawing room' :Room('drawing room','hall'         ,'nn washroom'  ,'game room'    ,'road'         , items[8]   ),
     'nn washroom'  :Room('nn washroom' ,'nn bedroom'   ,None           ,'drawing room' ,None           , items[9]   )
   }

# Main loop
man=Man(room,bag)
print(f'You are in {room}\n')

while 1:
    print('What do you want to do --\n1. Look\n2. Move\n3. Pick\n4. Drop\n5. Look in Bag\n6. Save and Exit\n')
    ch=input('Enter choice: ')
    print()
    if ch=='1':
        man.look()
    elif ch=='2':
        man.move(input('Enter direction: '))
    elif ch=='3':
        man.pick(input('Enter Item: '))
    elif ch=='4':
        man.showBag()
        man.drop(input('Enter Item: '))
    elif ch=='5':
        man.showBag()
    elif ch=='6':
        save()
        print('Thanks for playing :)')
        break
    else:
        print('Please enter correct choice')

    print()



