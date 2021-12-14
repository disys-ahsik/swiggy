restaurants={"Buhaari":{"c.briyani":150,"veg.briyani":80,"swarma":100,"parotta":15,"egg parotta":50,"full meals":90,"half meals":45,"ombulate":15},
"Appachivilas":{"c.briyani":180,"veg.briyani":80,"swarma":100,"parotta":30,"egg parotta":100,"full meals":100,"half meals":55,"ombulate":25},
"Muniyandivilas":{"kalaan.briyani":150,"veg.briyani":80,"veg.swarma":100,"parotta":25,"chilli parotta":90,"full meals":90,"half meals":45,"potatofry":15},
"Anjappar":{"Pongal":50,"veg.briyani":80,"Idly":10,"Dosa":15,"ghee roast":50,"full meals":90,"half meals":45,"egg dosa":55},
"Taj":{"Prawn.briyani":150,"Fish.briyani":80,"fish swarma":100,"prawn fry":55,"Fish fry":50,"full fish meals":90,"half boiled":45,"ombulate":15}}
order={}
class Hotels:
    print("***************WELCOME************************")

    def __init__(self):
        print("List Of Hotels :")
        print("*****************")
        print("1.Buhaari")
        print("2.Appachivilas")
        print("3.Muniyandivilas")
        print("4.Anjappar")
        print("5.Taj")
        print("*****************")
        self.hotelname=input("Choose The Hotel : ")
        print("*****************")
    def menu(self):
        if isinstance(self.hotelname,str):
            if self.hotelname in restaurants:
                hotel=self.hotelname
                value=restaurants.get(self.hotelname)
                for i,j in value.items():
                    print(f"{i} : {j}")
                    
            else:
                raise ValueError("data not present")

        else:
            raise TypeError("invalid datatype")

    def order(self):
        print("*****************")
        inpt=input("Do you want to order : yes or no ? ")
        if inpt == "yes":
            items=input("How many items do you want to order : ")
            if int(items)>0 and int(items)<25:
                for i in range(int(items)):
                    print("*****************")
                    dish=input("Enter The Dish You Need : ")
                    if(dish in restaurants[self.hotelname]):
                        quantity=input(f"Enter the Quantity of {dish} : ")
                        order[dish]=quantity
                    else:
                        raise ValueError("dish not present")
            else:
                raise ValueError("data is out of bound")
        else:
            print("Thank you")

    def bill(self):
        amt=0
        for i,j in order.items():
            val=restaurants[self.hotelname]
            amt=val[i]*int(j)
            print("Thank You For Ordering")
            print(f"Your Bill Amount is : {amt}")
              
            
        
            
        
            
        
food=Hotels()
food.menu()
food.order()
food.bill()
