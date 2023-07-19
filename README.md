<h1 align="center">Minefield - Portfolio Project 3</h1>

![REMS]()

Minefield is a python terminal game of [minesweeper](https://en.wikipedia.org/wiki/Minesweeper_(video_game)) and it is deployed on Heroku.

The game presents an introduction to the game's theme. The player is then prompted to enter his or her name.

Once the user has given his name, he will have a menu with 3 options at his disposal. Option 1 allows the user to start the game, option 2 allows the user to view the ranking and option 3 allows the user to end the interaction with the program.

If the user starts the game, he will be explained how to give the coordinates and will be presented with the minefield, the user can take values from 1 to 5 to give his coordinates. 

Every time the game ends, either because the player stepped on a mine or won, the score obtained will be saved and the menu will be presented for the user to decide if he wants to continue playing, check the ranking or end the interaction with the program.

Once the user has finished the interaction with the program, it will update the ranking for the next interaction.

The deployed application can be found at [REMS](https://rems-ag-58c10e6f7952.herokuapp.com/)
## UX & Design

### User Stories

* As a user, I want to be able to type my name and know if the information is valid.
* As a user, I want to be able to read the rules of the game.
* As a user, I want to be able to know how many mines are in the minefield.
* As a user, I want to be able to see the current ranking.
* As a user, I want to be able to see the given coordinate represented in the minefield.
* As a user, I want to be able to see the number of mines around the given position.
* As a user, I want to be able to see what coordinates I have entered during the game.
* As a user, I want to be able to see my score during and at the end of the game.
* As a user, I want to be able to know if the coordinates I am entering are valid.
* As a user, I want to be able to see mines when I lose.
* As a user, I want to be able to replay the game as many times as I want.
* As a user, I want to be able to exit the game.

### Flowchart

#### Main Flowchart
![main flowchart](media/flow_chart_main.JPG)

#### Play game
![play game option](media/flowchart_glay_game.JPG)

#### Check ranking & quit game
![Check ranking option](media/display_ranking_%26_quit_game.JPG)

## Features

* Welcome screen
  * The user is welcomed with an introduction to the game's theme, telling him/her the number of hidden mines.
  * The user will be asked to enter his/her name.

![welcome screen](media/welcome_name.JPG)

* Menu
  * The user will be presented with three options. Number 1 will send the user to start the game, number 2 will present the ranking and number 3 will finish the interaction with the application.
  * The user has the option to end the interaction after giving his/her name, every game played, or checking the ranking.

![Menu](media/menu.JPG)

* Game
  * The user is presented with the two simple rules of the game in order to give valid coordinates and to know how much he/she will win for each correct coordinate.
  * The user will be able to see the coordinate data represented on the board.
  * The user can see at the bottom of the board the coordinates previously given and current score.
  * If the user steps on a mine, user will be informed of it, his/her score will be presented, the location of the mines will be shown and the menu function will appear (2. image "Game lose").
  * If the user wins the game, user will be informed about it, his/her score will be displayed and the menu function will appear (3. image "Game win").

![Game](media/game.JPG)

![Game lose](media/game_lose.JPG)

![Game win](media/game_win.JPG)

* Ranking
  * The user will be able to see the top 10 scores of other players and below the ranking, the menu function will appear.

![Ranking](media/ranking.JPG)

### Features left to implement
* Revealed position controller:
  * I plan to add a function that checks the coordinates given by the user with the coordinates previously revealed by the function "check_mines_around". this way users will not be able to add points by giving coordinates that have already been previously revealed to them.

* Real-time score updater:
  * I plan to add a function that updates the score as soon as it is saved in the worksheet "ranking".This way users will be able to know if they have achieved a place in the ranking without having to finish the interaction and start it again.

### Technologies Used

  * Python
    * All program was written in python.
  * Google Sheets
    * It is used to store the raking.
  * Google Cloud
    * It was used to enable the APIs needed.
  * Github
    * It was used to store the project.
  * Gitpod
    * It was used to create, add, commit and push my code to Github.
  * Heroku
    * It was used to deploy the project.

### Imported libraries

  * Random was used to create and place mines inside the board.
  * os was used clear the screen and improve user experience.
  * islice was used to bring only the top ten score for the ranking.
  * gspread was used to connect the program with Google Sheets to bring and update the ranking.

## Testing

I have manually tested this project by doing the following:
* Passed the code through a PEP8 linter and confirmed there are no problems.
* Tested in my local terminal and the Code Institute Heroku terminal.

### Bugs

Solved Bugs
* My "get_name_data" function was accepting all kind of values, I fixed it by adding "isalpha()" inside the if statement.
* My "display_ranking" function was not letting me show the score Value next to the name because it was an integrer and my function was looking for strings to make the ranking tab. I fixed it by converting the top_ten variable again to str before the for loop.
* my "game" function was allowing to write the same coordinate indefinitely to increase the score. I fixed it by adding a list that collects the given coordinates. With the help of this list I was able to use an if statement to check if both the row and the column had already been called before and if yes then re-ask for new coordinates without adding score.

Remaining Bugs
* the ranking does not update names and scores during the same interaction. In case the user makes it into the top 10, he/she must first end the interaction and then start a new one.

### Validator Testing
* PEP8
  * No errors were returned from CI Python Linter
  
![PEP8 linter](media/pep8_linter.JPG)

### User Stories Testing
| User Goal | Requirement met | Image(s) |
| --------- | --------------- | -------- |
| As a user, I want to be able to type my name and know if the information is valid. | Yes | ![User test 1a](media/welcome_name.JPG) ![User test 1b](media/menu.JPG) ![User test 1c](media/name_error_1c.JPG) ![User test 1d](media/name_error_1d.JPG) |
| As a user, I want to be able to read the rules of the game. | Yes | ![User test 2a](media/rules_2a.JPG) |
| As a user, I want to be able to know how many mines are in the minefield. | Yes | ![User test 3a](media/rules_3a.JPG) |
| As a user, I want to be able to see the current ranking. | Yes | ![User test 4a](media/ranking.JPG) |
| As a user, I want to be able to see the given coordinate represented in the minefield. | Yes | ![User test 5a](media/game.JPG) |
| As a user, I want to be able to see the number of mines around the given position. | Yes | ![User test 6a](media/game.JPG) |
| As a user, I want to be able to see what coordinates I have entered during the game. | Yes | ![User test 7a](media/game.JPG) |
| As a user, I want to be able to see my score during and at the end of the game. | Yes | ![User test 8a](media/game.JPG) ![User test 8b](media/game_lose.JPG) ![User test 8c](media/game_win.JPG)  |
| As a user, I want to be able to know if the coordinates I am entering are valid. | Yes | ![User test 9a](media/coordinate_9b.JPG) |
| As a user, I want to be able to see mines when I lose. | Yes | ![User test 10a](media/game_lose.JPG) |
| As a user, I want to be able to replay the game as many times as I want. | Yes | ![User test 11a](media/game_lose.JPG) ![User test 11b](media/game_win.JPG) |
| As a user, I want to be able to exit the game. | Yes | ![User test 12a](media/quit_game_12a.JPG) |


### Program Validation Testing
| Section Tested | Input To Validate | Expected Outcome | Actual Outcome | Pass/Fail |
| -------------- | ----------------- | ---------------- | -------------- | --------- |
| Start Program | N/A | Load welcome message and prompt user to enter name | As expected | PASS |
| Enter Name | Input "Cami" | Display Menu Option | As expected | PASS |
| Enter Name | Input "1" | Notify user that this isn't a valid input and loop back | As expected | PASS |
| Enter Name | Input "A1" | Notify user that this isn't a valid input and loop back | As expected | PASS |
| Enter Name | Input "Cami garcia" | Notify user that this isn't a valid input and loop back | As expected | PASS |
| Enter Name | Press enter with no input | Notify user that this isn't a valid input and loop back | As expected | PASS |
| Menu Option | Input "1" | Start game | As expected | PASS |
| Menu Option | Input "2" | Display ranking and menu at the bottom | As expected | PASS |
| Menu Option | Input "3" | Say goodbye to user and exit program | As expected | PASS |
| Menu Option | Input "A" | Notify user that this isn't a valid input and loop back | As expected | PASS |
| Menu Option | Input "A1" | Notify user that this isn't a valid input and loop back | As expected | PASS |
| Menu Option | Input "0.1" | Notify user that this isn't a valid input and loop back | As expected | PASS |
| Menu Option | Input "ajc123" | Notify user that this isn't a valid input and loop back | As expected | PASS |
| Menu Option | Input "cami garcia" | Notify user that this isn't a valid input and loop back | As expected | PASS |
| Menu Option | Input "0" | Notify user that this isn't a valid input and loop back | As expected | PASS |
| Menu Option | Input "4" | Notify user that this isn't a valid input and loop back | As expected | PASS |
| Menu Option | Press enter with no input | Notify user that this isn't a valid input and loop back | As expected | PASS |
| Game row or column | Input "1" | Save value to calculate coordinate | As expected | PASS |
| Game row or column | Input "2" | Save value to calculate coordinate | As expected | PASS |
| Game row or column | Input "3" | Save value to calculate coordinate | As expected | PASS |
| Game row or column | Input "4" | Save value to calculate coordinate | As expected | PASS |
| Game row or column | Input "5" | Save value to calculate coordinate | As expected | PASS |
| Game row or column | Input "0" | Notify user that this isn't a valid input and loop back | As expected | PASS |
| Game row or column | Input "6" | Notify user that this isn't a valid input and loop back | As expected | PASS |
| Game row or column | Input "A" | Notify user that this isn't a valid input and loop back | As expected | PASS |
| Game row or column | Input "A1" | Notify user that this isn't a valid input and loop back | As expected | PASS |
| Game row or column | Input "cami garcia" | Notify user that this isn't a valid input and loop back | As expected | PASS |
| Game row or column | Press enter with no input | Notify user that this isn't a valid input and loop back | As expected | PASS |
| Game row or column | input was same as previous coordinates | Notify user that has already given that coordinate and loop back | As expected | PASS |

### Cross-browser Testing
I have tested it on Chrome, Firefox and Edge. The program has loaded correctly and had no issues running as expected across all browsers.

| Browser | Image |
| ------- | ----- |
| Chrome | ![Browser Chrome](media/chrome.JPG) |
| Firefox | ![Browser Firefox](media/firefox.JPG) |
| Edge | ![Browser Edge](media/Edge.JPG) |

## Deployment
This project was deployed using Code Institute's mock terminal for Heroku.

The deployed application can be found at [minefield](https://minefield.herokuapp.com/)

* Steps for deployment:
  * Clone template repository
  * Create a new Heroku app
  * Add in Config Vars `CREDS` with value and `PORT` with `8000` 
  * Set buildbacks to `Python` and `NodeJS` in that order
  * Link the Heroku app to the repository in Github
  * Click on Deploy

## Credits

### Code
* Code to add mines and display board taken from [Painless Programming](https://www.youtube.com/watch?v=bGr-j89FaRM) and [here](https://www.youtube.com/watch?v=Wjzgm6p0TJY&t=1s)
* Code to clear_screen function taken from [Rahul Janghu](https://www.scaler.com/topics/how-to-clear-screen-in-python/)

### Design
* Flowchart was made using [Smartdraw](https://www.smartdraw.com/)