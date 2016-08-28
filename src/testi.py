from store_ingredient import *
from store import *
from convertions import *
from recipe_ingredient import *
from recipe import *
from recipebook import *
from UI import *
    
Varasto = Store("Oma keittio")
Muunnos = Convert()


    
Tuote = StoreIngredient("Eggs", "2013-02-18", "12", None, None)
Tuote2 = StoreIngredient("Milk", "2013-02-20", "3l", "1.5", "Lactose")
Tuote3 = StoreIngredient("Bread", "2013-02-12", "0.5kg", None, "Gluten")
Tuote4 = StoreIngredient("Cheese", "2013-12-24y", "1kg", None, "Lactose")
Tuote5 = StoreIngredient("Powder", "2013-02-28", "1kg", None, "Gluten")
Tuote6 = StoreIngredient("Coffee", "2013-04-05", "0.5kg", None, None)
Tuote7 = StoreIngredient("Butter", "2013-08-27", "0.5kg", "2", "Lactose")
Tuote8 = StoreIngredient("Beer", "2014-01-01", "5l", "1", None)
Tuote9 = StoreIngredient("Sugar", "2014-01-01", "1kg", None, None)
Tuote10 = StoreIngredient("Eggs", "2013-03-29", "35", None, None)
Tuote11 = StoreIngredient("Sugar", "2014-02-06", "64dl", None, None)


    
Varasto.add_ingredient(Tuote)
Varasto.add_ingredient(Tuote2)  
Varasto.add_ingredient(Tuote3)
Varasto.add_ingredient(Tuote4)
Varasto.add_ingredient(Tuote5)
Varasto.add_ingredient(Tuote6)
Varasto.add_ingredient(Tuote7)
Varasto.add_ingredient(Tuote8)
Varasto.add_ingredient(Tuote9)
Varasto.add_ingredient(Tuote10)
Varasto.add_ingredient(Tuote11)
    
print Tuote.get_name(), "includes allergenic matter:", Tuote.is_allergenic(), "\n" 
print "You have", Varasto.get_count_of_ingredient("Eggs"), "eggs."
print "You have", Varasto.get_count_of_ingredient("Sugar"), "of sugar."
 
print Tuote2.get_name(), "includes allergenic matter:", Tuote2.is_allergenic(), "\n"
print "The allergenic matter that", Tuote2.get_name().lower(), "includes is", Tuote2.get_allergenic_matter().lower() + ".\n"
    
    
    
print Tuote3.get_name(), "includes allergenic matter:", Tuote3.is_allergenic(), "\n"
print "The allergenic matter that", Tuote3.get_name().lower(), "includes is", Tuote3.get_allergenic_matter().lower() + ".\n"


print "All ingredients without lactose:", Varasto.ingredients_without("lactose") + ".\n"
print "All ingredients without gluten:", Varasto.ingredients_without("gluten") + ".\n"
    
print "Store contains:\n", Varasto.get_ingredients() + ".\n"

    
print "Let's check the dates of ingredients:\n"
Varasto.check_dates()
    
print "Store contains:\n", Varasto.get_ingredients() + ".\n"

Resepti1 = Recipe("Herkku Letut")
Resepti2 = Recipe("Taikina")
Resepti3 = Recipe("Munakas")
Resepti4 = Recipe("SokeriMaito")
Resepti5 = Recipe("Taikina2")
Kaytto = RecipeBook()

Aine1 = RecipeIngredient("Milk", "1.5", "Lactose")
Aine2 = RecipeIngredient("Powder", None, "Gluten")
Aine3 = RecipeIngredient("Sugar", None, None)
Aine4 = RecipeIngredient("Eggs", None, None)
Aine5 = RecipeIngredient("Secret Ingredient", None, None)

Resepti2.add_ingredient(Aine1, "1l")
Resepti2.add_ingredient(Aine2, "500g")
Resepti2.add_ingredient(Aine3, "0.5kg")
Resepti2.add_ingredient(Aine4, "2")
Resepti1.add_ingredient(Aine5, "1")
Resepti1.add_ingredient(Aine1, "2kg")
Resepti3.add_ingredient(Aine4, "1")
Resepti4.add_ingredient(Aine1, "1l")
Resepti4.add_ingredient(Aine3, "0.5kg")
Resepti5.add_ingredient(Aine3, "3kg")
Resepti5.add_ingredient(Aine4, "13")


Resepti1.add_other_recipe(Resepti2, 3)

print "Recipe:", Resepti1.get_name(), "contains", Resepti1.get_count_of_ingredient("Milk"), "of milk."
print "Recipe:", Resepti1.get_name(), "contains", Resepti1.get_count_of_ingredient("Secret Ingredient"), "of secret ingredient."
print "Recipe:", Resepti1.get_name(), "contains", Resepti1.get_ingredients() + "."

print "Does the", Resepti1.get_name(), "include gluten?", Resepti1.recipe_has_allergenic("Gluten")

Kaytto.add_recipe(Resepti1)
Kaytto.add_recipe(Resepti2)
Kaytto.add_recipe(Resepti3)
Kaytto.add_recipe(Resepti4)
Kaytto.add_recipe(Resepti5)
Kaytto.add_store(Varasto)

print "Can we prepare", Resepti1.get_name(), "with our ingredients in", Varasto.get_name() + "?"
print Kaytto.enough_ingredients("Herkku Letut", "Oma keittio")

print "What recipes do we have in recipebook?", Kaytto.get_recipes()
print "What recipes can we prepare with our store?", Kaytto.can_prepare("Oma keittio")


Resepti1.add_comment("Vatkaa munat, maito ja sokeri kuohkeaksi vaahdoksi. Lisaa joukkoon jauhot ja salainen ainesosa."
                    "Nosta taikinaa kuumalle levylle ja paista lettuja molemmilta puolin 2min.")

print Resepti1.get_information()
print Resepti2.get_information()

Resepti6 = Recipe("Testi")
Kaytto.add_recipe(Resepti6)

Resepti6.add_ingredient(Aine1, "1kg")
Resepti6.add_ingredient(Aine2, "0.5liters")
Resepti6.add_ingredient(Aine3, "0.5grams")
Resepti6.add_ingredient(Aine4, "2")
print Resepti6.get_information()
print "Can we prepare", Resepti6.get_name(), "with our ingredients in", Varasto.get_name() + "?"
print Kaytto.enough_ingredients("Testi", "Oma keittio")

Resepti7 = Recipe("Testi2")
Kaytto.add_recipe(Resepti7)

Resepti7.add_ingredient(Aine1, "15dl")
Resepti7.add_ingredient(Aine2, "0.5tbs")
Resepti7.add_ingredient(Aine3, "0.5ts")
Resepti7.add_ingredient(Aine4, "1")
print Resepti6.get_information()
print "Can we prepare", Resepti7.get_name(), "with our ingredients in", Varasto.get_name() + "?"
print Kaytto.enough_ingredients("Testi2", "Oma keittio")
print Resepti7.get_information()

Resepti7.add_other_recipe(Resepti6, 1)

print Resepti7.get_information()