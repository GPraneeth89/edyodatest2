class Su_user:
    
    d={}
    reg={
        "Mon":["Chest","Chest","Chest","Chest"],
        "Tue":["Biceps","Biceps","Biceps","Biceps"],
        "Wed":["Rest","Cardio/Abs","Abs/Cardio","Cardio"],
        "Thu":["Back","Back","Back","Back"],
        "Fri":["Triceps","Triceps","Triceps","Triceps"],
        "Sat":["Rest","Legs","Legs","Cardio"],
        "Sun":["Rest","Rest","Cardio","Cardio"]
    }
    def CreatUser(self,name,age,gender,num,mail,BMI,duration):
        self.name=name
        self.age=age
        self.gender=gender
        self.num=num
        self.mail=mail
        self.BMI=BMI
        self.duration=duration
        Su_user.d[self.num]={
            "name":self.name,
            "age":self.age,

            "gender":self.gender,
            "Phone Number":self.num,
            "Mail":self.mail,
            "BMI":self.BMI,
            "Membership Plan":self.duration
            }
        # print(Su_user.d)



    def DeleteUser(self,num):
        Su_user.d.pop(num)
        # print(Su_user.d)



    def UpdateMember(self,num,plan,v):
        if v==1:
            Su_user.d[num]["Membership Plan"]+=plan
        elif v==2:
            Su_user.d[num]["Membership Plan"]=0
        # print(Su_user.d)



    def ViewUser(self,num):
        
        try:
            a=Su_user.d[num]
            for k,v in a.items():
                if k!="Regimen":
                    print(str(k)+" :"+str(v))
        except:
            print("User Not found")



    def CreateRegimen(self,num):
        temp=Su_user.d[num]["BMI"]
        if temp<18.5:
            Su_user.d[num]["Regimen"]={k:v[0] for k,v in Su_user.reg.items()}
        elif temp<25:
            Su_user.d[num]["Regimen"]={k:v[1] for k,v in Su_user.reg.items()}
        elif temp<30:
            Su_user.d[num]["Regimen"]={k:v[2] for k,v in Su_user.reg.items()}
        elif temp>30:
            Su_user.d[num]["Regimen"]={k:v[3] for k,v in Su_user.reg.items()}
        # print(Su_user.d)



    def ViewRegimen(self,num):
        try:
            for k,v in Su_user.d[num]["Regimen"].items():
                print(str(k)+" : "+str(v))
        except:
            print("User Has no Regimen")



    def DeleteRegimen(self,num):
        Su_user.d[num].pop("Regimen")
        # print(Su_user.d[num])


    def UpdateRegimen(self,num,BMI):
        
        tp=BMI
        Su_user.d[num]["BMI"]=BMI
        if tp<18.5:
            Su_user.d[num]["Regimen"]={k:v[0] for k,v in Su_user.reg.items()}
        elif tp<25:
            Su_user.d[num]["Regimen"]={k:v[1] for k,v in Su_user.reg.items()}
        elif tp<30:
            Su_user.d[num]["Regimen"]={k:v[2] for k,v in Su_user.reg.items()}
        elif tp>=30:
            Su_user.d[num]["Regimen"]={k:v[0] for k,v in Su_user.reg.items()}
        # print(Su_user.d[num])





