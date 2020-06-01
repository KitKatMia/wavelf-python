water = 400
milk = 540
coffee = 120
disposable_cups = 9
money = 550
flavor = ''

def material_available():
    print(f'''\nThe coffee machine has:\n{water} of water
{milk} of milk
{coffee} of coffee beans
{disposable_cups} of disposable cups
${money} of money''')

def remaining():
    material_available()
    select_action()

def check_availability():
    global flavor
    flavor = input('\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ')

    if flavor == '1':
        if water < 250:
            print('Sorry, not enough water!')
        elif coffee < 16:
            print('Sorry, not enough coffee!')
        elif disposable_cups < 1:
            print('Sorry, not enough cups!')
        else:
            print('I have enough resources, making you a coffee!')
            buy()

    elif flavor == '2':
        if water < 350:
            print('Sorry, not enough water!')
        elif milk < 75:
            print('Sorry, not enough milk!')
        elif coffee < 20:
            print('Sorry, not enough coffee!')
        elif disposable_cups < 1:
            print('Sorry, not enough disposable cups')
        else:
            print('I have enough resources, making you a coffee!')
            buy()

    elif flavor == '3':
        if water < 200:
            print('Sorry, not enough water!')
        elif milk < 100:
            print('Sorry, not enough milk!')
        elif coffee < 12:
            print('Sorry, not enough coffee!')
        elif disposable_cups < 1:
            print('Sorry, not enough disposable cups')
        else:
            print('I have enough resources, making you a coffee!')
            buy()
    select_action()

def buy():
    global water, milk, coffee, money, disposable_cups
    if flavor == '1':
        water -= 250
        coffee -= 16
        disposable_cups -= 1
        money += 4
    elif flavor == '2':
        water -= 350
        milk -= 75
        coffee -= 20
        disposable_cups -= 1
        money += 7
    elif flavor == '3':
        water -= 200
        milk -= 100
        coffee -= 12
        disposable_cups -= 1
        money += 6
    elif flavor == 'back':
        select_action()

def fill():
    global water, milk, coffee, money, disposable_cups
    add_water = int(input('\nWrite how many ml of water do you want to add: '))
    water += add_water
    add_milk = int(input('Write how many ml of milk do you want to add: '))
    milk += add_milk
    add_coffee = int(input('Write how many grams of water do you want to add: '))
    coffee += add_coffee
    add_cups = int(input('Write how many disposable cups of coffee do you want to add: '))
    disposable_cups += add_cups
    select_action()

def take():
    global money
    print(f'I gave you ${money}')
    money = 0
    select_action()

def select_action():
    action = input('\nWrite action (buy, fill, take, remaining, exit): ')
    if action == 'buy':
        check_availability()
    elif action == 'fill':
        fill()
    elif action == 'take':
        take()
    elif action == 'remaining':
        remaining()
    elif action == 'exit':
        exit()

select_action()
