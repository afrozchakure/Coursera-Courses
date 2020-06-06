class PartyAnimal:
    x = 0  # Each PartyAnimal object has a bit of data
    
    def party(self):  # Each party animal has a bit of code
        self.x = self.x + 1
        print('So far', self.x)
        
an = PartyAnimal()  # Construct a PartyAnimal object and store in variable

an.party()  # Tell the object to run party() code
an.party()  # ===> PartyAnimal.party(an)
an.party()
print('Type = ', type(an), end = '\n\n')
print('Dir = ', dir(an), end = '\n\n')  # dir() command is used to find the 'capabilities' of our newly created class

