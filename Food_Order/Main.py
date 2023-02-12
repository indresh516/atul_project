from Admin import admin
from User import user

class main:

    def execute(self,choice):
        if choice == 1:
            print("*******Add Food*******")
            obj.add_food()
        if choice == 2:
            print("*******View Food*******")
            obj.view_food()
        if choice == 3:
            print("*******Edit Food*******")
            obj.edit_food()
        if choice == 4:
            print("*******Remove Food*******")
            obj.remove_food()
        if choice == 0:
            pass
        
if __name__ == "__main__":
    
    
    obj1 = main()
    ch =0
    print("""
          ******************* PLEASE CHOOSE YOUR TYPE OF LOGIN ********************
          -------------------------------------------------------------------------
          ********** --------------------> 1. Admin <-------------------- **********
          
          ********** --------------------> 2. User  <-------------------- **********
          """)
    while ch != '3':
        
        ch = input("Please select your choice : ")
                 
        if ch == '1':
            obj = admin(1,1,1,1,1,1,1) 
            while True:
                choice = int(input("Enter \n1. Add Food \n2.View Food \n3.Edit Food \n4.Remove Food \n0.Exit : \n"))    
                obj1.execute(choice)
        if ch == '2':
            obj2 = user()
