import sys
from PyQt4 import QtGui
from convertions import *
from recipe_ingredient import *
from store_ingredient import *
from store import *
from recipe import *
from recipebook import *
from load_and_save import *

class MainWindow(QtGui.QMainWindow):
    
    def __init__(self, parent=None):
        
        super(MainWindow, self).__init__(parent)
        self.central = StartWindow()
        self.setCentralWidget(self.central)


class StartWindow(QtGui.QWidget):

    def __init__(self):
        
        super(StartWindow, self).__init__()
        self.StartUI()
        self.system = RecipeBook()
        self.loadsave = LoadAndSave()
        self.convertions = Convert()
        self.store = None
       
    def StartUI(self):

        self.message = QtGui.QLabel('Hello, and welcome to use Intellectual RecipeBook!\nMade by: Jesse Rantala, jesse.rantala@aalto.fi', self)
       
        self.new_store = QtGui.QPushButton("New Store", self)
        self.new_store.move(50, 50)
        self.new_store.clicked.connect(self.enter_new_store)
        
        self.load_store = QtGui.QPushButton("Load Store", self)
        self.load_store.move(150, 50)
        self.load_store.clicked.connect(self.load_old_store)    
        
        self.setGeometry(300, 300, 300 , 300)
        self.setWindowTitle('Intellectual RecipeBook')
        self.show()
        
    def enter_new_store(self):
        
        text, ok = QtGui.QInputDialog.getText(self, 'New Store', 'Give a name for your store:')
        if ok:
            self.store = Store(text)
            self.parentWidget().central = MainMenu()
            

    
    def load_old_store(self):
        
        text, ok = QtGui.QInputDialog.getText(self, 'Load Store', 'Give a file where to load your store:')
        if ok:
            if text == '':
                None
            else:
                r = 0
                while r == 0:
                    try:
                        self.store = self.loadsave.load_store(text)
                        r += 1
                        self.parentWidget().central = MainMenu()
                    except:
                        text, ok = QtGui.QInputDialog.getText(self, 'Load Store', 'Give a file where to load your store:')
            
        
class MainMenu(QtGui.QWidget):

    def __init__(self):
        
        super(MainMenu, self).__init__()
        self.MainMenu()
        self.system = RecipeBook()
        self.loadsave = LoadAndSave()
        self.convertions = Convert()
        self.store = None
            
    
    def MainMenu(self):
        
        self.ingredient = QtGui.QPushButton("Add Ingredient", self)
        self.ingredient.move(50, 150)
        self.ingredient.clicked.connect(self.MainMenu)
        
        self.recipe = QtGui.QPushButton("Add Recipe", self)
        self.recipe.move(50, 100)
        self.recipe.clicked.connect(self.MainMenu)
        
        self.load_recipe = QtGui.QPushButton("Load Recipe", self)
        self.load_recipe.move(150, 100)
        self.load_recipe.clicked.connect(self.MainMenu)
        
        self.search_ingredient = QtGui.QPushButton("Search Ingredient", self)
        self.search_ingredient.move(150, 200)
        self.search_ingredient.clicked.connect(self.MainMenu)
        
        self.search_recipes = QtGui.QPushButton("Search Recipes", self)
        self.search_recipes.move(50, 200)
        self.search_recipes.clicked.connect(self.MainMenu)
        
        self.setGeometry(300, 300, 600, 600)
        self.setWindowTitle('Main Menu')
        self.show()
        
    def closeEvent(self, event):
        
        reply = QtGui.QMessageBox.question(self, 'Message',
            "Do you want to quit without saving?", QtGui.QMessageBox.Yes | 
            QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            text, ok = QtGui.QInputDialog.getText(self, 'Save Store', 'Give a name for your store file:')
            if ok:
                self.loadsave.save_store(text, self.store)
            text, ok = QtGui.QInputDialog.getText(self, 'Save Recipes', 'Give a name for your recipe file:')
            if ok:
                self.loadsave.save_recipes(text, self.system)
            event.accept()
        
        
    def searching_recipes(self):
        
        text, ok = QtGui.QInputDialog.getText(self, 'Load Store', 'Give a file where to load your store:')
        
        text1, ok1 = QtGui.QInputDialog.getText(self, 'Load Store', 'Give a file where to load your store:')
        
        text2, ok2 = QtGui.QInputDialog.getText(self, 'Load Store', 'Give a file where to load your store:')
        
        text3, ok3 = QtGui.QInputDialog.getText(self, 'Load Store', 'Give a file where to load your store:')
        
        if ok or ok1 or ok2 or ok3:
            
            None
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = MainWindow()
    
    sys.exit(app.exec_())
    
if __name__ =='__main__':
    main()