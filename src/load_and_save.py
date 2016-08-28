from convertions import *
from recipe_ingredient import *
from store_ingredient import *
from store import *
from recipe import *
from recipebook import *
from UI import *

class LoadAndSave(object):

    def __init__(self):
        
        self.convertions = Convert()

    def load_store(self, input):
        
        '''
        Returns store, that is loaded from given file (input).
        Raises errors, and possibly stops loading, if file isn't in valid form.
        '''
        
        try:
            file = open(input)
            current_line = ''.join(file.readline().strip()).lower()
            if current_line != "#store":
                print "File syntax error!"
                raise LoadAndSaveError("Invalid data.")
            name = ''.join(file.readline().strip())
            store = Store(name)
            current_line = ''.join(file.readline().strip()).lower()
            
            while current_line:

                if current_line == "#ingredient":
                    name = ''.join(file.readline().strip())
                    if name == '':
                        print "Every ingredient must have a name."
                        raise LoadAndSaveError("Invalid ingredient data.")
                    count = ''.join(file.readline().strip())
                    if self.convertions.check_count(count) == False:
                        print "Given count", count, "for", name.lower(), "not valid."
                        raise LoadAndSaveError("Invalid count data.")
                    date = ''.join(file.readline().strip())
                    if date == 'None':
                        date = None
                    elif date != None:
                        try:
                            y = int(date[0:4])
                            m = int(date[5:7])
                            d = int(date[8:10])
                            datetime.date(y, m, d)
                        except:
                            print "Given date", date, "for", name.lower(), "not valid."
                            raise LoadAndSaveError("Invalid date data.")
                    allergenic = ''.join(file.readline().strip())
                    if allergenic == 'None':
                        allergenic = None
                    density = ''.join(file.readline().strip())
                    if density == 'None' or not self.convertions.check_time_count(density):
                        density = None
                    ingredient = StoreIngredient(name, date, count, density, allergenic)
                    store.add_ingredient(ingredient)
                    current_line = ''.join(file.readline().strip()).lower()
        
                else:
                    current_line = ''.join(file.readline().strip()).lower()
                 
            file.close()
            return store
            
        except IOError:
            
            raise LoadAndSaveError("Invalid data.")
        
        
    def load_ingredients(self, input, store):
        
        '''
        Returns store, that is formed when given ingredient file's ingredients
        are added to it.
        Raises errors, and possibly stops loading, if file isn't in valid form.
        '''
        
        try:
            file = open(input)
            current_line = ''.join(file.readline().strip()).lower()
            while current_line:
                
                if current_line == "#ingredient":
                    name = ''.join(file.readline().strip())
                    if name == '':
                        print "Every ingredient must have a name."
                        raise LoadAndSaveError("Invalid ingredient data.")
                    count = ''.join(file.readline().strip())
                    if self.convertions.check_count(count) == False:
                        print "Given count", count, "for", name.lower(), "not valid."
                        raise LoadAndSaveError("Invalid count data.")
                    date = ''.join(file.readline().strip())
                    if date == 'None':
                        date = None
                    elif date != None:
                        try:
                            y = int(date[0:4])
                            m = int(date[5:7])
                            d = int(date[8:10])
                            datetime.date(y, m, d)
                        except:
                            print "Given date", date, "for", name.lower(), "not valid."
                            raise LoadAndSaveError("Invalid date data.")
                    allergenic = ''.join(file.readline().strip())
                    if allergenic == 'None':
                        allergenic = None
                    density = ''.join(file.readline().strip())
                    if density == 'None' or not self.convertions.check_time_count(density):
                        density = None
                    ingredient = StoreIngredient(name, date, count, density, allergenic)
                    store.add_ingredient(ingredient)
                    current_line = ''.join(file.readline().strip()).lower()
        
                else:
                    current_line = ''.join(file.readline().strip()).lower()
                 
            file.close()
            return store
            
        except IOError:
            
            raise LoadAndSaveError("Invalid data.")
                
                
        
        
    def load_recipes(self, input, system):
        
        
        '''
        Returns recipebook, that is formed when given recipe file's recipes
        are added to it.
        Raises errors, and possibly stops loading, if file isn't in valid form.
        '''
        
        try:
            
            file = open(input)
            current_line = ''.join(file.readline().strip()).lower()
                       
            while current_line:            
                
                if current_line != "#recipe":
                    print "File syntax error!"
                    raise LoadAndSaveError("Invalid data.")
                     
                elif current_line == "#recipe":
                    name = ''.join(file.readline().strip())
                    recipe = Recipe(name)
                    current_line = ''.join(file.readline().strip()).lower()
                    while current_line != "#recipe" and current_line:     
                        if current_line == "#ingredient":
                            name = ''.join(file.readline().strip())
                            if name == '':
                                print "Every ingredient must have a name."
                                raise LoadAndSaveError("Invalid ingredient data.")
                            count = ''.join(file.readline().strip())
                            if self.convertions.check_count(count) == False:
                                print "Given count", count, "for", name.lower(), "not valid."
                                raise LoadAndSaveError("Invalid count data.")
                            allergenic = ''.join(file.readline().strip())
                            if allergenic == 'None':
                                allergenic = None
                            density = ''.join(file.readline().strip())
                            if density == 'None' or not self.convertions.check_time_count(density):
                                density = None
                            ingredient = RecipeIngredient(name, density, allergenic)
                            recipe.add_ingredient(ingredient, count)
                            current_line = ''.join(file.readline().strip()).lower()
                        elif current_line == "#comment":
                            comment = []
                            current_line = ''.join(file.readline().strip()).lower()
                            while current_line and current_line[0] != "#":
                                comment.append(current_line)
                                current_line = ''.join(file.readline().strip()).lower()
                            recipe.comment = comment
                        elif current_line == "#other recipe":
                            x = 0
                            name = ''.join(file.readline().strip())
                            count = ''.join(file.readline().strip())
                            for r in system.recipes:
                                if r.get_name().lower() == name.lower():
                                    recipe.add_other_recipe(r, count)
                                    x += 1
                                    break
                                   
                            if x == 0:
                                print "Couldn't add recipe", name.lower(), "to recipe", recipe.get_name().lower(), "because it couldn't be found in recipebook."
                                print "Please notice that in a file to be loaded, it must have the recipe, that you want to add to another, first, before you can refer to it."
                            current_line = ''.join(file.readline().strip()).lower()
                        else:
                            current_line = ''.join(file.readline().strip()).lower()
                    
                    system.add_recipe(recipe)
                    
                else:
                    current_line = ''.join(file.readline().strip()).lower()
            
            file.close()
            return system
            
        except:
                        
            raise LoadAndSaveError("Invalid data.")
    
        
    def save_store(self, name, store):
        
        '''
        Saves the given store to text file with given name of the file.
        '''
        
        file = open(name, 'w')
        file.write("#Store\n")
        file.write(store.get_name() + '\n')
            
        for ingredient in store.ingredients:
            file.write("#Ingredient\n")
            file.write(ingredient.get_name() + '\n')
            file.write(ingredient.get_count() + '\n')
            if ingredient.get_expire_date() == None:
                file.write("None\n")
            elif ingredient.get_expire_date() != None:
                file.write(ingredient.get_expire_date() + '\n')
            if ingredient.get_allergenic_matter() == None:
                file.write("None\n")       
            elif ingredient.get_allergenic_matter() != None:
                file.write(ingredient.get_allergenic_matter() + '\n')
            file.write(str(ingredient.get_density()) + '\n')
    
        file.close()
        
    def save_ingredients(self, name, store):
        
        '''
        Saves the given store's ingredients to text file with given name of the file.
        '''
        
        file = open(name, 'w')
        for ingredient in store.ingredients:
            file.write("#Ingredient\n")
            file.write(ingredient.get_name() + '\n')
            file.write(ingredient.get_count() + '\n')
            if ingredient.get_expire_date() == None:
                file.write("None\n")
            elif ingredient.get_expire_date() != None:
                file.write(ingredient.get_expire_date() + '\n')
            if ingredient.get_allergenic_matter() == None:
                file.write("None\n")       
            elif ingredient.get_allergenic_matter() != None:
                file.write(ingredient.get_allergenic_matter() + '\n')
            file.write(str(ingredient.get_density()) + '\n')
        file.close()
        
        
    def save_recipes(self, name, system):
        
        '''
        Saves the given recipebook's (system) recipes to text file with given name of the file.
        '''
        
        file = open(name, 'w')
        
        for recipe in system.recipes:
            file.write("#Recipe\n")
            file.write(recipe.get_name() + '\n')
            for ingredient in recipe.ilist:
                file.write("#Ingredient\n")
                file.write(ingredient.get_name() + "\n")
                file.write(recipe.ingredients[ingredient] + "\n")
                if ingredient.get_allergenic_matter() == None:
                    file.write("None\n")
                elif ingredient.get_allergenic_matter() != None:
                    file.write(ingredient.get_allergenic_matter() + "\n")
                file.write(str(ingredient.get_density()) + "\n")
            for recipe2 in recipe.rlist:
                file.write("#Other Recipe\n")
                file.write(recipe2.get_name() + "\n")
                file.write(recipe.recipes[recipe2] + "\n")
            file.write("#Comment\n")
            file.write(recipe.get_comment() + "\n")   
                 
        file.close()
                
            
class LoadAndSaveError(Exception):
    
    '''
    This is called if there occurs some not valid forms in files.
    '''

    def __init__(self, message):
        super(LoadAndSaveError, self).__init__(message)     
        