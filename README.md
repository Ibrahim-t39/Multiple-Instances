# Turtle Race Game

## Full Description

The Turtle Race Game is an engaging Python project that uses the Turtle graphics module to simulate a race between six turtles of different colors. The player starts by betting on a turtle, and the race begins with each turtle moving forward randomly. The first turtle to cross the finish line wins, and the game announces whether the player's bet was correct.

**Features:**
- **User Betting:** Players can bet on which turtle they think will win the race, adding an element of excitement and competition.
- **Randomized Racing:** Each turtle's movement is randomized, making the race unpredictable and thrilling.
- **Colorful Turtles:** Six turtles of different colors participate in the race, each starting from a different position.
- **Winner Announcement:** The game announces the winner and whether the player’s bet was successful.

**Note**: This project was inspired by Angela Yu's course on Udemy.

## Getting Started

### Prerequisites

- Python 3.x installed on your system.
- The Turtle graphics module (usually included with Python installations).

### How to Play

1. Clone or download the repository to your local machine.
2. Run the script using Python:

   ```bash
   python turtle_race.py
   ```

3. When prompted, enter your bet on which turtle (by color) you think will win the race.
4. Watch the race as the turtles move forward at random speeds.
5. The game will announce the winning turtle and whether your bet was correct.

### Customization

You can customize the Turtle Race Game by:
- **Changing Colors:** Modify the `colors` list to include different colors for the turtles.
- **Adjusting Speeds:** Change the range of random movement in the `randint(0,10)` function to make the race faster or slower.
- **Adding Turtles:** Increase or decrease the number of turtles in the race by adjusting the `colors` and `y_positions` lists and the loop that creates the turtles.
