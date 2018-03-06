# This is a tiny adventure game made using if statement

print("""
CONDOMINIUM UPPER LEVEL

You are in the upper level of a small condominium overlooking Boardman Lake.
It is tastefully decorated with modern furnishings. The walls are covered with
paintings contemporary artists. You examine one, which depicts nudes falling
from the sky near a lake. Stairs lead down, and an open sliding glass door
leads east to a balcony.
""")

direction = input("> ")

if direction == "E" or direction == "East" or direction == "e" or direction == "east":
    print("""
BALCONY

You are standing on a balcony overlooking Boardman Lake. The lake is a
breathtaking blue and small sailboats ply the waters. On the north end
of the lake is a small boathouse. Across the lake to the east you see a
clock tower.
    """)

    direction = input("> ")

    if direction == "W" or direction == "West" or direction == "w" or direction == "west":
        print("""
CONDOMINIUM UPPER LEVEL

You are back in the condominium upper level. Stairs lead down and
an open sliding glass door leads to a balcony to the east.
        """)

        direction = input("> ")

        if direction == "E" or direction == "East" or direction == "e" or direction == "east":
            print("""
BALCONY

You return to the balcony. A soft breeze brushes your face. You sit
in a rocking chair, and help yourself to a glass of wine. Soon, you
fall asleep, secure in the knowledge that your adventure is over
for today.

    *** Game Over ***
            """)
            quit()

        elif direction == "D" or direction == "Down" or direction == "d" or direction == "down":
            print("""
CONDOMINIUM LOWER LEVEL

You descend carpeted stairs and enter a large room. One end contains
a home office, the other a media center with a flat screen TV and a
very comfy looking sofa. Bookshelves and art line the walls. To the
east, an open sliding door leads to the outside.
            """)

            direction = input("> ")

            if direction == "E" or direction == "East" or direction == "e" or direction == "east":
                print("""
TRAIL NEAR CONDOMINIUM

You exit the condominium and scramble down a steep grassy slope,
reaching the Boardman Lake Trail. Waves lap invitingly against
the shore. The trail stretches to the north and south, but you
are content to stay where you are, soaking up the sunshine and
admiring the ducks swimming nearby.

    *** Congratulations! You win!! ***
                """)
                quit()

            elif direction == "U" or direction == "Up" or direction == "u" or direction == "up":
                print("""
CONDOMINIUM LOWER LEVEL

You look at the stairs, realize you are too lazy to climb them,
and flop down on the comfy sofa. Soon, you are snoozing away,
secure in the knowledge your adventure is over for today.

    *** Game Over ***
                """)
                quit()

            else:
                print("""
CONDOMINIUM LOWER LEVEL

You wander about, realize you are too lazy to climb the stairs,
and flop down on the comfy sofa. Soon, you are snoozing away,
secure in the knowledge your adventure is over for today.

    *** Game Over ***
                """)
                quit()

        else:
            print("""
CONDOMINIUM UPPER LEVEL

You walk into a wall. A heavy work of art falls down, hitting you
on the head. As you sink into unconsciousness, you regret that the
owners hadn't collected more work by Carl Andre.

    *** You have died. ***
            """)
            quit()

    else:
        print("""
GROUND BENEATH BALCONY

You leap off the balcony, landing on your head. As you slip into
unconsciousness, you admire Boardman Lake for the very last time.

        *** You have died. ***
        """)
        quit()

elif direction == "D" or direction == "Down" or direction == "d" or direction == "down":
    print("""
CONDOMINIUM LOWER LEVEL

You descend carpeted stairs and enter a large room. One end contains
a home office, the other a media center with a flat screen TV and a
very comfy looking sofa. Bookshelves and art line the walls. To the
east, an open sliding door leads to the outside.
            """)

    direction = input("> ")

    if direction == "E" or direction == "East" or direction == "e" or direction == "east":
        print("""
TRAIL NEAR CONDOMINIUM

You exit the condominium and scramble down a steep grassy slope,
reaching the Boardman Lake Trail. Waves lap invitingly against
the shore. The trail stretches to the north and south, but you
are content to stay where you are, soaking up the sunshine and
admiring the ducks swimming nearby.

    *** Congratulations! You win!! ***
                """)
        quit()

    elif direction == "U" or direction == "Up" or direction == "u" or direction == "up":
        print("""
CONDOMINIUM LOWER LEVEL

You look at the stairs, realize you are too lazy to climb them,
and flop down on the comfy sofa. Soon, you are snoozing away,
secure in the knowledge your adventure is over for today.

    *** Game Over ***
                """)
        quit()

    else:
        print("""
CONDOMINIUM LOWER LEVEL

You wander about, realize you are too lazy to climb the stairs,
and flop down on the comfy sofa. Soon, you are snoozing away,
secure in the knowledge your adventure is over for today.

    *** Game Over ***
                """)
        quit()

else:
    print("""
CONDOMINIUM UPPER LEVEL

You walk into a wall. A heavy work of art falls down, hitting you
on the head. As you sink into unconsciousness, you regret that the
owners hadn't collected more work by Carl Andre.

*** You have died. ***
    """)
    quit()
