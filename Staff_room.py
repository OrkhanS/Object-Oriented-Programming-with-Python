
class Staff_room:
    def set(self, staff_id, first_name, last_name, office, tel):
        self.staff_id = staff_id
        self.first_name = first_name
        self.last_name = last_name
        self.office = office
        self.tel = tel

    def getDetailsStaff(self):
        return {"staff_id": self.staff_id, "first_name": self.first_name, "last_name": self.last_name, "office": self.office, "tel": self.tel}
