#Query user for amount of resources and store as separate integers.  Use while loop and try/except to catch errors and report them to user
def craftRecipes(resources, recipeList):
  #resources is an integer holding the number of resources, recipeList is a dictionary of items you can craft with that resource
  #store resource number, prepare dictionary for crafted items
  finalResources = resources
  craftedItems = {}
  craftCount = 0

  #iterate through recipeList, starting with recipes that use the most resources
  for key in recipeList:
    while finalResources >= key:
      #when there's enough resources to craft an item, craft and record it 
      craftCount += 1
      craftedItems[recipeList[key]] = craftCount
      finalResources -= key

    craftCount = 0
  
  #record leftover resource count   
  if finalResources > 0:
    craftedItems["Spare Resources"] = finalResources

  return craftedItems

def profitRecipes(goods, recipeProfit):
#goods is a dictionary of the crafted items, recipeProfit is a dictionary of the sell price of items
  profit = 0

  for key in goods:
    if key in recipeProfit:
      profit += goods[key] * recipeProfit[key]

  return profit

def main():
  while True:
    try:
      print("Hello, this program is to help you select items to craft in Animal Crossing New Horizons based off your resources.\nThe goal is to craft profitable items while minimizing crafting time.\n When asked, please type the amount of resources you have as a positive integer or 0.")
      stoneNum = int(input("How much stone do you have?: "))
      ironNum = int(input("How much iron do you have?: "))
      clayNum = int(input("How much clay do you have?: "))
      woodNum = int(input("How much wood do you have?: "))
      hardwoodNum = int(input("How much hardwood do you have?: "))
      softwoodNum = int(input("How much softwood do you have?: "))
      
      if stoneNum < 0 or ironNum < 0 or clayNum < 0 or woodNum < 0 or hardwoodNum < 0 or softwoodNum < 0:
        raise ValueError
        
    except ValueError:
      print("Please type the number of resources you have as a positive integer.")
    else:
      break

  stoneRecipes = {90: "Stone Arch", 60: "Tall Garden Rock", 30: "Western-Style Stone", 24: "Stone Lion-Dog", 20: "Flat Garden Rock", 18: "Tall Lantern", 15: "Garden Rock", 12: "Stone Tablet", 10: "Pond Stone", 8: "Stone Table", 6: "Birdbath", 3: "Stone Stool"}
  craftedStone = craftRecipes(stoneNum, stoneRecipes)
  print("You should craft:", craftedStone)
  stoneValue = {"Stone Arch": 13500, "Tall Garden Rock": 9000, "Western-Style Stone": 4500, "Stone Lion-Dog": 3600, "Flat Garden Rock": 3000, "Tall Lantern": 2700, "Garden Rock": 2250, "Stone Tablet": 1800, "Pond Stone": 1500, "Stone Table": 1200, "Birdbath": 900, "Stone Stool": 450}
  stoneProfit = profitRecipes(craftedStone, stoneValue)

  ironRecipes = {20: "Iron Frame", 14: "Iron Shelf", 12: "Iron Closet", 10: "Iron Worktable", 8: "Iron Armor", 7: "Steel Flooring", 5: "Knight's Helmet", 4: "Armor Shoes", 3: "Standard Umbrella Stand", 2: "Iron Doorplate"}
  craftedIron = craftRecipes(ironNum, ironRecipes)
  print("You should craft:", craftedIron)
  ironValue = {"Iron Frame": 15000, "Iron Shelf": 10500, "Iron Closet": 9000, "Iron Worktable": 7500, "Iron Armor": 6000, "Steel Flooring": 5250, "Knight's Helmet": 3750, "Armor Shoes": 3000, "Standard Umbrella Stand": 2250, "Iron Doorplate": 1500}
  ironProfit = profitRecipes(craftedIron, ironValue)

  clayRecipes = {6: "Raccoon Figurine", 5: "Pot", 2: "Modeling Clay"}
  craftedClay = craftRecipes(clayNum, clayRecipes)
  print("You should craft:", craftedClay)
  clayValue = {"Raccoon Figurine": 1200, "Pot": 1000, "Modeling Clay": 400}
  clayProfit = profitRecipes(craftedClay, clayRecipes)

  woodRecipes = {30: "Wooden Double Bed", 18: "Wooden Simple Bed", 16: "Wooden Chest", 15: "Wooden-Mosaic Wall", 12: "Wooden Wardrobe", 10: "Wooden Low Table", 8: "Birdcage", 6: "Wooden Chair", 4: "Wooden Stool", 3: "Paw-Print Doorplate"}
  craftedWood = craftRecipes(woodNum, woodRecipes)
  print("You should craft:", craftedWood)
  woodValue = {"Wooden Double Bed": 3600, "Wooden Simple Bed": 2160, "Wooden Chest": 1920, "Wooden-Mosaic Wall": 1800, "Wooden Wardrobe": 1440, "Wooden Low Table": 1200, "Birdcage": 960, "Wooden Chair": 720, "Wooden Stool": 480, "Paw-Print Doorplate": 360}
  woodProfit = profitRecipes(craftedWood, woodRecipes)

  hardwoodRecipes = {30: "Log Bed", 15: "Cabin Wall", 12: "Log Garden Lounge", 8: "Music Stand", 5: "Wooden-Plank Sign", 4: "Log Stool", 3: "Boomerang"}
  craftedHardwood = craftRecipes(hardwoodNum, hardwoodRecipes)
  print("You should craft:", craftedHardwood)
  hardwoodValue = {"Log Bed": 3600, "Cabin Wall": 1800, "Log Garden Lounge": 1440, "Music Stand": 960, "Wooden-Plank Sign": 600, "Log Stool": 480, "Boomerang": 360}
  hardwoodProfit = profitRecipes(craftedHardwood, hardwoodRecipes)

  softwoodRecipes = {15: "Brown Herringbone Wall", 8: "Deer Decoration", 5: "Rocking Horse", 4: "Decoy Duck", 3: "Old-Fashioned Washtub"}
  craftedSoftwood = craftRecipes(softwoodNum, softwoodRecipes)
  print("You should craft:", craftedSoftwood)
  softwoodValue = {"Brown Herringbone Wall": 1800, "Deer Decoration": 960, "Rocking Horse": 600, "Decoy Duck": 480, "Old-Fashioned Washtub": 360}
  softwoodProfit = profitRecipes(craftedSoftwood, softwoodRecipes)
  
  totalProfit = stoneProfit + ironProfit + clayProfit
  #note that bells are the currency of the game
  print("Selling all of these items will yield", totalProfit, "bells.")

if __name__ == '__main__':
  main()
