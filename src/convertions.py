class Convert(object):

    def __init__(self):
        
        self.counts = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", ' ']
        self.units = ["l", "liters", "kg", "kilograms", "dl", "deciliters", "g", "grams", "ml", "milliters", "ts", "teaspoon", "tbs", "tablespoon"]


    def check_time_count(self, a):
        
        '''
        Returns True if count is valid number.
        Returns False if count is not valid number.
        '''
        x = 0
        while x < len(a) and ''.join(a)[x] in self.counts:
            x += 1
        if x < len(a):
            return False
        return True
        

    def check_count(self, a):
        
        '''
        Returns True if count is in valid units.
        Returns False if count is not in valid units.
        '''
        
        x = 0
        while x < len(a) and ''.join(a)[x] in self.counts:
            x += 1
        if x < len(a):
            unit = ''.join(a)[x:]
            if unit.lower() in self.units:
                return True
            else:
                return False
        return True
    
    
    def a_enough_for_b(self, a, b):
        
        '''
        Returns True if a is bigger or even than b.
        Returns False if a is not bigger or even than b.
        '''
        
        x = 0
        y = 0
        while x < len(a) and ''.join(a)[x] in self.counts:
            x += 1
        if x < len(a):
            count1 = ''.join(a)[:x]
        else:
            count1 = a
        while y < len(b) and ''.join(b)[y] in self.counts:
            y += 1
        if y < len(b):
            count2 = ''.join(b)[:y]
        else:
            count2 = b
        return float(count1) >= float(count2)
        
        
    def add_a_to_b(self, a, b):
        
        '''
        Returns new count, with units, where a and b are summed.
        '''
        
        x = 0
        y = 0
        while x < len(a) and ''.join(a)[x] in self.counts:
            x += 1
        if x < len(a):
            unit1 = ''.join(a)[x:]
            count1 = ''.join(a)[:x]
        else:
            count1 = a
            unit1 = ''
        while y < len(b) and ''.join(b)[y] in self.counts:
            y += 1
        if y < len(b):
            unit2 = ''.join(b)[y:]
            count2 = ''.join(b)[:y]
        else:
            count2 = b
            unit2 = ''
        if unit1 == unit2:
            count = float(count1) + float(count2)
            return str(count) + str(unit1)
        
    def subtract_from_a(self, a, count):
        
        '''
        Returns new count, with units, where count is subtracted from a.
        '''
        
        x = 0
        y = 0
        while x < len(a) and ''.join(a)[x] in self.counts:
            x += 1
        if x < len(a):
            unit1 = ''.join(a)[x:]
            count1 = ''.join(a)[:x]
        else:
            count1 = a
            unit1 = ''
        while y < len(count) and ''.join(count)[y] in self.counts:
            y += 1
        if y < len(count):
            unit2 = ''.join(count)[y:]
            count2 = ''.join(count)[:y]
        else:
            count2 = count
            unit2 = ''
        if unit1 == unit2:
            if float(count2) >= float(count1):
                return 0
            else:    
                count = float(count1) - float(count2)
            return str(count) + str(unit1)

    def b_times_a(self, a, b):
        
        '''
        Returns new count, with units, where a is multiplied by b.
        '''
        
        x = 0
        while x < len(a) and ''.join(a)[x] in self.counts:
            x += 1
        if x < len(a):
            unit1 = ''.join(a)[x:]
            count1 = ''.join(a)[:x]
        else:
            count1 = a
            unit1 = ''
        count = float(count1) * float(b)
        return str(count) + str(unit1)
    
    def convert_a_to_b(self, a, counta, b):
        
        '''
        Returns converted count (counta) for ingredient a, with same unit as b's.
        If units are the same, returns original value of counta.
        If one of the units, counta or b, is by pieces and other isn't, returns False, as units cannot be converted to same.
        '''

        x = 0
        y = 0
        while x < len(counta) and ''.join(counta)[x] in self.counts:
            x += 1
        if x < len(counta):
            unit1 = ''.join(counta)[x:]
            count1 = ''.join(counta)[:x]
        else:
            count1 = counta
            unit1 = ''
        while y < len(b) and ''.join(b)[y] in self.counts:
            y += 1
        if y < len(b):
            unit2 = ''.join(b)[y:]
            count2 = ''.join(b)[:y]
        else:
            count2 = b
            unit2 = ''
        
        if unit1 == unit2:
            return counta
        
        elif unit1 == '' or unit2 == '':
            return False
            
        elif unit1 == 'l' or unit1 == 'liters':
            if unit2 == 'kg' or unit2 == 'kilograms':
                return str(self.liters_to_kilograms(count1, a)) + unit2
            elif unit2 == 'dl' or unit2 == 'deciliters':
                return str(self.liters_to_desiliters(count1)) + unit2
            elif unit2 == 'g' or unit2 == 'grams':
                return str(float(self.liters_to_kilograms(count1, a)) * 1000) + unit2
            elif unit2 == 'ml' or unit2 == 'milliters':
                return str(float(count1) * 1000) + unit2
            elif unit2 == 'tbs' or unit2 == 'tablespoon':
                return str((float(count1) * 1000) / 15) + unit2
            elif unit2 == 'ts' or unit2 == 'teaspoon':
                return str((float(count1) * 1000) / 5) + unit2
        elif unit1 == 'kg' or unit1 == 'kilograms':
            if unit2 == 'l' or unit2 == 'liters':
                return str(self.kilograms_to_liters(count1, a)) + unit2
            elif unit2 == 'dl' or unit2 == 'deciliters':
                liters = self.kilograms_to_liters(count1, a)
                return str(self.liters_to_desiliters(liters)) + unit2 
            elif unit2 == 'g' or unit2 == 'grams':
                return str(float(count1) * 1000) + unit2
            elif unit2 == 'ml' or unit2 == 'milliters':
                liters = self.kilograms_to_liters(count1, a)
                return str(float(liters) * 1000) + unit2
            elif unit2 == 'tbs' or unit2 == 'tablespoon':
                liters = self.kilograms_to_liters(count1, a)
                return str((float(liters) * 1000) / 15) + unit2
            elif unit2 == 'ts' or unit2 == 'teaspoon':
                liters = self.kilograms_to_liters(count1, a)
                return str((float(liters) * 1000) / 5) + unit2
        elif unit1 == 'dl' or unit1 == 'deciliters':
            if unit2 == 'l' or unit2 == 'liters':
                return str(float(count1) / 10) + unit2
            elif unit2 == 'kg' or unit2  == 'kilograms':
                liters = float(count1) / 10
                return str(self.liters_to_kilograms(liters, a)) + unit2
            elif unit2 == 'g' or unit2 == 'grams':
                liters = float(count1) / 10
                return str(self.liters_to_kilograms(liters, a) * 1000) + unit2
            elif unit2 == 'ml' or unit2 == 'milliters':
                return str(float(count1) * 100) + unit2
            elif unit2 == 'ts' or unit2 == "teaspoon":
                liters = float(count1) / 10
                return str(float((liters * 1000) / 5)) + unit2
            elif unit2 == 'tbs' or unit2 == "tablespoon":
                liters = float(count1) / float(10)
                return str(float((liters * 1000) / 15)) + unit2
        elif unit1 == 'g' or unit1 == 'grams':       
            if unit2 == 'l' or unit2 == 'liters':
                kilograms = str(float(count1) / 1000)
                return str(self.kilograms_to_liters(kilograms, a)) + unit2
            elif unit2 == 'kg' or unit2  == 'kilograms':
                return str(float(count1) / 1000) + unit2
            elif unit2 == 'dl' or unit2 == 'deciliters':
                kilograms = str(float(count1) / 1000)
                return str(self.kilograms_to_liters(kilograms, a) * 10) + unit2
            elif unit2 == 'ml' or unit2 == 'milliters':
                kilograms = float(count1) / 1000
                liters = self.kilograms_to_liters(kilograms, a)
                return str(float(liters) * 1000) + unit2
            elif unit2 == 'ts' or unit2 == "teaspoon":
                kilograms = float(count1) / 1000
                liters = self.kilograms_to_liters(kilograms, a)
                return str((liters * 1000) / 5) + unit2
            elif unit2 == 'tbs' or unit2 == "tablespoon":
                kilograms = float(count1) / 1000
                liters = self.kilograms_to_liters(kilograms, a)
                return str((float(liters) * 1000) / 15) + unit2
        elif unit1 == 'ts' or unit1 == 'teaspoon':
            if unit2 == 'l' or unit2 == 'liters':
                return str(self.teaspoon_to_liters(count1)) + unit2
            elif unit2 == 'kg' or unit2  == 'kilograms':
                liters = self.teaspoon_to_liters(count1)
                return str(self.liters_to_kilograms(liters, a)) + unit2
            elif unit2 == 'dl' or unit2 == 'deciliters':
                return str(self.teaspoon_to_liters(count1) * 10) + unit2
            elif unit2 == 'g' or unit2 == "grams":
                liters = self.teaspoon_to_liters(count1)
                return str(self.liters_to_kilograms(liters, a) * 1000) + unit2
            elif unit2 == 'ml' or unit2 == 'milliters':
                return str(float(count1) / 5) + unit2
            elif unit2 == 'tbs' or unit2 == "tablespoon":
                liters = self.teaspoon_to_liters(count1)
                return str((float(liters) * 1000) / 15) + unit2
        elif unit1 == 'tbs' or unit1 == 'tablespoon':
            if unit2 == 'l' or unit2 == 'liters':
                return str(self.tablespoon_to_liters(count1)) + unit2
            elif unit2 == 'kg' or unit2  == 'kilograms':
                liters = self.tablespoon_to_liters(count1)
                return str(self.liters_to_kilograms(liters, a)) + unit2
            elif unit2 == 'dl' or unit2 == 'deciliters':
                return str(self.tablespoon_to_liters(count1) * 10) + unit2
            elif unit2 == 'g' or unit2 == "grams":
                liters = self.tablespoon_to_liters(count1)
                return str(self.liters_to_kilograms(liters, a) * 1000) + unit2
            elif unit2 == 'ml' or unit2 == 'milliters':
                return str(float(count1) / 15) + unit2
            elif unit2 == 'ts' or unit2 == "teaspoon":
                liters = self.tablespoon_to_liters(count1)
                return str((float(liters) * 1000) / 5) + unit2
        elif unit1 == "ml" or unit1 == "milliters":
            if unit2 == 'l' or unit2 == 'liters':
                return str(float(count1) / 1000) + unit2
            elif unit2 == 'kg' or unit2  == 'kilograms':
                liters = float(count1) / 1000
                return str(self.liters_to_kilograms(liters, a)) + unit2
            elif unit2 == 'dl' or unit2 == 'deciliters':
                return str((float(count1) / 1000) * 10) + unit2
            elif unit2 == 'g' or unit2 == "grams":
                liters = float(count1) / 1000
                return str(self.liters_to_kilograms(liters, a) * 1000) + unit2
            elif unit2 == 'ts' or unit2 == "teaspoon":
                return str(float(count1) * 5) + unit2
            elif unit2 == 'tbs' or unit2 == "tablespoon":
                return str(float(count1) * 15) + unit2
                        
    def kilograms_to_liters(self, count, ingredient):
        
        '''
        Returns ingredient's value of count, that is in kilograms, in liters. 
        '''
        
        return float(count) / float(ingredient.get_density())
        
    def liters_to_kilograms(self, count, ingredient):
        
        '''
        Returns ingredient's value of count, that is in liters, in kilograms. 
        '''
        
        return float(ingredient.get_density()) * float(count)
    
    def liters_to_desiliters(self, count):
        
        '''
        Returns ingredient's value of count, that is in liters, in desiliters. 
        '''
        
        return float(count) * 10
        
    def kilograms_to_grams(self, count):
        
        '''
        Returns ingredient's value of count, that is in kilograms, in grams. 
        '''
        
        return float(count) * 10
    
    def teaspoon_to_liters(self, count):
        
        '''
        Returns ingredient's value of count, that is in teaspoons, in liters. 
        '''

        return (float(count) * 5) / 1000
    
    def tablespoon_to_liters(self, count):
        
        '''
        Returns ingredient's value of count, that is in tablespoons, in liters. 
        '''
        
        return (float(count) * 15) / 1000