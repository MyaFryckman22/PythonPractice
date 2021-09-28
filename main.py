#define function 
def topfivefryproviders():
    #print first fry
    print("Space Aliens")

    #print second fry
    print("Dairy Queen")

    #print third fry
    print("Disco Fries R.I.P.")

    #print fourth fry
    print("Culvers")

    #print fifth fry
    print("waffle fries")
topfivefryproviders()

def myNameIs(Emotionalsupportstring):
    print(Emotionalsupportstring + " is my name")

myNameIs("Mya")
myNameIs("Libby Leonard")

# define function 
def timesTen(num):
    print(num * 10)

timesTen(31)

#define function
def plusFive(num):
    print(num + 5)

plusFive(2)

#define function 
def divideByTwo(num):
    print(num / 2)

divideByTwo(6)

def addTwoNumbers(x, y, z):
    print(x + y + z)

addTwoNumbers(4,2,236)

#define function 
def color():   
    #return color
    return "lavender"

print(color() + " is my favorite color")

def greaterThan10(x):
    if x > 10:
        return "x is greater than 10"

    elif x == 10:
        return "x equals 10"

    else:
        return "x is not greater than 10"

print(greaterThan10(10))

def potato(x,y):
    if x+ y > 10:
        return "potato"

    elif x + y == 10:
        return "tomato" 

    else:
        return "alfredo" 

print(potato(3, 3))



if "cat" < "dog":
    print ("wow I can't believe this worked")
else:
    print ("wow I still can't believe this worked")



def login(password):
    if password == "Ratchelor":
        return "ACCESS GRANTED"
    else:
        return "ACCESS DENIED"

print(login("Ratchelor"))

def trivia(answer):
    if answer.lower() == "gerald":
        return "bingo"
    else: 
        return "git gud lol"

print (trivia("Gerald"))

print("Gerald".lower())
print("Gerald".upper())

def fiveSauces(sauce):

    sauce = sauce.lower()

    if sauce == "tomato":
        return "Bingo"

    elif sauce == "mayonaise":
        return "Bingo"

    elif sauce == "bechamel":
        return "Bingo"

    elif sauce == "espagnole":
        return "Bingo"

    elif sauce == "veloute":
        return "Bingo"

    else:
        return "uncultured swine..."

print(fiveSauces("tomato"))

def define(word):

    word = word.lower()

    if word == "cat":
        return "a small domesticated carnivorous mammal with soft fur, a short snout, and retractable claws. It is widely kept as a pet or for catching mice, and many breeds have been developed"

    elif word == "dog":
        return "a domesticated carnivorous mammal that typically has a long snout, an acute sense of smell, nonretractable claws, and a barking, howling, or whining voice."

    elif word == "bird":
        return "a warm-blooded egg-laying vertebrate distinguished by the possession of feathers, wings, and a beak and (typically) by being able to fly"

    elif word == "rabbit":
        return "a burrowing, gregarious, plant-eating mammal with long ears, long hind legs, and a short tail"

    elif word == "mouse":
        return "a small rodent that typically has a pointed snout, relatively large ears and eyes, and a long tail."

    elif word == "fish":
        return "a limbless cold-blooded vertebrate animal with gills and fins and living wholly in water."

    elif word == "lizard":
        return "a reptile that typically has a long body and tail, four legs, movable eyelids, and a rough, scaly, or spiny skin"

    elif word == "goat":
        return "a hardy domesticated ruminant animal that has backward curving horns and (in the male) a beard. It is kept for its milk and meat and is noted for its lively and frisky behavior."

    elif word == "chicken":
        return "a domestic fowl kept for its eggs or meat, especially a young one."

    elif word == "hedgehog":
        return "a small nocturnal Old World mammal with a spiny coat and short legs, able to roll itself into a ball for defense."

    else:
        return "that word is not recognized in this dictionary"

print(define("worm"))