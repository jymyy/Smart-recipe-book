import datetime
from store import *


class StoreIngredient():


    def __init__(self, name, date, count, density, allergenic):
        
        '''
        Saves the given values for StoreIngredient.
        If density is set to None, it is here set to default value of 1.
        '''
        
        self.name = name
        self.date = date
        self.count = count
        self.allergenic = allergenic
        self.density = density
        if density == None:
            self.density = 1
 

    def get_name(self):
        
        '''
        Returns the name of the ingredient.
        '''
        
        return self.name
    
    def get_expire_date(self):
        
        '''
        Returns the expire date of the ingredient.
        '''
        
        return self.date
    
    def get_count(self):
        
        '''
        Returns the count of the ingredient.
        '''
        
        return self.count
                    
    def is_allergenic(self):
        
        '''
        Returns True if the ingredient contains allergenic matter.
        Returns False if the ingredient doesn't contain allergenic matter.
        '''
        
        if self.allergenic:
            return True
        else:
            return False
        
    def get_allergenic_matter(self):
        
        '''
        Returns the allergenic matter of the ingredient.
        '''
        
        return self.allergenic
    
    def get_density(self):
        
        '''
        Returns the density of the ingredient.
        '''
        
        return self.density
        
    def is_expired(self):
        
        '''
        Returns True, if the expire date of the ingredient has passed.
        Returns False, if the expire date of the ingredient hasn't passed.
        In other words, checks if the ingredient's given date is expired.
        '''
    
        if self.date == None:
            return False
        y = int(self.date[0:4])
        m = int(self.date[5:7])
        d = int(self.date[8:10])
        tuote = datetime.date(y, m, d)
        today = datetime.date.today()
        if tuote - today > datetime.timedelta(0, 0):
            return False
        elif tuote - today < datetime.timedelta(0, 0):
            print self.name, "expired", (today - tuote).days, "days ago."
            return True
                    
    
    
    