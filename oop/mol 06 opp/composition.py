class Engine:
    def __init__(self) -> None:
        pass
    def start(self):
        return "Engine started"



#car has a engine
class Car:
    def __init__(self) -> None:
        self.engine = Engine()
        self.driver = Driver()




class CPU:
    def __init__(self,cores) -> None:
        self.cores = cores

class RAM:
    def __init__(self,size) -> None:
        self.size=size
class HardDrive:
    def __init__(self,capacity) -> None:
        self.capacity = capacity


class Computer:
    def __init__(self,cores,ram_size,hd_capacity) -> None:
        self.cpu = CPU(cores)
        self.ram = RAM(ram_size)
        self.hard_disc = HardDrive(hd_capacity)

mac = Computer()
        
        
        
        