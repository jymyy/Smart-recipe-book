class RecipeIngredient():


    def __init__(self, name, density, allergenic):
        
        '''
        Saves the given values for RecipeIngredient.
        If density is set to None, it is here set to default value of 1.
        '''
        
        self.name = name
        self.allergenic = allergenic
        self.density = density
        if density == None:
            self.density = 1
        
            
    def get_name(self):
        
        '''
        Returns name of the ingredient.
        '''
        
        return self.name
    
    def get_density(self):
        
        '''
        Returns the density of the ingredient.
        '''
        
        return self.density
                     
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
    
    