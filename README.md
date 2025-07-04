# 🔢 Number Guessing Game

## 🚀 Purpose  
This is a simple command-line number guessing game built in Python. The computer randomly selects a number between 1 and 20, and the player tries to guess it. After each attempt, the game provides feedback on whether the guess is too high or too low.

## 🧠 Key Concepts Practiced  
- `while` loops  
- Conditionals (`if`, `elif`)  
- Functions and variable scope  
- User interaction through terminal  
- Random number generation

## 🛠️ Technologies Used  
- Python 3.x  
- `random` module  
- No external dependencies

## 📋 Features  
- Infinite loop with the option to play again  
- Dynamic feedback on guess accuracy  
- Simple and clean CLI menu  
- Tracks number of attempts (partially implemented)

## 📦 How to Run
```bash
git clone https://github.com/masaldede/numbergame.git
cd numbergame
python numbergame.py

Welcome Player
I choose the number between 1 to 20

Make a guess: 14
14 is higher than my number
Make a new guess: 6
6 is lower than my number
Make a new guess: 9
CORRECT! 9 is my number!
You tried 3 times!

Type 1 to play again, or any other number to exit

🔧 Known Limitations
	•	The counter variable is not incremented — it always shows 0 attempts
	•	Error handling is not implemented (e.g., non-integer inputs)

🛠️ Possible Improvements
	•	Fix the counter to track number of attempts
	•	Add input validation for robustness
	•	Add difficulty levels or high score tracking

🎯 Learning Outcome

This project was built to reinforce basic Python logic and to practice building interactive terminal apps. It’s a great starting point for anyone learning how to use loops, conditions, and functions in a fun way.


