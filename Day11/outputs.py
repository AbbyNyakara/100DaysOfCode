# Functions that have outputs 

# Create a function that retunrs the capitalized first letter of every word
# Docstrings provide information on the function

# When you hover over it, it will say what the function does.
def capitalize_letters(first_name, last_name):
    """
    Takes in the first and last name and returns the title case version
    of the string
    """
    return(f"{first_name.title()} {last_name.title()}")

print(capitalize_letters('Abby', 'nyakara'))