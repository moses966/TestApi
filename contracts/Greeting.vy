# pragma version ^0.3.10

# Declaring a public variable 'greet'
greet: public(String[30])

@external
def __init__():
    self.greet = "Kyakonye, goodmorning!"
