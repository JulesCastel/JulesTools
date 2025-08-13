import requests
from bs4 import BeautifulSoup
import sys

# TODO: add a UI maybe?

# stolen from https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def checkAvailability():
    """
    for checking to see if PHYS 2425 with Song has any open spots.
    theoretically this should work for other classes if you change the URL and course number
    """
    url = "https://schedule.dallascollege.edu//FALL/RLC/Prefix/PHYS"
    regNumber = "4008317"

    try:
        print(f"{bcolors.OKCYAN}checking availability...")
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')

        rows = soup.find_all('tr')

        if rows:
            for row in rows:
                # ignore the PyLance error here, the type hinting is gonna be changed soon according to the BS4 repo
                # https://github.com/python/typeshed/issues/8356
                cells = row.find_all('td') # type: ignore
                if len(cells) >= 5:
                    rowText = row.get_text()
                    if regNumber in rowText:
                        statusCell = cells[3]
                        status = statusCell.get_text().strip().lower()

                        print(f"{bcolors.BOLD + bcolors.OKBLUE}result: {status.upper()}")

                        if "open" in status:
                            print(f"{bcolors.OKGREEN}SPOTS AVAILABLE!!! register NOW!!!! GOGOGOGO: https://www.myworkday.com/dallascollege/d/task/2998$28771.htmld#backheader=true")
                            return True
                        elif "full" in status:
                            print(f"{bcolors.FAIL}course is still full :(")
                            return False
                        else:
                            print(f"{bcolors.WARNING}unknown result: {status}")
                            return None

        # if we get here, we didn't find the course somehow
        print(f"{bcolors.WARNING}course {regNumber} not found on the page!")
        print("did:")
        print("- the course number change?")
        print("- the page structure change?")
        print("- the course get removed from the schedule?")
        print("idk, double check the page")
        return None

    except requests.exceptions.RequestException as e:
        print(f"{bcolors.FAIL}error fetching webpage: {e}")
        return None
    except Exception as e:
        print(f"{bcolors.FAIL}unexpected error: {e}")
        return None

if __name__ == "__main__":
    print(f"{bcolors.HEADER}is PHYS2425 with Song open or not?")
    print(f"{bcolors.HEADER}=" * 45)
    result = checkAvailability()

    if result is True:
        sys.exit(0)
    elif result is False:
        sys.exit(1)
    else:
        sys.exit(2)