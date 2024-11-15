# define a class called VirtualPet with the following fields:
# (1) name - the name of the pet
# (2) energy - the enery points for the pet, default value is 10
# (3) hunger - the pet's hunger level, default value is 0
# When an instance of VirtualPet is created, only the name is needed
# for the __init__ method

class VirtualPet:
    def __init__(self,name):
        self.name=name
        self.energy=10
        self.hunger=0

    def play(self):
        if self.energy<2:
            print("Too tired to play")
        else:
            self.energy-=2
            self.hunger+=2

    def feed(self):
        self.hunger=max(0,self.hunger-3)

    def sleep(self):
        self.energy+=10

    def __str__(self):
        return f"{self.name} with {self.energy} energy points and {self.hunger} hunger level"

# this class has the following methods:
# (1) play() - simulate playing by reducing the energy by 2 and increase the hunger by 2
#     each time this method is called. If insufficient energy, prints "Too tired to play"
# (2) feed() - to simulate feeding the pet and reducing hunger by reducing hunger by the formula
#     hunger = max(0, hunger - 3). If hunger is less than 0, the pet is overfeed (which is possible)
# (3) sleep() - let the pet sleep to restore energy by increasing the energy by 10.
# (4) __str__ - returns the details of the pet in the format "pet_name with x energy points and y hunger level", 
#     e.g., Timmy with 100 energy points and 0 hunger level
