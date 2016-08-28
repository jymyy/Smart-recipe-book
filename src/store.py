from store_ingredient import *
from convertions import *

class Store():

    def __init__(self, name):
        
        '''
        Saves the given value for Store.
        Holds the list of the ingredients in Store.
        '''

        self.ingredients = []
        self.name = name
        self.convertions = Convert()
        
        
    def get_name(self):
        
        '''
        Returns the name of the Store.
        '''
        
        return self.name
        
    def add_ingredient(self, ingredient):
        
        '''
        Adds ingredient to Store, which means, it is appended to the list self.ingredients.
        Checks if ingredient already exists in store (is there a ingredient by same name in store)
        if there is, their counts (which are first converted to same units) are summed, and 
        ingredient's expire date is set to one, which is first going to expire.
        If ingredients' counts couldn't be converted to same (look up for class Convertions function convert_a_to_b),
        only the older one remains in Store, and the new one won't be added.
        '''
    
        x = 0
        for i in self.ingredients:
            if i.get_name().lower() == ingredient.get_name().lower():
                counta = self.convertions.convert_a_to_b(i, i.get_count(), ingredient.get_count())
                if counta:
                    i.count = self.convertions.add_a_to_b(counta, ingredient.get_count())
                    i.name = i.get_name()
                    if ingredient.get_expire_date() != None and i.get_expire_date() != None:
                        if i.get_expire_date() < ingredient.get_expire_date():
                            i.date = i.get_expire_date()
                        else:
                            i.date = ingredient.get_expire_date()
                    else:
                        if ingredient.get_expire_date() == None:
                            i.date = i.get_expire_date()
                        elif i.get_expire_date() == None:
                            i.date = ingredient.get_expire_date()
                    if ingredient.get_density() == 1:
                        i.density = i.get_density()
                    else:
                        i.density = ingredient.get_density()
                    if ingredient.get_allergenic_matter() == None:
                        i.allergenic = i.get_allergenic_matter()
                    else:
                        i.allergenic = ingredient.get_allergenic_matter()
                    x += 1
                    break
                else:
                    x += 1
                    print ingredient.get_name(), "already exists in your store. With given count's units, it couldn't be summed with previous ingredient's count."
                    break
        if x == 0:
            self.ingredients.append(ingredient)
        
    def get_rid_of(self, ingredient):
        
        '''
        Removes the given ingredient from Store.
        '''
        
        self.ingredients.remove(ingredient)
            
    def get_ingredients(self):
        
        '''
        Returns ingredients' names and their counts.
        '''
        
        list = []
        
        for ingredient in self.ingredients:
            list.append(str(ingredient.get_name().lower()) + ' ' + str(ingredient.get_count()))
        
        list.sort()
        return ', '.join(list)
    
    def get_ingredients_without_counts(self):
        
        '''
        Returns only ingredients' names.
        '''
        
        list = []
        
        for ingredient in self.ingredients:
            list.append(ingredient.get_name().lower())
        
        list.sort()
        return ', '.join(list)
    
    def get_count_of_ingredient(self, ingredient):
        
        '''
        Returns the count of the given ingredient.
        If Store doesn't include given ingredient, the user is informed of this.
        '''
        
        for i in self.ingredients:
            if i.get_name().lower() == ingredient.lower():
                return i.get_count()
        return "You don't have", ingredient.lower(), "in store."
            
    def check_dates(self):
        
        '''
        Checks the dates of the ingredients in Store, using the ingredients'
        function is_expired.
        In every case, ingredient's expire date is expired, asks whether
        to remove ingredient from Store or not.
        '''
        
        x = 0
        if len(self.ingredients) == 0:
            print "Your store is empty."
        while x < len(self.ingredients):
            if self.ingredients[x].is_expired() == True:
                print "Get rid of", self.ingredients[x].name.lower(), "? Y/N"
                answer = raw_input("").lower()
                if answer == "y":
                    print "Getting rid of", self.ingredients[x].name.lower() + "." 
                    self.get_rid_of(self.ingredients[x])
                    x -= 1
                elif answer == "n":
                    None
                else:
                    x -= 1
                    print "Only answer Y or N is valid."
            x += 1
        return "Dates checked."
            
            
    def ingredients_without(self, allergenic):
        
        '''
        Returns all the ingredients' names, which don't include given allergenic.
        '''
        
        list = []
        if not self.ingredients:
            return "Your store is out of ingredients."
        for ingredient in self.ingredients:
            a = ingredient.get_allergenic_matter()
            if  a == None or a.lower() != allergenic.lower():
                list.append(ingredient.get_name().lower())
        
        list.sort()
        return ', '.join(list)
        
        
        
        
        
        

        
    
        