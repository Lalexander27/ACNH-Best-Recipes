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
      
      if stoneNum < 0 or ironNum < 0 or clayNum < 0:
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

  totalProfit = stoneProfit + ironProfit + clayProfit
  #note that bells are the currency of the game
  print("Selling all of these items will yield", totalProfit, "bells.")

if __name__ == '__main__':
  main()
