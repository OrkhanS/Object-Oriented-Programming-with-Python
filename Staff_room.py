from random import randint

class Staff_room:  
    def set_staff(self, first_name, last_name, office, tel):
        flag = 0
        while(flag == 0):
            s_id = str(randint(100000, 999999))
            with open('staff.txt') as f:
                    if s_id not in f.read():
                        flag = 1
                        self.staff_id = s_id
        if len(str(tel)) != 4 or office[:2] != 'A-' or len(office[2:]) != 3:
            return
        self.first_name = first_name
        self.last_name = last_name
        self.office = office
        self.tel = tel

        f=open("staff.txt", "a+")
        f.write("\n"+s_id+' '+first_name+" "+last_name+" "+ office+" "+str(tel))
