# Text Adventure Calculator Game

## Overview
This is a Python-based text adventure game combined with a calculator application.  
Users can navigate through different game scenarios by making choices and perform basic arithmetic operations.

## Features
- Interactive text-based adventure with multiple paths and inventory management  
- Basic calculator supporting addition, subtraction, multiplication, and division  
- Error handling for invalid inputs and division by zero  
- Operation logging and optional SQLite history storage  

## Technologies
- Python 3.x  
- SQLite (optional, for saving calculation history)  
- Optional GUI with Tkinter (not included in current version)  

## How to Run
1. Clone the repository:  
   `git clone <your-repository-url>`

2. Navigate to the project directory:  
   `cd text_adventure_calculator`

3. Run the calculator CLI:  
   `python calculator/calculator_cli.py`

4. Run the text adventure game main script:  
   `python game/main.py`

## Project Structure
text_adventure_calculator/
├── calculator/
│ ├── calculator_cli.py
│ ├── db_handler.py
│ ├── logger.py
│ └── init.py
├── game/
│ ├── main.py
│ └── init.py
├── reports/
│ └── operation_logs.txt
├── run.py
└── README.md


## License
This project is open source and free to use.

---

Feel free to edit or expand this README file before committing it to your repo. Would you like me to generate it for you as a file?
