from convertions import *
from store import *
from recipe import *


class RecipeBook():
    
    def __init__(self):
        
        '''
        Holds the lists of recipes and stores in RecipeBook.
        '''
        
        self.recipes = []
        self.stores = []
        self.convertions = Convert()
    
    
    def get_recipes(self):
        
        '''
        Returns all the recipes that RecipeBook includes.
        If RecipeBook hasn't recipes, the user is informed.
        '''
        
        list = []
        if len(self.recipes) > 0:
            for recipe in self.recipes:
                list.append(recipe.get_name())
            return ', '.join(list)
        else:
            return "You don't have recipes yet." 
        
    def add_recipe(self, recipe):
        
        '''
        Adds the given recipe to RecipeBook.
        Checks if the RecipeBook already has recipe by same name as the given one.
        If it has, asks for the user, whether he/she likes to overwrite the old one.
        '''
        
        x = 0
        for r in self.recipes:
            if r.get_name().lower() == recipe.get_name().lower():
                print "Given recipe", r.get_name().lower(), "is already in recipebook."
                question = raw_input("Do you want to overwrite the old one? Y/N")
                y = 0
                while y == 0:
                    if question.lower() == 'y':
                        y += 1
                        self.delete_recipe(r)
                    elif question.lower() == 'n':
                        y += 1
                        x += 1
                    else:
                        question = raw_input("Only Y or N are valid answers.")
        
        if x == 0:
            self.recipes.append(recipe)
    
    def add_store(self, store):
        
        '''
        Adds given store to the RecipeBook.
        '''
        
        self.stores.append(store)
        
    def add_other_recipe_to_other(self, where, toadd, count):
        
        '''
        Adds given recipe (toadd) to another (where) by multiplying count (count).
        '''
        
        for recipe in self.recipes:
            if toadd.lower() == recipe.get_name().lower():
                if where.add_other_recipe(recipe, count):
                    return True
                    break
                else:
                    return False
        print toadd, "couldn't be found in your recipebook."
        return False
        
    def enough_ingredients(self, recipe, store):
        
        '''
        Checks if given store has enough ingredients for given recipe.
        Returns True if it has, False if it hasn't.
        '''
        
        x = 0
        y = 0
        
        for r in self.recipes:
            name = r.get_name()
            if recipe.lower() == name.lower():
                recipe = r
                x = 1
                break
            
        for s in self.stores:
            name = s.get_name()
            if store.lower() == name.lower():
                store = s
                y = 1
                break
        
        if x == 1 and y == 1:
            for s in store.ingredients:
                for r in recipe.get_ingredients().split(', '):
                    if r not in store.get_ingredients_without_counts().split(', '):
                        return False
                sname = s.get_name()
                counts = s.get_count()
                countr = recipe.get_count_of_ingredient(sname)
                if countr != 0:
                    counta = self.convertions.convert_a_to_b(s, counts, countr)
                    if not counta or not self.convertions.a_enough_for_b(counta, countr):
                        return False
                    
        if y == 1 and len(store.ingredients) > 0:
            return True
        else:
            return False
    
    def can_prepare(self, store):
        
        '''
        Returns the list of all the recipes that is available to prepare with given store.
        '''
        
        list = []
        for recipe in self.recipes:
            if self.enough_ingredients(recipe.get_name(), store):
                list.append(recipe.get_name())           
                                     
        return list
    
    
    def recipes_without(self, allergenic):
        
        '''
        Returns the list of all the recipes without given allergenic.
        '''
        
        list = []
        for recipe in self.recipes:
            if not recipe.recipe_has_allergenic(allergenic):
                list.append(recipe.get_name())
                              
        return list
               
        
    def store_in_date(self, store):
        
        '''
        Checks expire dates of the ingredients of given store.
        '''
        
        return store.check_dates()
    
    def modified_recipe(self, recipe):
        
        '''
        Removes old recipe, with same name as the new modified recipe, from the RecipeBook and other recipes that include it.
        Then adds this modified recipe everywhere the old one was found.
        '''
        
        for r in self.recipes:
            if r.get_name().lower() == recipe.get_name().lower():
                recipe1 = r
                break
        for r in self.recipes:
            if len(r.rlist) > 0:
                for r2 in r.rlist:
                    if r2.get_name().lower() == recipe1.get_name().lower():
                        count = r.recipes[r2]
                        r.rlist.remove(r2)
                        del r.recipes[r2]
                        r.recipes[recipe] = count
                        r.add_other_recipe(recipe, count)
        self.recipes.remove(recipe1)
        self.add_recipe(recipe)
            
    def delete_recipe(self, recipe):
        
        '''
        Removes given recipe from RecipeBook and other recipes that include it.
        '''

        for r in self.recipes:
            if len(r.rlist) > 0:
                for r2 in r.rlist:
                    if r2.get_name() == recipe.get_name():
                        r.rlist.remove(r2)
                        del r.recipes[r2]
        self.recipes.remove(recipe)
        
    
    def recipes_without_n(self, store, count):
        
        '''
        Returns the list of all the recipes from where given store lacks given count
        of ingredients.
        '''
        
        y = 0
        recipes = []
        for s in self.stores:
            if s.get_name().lower() == store.get_name().lower():
                store = s
                y += 1
                break
        if y == 1:
            for r in self.recipes:
                rilist = []
                x = 0
                for i in r.ilist:
                    rilist.append(i.get_name().lower())
                for r2 in r.rlist:
                    for ingredient in r2.ilist:
                        if ingredient.get_name().lower() not in rilist:
                            rilist.append(ingredient.get_name().lower())
                for i in store.ingredients:
                    if i.get_name().lower() in rilist:
                        x += 1
                if len(rilist) - x <= int(count):
                    recipes.append(r.get_name())
                    
        return recipes
                    
    
    
    def recipes_with_ingredients(self, ingredientlist):
        
        '''
        Returns the list of the recipes, that includes all the ingredients
        in given ingredientlist.
        '''
        
        recipes = []
        for r in self.recipes:
            rilist = []
            x = 0
            for i in r.ilist:
                rilist.append(i.get_name().lower())
            for r2 in r.rlist:
                for ingredient in r2.ilist:
                    if ingredient.get_name().lower() not in rilist:
                        rilist.append(ingredient.get_name().lower())
            for i in ingredientlist:
                if i.lower() in rilist:
                        x += 1
            if len(ingredientlist) == x:
                recipes.append(r.get_name())
                    
        return recipes
