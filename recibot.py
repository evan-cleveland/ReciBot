from selenium import webdriver 
from selenium.webdriver.common.by import By
import os
import pathlib
import textwrap
import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

#####CONSTANTS ANDS VARIABLES - Note that I originally had plans to add multiple stores, but ad accessibility limited me, so everything still says pub or publix, will change :)#######
publixGroceryLink = "https://accessibleweeklyad.publix.com/PublixAccessibility/BrowseByListing/ByCategory/?ListingSort=8&StoreID=2506077&CategoryID=5232529"
publixMeatLink = "https://accessibleweeklyad.publix.com/PublixAccessibility/BrowseByListing/ByCategory/?ListingSort=8&StoreID=2506077&CategoryID=5232533"
publixProduceLink = "https://accessibleweeklyad.publix.com/PublixAccessibility/BrowseByListing/ByCategory/?ListingSort=8&StoreID=2506077&CategoryID=5232537"
publixDairyLink = "https://accessibleweeklyad.publix.com/PublixAccessibility/BrowseByListing/ByCategory/?ListingSort=8&StoreID=2506077&CategoryID=5232525"
publixDeliLink = "https://accessibleweeklyad.publix.com/PublixAccessibility/BrowseByListing/ByCategory/?ListingSort=8&StoreID=2506077&CategoryID=5232526"
publixBOGOLink = "https://accessibleweeklyad.publix.com/PublixAccessibility/BrowseByListing/ByCategory/?ListingSort=8&StoreID=2506077&CategoryID=5232540"

pubGroceryList = []
pubMeatList = []
pubProduceList = []
pubBOGOList = []
pubDairyList = []
pubDeliList = []
bogoMeat = []
bogoGrocery = []
bogoDeli = []
bogoProduce = []
bogoDairy = []
masterBogoList = []


scrapedGrocery = False
scrapedMeat = False
scrapedProduce = False
scrapedBOGO = False
scrapedDairy = False
scrapedDeli = False
masterListCreated = False

########SCRAPING FUNCTIONS########

def scrapeGrocery():
    global scrapedGrocery
    global scrapedBOGO
    if not scrapedBOGO:
        scrapeBogo()
    if not scrapedGrocery:
        pubGroceryList.clear()
        publixGroceryDriver = webdriver.Firefox()
        publixGroceryDriver.get(publixGroceryLink)
        pubGroceryItemsString = publixGroceryDriver.find_element(By.XPATH, '//*[@id="BrowseLayout"]/div/h1').get_attribute("innerText")
        pubGroceryItemsNum = int(''.join(x for x in pubGroceryItemsString if x.isdigit()))
        for i in range(pubGroceryItemsNum):
            xpath = '//*[@id="BrowseContent"]/div/ul/li/div/div/div[' + str(i + 1) + ']/div/div[3]/div[1]/h2'
            pubGroceryList.append(publixGroceryDriver.find_element(By.XPATH, xpath).text)
        publixGroceryDriver.close()
        global bogoGrocery
        bogoGrocery = [item for item in pubGroceryList if item in pubBOGOList]
        scrapedGrocery = True

def scrapeMeat():
    global scrapedMeat
    global scrapedBOGO
    if not scrapedBOGO:
        scrapeBogo()
    if not scrapedMeat:
        pubMeatList.clear()
        publixMeatDriver = webdriver.Firefox()
        publixMeatDriver.get(publixMeatLink)
        pubMeatItemsString = publixMeatDriver.find_element(By.XPATH, '//*[@id="BrowseLayout"]/div/h1').get_attribute("innerText")
        pubMeatItemsNum = int(''.join(x for x in pubMeatItemsString if x.isdigit()))
        for i in range(pubMeatItemsNum):
            xpath = '//*[@id="BrowseContent"]/div/ul/li/div/div/div[' + str(i + 1) + ']/div/div[3]/div[1]/h2'
            pubMeatList.append(publixMeatDriver.find_element(By.XPATH, xpath).text)
        publixMeatDriver.close()
        global bogoMeat
        bogoMeat = [item for item in pubMeatList if item in pubBOGOList]
        scrapedMeat = True

def scrapeProduce():
    global scrapedProduce
    global scrapedBOGO
    if not scrapedBOGO:
        scrapeBogo()
    if not scrapedProduce:
        pubProduceList.clear()
        publixProduceDriver = webdriver.Firefox()
        publixProduceDriver.get(publixProduceLink)
        pubProduceItemsString = publixProduceDriver.find_element(By.XPATH, '//*[@id="BrowseLayout"]/div/h1').get_attribute("innerText")
        pubProduceItemsNum = int(''.join(x for x in pubProduceItemsString if x.isdigit()))
        for i in range(pubProduceItemsNum):
            xpath = '//*[@id="BrowseContent"]/div/ul/li/div/div/div[' + str(i + 1) + ']/div/div[3]/div[1]/h2'
            pubProduceList.append(publixProduceDriver.find_element(By.XPATH, xpath).text)
        publixProduceDriver.close()
        global bogoProduce
        bogoProduce = [item for item in pubProduceList if item in pubBOGOList]
        scrapedProduce = True

def scrapeDairy():
    global scrapedDairy
    global scrapedBOGO
    if not scrapedBOGO:
        scrapeBogo()
    if not scrapedDairy:
        pubDairyList.clear()
        publixDairyDriver = webdriver.Firefox()
        publixDairyDriver.get(publixDairyLink)
        pubDairyItemsString = publixDairyDriver.find_element(By.XPATH, '//*[@id="BrowseLayout"]/div/h1').get_attribute("innerText")
        pubDairyItemsNum = int(''.join(x for x in pubDairyItemsString if x.isdigit()))
        for i in range(pubDairyItemsNum):
            xpath = '//*[@id="BrowseContent"]/div/ul/li/div/div/div[' + str(i + 1) + ']/div/div[3]/div[1]/h2'
            pubDairyList.append(publixDairyDriver.find_element(By.XPATH, xpath).text)
        publixDairyDriver.close()
        global bogoDairy
        bogoDairy = [item for item in pubDairyList if item in pubBOGOList]
        scrapedDairy = True

def scrapeDeli():
    global scrapedDeli
    global scrapedBOGO
    if not scrapedBOGO:
        scrapeBogo()
    if not scrapedDeli:
        pubDeliList.clear()
        publixDeliDriver = webdriver.Firefox()
        publixDeliDriver.get(publixDeliLink)
        pubDeliItemsString = publixDeliDriver.find_element(By.XPATH, '//*[@id="BrowseLayout"]/div/h1').get_attribute("innerText")
        pubDeliItemsNum = int(''.join(x for x in pubDeliItemsString if x.isdigit()))
        for i in range(pubDeliItemsNum):
            xpath = '//*[@id="BrowseContent"]/div/ul/li/div/div/div[' + str(i + 1) + ']/div/div[3]/div[1]/h2'
            pubDeliList.append(publixDeliDriver.find_element(By.XPATH, xpath).text)
        publixDeliDriver.close()
        global bogoDeli
        bogoDeli = [item for item in pubDeliList if item in pubBOGOList]
        scrapedDeli = True

def scrapeBogo():
    global scrapedBOGO
    global pubBOGOList
    if not scrapedBOGO:
        pubBOGOList.clear()
        publixBOGODriver = webdriver.Firefox()
        publixBOGODriver.get(publixBOGOLink)
        pubBOGOItemsString = publixBOGODriver.find_element(By.XPATH, '//*[@id="BrowseLayout"]/div/h1').get_attribute("innerText")
        pubBOGOItemsNum = int(''.join(x for x in pubBOGOItemsString if x.isdigit()))
        for i in range(pubBOGOItemsNum):
            xpath = '//*[@id="BrowseContent"]/div/ul/li/div/div/div[' + str(i + 1) + ']/div/div[3]/div[1]/h2'
            pubBOGOList.append(publixBOGODriver.find_element(By.XPATH, xpath).text)
        publixBOGODriver.close()
        scrapedBOGO = True

def createMaster():
    global masterBogoList
    scrapeBogo()
    scrapeDairy()
    scrapeDeli()
    scrapeGrocery()
    scrapeMeat()
    masterBogoList = bogoMeat + bogoDairy + bogoDeli + bogoGrocery + bogoProduce
    global masterListCreated
    masterListCreated = True
        
#####SHOW DEALS#######
    
def show_deals():
    print("Select from the following options: Grocery, Dairy, Deli, Meat, Produce, or Return to go back")

    options = {
        "grocery": printGrocery,
        "dairy": printDairy,
        "deli": printDeli,
        "meat": printMeat,
        "produce": printProduce,
        "return": main,
    }

    while True:
        user_input = input("Enter your choice: ").lower()
        if user_input in options:
            options[user_input]()
        else:
            print("Select from the provided options.")

def printGrocery():
    scrapeGrocery()
    scrapeBogo()
    print("These are the BOGO Grocery items: \n")
    for item in bogoGrocery:
        print(item + "\n")

def printDairy():
    scrapeDairy()
    scrapeBogo()
    print("These are the BOGO Dairy items: \n")
    for item in bogoDairy:
        print(item + "\n")

def printDeli():
    scrapeDeli()
    scrapeBogo()
    print("These are the BOGO Deli items: \n")
    for item in bogoDeli:
        print(item + "\n")

def printMeat():
    scrapeMeat()
    scrapeBogo()
    print("These are the BOGO Meat items: \n")
    for item in bogoMeat:
        print(item + "\n")

def printProduce():
    scrapeProduce()
    scrapeBogo()
    print("These are the BOGO Produce items: \n")
    for item in bogoProduce:
        print(item + "\n")

######SCORE MEALS########

def calcScore(list):
    if not masterListCreated:
        createMaster()
    score = 0
    for item in list:
        if any(item in s for s in masterBogoList):
            score+=1
            if any(item in s for s in bogoMeat):
                score+=2
            elif any(item in s for s in bogoMeat):
                score+=1
    return score

def listRecipes():
    files = os.listdir()
    recipe_files = [file for file in files if file.endswith('.txt')]
    if recipe_files:
        print("Recipe files found:")
        for file in recipe_files:
            print(file.replace('_', ' ').capitalize().replace('.txt', ''))
    else:
        print("No recipe files found in the directory.")
    scoreRecipe()

def scoreRecipe():
    recipe_name = input("For a list of recipes, type ##. To go back, type Return. Enter the name of the recipe file (without extension):").strip()
    if recipe_name == "##":
        listRecipes()
        return
    elif recipe_name.lower() == "return":
        viewMeals()
    filename = f"{recipe_name.replace(' ', '_').lower()}.txt"

    try:
        with open(filename, 'r') as file:
            ingredients = [line.strip() for line in file.readlines()]
            print(f"Ingredients read from {filename}: {ingredients}")

        savings_score = calcScore(ingredients)
        print(f"Savings score for the recipe '{recipe_name}': {savings_score}")

    except FileNotFoundError:
        print(f"File '{filename}' not found. Please ensure the recipe file exists.")

def scoreAll():
    recipes = listRecipesNoPrint()
    tupList = []
    for recipe in recipes:
        tupList.append(scoreRecipeGivenName(recipe))

    tupList.sort(key=lambda tup: tup[1])
    print("Here are the saving scores of your recipes:")
    for i in range(len(tupList)):
        print(tupList[0] + ":" + str(tupList[1]))

def viewMeals():

    options = {
        "score meal": scoreRecipe,
        "show all meals": scoreAll,
        "return": main
    }

    while True:
        user_input = input("Select from the following options: Score Meal, Show Best Deals, Return\nEnter your choice: ").lower()
        if user_input in options:
            options[user_input]()
        else:
            print("Select from the provided options.")

########HELPER FUNCTIONS FOR SCORE##########

def scoreRecipeGivenName(name):
    filename = name
    try:
        with open(filename, 'r') as file:
            ingredients = [line.strip() for line in file.readlines()]

        savings_score = calcScore(ingredients)
        scoreTuple = (name, savings_score)
        return scoreTuple
    
    except FileNotFoundError:
        print(f"File '{filename}' not found. Please ensure the recipe file exists.")

def listRecipesNoPrint():
    files = os.listdir()
    recipe_files = [file for file in files if file.endswith('.txt')]
    if recipe_files:
        return recipe_files  
    else:
        print("No recipe files found in the directory.")




##########ADD RECIPE################

def addRecipe():
    recipe_name = input("Enter the name of the recipe: ").strip()
    if not recipe_name:
        print("Recipe name cannot be empty. Please try again.")
        return
    elif recipe_name == "##" or recipe_name.lower() == "return":
        print("Restricted word - title cannot be '##' or 'return'")
        return
    filename = f"{recipe_name.replace(' ', '_').lower()}.txt"
    ingredients = []
    print("Enter each ingredient followed by Enter. Type 'Done' when finished.")
    while True:
        ingredient = input("Ingredient: ").strip()
        if ingredient.lower() == "done":
            break
        if ingredient:
            ingredients.append(ingredient)
        else:
            print("Ingredient cannot be empty. Please enter a valid ingredient.")
    with open(filename, 'w') as file:
        for ing in ingredients:
            file.write(f"{ing}\n")
        file.close()
    print(f"Recipe '{recipe_name}' saved to {filename}")
    next_action = input("Would you like to add another recipe or return to the main menu? (Add/Return): ").strip().lower()
    if next_action.lower() == "return":
        main()
    elif next_action.lower() == "add":
        addRecipe()

#########GENERATE RECIPE############

def generateRecipe():
    print("Generating Recipe:")
    global masterListCreated
    if not masterListCreated:
        createMaster()
    global masterBogoList
    stringList = ''.join(masterBogoList)
    prompt = "The following list contains relevant items on sale at Publix. Generate a few meals that utilize some of the ingredients found on the sale list. Recipes should not contain only ingredients that I have provided, and should be relatively simple and popular. Prioritize utilizing more expensive components such as meat and produce off of the sale list if possible. Here is the list:" + stringList
    response = model.generate_content(prompt)
    print(response.text)

#######MAIN############

def main():
    print("Welcome to Recibot. What would you like me to do for you?")

    options = {
        "show deals": show_deals,
        "calculate cheap meals": viewMeals,
        "add recipe": addRecipe,
        "generate recipe": generateRecipe
    }

    while True:
        user_input = input("Select from the following options: Show Deals, Calculate Cheap Meals, Add Recipe, Generate Recipe\nEnter your choice: ").lower()
        if user_input in options:
            options[user_input]()
        else:
            print("Select from the provided options.")

if __name__ == "__main__":
    main()