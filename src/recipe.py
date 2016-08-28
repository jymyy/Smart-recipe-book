from recipe_ingredient import *
from store import *
from convertions import *
from recipebook import *

class Recipe():


    def __init__(self, name):
        
        '''
        Saves the given information of the Recipe.
        Holds the lists of ingredients, comment and other recipes in recipes.
        Holds the dictionaries of counts of ingredients and other recipes.
        '''

        self.name = name
        self.ingredients = {}
        self.ilist = []
        self.recipes = {}
        self.rlist = []
        self.comment = []
        self.recipebook = RecipeBook()
        self.convert = Convert()
        
    
    def get_name(self):
        
        '''
        Returns the name of the recipe.
        '''
        
        return self.name
    
    def get_comment(self):
        
        '''
        Returns the preparation comment of the Recipe.
        '''
        
        return ''.join(self.comment)
    
    def get_ingredients(self):
        
        '''
        Returns all the ingredients, used in Recipe.
        This is done by, appending first Recipe's own ingredients
        to empty list, and then appending other recipes', that Recipe includes,
        ingredients that aren't in the list, to the list.
        Finally returns list in string form.
        '''
        
        list = []
        for i in self.ilist:
            list.append(i.get_name().lower())
        for r in self.rlist:
            for ingredient in r.ilist:
                if ingredient.get_name().lower() not in list:
                    list.append(ingredient.get_name().lower())
        
        list.sort()            
        return ', '.join(list)
    
    def get_count_of_ingredient(self, ingredient):
        
        '''
        Returns the count of given ingredient.
        First checks if Recipe has ingredient in its' own ingredientlist.
        Then checks if recipes, that Recipe includes, have ingredient in their
        ingredientlists.
        Returns the summed count, if ingredient is found in more than one recipe in Recipe. 
        '''
        
        i1 = 0
        
        for i in self.ilist:
            if i.get_name().lower() == ingredient.lower():
                i1 = self.ingredients[i]
                ingredienta = i
                
        for r in self.rlist:
            for i2 in r.ilist:
                if i2.get_name().lower() == ingredient.lower():
                    if i1 == 0:
                        return self.convert.b_times_a(r.ingredients[i2], self.recipes[r])
                    else:
                        timecount = self.convert.b_times_a(r.ingredients[i2], self.recipes[r])
                        counta = self.convert.convert_a_to_b(ingredienta, i1, timecount)
                        if counta:
                            return self.convert.add_a_to_b(timecount, counta)
                        else:
                            return None

        return i1
    
    def add_ingredient(self, ingredient, count):
        
        '''
        Adds given ingredient with given count to Recipe.
        If ingredient is already in Recipe, sums their counts together.
        If counts cannot be converted to same units, the older count of the ingredient
        remains in Recipe and the user is informed that summing couldn't been made.
        '''
        
        y = 0
        for i in self.ilist:
            if i.get_name().lower() == ingredient.get_name().lower():
                counta = self.convert.convert_a_to_b(ingredient, count, self.ingredients[i])
                if not counta:
                    y += 1
                    print ingredient.get_name(), "already exists in recipe. With given count's units, it couldn't be summed with ingredient's previous count."
                    break
                else:
                    new_count = self.convert.add_a_to_b(counta, self.ingredients[i])
                    del self.ingredients[i]
                    self.ingredients[i] = new_count
                    y += 1
                    break        
        if y == 0:
            self.ingredients[ingredient] = count
            self.ilist.append(ingredient)
        
    def add_comment(self, comment):
        
        '''
        Adds given comment (information of preparation of the Recipe), to Recipe.
        '''
        
        self.comment.append(comment)
        
    def add_other_recipe(self, recipe, count):
        
        '''
        Adds given recipe to Recipe with multiplying value of count.
        If these two Recipes have same ingredients, checks if their
        counts can be converted to same units.
        If these counts cannot be converted to same units, deletes
        given recipe from Recipe and informs users, that all the ingredients',
        that are in both recipes, values has to be in same units.
        '''
        
        self.rlist.append(recipe)
        self.recipes[recipe] = count
        x = 0
        for i in self.ilist:        
            for r in self.rlist:
                for i2 in r.ilist:
                    if i2.get_name().lower() == i.get_name().lower():
                        timecount = self.convert.b_times_a(r.ingredients[i2], self.recipes[r])
                        counta = self.convert.convert_a_to_b(i, self.ingredients[i], timecount)
                        if not counta:
                            x += 1
        if x != 0:
            print "Recipes included same ingredients with units which counts couldn't be summed."
            print recipe.get_name(), "couldn't be added to", self.get_name()
            self.rlist.remove(recipe)
            del self.recipes[recipe]
            return False
            
        
    
    def get_allergenics(self):
        
        '''
        Checks all the ingredients of the Recipe and recipes that Recipe includes,
        and returns allergenics that are found.
        '''
        
        list = []
        
        for ingredient in self.ilist:
            a = ingredient.get_allergenic_matter()
            if a == None:
                None
            else:
                list.append(a.lower())
        for recipe in self.rlist:
            for ingredient in recipe.ilist:
                a = ingredient.get_allergenic_matter()
                if a == None:
                    None
                else:
                    if a.lower() not in list:
                        list.append(a.lower())
        if list == []:
            return "None"
        else:
            return ', '.join(list)
        
    
    def recipe_has_allergenic(self, allergenic):
        
        '''
        Checks all the ingredients of the Recipe and recipes that Recipe includes.
        Returns True if given allergenic is found and False if it isn't.
        '''
        
        x = 0
        for ingredient in self.ilist:
            a = ingredient.get_allergenic_matter()
            if a == None:
                None
            elif  a.lower() == allergenic.lower():
                return True
                x += 1
                break
        if x == 0:
            for recipe in self.rlist:
                for ingredient in recipe.ilist:
                    a = ingredient.get_allergenic_matter()
                    if a == None:
                        None
                    elif a.lower() == allergenic.lower():
                        return True
                        x += 1
                        break
        if x == 0:
            return False
        
                
    def recipe_has_ingredient(self, ingredient):
        
        '''
        Checks all the ingredients of the Recipe and recipes that Recipe includes.
        Returns True if given ingredient is found and False if it isn't.
        '''
        
        for i in self.ilist:
            a = i.get_name()
            if  a.lower() == ingredient.lower():
                return True                
        for recipe in self.rlist:
            for i in recipe.ilist:
                a = i.get_name()
                if  a.lower() == ingredient.lower():
                    return True
        return False

    def get_information(self):
        
        '''
        Returns the information of the Recipe.
        First it prints the name of the Recipe.
        Then it prints ingredients of the Recipe, each in seperate
        line with ingredient's count and name.
        Then it prints the information of the preparation of the Recipe.
        Finally it prints the allergenics that Recipe includes.
        '''
        
        print "\n", self.name
        print "\nIngredients:"
        for ingredient in list(self.get_ingredients().split(', ')):
            print "\n", self.get_count_of_ingredient(ingredient), ingredient
        print "\nPreparation:\n", ''.join(self.comment)
        print "\nRecipe includes following allergenics:"
        return self.get_allergenics()
        
        
        