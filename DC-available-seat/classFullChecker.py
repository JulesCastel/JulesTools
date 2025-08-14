import requests
from bs4 import BeautifulSoup, Tag
import sys
from typing import Optional, List

# TODO: add a UI maybe?

# stolen from https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal
class bcolors:
    HEADER: str = '\033[95m'
    OKBLUE: str = '\033[94m'
    OKCYAN: str = '\033[96m'
    OKGREEN: str = '\033[92m'
    WARNING: str = '\033[93m'
    FAIL: str = '\033[91m'
    ENDC: str = '\033[0m'
    BOLD: str = '\033[1m'
    UNDERLINE: str = '\033[4m'

def checkAvailability(url: str, regNumber: str) -> Optional[bool]:
    """
    for checking to see if PHYS 2425 with Song has any open spots.
    theoretically this should work for other classes if you change the URL and course number
    """

    try:
        print(f"{bcolors.OKCYAN}checking availability...")
        response: requests.Response = requests.get(url, timeout=10)
        response.raise_for_status()

        soup: BeautifulSoup = BeautifulSoup(response.content, 'html.parser')

        rows: List[Tag] = soup.find_all('tr') # type: ignore

        if rows:
            for row in rows:
                # ignore the PyLance error here, the type hinting is gonna be changed soon according to the BS4 repo
                # https://github.com/python/typeshed/issues/8356
                cells: List[Tag] = row.find_all('td') # type: ignore
                # we're looking for the table rows for classes, which have 7 columns
                # so cutting out any other tables that might not apply
                if len(cells) >= 5:
                    rowText: str = row.get_text()
                    if regNumber in rowText:
                        # we are looking for the 5th column of each class table row
                        # but each row starts with a <th> element
                        # so technically, we're only looking for the 4th <td> element
                        statusCell: Tag = cells[3]
                        status: str = statusCell.get_text().upper()

                        print(f"{bcolors.BOLD + bcolors.OKBLUE}result: {status}")

                        if "OPEN" in status:
                            print(f"{bcolors.OKGREEN}SPOTS AVAILABLE!!! register NOW!!!! \nGOGOGOGO: https://www.myworkday.com/dallascollege/d/task/2998$28771.htmld#backheader=true")
                            return True
                        elif "FULL" in status:
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
        print("- the school block the request? lol")
        print("idk, double check the page or try again if it got blocked")
        return None

    except requests.exceptions.RequestException as e:
        print(f"{bcolors.FAIL}error fetching webpage: {e}")
        return None
    except Exception as e:
        print(f"{bcolors.FAIL}unexpected error: {e}")
        return None

def main() -> None:
    # change the semester/campus/subject to whatever you need
    url: str = "https://schedule.dallascollege.edu//FALL/RLC/Prefix/PHYS"
    # change to the desired course registration number
    regNumber: str = "4008317"

    print(f"{bcolors.HEADER}is PHYS2425 with Song open or not?")
    print(f"{bcolors.HEADER}=" * 45 + '\n')

    result: Optional[bool] = checkAvailability(url, regNumber)

    if result is True:
        sys.exit(0)
    elif result is False:
        sys.exit(1)
    else:
        sys.exit(2)

if __name__ == "__main__":
    main()