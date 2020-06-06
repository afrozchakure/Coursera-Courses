class PartyAnimal:
    x = 0
    
    def __init__(self):  # Constructor
        print('I am constructed')
        
    def party(self):
        self.x = self.x + 1
        print('So far', self.x)
        
    def __del__(self):  # Destructor
        print('I am destructed', self.x)
        
an = PartyAnimal()
an.party()
an.party()
an = 42  # This code calls the destructor
print('an contains', an)

# After the end of the program the destructed message is 
# called or it will be called when the object variable
# is assigned a new value
