from reg import *
if __name__=="__main__":
    super_id_pass={"gpraneeth621@gmail.com":"12345678"}
    obj=Su_user()
    
    while True:
        print("Login \n 1-Admin \n 2-Normal User")
        n=int(input())
        if n==1:
            user=input("Enter Email Id")
            password=input("Enter password")
            if user in super_id_pass and super_id_pass[user]==password:
                print("Login success as super user")
                print("Choose the function for operation")
                while True:
                    print(" 1 Create Member \n 2 View Member \n 3 Delete Member \n 4 Update Member \n 5 Create Regimen \n 6 View Regimen \n 7 Delete Regimen \n 8 Update Regimen \n 0 Logout")
                    choose_function=int(input())
                    if choose_function==1:
                        # Create Member
                        name=input("Enter Name")
                        age=input("Enter Age")
                        gender=input("Enter Gender")
                        num=input("Enter Mobile Number")
                        mail=input("Enter Email")
                        BMI = float(input("Enter BMI"))
                        duration = int(input("Please enter how many months membership is need from 1 ,3,6,12"))
                        obj.CreatUser(name=name,age=age,gender=gender,num=num,mail=mail,BMI=BMI,duration=duration)
                
                    elif choose_function==2:
                        # View Member
                        obj.ViewUser(num=input("Enter Phone Number to see User details"))
                    elif choose_function==3:
                        # Delete Member
                        obj.DeleteUser(num=input("Enter phone  Number of theb user to delete "))

                    elif choose_function==4:
                        print(" 1 Extend membership \n 2 Cancel Membership")
                        option=int(input())
                        num=input("Enter the Phone Number  to Update Plan")
                        
                        if option==1:
                            plan=int(input("How many month user wants to extend"))
                        else:
                            plan=0
                        obj.UpdateMember(num=num,plan=plan,v=option)
        

                    elif choose_function==5:
                        # Create Regimen
                        obj.CreateRegimen(num=input("Enter User number to create regimen"))
                    elif choose_function==6:
                        # View Regimen
                        obj.ViewRegimen(num=input("Enter the user number to view user's Regimen"))
                    elif choose_function==7:
                        # Delete Regimen
                        obj.DeleteRegimen(num=input("Enter the user's number to delete User's Regimen"))
                    elif choose_function==8:
                        # Update Regimen
                        num=input("Enter Number of User's")
                        BMI=int(input("Enter new BMI of User"))
                        obj.UpdateRegimen(num=num,BMI=BMI)
                    elif choose_function==0:
                        break
            else:

                print("enter Again")

        elif n==2:
            check_id=input("enter email id ")
            check_pass=input("enter passoword")
            while True:
                
                id_pass={"ptsp@gmail.com":"12345678","mwe1245@gmail.com":"12345678"}
                
                if check_id in id_pass and id_pass[check_id]==check_pass:

                    option=int(input("1 Show Profile\n2 Show Regimen\n0 logout"))
                    if option==0:
                        break
                    num=input("Enter your phone number")
                    try:
                        if option==1:
                            obj.ViewUser(num=num)
                        elif option==2:
                            obj.ViewRegimen(num=num)
                        else:
                            break
                    except:
                        print("User doesmot exists")
                else:
                    print("enter again")
        else:
            break

# {
# '7989656579': {
# 'name': 'Praneeth', 
# 'age': '21', 'gender': 'M', 
# 'Phone Number': '7989656579', 
# 'Mail': 'gpraneeth2734@gmail.com', 
# 'BMI': 18.5, 'Membership Plan': 3, 
# 'Regimen': {
# 'Mon': 'Chest', 
# 'Tue': 'Biceps', 
# 'Wed': 'Cardio/Abs', 
# 'Thu': 'Back',
#  'Fri': 'Triceps',
#  'Sat': 'Legs', 
# 'Sun': 'Rest'}
# }
# }


        
