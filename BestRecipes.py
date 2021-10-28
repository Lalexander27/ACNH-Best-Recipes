#Query user for amount of resources and store as separate integers.  Use while loop and try/except to catch errors and report them to user
def craftRecipes(resources, recipeList):
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

def main():
  while True:
    try:
      print("Hello, this program is to help you select items to craft in Animal Crossing New Horizons based off your resources.\nThe goal is to craft profitable resources while minimizing crafting time.\n When asked, please type the amount of resources you have as a positive integer or 0.")
      stoneNum = int(input("How much stone do you have?: "))
      ironNum = int(input("How much iron do you have?: "))
      clayNum = int(input("How much clay do you have?: "))
    except ValueError:
      print("Please type the number of resources you have as an integer.")
    else:
      break

  stoneRecipes = {90: "Stone Arch", 60: "Tall Garden Rock", 30: "Western-Style Stone", 24: "Stone Lion-Dog", 20: "Flat Garden Rock", 18: "Tall Lantern", 15: "Garden Rock", 12: "Stone Tablet", 10: "Pond Stone", 8: "Stone Table", 6: "Birdbath", 3: "Stone Stool"}
  print("You should craft:", craftRecipes(stoneNum, stoneRecipes))

  ironRecipes = {20: "Iron Frame", 14: "Iron Shelf", 12: "Iron Closet", 10: "Iron Worktable", 8: "Iron Armor", 7: "Steel Flooring", 5: "Knight's helmet", 4: "Armor Shoes", 3: "Standard Umbrella Stand", 2: "Iron Doorplate"}
  print("You should craft:",craftRecipes(ironNum, ironRecipes))

  clayRecipes = {6: "Raccoon Figurine", 5: "Pot", 2: "Modeling Clay"}
  print("You should craft:",craftRecipes(clayNum, clayRecipes))

if __name__ == '__main__':
  main()
