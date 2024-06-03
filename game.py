def mad_libs():
    # Get user inputs
    name = input("Enter your name: ")
    friend = input("Enter a friend's name: ")
    disney_character = input("Enter a Disney character: ")
    superhero = input("Enter a superhero: ")
    famous_person = input("Enter a famous person: ")
    noun1 = input("Enter a noun: ")
    noun2 = input("Enter another noun: ")
    adjective1 = input("Enter an adjective: ")
    adjective2 = input("Enter another adjective: ")
    adjective3 = input("Enter one more adjective: ")
    verb1 = input("Enter a verb: ")
    verb2 = input("Enter another verb: ")
    place = input("Enter a place: ")
    animal = input("Enter an animal: ")
    food = input("Enter a type of food: ")
    number = input("Enter a number: ")
    exclamation = input("Enter an exclamation: ")
    color = input("Enter a color: ")
    vehicle = input("Enter a type of vehicle: ")

    # Create the story using f-strings
    story = f"""
    Once upon a time, in the {adjective1} land of {place}, there lived a {adjective2} {animal} named {disney_character}.
    One day, {disney_character} decided to go on an adventure with {superhero} and {famous_person}.
    They packed their {noun1}, hopped on a {color} {vehicle}, and set off for the {adjective3} journey of a lifetime.

    As they traveled, they encountered a talking {noun2} who could {verb1}. 
    "{exclamation}!" said {name}, "I've never seen anything like this!"

    The group decided to follow the talking {noun2}, which led them to a hidden treasure chest filled with {food}.
    Overjoyed, {friend} exclaimed, "This is the best day ever!" and started to {verb2}.

    Suddenly, a wild {animal} appeared and challenged them to a dance-off. 
    With the help of {superhero} and {disney_character}, they performed the most epic dance routine ever seen.
    In the end, they won the dance-off and the {animal} joined their team.

    Together, they all {verb2}ed back home and celebrated their victory by eating {number} servings of {food}.
    And from that day on, they were known as the {adjective2} heroes of {place}, living {adjective3}ly ever after.
    """

    # Print the story
    print(story)

# Run the game
mad_libs()
