# 15_tile_puzzle_tekzen

This project implements a classic sliding puzzle game where the goal is to arrange tiles in order, either numerically or alphabetically, within a 4x4 grid. The puzzle is built using Python Flask for the backend and HTML and CSS for the frontend.  

## Features  

Interactive Gameplay: Click tiles to move them within the grid.  
Solvable Puzzles: Ensures every generated puzzle configuration is solvable.  
Attractive UI/UX: Intuitive and visually appealing design, suitable for first-time users.  
Robust Error Handling: Prevents crashes or freezes during gameplay.  
Unit Testing: Comprehensive test cases for backend functionality.  

## Installation  
Clone the repository:  
git clone https://github.com/Shreya1293/15_tile_puzzle_tekzen.git
  
go to the project directory:  
cd 15-tile-puzzle  
  
Run the Flask server:  
python main.py  
  
Open your browser and navigate to the given Local host URL  

for testing the unit test cases:  
python -m unittest test_app.py  
  
## Project Structure  
  
15-tile-puzzle/  
├── static/  
│   ├── css/  
│   │   └── styles.css  
├── templates/  
│   └── index.html  
├── tests/  
│   └── test_app.py  
├── main.py  
  
static/: Contains CSS files for the frontend.  
templates/: Contains HTML templates.  
tests/: Unit test cases for backend logic.  
main.py: Main Flask application.  
  
The following is the web preview of the project:  
![image](https://github.com/user-attachments/assets/3ee20f65-e114-4cb6-98bc-d074df7e1a20)
