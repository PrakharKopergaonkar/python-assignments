fruits = {"apple":{"binomial name": "malus domestica", "major producers": ["china", "united states", "turkey"], "nutrition":{"carbohydrates":"13.81", "fat":"0.17", "protein":"0.26"}},
          "banana":{"binomial name": "malus domestica2", "major producers": ["india", "china", "pakistan"], "nutrition":{"carbohydrates":"13.00", "fat":"0.15", "protein":"0.23"}},
          "mango":{"binomial name": "malus domestica3", "major producers": ["india", "brazil", "sri lanka"], "nutrition":{"carbohydrates":"14.21", "fat":"0.25", "protein":"1.26"}}}
maxproteinvalues = 0
maxproteinfruit = ""
maxproteinvalueinchina = 0
maxproteinfruitinchina = ""
for itemvalues in fruits.keys():
    item = False
    itemvalues1 = fruits[itemvalues]
    for fruitvalues in itemvalues1.keys():
        if(fruitvalues == "major producers" and "china" in itemvalues1[fruitvalues]):
            item = True
        if(fruitvalues == "nutrition"):
            for nutritionvalues in itemvalues1[fruitvalues].keys():
                if(nutritionvalues == "protein" and float(itemvalues1[fruitvalues][nutritionvalues])>maxproteinvalues):
                    maxproteinvalues = float(itemvalues1[fruitvalues][nutritionvalues])
                    maxproteinfruit = itemvalues
                if(item==True and nutritionvalues == "protein" and float(itemvalues1[fruitvalues][nutritionvalues]) > maxproteinvalueinchina):
                    maxproteinvalueinchina = float(itemvalues1[fruitvalues][nutritionvalues])
                    maxproteinfruitinchina = itemvalues
print("max protein fruit : {} with protein value : {}".format(maxproteinfruit, maxproteinvalues))
print("max protein fruit in china : {} with protein value: {}".format(maxproteinfruitinchina, maxproteinvalueinchina))
