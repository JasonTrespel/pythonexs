# CHALLENGE: Complex Data Slicing, For Loops, and Superhero Programmers!

<img src="https://simpleprogrammer.com/wp-content/uploads/2019/04/programmer-hero.png" alt="drawing" width="300"/>

### Attempt these challenges in increasing difficulty!

**Part 1.** Find your name in the `classinfo` dictionary below. Write code that prints your first name from the `classinfo` data shown here.

**Part 2.** Find your name in the `classinfo` dictionary below.  Write a script that outputs **ONE** of the following using the `classinfo` dictionary below. (fill in the blank!):

	My name is ______ and my spirit animal is _______.

	My name is ______ and my skills are _______.

	My name is ______ and my super power is _______.


**Part 3.** Write a script that loops through the entire `classinfo` dictionary. Have it output the following for every person in class:

#### EXAMPLE:
	

    Mario, a <wondrous> <alpaca> of a programmer, possesses a <structure weakening> factor for moonlighting as a superhero!
    
    Luigi, an <admirable> <donkey> of a programmer, possesses a <super strength> factor for moonlighting as a superhero!

[...and so on!]


```python
classinfo = {
    "all": [
        {
            "name": "Aaron",
            "skill level": "wondrous",
            "spirit animal": "Alpaca",
            "super power": "Structure Weakening",
        },
        {
            "name": "Alexandra",
            "skill level": "admirable",
            "spirit animal": "Shark",
            "super power": "Super Strength",
        },
        {
            "name": "Alice",
            "skill level": "amazing",
            "spirit animal": "Goat",
            "super power": "Weather Control",
        },
        {
            "name": "Angela",
            "skill level": "astonishing",
            "spirit animal": "Banana",
            "super power": "Flight",
        },
        {
            "name": "Ayrat",
            "skill level": "awesome",
            "spirit animal": "Horse",
            "super power": "X-ray Vision",
        },
        {
            "name": "Blake",
            "skill level": "brilliant",
            "spirit animal": "Eagle",
            "super power": "Shape of: A Giant Shark",
        },
        {
            "name": "Brandon",
            "skill level": "cool",
            "spirit animal": "Rabbit",
            "super power": "Invisibility",
        },
        {
            "name": "Carl",
            "skill level": "enjoyable",
            "spirit animal": "Water buffalo",
            "super power": "Transformation",
        },
        {
            "name": "Chris",
            "skill level": "excellent",
            "spirit animal": "Chicken",
            "super power": "Pyrokinesis",
        },
        {
            "name": "Christian",
            "skill level": "fabulous",
            "spirit animal": "Duck",
            "super power": "Invulnerability",
        },
        {
            "name": "Deepak",
            "skill level": "fantastic",
            "spirit animal": "Goose",
            "super power": "Explosive Shouts",
        },
        {
            "name": "Dom",
            "skill level": "great",
            "spirit animal": "Pigeon",
            "super power": "Matter Ingestion",
        },
        {
            "name": "Felicia",
            "skill level": "incredible",
            "spirit animal": "Turkey",
            "super power": "Zoolingualism",
        },
        {
            "name": "Gabriel",
            "skill level": "magnificent",
            "spirit animal": "Aardvark",
            "super power": "Height Manipulation",
        },
        {
            "name": "Julian",
            "skill level": "marvelous",
            "spirit animal": "Aardwolf",
            "super power": "Hydrokinesis",
        },
        {
            "name": "Kelly",
            "skill level": "outstanding",
            "spirit animal": "Elephant",
            "super power": "Needle Projection",
        },
        {
            "name": "Lashay",
            "skill level": "phenomenal",
            "spirit animal": "Leopard",
            "super power": "Stretchy",
        },
        {
            "name": "Ripal",
            "skill level": "pleasant",
            "spirit animal": "Albatross",
            "super power": "Steel Skin",
        },
        {
            "name": "Rod",
            "skill level": "pleasing",
            "spirit animal": "Alligator",
            "super power": "Teleportation",
        },
        {
            "name": "Samuel",
            "skill level": "remarkable",
            "spirit animal": "Lynx",
            "super power": "Polyglot",
        },
        {
            "name": "Thomas",
            "skill level": "super",
            "spirit animal": "Fox",
            "super power": "Eat Anything",
        },
    ]
}
```


THE SOLUTION IS BELOW! NO CHEATING! 





### SOLUTION

```python
# parts 1 and 2
name= classinfo["all"][2]["name"]
power= classinfo["all"][2]["super power"]

print(name, "has the power of", power)

# part 3
for x in classinfo["all"]:
    name= x["name"]
    skill= x["skill level"]
    power= x["super power"]
    animal= x["spirit animal"]

    # Mario, a <wondrous> <alpaca> of a programmer, possesses a <structure weakening> factor for moonlighting as a superhero!
    print(f"{name}, a {skill} {animal} of a programmer, possesses a {power} factor for moonlighting as a superhero!")
```
