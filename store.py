#1000,shampoo,12500,30
#1005,piaz,7650,100
#1014,doogh,10000,25
#2000,chips,8000,15
from pyfiglet import Figlet
import qrcode


PRODUCT=[]


def load_from_database():
    print('loading...')
    f=open('database.csv','r')
    text=f.read()
    product_list=text.split('\n')
    for i in range(len(product_list)):
        info=product_list[i].split(',')
        new_dict={'id':info[0],'name':info[1],'price':info[2],'count':info[3]}
        PRODUCT.append(new_dict)
    print('load compleat')


def show_list():
    for product in PRODUCT:
        print(product)


def add():
    new_prodact={}
    new_prodact['id']=input('please enter id:')
    new_prodact['name']=input('please enter name:')
    new_prodact['price']=input('please enter price:')
    new_prodact['count']=input('please enter count:')
    PRODUCT.append(new_prodact)


def edit():
    id=input('please enter ure id u want to change: ')
    f=0
    for i in range(len(PRODUCT)):
        if PRODUCT[i]['id']==id:
            print('what do u want to change?')
            print('1.name')
            print('2.price')
            print('3.count')
            change=int(input('what do u want to change?'))
            if change==1:
                name=input('enter new name:')
                PRODUCT[i]['name']=name
            elif change==2:
                price=input('enter new price:')
                PRODUCT[i]['price']=price
            elif change==3:
                count=input('enter new count:')
                PRODUCT[i]['count']=count
            f=1
    if f==0:
        print('id is wrong') 


def delete():
  id= input('enter id:')
  f=0
  for i in range(len(PRODUCT)):
    if PRODUCT[i]['id']==id: 
        del PRODUCT[i]
        f=1
        break
  if f==0:
      print('id is wrong')


def search():
    name=input('enter name:')
    f=0
    for i in range(len(PRODUCT)):
        if PRODUCT[i]['name']  == name:
            print(PRODUCT[i])
            f=1
    if f==0:
        print('wrong name')


def qrcode():
    id=input('enter id:')
    f=0
    for i in range(len(PRODUCT)):
        if PRODUCT[id]['id']==id:
            img=qrcode.make(PRODUCT[i])
            img.save('qrcode.ping')
            f=1
    if f==0:
        print('wrong id')




def buy():
    buy_basket=[]
    price=0
    while True:
        print('1.shop:')
        print('exit')
        choose=int(input('please enter ure choose:'))
        if choose==1:
          id=input('enter id:')
          f=0
          for i in range(len(PRODUCT)):
              if PRODUCT[i]['id']==id:
                  m=int(input('please enter how many?'))
                  if int(PRODUCT[i]['count'])<m:
                      print('sorry!we dont have enough product')
                  elif int(PRODUCT[i]['count'])>=m:
                      buy_product={}
                      new_count=int(PRODUCT[i]['count'])-m
                      PRODUCT[i]['count']=str(new_count)
                      price+=int(PRODUCT[i]['price'])*m
                      buy_product['name']=PRODUCT[i]['name']
                      buy_product['m']=m
                      buy_product['price']=PRODUCT[i]['price']
                      buy_basket.append(buy_product)
                  f=1
          if f==0:
              print('sorry!we dont have this product')
        elif choose==2:
          print('tnx for ure buying')
          for i in range(len(buy_basket)):
              print(buy_basket[i])
          print('ure price: ',price)
          return False


def exit():
    new_product=''
    for i in range(len(PRODUCT)):
      id=PRODUCT[i]['id']
      name=PRODUCT[i]['name']
      price=PRODUCT[i]['price']
      count=PRODUCT[i]['count']
      if i==len(PRODUCT)-1:
          new_product=id+','+name+','+price+','+count
      else:
          new_product=id+','+name+','+price+','+count+'\n'
      new_product+=new_product
    file=open('database.text','w')
    file.write(new_product)
    exit()  

def show_menu():
    print('welcome to sadjad')
    print('1.show_list')
    print('2.add')
    print('3.edit')
    print('4.sdelete')
    print('5.search')
    print('6.buy')
    print('7.exit')

load_from_database()

f=Figlet(front='standard')
print(f.renderText('sadjad'))

while True:
    show_menu()
    choice=int(input('please enter ure choice: '))
    if choice==1:
      show_list()
    elif choice==2:
        add()
    elif choice==3:
        edit()
    elif choice==4:
        delete()
    elif choice==5:
        search()
    elif choice==6:
        buy()
    elif choice==7:
        exit()
