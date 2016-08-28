from convertions import *
from recipe_ingredient import *
from store_ingredient import *
from store import *
from recipe import *
from recipebook import *
from load_and_save import *

class UI():
    
    '''
    The functionality of this class is best explained in "Dokumentaatio".
    The functionality comes also clearer by running this class.
    '''

    def __init__(self):
        self.system = RecipeBook()
        self.loadsave = LoadAndSave()
        self.convertions = Convert()
        self.store = None
        

    def Start(self):
        print "\nHello, and welcome to use Intellectual RecipeBook!\nMade by: Jesse Rantala, jesse.rantala@aalto.fi\n"
        question = raw_input("TYPE\n 'new' - to create new store\n 'load' - to load your already created store\n 'exit' - to exit program\n")
        if question.lower() == "new":
            answer = (raw_input("Please, give a name for your store.\n"))
            while answer.strip() == '':
                print "You have to give a name for your store."
                answer = (raw_input("Please, give a name for your store.\n"))
            self.store = Store(answer)
            self.system.add_store(self.store)
            print "\nWelcome to store", self.store.get_name() + "."
            self.MainMenu()
        elif question.lower() == "load":
            self.Load()
        elif question.lower() == "exit":
            self.Exit()
        else:
            print "Only given commands are available."
            self.Start()
    
    def Exit(self):
        print "Program shut down."
      
    def Load(self):
        file = raw_input("Give a name of the file from where to load, in form 'file_name.txt':\n")
        x = 0
        try:
            self.store = self.loadsave.load_store(file)
            self.system.add_store(self.store)
            print "Store file loaded succesfully."
            print "\nWelcome to store", self.store.get_name() + "."
            x += 1
        except:
            print "Error occured in loading file."
        if x == 1:
            self.MainMenu()
        else:
            self.Start()

    def MainMenu(self):
        question = raw_input("\nMain Menu\n\nWhat would you like to do?\nTYPE\n 'i' - to add ingredients manually to your store\n 'lr' - to load recipe(s) from a file\n 'li' - to load more ingredient(s) to your store from a file\n 'r' - to add recipe to your recipebook\n"
                             " 'si' - to search ingredient from your store\n 'sr' - to search recipe\n 'c' - to check your store's dates\n 'mr' - to modify already existing recipe\n 'ms - to modify / change your store or its ingredients\n 's' - to save changes\n 'q' - to quit\n")
        if question.lower() == "i":
            self.AddIngredient()
        elif question.lower() == "r":
            self.AddRecipe()
        elif question.lower() == "lr":
            self.LoadRecipe()
        elif question.lower() == "li":
            self.LoadIngredient()
        elif question.lower() == "c":
            self.CheckDates()
        elif question.lower() == "si":
            self.IngredientSearch()
        elif question.lower() == "sr": 
            self.RecipeSearch()
        elif question.lower() == "q":
            self.Quit()
        elif question.lower() == "s":
            self.Save()
        elif question.lower() == "ms":
            self.ModifyStore()
        elif question.lower() == "mr":
            question = raw_input("Give the name of the recipe you would like to modify:\n")
            x = 0
            for recipe in self.system.recipes:
                if question.lower() == recipe.get_name().lower():
                    x += 1
                    self.ModifyRecipe(recipe)
                    break
            if x == 0:
                print "Recipe given couldn't be found."
                self.MainMenu()
        else:
            print "Only given commands are available."
            self.MainMenu()
            
    def LoadRecipe(self):
        file = raw_input("Give a name of the file from where to load, in form 'file_name.txt':\n")
        try:
            self.system = self.loadsave.load_recipes(file, self.system)
            print "Recipe file loaded succesfully."
        except:
            print "Error occured in loading file."
        self.MainMenu()
        
    def LoadIngredient(self):
        file = raw_input("Give a name of the file from where to load, in form 'file_name.txt':\n")
        try:
            self.store = self.loadsave.load_ingredients(file, self.store)
            print "Ingredient file loaded succesfully."
        except:
            print "Error occured in loading file."
        self.MainMenu()
                    
    def AddIngredient(self):
        iname = raw_input("Please type in the name of the ingredient you would like to add in your store:\n")
        while iname.strip() == '':
            print "You have to give a name of the ingredient."
            iname = raw_input("Please type in the name of the ingredient you would like to add in your store:\n")
        icount = raw_input("Please type in the count of the ingredient you bought:\n")
        while icount.strip() == '' or self.convertions.check_count(icount) == False:
            print "Not valid count. Valid units are liters, kilograms, deciliters, grams, milliters, teaspoon and tablespoon, or each with proper shortening. For count by pieces, feed only number."
            icount = raw_input("Please type in the count of the ingredient you bought:\n")
        idate = raw_input("Please type in the last date of use of your ingredient:\n")
        error = True
        while error == True and idate.strip() != '':
            try:
                y = int(idate[0:4])
                m = int(idate[5:7])
                d = int(idate[8:10])
                datetime.date(y, m, d)
                error = False
            except:
                error = True
                print "Given date not valid. Valid form: YYYY-MM-DD."
                idate = raw_input("Please type in the last date of use of your ingredient:\n")
        if idate.strip() == '':
            idate = None
            
        idensity = raw_input("Please type in the density of the ingredient:\n")
        if idensity.strip() == '':
            idensity = None
        iallergenic = raw_input("Please type in the allergenic matter of the ingredient:\n")
        if iallergenic.strip() == '':
            iallergenic = None
        print "\nAdding", iname.lower(), "to your store."
        to_add = StoreIngredient(iname, idate, icount, idensity, iallergenic)
        self.store.add_ingredient(to_add)
        for store in self.system.stores:
            if store.get_name().lower() == self.store.get_name():
                self.system.stores.remove(store)
        self.system.add_store(self.store)
        self.MainMenu()
    

    def AddRecipe(self):
        rname = raw_input("Please type in the name of your recipe:\n")
        x = 0
        for recipes in self.system.recipes:
            if recipes.get_name().lower() == rname.lower():
                print "Recipebook already has recipe called", rname
                question = raw_input("TYPE\n 'm' - to modify already existing recipe\n 'r' - to remove already existing recipe and create new one with the same name\n 'b' - to go back to MainMenu\n")
                if question.lower() == 'b':
                    self.MainMenu()
                    x += 1
                elif question.lower() == 'm':
                    x += 1
                    self.ModifyRecipe(recipes)
                elif question.lower() == 'r':
                    self.system.delete_recipe(recipes) 
                break             
        if x == 0:
            recipe = Recipe(rname)
            question2 = raw_input("TYPE\n 'a' - to add more ingredients to your recipe\n 'c' - to leave comment\n 'r' - to add another recipe to recipe\n 'b' - to go back and save created recipe\n")
            while question2.lower() != "b":
                if question2.lower() == "a":
                    i = raw_input("Please type in the ingredient to add:\n")
                    while i.strip() == '':
                        print "You have to give a name of the ingredient."
                        i = raw_input("Please type in the ingredient to add:\n")
                    a = raw_input("Please type in the allergenic matter of ingredient:\n")
                    if a.strip() == '':
                        a = None
                    b = raw_input("Please type in the density of ingredient:\n")
                    if b.strip() == '':
                        b = None
                    Ingredient = RecipeIngredient(i, b, a)
                    c = raw_input("Please type in the count of ingredient:\n")
                    while c.strip() == '' or self.convertions.check_count(c) == False:
                        print "Not valid count. Valid units are liters, kilograms, deciliters, grams, milliters, teaspoon and tablespoon, or each with proper shortening. For count by pieces, feed only number."
                        c = raw_input("Please type in the count of ingredient:\n")
                    print "Adding", i.lower(), "to", recipe.get_name().lower()
                    recipe.add_ingredient(Ingredient, c)
                    question2 = raw_input("TYPE\n 'a' - to add more ingredients to your recipe\n 'c' - to leave comment\n 'r' - to add another recipe to recipe\n 'b' - to go back and save created recipe\n")
                elif question2.lower() == "c":
                    c = raw_input("Please type your comment:\n")
                    recipe.add_comment(c)
                    question2 = raw_input("TYPE\n 'a' - to add more ingredients to your recipe\n 'c' - to leave comment\n 'r' - to add another recipe to recipe\n 'b' - to go back and save created recipe\n")
                elif question2.lower() == "r":
                    other = raw_input("Please type in the name of recipe to add:\n")
                    count = raw_input("Please type in the count of the other recipe to add:\n")
                    while count.strip() == '' or self.convertions.check_time_count(count) == False:
                        print "Please give count only in numbers."
                        count = raw_input("Please type in the count of the other recipe to add:\n")
                    if count.strip() == '0':
                        None
                    elif self.system.add_other_recipe_to_other(recipe, other, count):
                        print other, "added to your recipe.\n"
                    question2 = raw_input("TYPE\n 'a' - to add more ingredients to your recipe\n 'c' - to leave comment\n 'r' - to add another recipe to recipe\n 'b' - to go back and save created recipe\n")  
                else:
                    print "\nOnly given commands are available.\n"
                    question2 = raw_input("TYPE\n 'a' - to add more ingredients to your recipe\n 'c' - to leave comment\n 'r' - to add another recipe to recipe\n 'b' - to go back and save created recipe\n")
           
            if question2.lower() == "b":
                self.system.add_recipe(recipe)
                self.MainMenu()
        else:
            None
                
    
    def CheckDates(self):
        
        print self.system.store_in_date(self.store)
        self.MainMenu()
        
    
    def ModifyStore(self):
        
        question = raw_input("TYPE\n 'ri' - to remove ingredient\n 'mi' - to reduce count of ingredient\n 'n' - to change name of the store\n 'c' - to change your store to another\n 'b' - to go back\n")
        if question.lower() == 'ri':
            ingredient = raw_input("Give an ingredient you wish to remove:\n")
            while ingredient.strip() == '':
                print "You have to give an ingredient."
                ingredient = raw_input("Give an ingredient you wish to remove:\n")
            x = 0
            for i in self.store.ingredients:
                if ingredient.lower() == i.get_name().lower():
                    self.store.ingredients.remove(i)
                    x += 1
                    break
            if x == 0:
                print "Given ingredient could not be found."
            else:
                print ingredient, "removed."
            self.ModifyStore()
        elif question.lower() == 'mi':
            ingredient = raw_input("Give an ingredient which count you wish to reduce:\n")
            while ingredient.strip() == '':
                print "You have to give an ingredient."
                ingredient = raw_input("Give an ingredient which count you wish to reduce:\n")
            count = raw_input("Give a count how much you want to reduce:\n")
            while count.strip() == "" or self.convertions.check_count(count) == False:
                print "Not valid count. Valid units are liters, kilograms, deciliters, grams, milliters, teaspoon and tablespoon, or each with proper shortening. For count by pieces, feed only number."
                count = raw_input("Give a count how much you want to reduce:\n")
            x = 0
            y = 0
            for i in self.store.ingredients:
                if ingredient.lower() == i.get_name().lower():
                    counta = self.convertions.convert_a_to_b(i, i.get_count(), count)
                    if counta == False:
                        print "Not able to subtract given count from ingredient. Ingredient's count's units and given count's units are not valid for sum or subtract."
                        self.ModifyStore()
                        y += 1
                        break
                    else:
                        new_count = self.convertions.subtract_from_a(counta, count)
                        if new_count == 0:
                            self.store.get_rid_of(i)
                            x += 1
                        else:
                            i.count = new_count
                            x += 1
                        break
            if x == 0 and y == 0:
                print "Given ingredient could not be found."
                self.ModifyStore()
            elif y == 0:
                print "Reduced count of", ingredient + "."
                self.ModifyStore()
                    
        elif question.lower() == 'n':
            name = raw_input("Give a new name for your store:\n")
            while name.strip() == '':
                print "You have to give a name."
                name = raw_input("Give a new name for your store:\n")
            self.store.name = name
            self.ModifyStore()
        elif question.lower() == 'b':
            self.MainMenu()
        elif question.lower() == 'c':
            question1 = raw_input("Do you want to save your old store? Y/N\n")
            if question1.lower() == 'y':
                file = raw_input("Give a name of the file where to save store, in form 'file_name.txt'.\n")
                if file.strip() == "":
                    None
                else:
                    self.loadsave.save_store(file, self.store)
            elif question1.lower() == 'n':
                None
            else:
                print "\nOnly give commands are available.\n"
                self.ModifyStore()
            question = raw_input("TYPE\n 'new' - to create new store\n 'load' - to load your already created store\n 'b' - to go back\n")
            if question.lower() == "new":
                answer = (raw_input("Please, give a name for your store.\n"))
                while answer.strip() == '':
                    print "You have to give a name for your store."
                    answer = (raw_input("Please, give a name for your store.\n"))
                self.system.stores.remove(self.store)
                self.store = Store(answer)
                self.system.add_store(self.store)
                print "\nWelcome to store", self.store.get_name() + "."
                self.MainMenu()
            elif question.lower() == "load":
                file = raw_input("Give a name of the file from where to load, in form 'file_name.txt':\n")
                try:
                    store = self.loadsave.load_store(file)
                    self.system.stores.remove(self.store)
                    self.store = store
                    self.system.add_store(self.store)
                    print "Store file loaded succesfully."
                    print "\nWelcome to store", self.store.get_name() + "."
                    self.MainMenu()
                except:
                    print "Error occured in loading file."
                    self.ModifyStore()
                    
            elif question.lower() == 'b':
                self.MainMenu()
        else:
            print "\nOnly give commands are available.\n"
            self.ModifyStore()
        
    def ModifyRecipe(self, recipe):
        deletecount = 0
        question2 = raw_input("TYPE\n 'a' - to add more ingredients to your recipe\n 'c' - to leave comment\n 'r' - to add another recipe to recipe\n 'n' - to change the name of the recipe\n 'd' - to remove recipe from recipebook\n"
                        " 'ri' - to remove ingredient from recipe\n 'mi' - to reduce count of ingredient\n 'rr' - to remove another recipe from recipe\n 'rc' - to remove comment\n 'b' - to go back and save created recipe\n")
        while question2.lower() != "b" and deletecount == 0:
            if question2.lower() == "a":
                i = raw_input("Please type in the ingredient to add:\n")
                while i.strip() == '':
                    print "You have to give a name of the ingredient."
                    i = raw_input("Please type in the ingredient to add:\n")
                a = raw_input("Please type in the allergenic matter of ingredient:\n")
                if a.strip() == '':
                    a = None
                b = raw_input("Please type in the density of ingredient:\n")
                if b.strip() == '':
                    b = None
                Ingredient = RecipeIngredient(i, b, a)
                c = raw_input("Please type in the count of ingredient:\n")
                while c.strip() == '' or self.convertions.check_count(c) == False:
                    print "Not valid count. Valid units are liters, kilograms, deciliters, grams, milliters, teaspoon and tablespoon, or each with proper shortening. For count by pieces, feed only number."
                    c = raw_input("Please type in the count of ingredient:\n")
                print "Adding", i.lower(), "to", recipe.get_name().lower()
                recipe.add_ingredient(Ingredient, c)
                
            elif question2.lower() == "c":
                c = raw_input("Please type your comment:\n")
                recipe.add_comment(c)
                
            elif question2.lower() == "r":
                other = raw_input("Please type in the name of recipe to add:\n")
                count = raw_input("Please type in the count of the other recipe to add:\n")
                while count.strip() == '' or self.convertions.check_time_count(count) == False:
                    print "Please give count only in numbers."
                    count = raw_input("Please type in the count of the other recipe to add:\n")
                if count.strip() == '0':
                    None
                elif self.system.add_other_recipe_to_other(recipe, other, count):
                    print other, "added to your recipe.\n"
                else:
                    print other, "couldn't be found in your recipebook."
                
            elif question2.lower() == "n":
                name = raw_input("Give a new name for the recipe:\n")
                while name.strip() == "":
                    print "You have to give a name."
                    name = raw_input("Give a new name for the recipe:\n")
                recipe.name = name
                
            elif question2.lower() == "d":
                self.system.delete_recipe(recipe)
                deletecount += 1
                print "Recipe removed from recipebook."
        
            elif question2.lower() == "ri":
                ingredient = raw_input("Give an ingredient to be removed from recipe:\n")
                while ingredient.strip() == '':
                    print "You have to give an ingredient."
                    ingredient = raw_input("Give an ingredient to be removed from recipe:\n")
                x = 0
                for i in recipe.ilist:
                    if i.get_name().lower() == ingredient.lower():
                        x += 1
                        recipe.ilist.remove(i)
                        del recipe.ingredients[i]
                        print ingredient, "removed from", recipe.get_name().lower()
                        break
                if x == 0:
                    print "Given ingredient couldn't be found in", recipe.get_name().lower()
                    
            elif question2.lower() == "mi":
                ingredient = raw_input("Give an ingredient which count you want to reduce in recipe:\n")
                while ingredient.strip() == '':
                    print "You have to give an ingredient."
                    ingredient = raw_input("Give an ingredient which count you want to reduce in recipe:\n")
                count = raw_input("Give a count how much you want to reduce:\n")
                while count.strip() == '' or not self.convertions.check_count(count):
                    print "Not valid count. Valid units are liters, kilograms, deciliters, grams, milliters, teaspoon and tablespoon, or each with proper shortening. For count by pieces, feed only number."
                    count = raw_input("Give a count how much you want to reduce:\n")
                x = 0
                y = 0
                for i in recipe.ilist:
                    if ingredient.lower() == i.get_name().lower():
                        counta = self.convertions.convert_a_to_b(i, recipe.ingredients[i], count)
                        if counta == False:
                            print "Not able to subtract given count from ingredient. Ingredient's count's units and given count's units are not valid for sum or subtract."
                            y += 1
                            break
                        else:
                            new_count = self.convertions.subtract_from_a(counta, count)
                            if new_count == 0:
                                recipe.ilist.remove(i)
                                del recipe.ingredients[i]
                                x += 1
                            else:
                                del recipe.ingredients[i]
                                recipe.ingredients[i] = new_count
                                x += 1
                            break
                if x == 0 and y == 0:
                    print "Given ingredient could not be found."
                elif y == 0:
                    print "Reduced count of", ingredient + "."
            
            elif question2.lower() == "rr":
                recipe2 = raw_input("Give a name of the recipe to be removed:\n")
                while recipe2.strip() == '':
                    print "You have to give a name for the recipe to be removed."
                    recipe2 = raw_input("Give a name of the recipe to be removed:\n")
                x = 0
                for r in recipe.rlist:
                    if r.get_name().lower() == recipe2.lower():
                        recipe.rlist.remove(r)
                        del recipe.recipes[r]
                        x += 1
                        print recipe2, "removed from", recipe.get_name()
                        break  
                    
                if x == 0:
                    print recipe2, "couldn't be found in", recipe.get_name()
                
            elif question2.lower() == "rc":
                
                recipe.comment = []
                print "Comment removed from", recipe.get_name()
                
            else:
                print "\nOnly given commands are available.\n"
            
            if deletecount == 0:    
                question2 = raw_input("TYPE\n 'a' - to add more ingredients to your recipe\n 'c' - to leave comment\n 'r' - to add another recipe to recipe\n 'n' - to change the name of the recipe\n 'd' - to remove recipe from recipebook\n"
                        " 'ri' - to remove ingredient from recipe\n 'mi' - to reduce count of ingredient\n 'rr' - to remove another recipe from recipe\n 'rc' - to remove comment\n 'b' - to go back and save created recipe\n")
        if deletecount == 0:
            self.system.modified_recipe(recipe)
            self.MainMenu()
        else:
            self.MainMenu()
        
    def IngredientSearch(self):
        
        question = raw_input("TYPE\n 'all' - to get all ingredients in your store\n 'exact' - to search for information of the exact ingredient\n 'allergenic' - to search for ingredients with/without allergenic\n"
                            " 'b' - to go back\n")
        if question.lower() == 'all':
            print "\nYour store contains", self.store.get_ingredients(), "\n"
            self.IngredientSearch()
        elif question.lower() == 'exact':
            name = raw_input("Give the name of the ingredient to be searched.\n")
            x = 0
            for i in self.store.ingredients:
                name2 = i.get_name()
                if name2.lower() == name.lower():
                    x += 1
                    print i.get_name() + "'s expire date is", i.get_expire_date(), "you have it", i.get_count(), "in your store, it's allergenic matter is", i.get_allergenic_matter(), "and density is", i.get_density()
                    break
            if x == 0:
                print "\nThere is no", name, "in your store.\n"
            self.IngredientSearch()
        elif question.lower() == "allergenic":
            allergenic = raw_input("Give the allergenic, you wouldn't like ingredients to include.\n")
            print self.store.ingredients_without(allergenic)
            self.IngredientSearch()
        elif question.lower() == "b":
            self.MainMenu()
        else:
            print "Only given commands are available."
            self.IngredientSearch()
        
    def RecipeSearch(self):
        
        question = raw_input("TYPE\n 'all' - to get all recipes in your recipebook\n 'exact' - to search for information of exact recipe\n 'prepare' - to get all recipes you can prepare with your store\n"
                             " 'm' - to modified search, with limits you want\n 'b' - to go back\n")
        if question.lower() == 'all':
            print self.system.get_recipes()
            self.RecipeSearch()
        elif question.lower() == 'exact':
            name = raw_input("Give the name of the recipe to be searched.\n")
            x = 0
            for recipe in self.system.recipes:
                name2 = recipe.get_name()
                if name2.lower() == name.lower():
                    print recipe.get_information()
                    x += 1
                    break
            if x == 0:
                print "There is no", name, "in your store."
            self.RecipeSearch()
        elif question.lower() == "prepare":
            if len(self.system.can_prepare(self.store.get_name())) > 0:
                print ', '.join(self.system.can_prepare(self.store.get_name()))
            else:
                print "No recipes found."
            self.RecipeSearch()
        elif question.lower() == "b":
            self.MainMenu()
        elif question.lower() == "m":
            question = raw_input("TYPE\n 'allergenic' - to search for recipes without allergenic\n 'ingredient' - to get recipes with certain ingredient(s)\n 'n' - to get recipes without N ingredient(s)\n"
                " 'prepare' - to search for recipes you can prepare with your store\n 's' - to execute search with given limits\n")
            list = []
            while question.lower() != "s":
                if question.lower() == "allergenic":
                    allergenic = raw_input("Give the allergenic, you wouldn't like recipes to include.\n")
                    list2 = self.system.recipes_without(allergenic)
                    if len(list2) == 0:
                        print "No recipes found with given limit, modified search was therefore stopped.\n"
                        self.RecipeSearch()
                        break
                    elif len(list) == 0:
                        list = list2
                    else:
                        x = 0
                        while x < len(list):
                            if list[x] not in list2:
                                list.remove(list[x])
                                x -= 1
                            x += 1
                elif question.lower() == "ingredient":
                    ingredient = raw_input("Give the ingredient you would like recipe to include.\n")
                    ilist = []
                    while ingredient.strip().lower() != 'done':
                        ilist.append(ingredient)
                        ingredient = raw_input("Give another ingredient you would like recipe to include, or type 'done' if you don't want more ingredients to limit your search.\n")
                    if ingredient.strip().lower() == 'done' and len(ilist) > 0:
                        list2 = self.system.recipes_with_ingredients(ilist)
                        if len(list2) == 0:
                            print "No recipes found with given limit, modified search was therefore stopped.\n"
                            self.RecipeSearch()
                            break
                        elif len(list) == 0:
                            list = list2
                        else:
                            x = 0
                            while x < len(list):
                                if list[x] not in list2:
                                    list.remove(list[x])
                                    x -= 1
                                x += 1     
                    else:
                        print "Invalid data given."
                elif question.lower() == "prepare":
                    list2 = self.system.can_prepare(self.store.get_name())
                    if len(list2) == 0:
                        print "No recipes found with given limit, modified search was therefore stopped.\n"
                        self.RecipeSearch()
                        break
                    elif len(list) == 0:
                        list = list2
                    else:
                        x = 0
                        while x < len(list):
                            if list[x] not in list2:
                                list.remove(list[x])
                                x -= 1
                            x += 1  
                elif question.lower() == "n":
                    count = raw_input("Please give the count that your store can lack ingredients when recipes are searched.\n")
                    while not self.convertions.check_time_count(count) or count.strip() == '':
                        print "Only numbers are valid."
                        count = raw_input("Please give the count that your store can lack ingredients when recipes are searched.\n")
                    list2 = self.system.recipes_without_n(self.store, count)
                    if len(list2) == 0:
                        print "No recipes found with given limit, modified search was therefore stopped.\n"
                        self.RecipeSearch()
                        break
                    elif len(list) == 0:
                        list = list2
                    else:
                        x = 0
                        while x < len(list):
                            if list[x] not in list2:
                                list.remove(list[x])
                                x -= 1
                            x += 1
                else:
                    print "Only given commands are available."
                
                question = raw_input("TYPE\n 'allergenic' - to search for recipes without allergenic\n 'ingredient' - to get recipes with certain ingredient(s)\n 'n' - to get recipes without N ingredient(s)\n"
                " 'prepare' - to search for recipes you can prepare with your store\n 's' - to execute search with given limits\n")
        else:
            print "Only given commands are available."
            self.RecipeSearch()
            
        if question.lower() == "s" and len(list) > 0:
            print ', '.join(list)
            self.RecipeSearch()
        elif question.lower() == "s":
            print "No recipes found with given limits."
            self.RecipeSearch() 
            
    def Save(self):
        
        print "If you don't wish to save something, enter empty line."
        file = raw_input("Give a name of the file where to save store, in form 'file_name.txt'.\n")
        if file.strip() == "":
            None
        else:
            self.loadsave.save_store(file, self.store)
        file = raw_input("Give a name of the file where to save ingredients, in form 'file_name.txt'.\n")
        if file.strip() == "":
            None
        else:
            self.loadsave.save_ingredients(file, self.store)
        file = raw_input("Give a name of the file where to save recipes, in form 'file_name.txt'.\n")
        if file.strip() == "":
            None
        else:
            self.loadsave.save_recipes(file, self.system)
        print "Files saved."
        self.MainMenu()
        
    def Quit(self):
        question = raw_input("Do you want to quit without saving? Y/N\n")
        if question.lower() == "y":
            print "Program shut down."
        elif question.lower() == "n":
            print "If you don't wish to save something, enter empty line."
            file = raw_input("Give a name of the file where to save store, in form 'file_name.txt'.\n")
            if file.strip() == "":
                None
            else:
                self.loadsave.save_store(file, self.store)
            file = raw_input("Give a name of the file where to save ingredients, in form 'file_name.txt'.\n")
            if file.strip() == "":
                None
            else:
                self.loadsave.save_ingredients(file, self.store)
            file = raw_input("Give a name of the file where to save recipes, in form 'file_name.txt'.\n")
            if file.strip() == "":
                None
            else:
                self.loadsave.save_recipes(file, self.system)
            print "Files saved and program shut down."
        else:
            print "Only given commands are available."
            self.Quit()

    
if __name__ == "__main__":
    Kaytto = UI()
    Kaytto.Start()

    