
products=[]
def read_data():
    f=open("shop.txt","r")
    for i in f :
        kala1=i.split(",")
        dic={"id":kala1[0],"name":kala1[1],"price":kala1[2],"count":kala1[3]}
        products.append(dic)

        
def show_menu():
    print("1_add")
    print("2_delete")
    print("3_search")
    print("4_buy")
    print("5_edit")
    print("6_exit")
    print("7_show products")


def add():
    id=input("Enter id's kala :")
    name=input("Enter name's kala: ")
    price=input("Enter price for kala: ")
    count=input("Enter count of kala: ")
    dic={"id":id,"name":name,"price":price,"count":count}
    products.append(dic)
    print(products)
    print("added!!!!!!!!!!!!!!!!")








def delete():
    id=input("Enter id's kala:  ")
    for kala in products:
        if id==kala["id"]:
            products.remove(kala)
            print(products)
            print(kala,"hazf shod!!!!!!!")
            break
        else:
            print("kala ba in id iaft nzshod!!!!!!")
            break



def search():
    show_menu()
    key=input("Enter your key : ")
    for kala in products:
        if key==kala["id"] or key==kala["name"] :
            print(kala)
            break
    else:
        print("not found!!!")



def buy():
    range=[]
    while True:
        id=input("Enter id's kala or ( paian): ")
        if id=="paian":
            
            break
        for kala in products:

            if (id)==(kala["id"]):
                print("in kala ba in id mojod ast")
                count=(input("Enter count ke mikhai: "))
                if int(count)<int(kala["count"]) or int(count)== int(kala["count"]):
                    print("mojod ast")
                    a=kala["count"]
                    kala["count"]=int(kala["count"])-int(count)
                    print(a,"be",kala["count"],"taghir kard!!!!!!!!!!")
                    jadid= {"id":kala["id"],
                        "name":kala["name"],
                        "price":kala["price"],
                        "count":count}
                    range.append(jadid)
                    
                    for jadid in range:
                        
                        print(int(jadid["price"])*int(jadid["count"]))

                        
                #     break
                # else:
                #     print("mojodi kafi nist!!!")

    gheimat=0
    for jadid in range:
        gheimat=(gheimat+(int(jadid["count"])*int(jadid["price"])))
    print("gheimat kol :",gheimat)
                    
            
                
            



def edit():
    id=input("Enter id's kala: ")
    for kala in products:
        if id==kala["id"]:
            print("1_Name")
            print("2_Price")
            print("3_Count")
            #read_data()
            user=int(input("Enter a number bein 1 ta 3:!!!!!!!:   "))
            if user==1:
                new_name=input("Enter a new name:   ")
                a=kala["name"]
                kala["name"]=new_name
                print("name:",new_name)
                print(a, "be" ,new_name,"taghir kard!!!!!!!!")
                break
            elif user==2:
                new_price=int(input("Enter a new price:  "))
                b=kala["price"]
                kala["price"]=new_price
                print("price:",new_price)
                print(b,"be",new_price,"taghir kard!!!!!!!!!!!!")
                break
            elif user==3:
                new_count=int(input("Enter a new count:  "))
                c=kala["count"]
                kala["count"]=new_count
                print("count: ",new_count)
                print(c,"be",new_count,"taghir kard!!!!!!!!!!!!!!")
                break
        else:
            print("kala ba in id iaft nzshod!!!!!!")
            break
        


def exit():
    pass



def show_products():
    print("id \t name \t price \t count \t")
    print()
    for key in products:
        print(key["id"],"\t",key["name"],"\t",key["price"],"\t",key["count"],"\t")
read_data()
show_menu()



user_choice=int(input("Enter a number bein 1 ta 7 : "))
while True:
    if user_choice==1:
        add()
        break
    elif user_choice==2:
        delete()
        break
    elif user_choice==3:
        search()
        break
    elif user_choice==4:
        buy()
        break
    elif user_choice==5:
        edit()
        break
    elif user_choice==6:
        exit()
        break
    elif user_choice==7:
        show_products()
        break
    else:
        print("ERORR!!!  baiad adadi bein 1 ta 7 entekhab koni !!!")



read_data()
show_menu()
