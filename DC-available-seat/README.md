# Dallas College Class Availability Checker

a simple Python program (with color coded terminal output!) to check if a course at Dallas College has open slots, assuming you already know the registration # you're signing up for and the class prefix

## DISCLAIMER

i wrote this **PURELY** for educational purposes.

be respectful of the Dallas College website and don't run it too frequently to avoid putting unnecessary load on their servers

**pls don't get me in trouble for this LOL**

## setup
### requirements
- Python 3.7 or higher
- an internet connection (duh lol)

### 1. download/clone the repo
```bash
git clone https://github.com/JulesCastel/JulesTools.git
```
or just download the files
### 2. set up the virtual environment

**Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**MacOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

you'll know you did it right when you have `(.venv)` at the beginning of your terminal prompt
### 3. install dependencies

```bash
pip3 install -r requirements.txt
```

## usage

make sure the virtual environment is activated (you should see `(.venv)` in your terminal), see above

then run:
```bash
python3 main.py
```

if you close your terminal, you'll need to reactivate the venv before running the script again:
- **Windows:** `.venv\Scripts\activate`
- **Mac/Linux:** `source .venv/bin/activate`

## finding course information

1. go to the [Dallas College Schedule](https://schedule.dallascollege.edu) website
2. navigate to your semester and (optionally) campus
3. find your subject (eg PHYS, MATH, COSC, whatever)
4. select it in the program's dropdown menu
5. look for the course's registration number that you're trying to sign up for (it's the 7 digit number in the leftmost column)
6. copy that number and paste it into the registration # box in the program

## contributing

feel free to modify and improve this script by opening a pull request! Some ideas:
- add email notifications
- add support for multiple courses
- add scheduling to run automatically
- idk, whatever else you can come up? go nuts

---
# glhf 😼