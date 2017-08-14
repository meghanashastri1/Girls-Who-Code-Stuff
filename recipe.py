print ("Here's a recipe for Oreo truffles")
ingredients = {'Oreos':'16 ounces', 'Cream Cheese':'8 ounces', 'Chocolate':'16 ounces'}
directions = []
directions.append("Step 1. Crush the oreos to crumbs and mix it in with cream cheese")
directions.append("Step 2. roll the mixture into truffles and place the truffles in a tray")
directions.append("Step 3. Place the tray into the fridge for 30 minutes")
directions.append("Step 4. Melt the chocolate for 40 seconds in the microwave using a heatproof bowl")
directions.append("Step 5. Take the truffles out of the fridge and place each one in the melted chocolate to cover them")
directions.append("Step 6. Place the truffles onto a tray and let them cool down")

for item in ingredients.items():
    print (item)
for index in directions:
    print (index)
