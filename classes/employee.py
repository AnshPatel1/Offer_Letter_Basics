class Address:
    def __init__(self, building, street, area, state, country, pincode):
        self.address_line_1 = building + ','
        self.address_line_2 = street + ', ' + area + ','
        self.address_line_3 = f'{state}, {country}, {pincode}'


class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    def __init__(self, fname, lname, address):
        self.fname = fname
        self.lname = lname
        self.set_address(address)

    def set_address(self, address):
        self.address = address
        self.formatted_address = f'{self.address.address_line_1}\n{self.address.address_line_2}\n{self.address.address_line_3}'

    def set_job(self, job):
        self.job = job


# emp = Employee('Vishv', 'Patel', Address('Bhagyadev Flat', 'Nr. Sanjivani', 'Vastrapur', 'Gujarat', 'India', '380015'))
#
# print(f'Hi, {emp.fname} {emp.lname}\n'
#       f'{emp.formatted_address}')
