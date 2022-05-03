class Job:
    def __init__(self, salary, da, ta, hq, health_insurance, position):
        self.salary = int(salary)
        self.daily_allowance = int(da)
        self.travel_allowance = int(ta)
        self.headquarters = hq
        self.health_insurance = health_insurance
        self.position = position
        self.is_open = True
        self.is_accepted = False

    def cancel_job(self):
        self.is_open = False

    def close_job(self, accepted_by):
        self.is_open = False
        self.is_accepted = True
        self.accepted_by = accepted_by


class Offerer:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def __init__(self, name, position, sign):
        self.name = name
        self.position = position
        self.signature = sign

    def upload_signature(self, sign):
        self.signature = sign


class Company:
    def __init__(self, name):
        self.company_name = name
        self.jobs = []
        self.headquarters = []
        self.offerers = []

    def add_job(self, job):
        c = Job(0, 0, 0, 0, 0, 0)
        if type(job) == type(c):
            self.jobs.append(job)
        else:
            print('Invalid object')

    def add_headquarter(self, name):
        if name not in self.headquarters:
            self.headquarters.append(name)
        else:
            print('Already Exists')

    def add_offerer(self, offerer):
        c = Offerer('x', 'x', 'x')
        if type(offerer) == type(c):
            self.jobs.append(offerer)
        else:
            print('Invalid object')


co = Company("meta")
co.add_offerer(Offerer('Ansh', "Pattawalo", '🧚🏻‍♂️'))
