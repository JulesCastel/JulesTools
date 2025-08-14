# Dallas College Class Availability Checker

a simple Python program (with color coded terminal output!) to check if a course at Dallas College has open slots, assuming you already know the registration # you're signing up for and the class prefix

i set it up for checking `PHYS 2425` and reg# `4008317`, but you can change those variables in `main()` for any class you need, see the `customize for other courses` section

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
python3 classFullChecker.py
```

if you close your terminal, you'll need to reactivate the venv before running the script again:
- **Windows:** `.venv\Scripts\activate`
- **Mac/Linux:** `source .venv/bin/activate`

## customize for other courses

1. open `classFullChecker.py` in your IDE/text editor
2. in `main()`, change these variables:
   ```python
   # change the semester/campus/subject to whatever you need
    url: str = "https://schedule.dallascollege.edu//FALL/RLC/Prefix/PHYS"
    # change to the desired course registration number
    regNumber: str = "4008317"
   ```

## finding course information

1. go to the [Dallas College Schedule](https://schedule.dallascollege.edu) website
2. navigate to your semester and (optionally) campus
3. find your subject (eg PHYS, MATH, COSC, whatever)
4. copy the url and paste it into the `url: str` variable in `main()`
5. look for the course's registration number that you're trying to sign up for (it's the 7 digit number in the leftmost column)
6. copy that number and paste it into the `regNumber: str` variable in `main()`, be sure to put it in the quotes bc it needs to be a string

## color coding:
- **green**: spots are available! the script will show a direct link to register on Workday
- **red**: course is still full or there was some error
- **tellow**: warning/unknown status

## exit codes
the program returns different exit codes that can be useful if you want to use it in other scripts:
- `0`: course has open spots
- `1`: course is full
- `2`: error occurred or course not found

## contributing

feel free to modify and improve this script by opening a pull request! Some ideas:
- add email notifications
- create a GUI interface
- add support for multiple courses
- add scheduling to run automatically
- idk, whatever else you can come up? go nuts

---
# glhf 😼