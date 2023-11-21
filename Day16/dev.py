from Day17.main import MENU, resources


def generate_resources(resources):
    return

# TODO 1 - Ask the user for input:

is_on = True

while is_on:
    choice = input('What would you like? (espresso/latte/cappuccino: ').lower()
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        for key, value in resources.items():
            print(f"{value}")





