from abc import ABC, abstractmethod
from datetime import datetime

class Ride_sharing:
    def __init__(self,company_name) -> None:
        self.company_name = company_name
        self.riders = []
        self.drivers = []
        self.rides = []
    
    def add_rider(self,rider):
        self.riders.append(rider)
    
    def add_drivers(self,driver):
        self.drivers.append(driver)
    
    
    def __repr__(self) -> str:
        return f'{self.company_name} with riders: {len(self.riders)} with drivers: {len(self.drivers)}'


class User(ABC):
    def __init__(self,name,email,NID) -> None:
        self.name = name 
        self.email = email
        self.NID = NID
        self.wallet = 0
        self.__id = 0
    @abstractmethod
    def display(self):
        raise NotImplementedError

class Rider(User):
    def __init__(self, name, email, NID,current_location,initial_amount) -> None:
        super().__init__(name, email, NID)
        self.current_location = current_location
        self.wallet = initial_amount
        self.current_ride = None

    def display(self):
        print(f'riders name: {self.name} and email: {self.email}')
    
    def load_cash(self,amount):
        if amount > 0:
            self.wallet += amount

    def update_location(self,current_location):
        self.current_location = current_location
    
    def request_ride(self,ride_sharing,destination):
        if not self.current_ride:
            ride_request = Ride_Request(self,destination)
            ride_matcher = Ride_Matching(ride_sharing.drivers)
            ride = ride_matcher.find_driver(ride_request)

class Driver(User):
    def __init__(self, name, email, NID,current_location) -> None:
        self.current_location = current_location
        self.wallet = 0
        super().__init__(name, email, NID)
        

    def display_profile(self):
        print(f'Driver with name: {self.name} and email: {self.email}')
    
    def accept_ride(self,ride):
        ride.set_driver(self)

class Ride_Request:
    def __init__(self,rider,end_location) -> None:
        self.rider = rider
        self.end_location = end_location



class Ride_Matching:
    def __init__(self,drivers) -> None:
        self.available_drivers = drivers

    def find_driver(self,ride_request):
        if len(ride_request.drivers) > 0:
            driver = self.available_drivers[0]
            ride = Ride(ride_request.rider.current_location,ride_request.end_location)
            driver.accept_ride(ride)
            return ride
        
class Ride:
    def __init__(self,start_location,end_location) -> None:
        self.start_location = start_location
        self.end_location = end_location
        self.driver = None
        self.rider = None
        self.start_time = None
        self.end_time = None
        self.estimated_fare = None


        def set_driver(self,driver):
            self.driver = driver
    

    def start_ride(self):
        self.start_time = datetime.now()

    def end_ride(self,amount):
        self.end_time = datetime.now()
        self.rider.wallet -= self.estimated_fare
        self.driver.wallat += self.estimated_fare
    
    def __repr__(self) -> str:
        return f'Ride details. Started: {self.start_location} to {self.end_location}'
    

niye_jao = Ride_sharing('NIye_jao')

sakib = Rider("sakib", 'sakib@khan.com',1234,'mohakhali',1200)

niye_jao.add_rider(sakib)

sohag = Driver('sohag','sohag@ali.com',234,'gulshan 1')
niye_jao.add_drivers(sohag)

print(niye_jao)

sakib.requenst_ride(niye_jao, 'uttara')
sakib.show_current_ride()
        
        
