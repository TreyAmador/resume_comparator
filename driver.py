from comparator import Comparator
from gui import GUI


def driver():
    gui = GUI()
    comparator = Comparator()

    while True:
        descr,letter = gui.read()
        comparator.compare(descr,letter)

    # this returns true
    #comp = comparator.search_word('ab','ab+')
    print(comp)



driver()

