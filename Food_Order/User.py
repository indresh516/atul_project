import json as js
import datetime as dt

class user:
    profile = {}
    def __init__(self,full_name,phone_number,address,email,password):
        self.full_name = full_name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.password = password

                
    def sign_up(self):
        self.full_name = input("Please Enter your name : ")
        print(f"""
              <-><-><-><-><-> ********** Welcome to A and C Cafe Restaurant ********** <-><-><-><-><->
              ----------------------------------------------------------------------------------------
            
              ********** Hello {self.full_name} Please complete creating your profile below **********
              ________________________________________________________________________________________
              ----------------------------------------------------------------------------------------
              <-><-><-><-><-><-><-><-> ************************************** <-><-><-><-><-><-><-><->
               
              """)        
        self.phone_number = input("Enter your Phone Number : ")
        self.address = input("Enter your complete Address : ")
        self.email = input("Enter your Email Addres : ")
        self.password = input("Please create a log in password : ")
        self.profile[self.full_name] = [self.phone_number,self.address,self.phone_number,self.email,self.password]
        print(self.profile)
        f = open('profile.json','w')
        data = js.dump(self.profile,f)
        print(data)
        print("Your profile is now created")
        f.close()
            
    def log_in(self):
        
        password = input("Enter your password : ")
        f = open('profile.json')
        data = js.load(f)
        #print(data)
        f.close()
        
        for (k,v) in data.items():
            if str(v[4]) == password:
                print("login Successfull")
                print(f"""
              <-><-><-><-><-> ********** Welcome to A and C Cafe Restaurant ********** <-><-><-><-><->
              ----------------------------------------------------------------------------------------
            
              Hello {k} You have now successfully Logged Into our system 
              
              ________________________________________________________________________________________
              ----------------------------------------------------------------------------------------
              <-><-><-><-><-><-><-><-> ************************************** <-><-><-><-><-><-><-><->
               
              """)
                print("key: " + k)
                print("value: "+ str(v))
            else:
               print("Invalid Credentials")
        
        

        
    def new_order(self):
        f = open("Menu.json",'r+')
        data = js.load(f)
        f.close()
        
        for (k,v) in data.items():
            print("Food ID: " + k)
            print((v)[0],(v)[1],(v)[2])
    
 





#print("""
 #     Please choose one of the option given below
  #    
   #   1. To create an account
    #  2. To login to the account
     # 
      #""")
#obj = user(1,1,1,1,1)
#obj.new_order()
#ch = int(input("Please type in an option from above given one : "))    
#if ch == 1:    
 #   obj.sign_up()
#if ch == 2:
 #   obj.log_in()