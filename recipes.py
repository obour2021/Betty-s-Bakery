import numpy as np
import csv
cupcakes = np.array([2, 0.75, 2, 1, 0.5])
recipes = np.genfromtxt('recipes.csv', delimiter=',')
print(recipes)
eggs = recipes[:,2]
# print(eggs)
one_egg_recipe = recipes[(eggs == 1)]
print(one_egg_recipe)
cookies = recipes[2,:]
print(cookies)
double_batch = 2 * cupcakes
grocery_list = cookies + double_batch
print(grocery_list)
