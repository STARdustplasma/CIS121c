
## 1
## Address is a class that asks for street, city, country, and state as strings, and a zipcode as an integer. 
## The Address class has 5 methods, getAddress(), getCity(), getZipcode(), getState(), and getCountry()
## Person is a child class of Address but does not call to it. The Person class asks for name, phone number, and email address as strings. 
## Student and Teacher are child classes of Person.
## Student class asks for the student number of the person as an integer and the gpa of the person as a float. It has two methods, getGPA() and getstudentNumber()
## Teacher class asks for the teachers ID, workhours, work rate, and years of service as integers. It has 5 methods, getteacherID(), getworkhours(), getwork_rate(), getYearsOfService(), calculateYearlySalary()


## 2
## Address is a parent class because Person inherits from it. Person is a parent class because Student and Teacher inherit from it. 
## Student and Teacher are child classes because they both inherit from Person. Person is a child class of Address.


## 3
class Address :
    def __init__(self, street, city, state, zipcode, country) :
        self.street = street
        self.city = city
        self.country = country
        self.state = state
        self.zipcode = zipcode

    def getAddress(self) :
        return f'{self.street}, {self.city}, {self.state}, {self.zipcode}, {self.country}'

    def getCity(self) :
        return f'{self.city}'
    
    def getZipcode(self) :
        return f'{self.zipcode}'

    def getState(self) :
        return f'{self.state}'

    def getCountry(self) :
        return f'{self.country}'

    def __str__(self) :
        print('===Address===')
        print(f'Street : {self.street}')
        print(f'City : {self.city}')
        print(f'State : {self.state}')
        print(f'Zip Code : {self.zipcode}')
        print(f'Country : {self.country}')
        return '============='

class Person(Address) :
    def __init__(self, name, phoneNumber, emailAddress, street, city, state, zipcode, country):
        super().__init__(street, city, state, zipcode, country)
        self.name = name
        self.phone = phoneNumber
        self.email = emailAddress

    def __str__(self):
        print('===Person====')
        print(f'Name : {self.name}')
        print(f'Phone Number : {self.phone}')
        print(f'Email Address : {self.email}')
        super().__str__()
        return '============='

class Student(Person) :
    def __init__(self, name, phoneNumber, emailAddress, studentNumber, GPA, street, city, state, zipcode, country):
        super().__init__(name, phoneNumber, emailAddress, street, city, state, zipcode, country)
        self.ID = studentNumber
        self.gpa = GPA
    
    def getGPA(self) :
        return f'{self.gpa}'

    def getStudentNumber(self) :
        return f'{self.ID}'

    def __str__(self):
        super().__str__()
        print('===Student===')
        print(f'Student Number : {self.ID}')
        print(f'GPA : {self.gpa}')
        return '============='
    
class Teacher(Person) :
    def __init__(self, name, phoneNumber, emailAddress, teacherID, workHours, work_rate, YearsOfService,street, city, state, zipcode, country):
        super().__init__(name, phoneNumber, emailAddress, street, city, state, zipcode, country)
        self.ID = teacherID
        self.hours = workHours
        self.rate = work_rate
        self.years = YearsOfService
    
    def getTeacherID(self) :
        return f'{self.ID}'

    def getworkhours(self) :
        return f'{self.hours}'

    def getwork_rate(self) :
        return f'{self.rate}'

    def getYearsOfService(self) :
        return f'{self.years}'

    def calculateYearlySalary(self) :
        return self.hours * self.rate * 52

    def __str__(self):
        super().__str__()
        print('===Teacher===')
        print(f'Teacher ID : {self.ID}')
        print(f'Work Hours : {self.hours}')
        print(f'Pay Rate : {self.rate}')
        print(f'Years of Service : {self.years}')
        print(f'Yearly Salary : {self.calculateYearlySalary()}')
        return '============='


x = Address('street ave', 'town city', 'MN', 56001, 'USA')
y = Person('tom','1231231234', 'email123@email.com', 'street ave', 'town city', 'MN', 56001, 'USA')
z = Student('tim','3213214321', 'email321@email.com', 123123, 3.6, 'ave street', 'town city', 'MN', 55106, 'USA')
a = Teacher('tam','5675675678', 'email567@email.com', 567567, 40, 26, 3, 'street apt', 'town city', 'MN', 55602, 'USA')
print(a)