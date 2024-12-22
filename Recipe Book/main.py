import datetime 
import os
print('Welcome to Recipe Book. \n')
recipes_available = open('Recipes_file_and_name.csv', 'r')
print(recipes_available.read())

# 1. Add a Recipe: Prompt the user to enter the title, ingredients, and preparation steps of a recipe.
yes = input('Do you want to add a Recipe?, please type yes or no: ')
file_name = input('File name to save the information to: ')
if yes == 'yes':
    class add:
        def day():
            started = datetime.datetime.now()
            p = open(f'{file_name}', 'a')
            p.write(f'{str(started)}\n')
        day()
        # Title
        def title():
            title = input('Title of the Recipe: ')
            p = open(str(file_name), 'a')
            p.write(f"Title: {str(title)}\n")
        title()

        # Ingredients
        print('Please list the Ingredients.')
        def ingre():
            t = open(str(file_name), 'a')
            t.write('\nIngredients:\n')
        ingre()

        num_of_list = 0
        while num_of_list <= 14:
            if num_of_list <=100:
                num_of_list+=1
            def ingredient(num_of_list):
                t = open(str(file_name), 'a')
                t.write(f'{num_of_list}{input()}\n')
            ingredient(f'{num_of_list}. ')

        # Preparation steps
        print('Preparation steps')
        def name():
            t = open(str(file_name), 'a')
            t.write('\nPreparation steps:\n')
        name()

        num = 0
        while num <=9:
            if num <=100:
                num+=1
            def number(num):
                f = open(str(file_name), 'a')
                f.write(f'{num}{input()}\n')
            number(f'{num}. ')
else:
    print('bye')


# # 2. View Recipes: Display a list of all recipes and allow the user to select one to view its details.
# View_Recipes name and file name
print('------------------------------------------')
w = open(f'Recipes_file_and_name.csv', 'r')
print(w.read())

# select Recipe and view detail
print('------------------------------------------')
recipe_data = input('Which Recipe do you want to view?(Please type in the file name.): ')
q = open(f'{recipe_data}.csv', 'r')
print(q.read())

print('------------------------------------------')


# 3. Edit a Recipe: Allow the user to edit an existing recipe's title, ingredients, or preparation steps.
added = input('Do you want to edit the Recipe?, please type yes or no: ')
if added == 'yes':
    file = input('File name: ')
    day = datetime.datetime.now()
    update = open(f'{file}.csv', 'a')
    update.write(f'\n\n\n\n\n\nUPDATE! {day}\nCHANGES MADE IN THE RECIPE!')
    info = input('Which put do you want to edit: ')

    # edited the title
    if info == 'title':
        title = input('Title: ')
        u = open(f'{file}.csv','a')
        u.write(f'\nTitle: {str(title)}')
    else:
        print('No edit for title.')

    # edited the ingredients
    if info == 'ingredients':
        ingredients = input('ingredients: \n')
        u = open(f'{file}.csv','a')
        u.write(f'\nIngredients:\n{str(ingredients)}')
    else:
        print('No edit for ingredients.')

    # edited the preparation steps
    if info == 'preparation steps':
        preparation = input('Preparation steps:  \n')
        u = open(f'{file}.csv','a')
        u.write(f'\nPreparation:\n{str(preparation)}')
    else:
        print('No edit for preparation.')
else:
    print('bye')

# 4. Delete a Recipe: Provide an option to delete a recipe from the book.
do = input('Do you want to delete a Recipe file? Please type yes or no: ')
if do == 'yes':
    delete_file = input('Which Recipe File do you want to delete: ')
    if os.path.exists(f'{delete_file}.csv'):
        os.remove(f'{delete_file}.csv')
    else:
        print("File Recipe has already been deleted")
else:
    print('bye')
