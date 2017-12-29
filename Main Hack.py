from graphics import *


# Formatting Function
def formClk(win):
    clickPoint = win.getMouse()
    clickPoint = str(clickPoint)
    print(clickPoint)

    for char in "Point":
        clickPoint = clickPoint.strip(char)

    clickPoint = clickPoint.strip(")")
    clickPoint = clickPoint.strip("(")
    clickPoint = clickPoint.split(",")
    return clickPoint

# Registering click
def mainClk(clickPoint, win):
    if (float(clickPoint[0]) >= 50 and float(clickPoint[0]) <= 250) and (float(clickPoint[1]) >= 50 and float(clickPoint[1]) <= 200):
        sleepWin = GraphWin("Sleep Record", 50, 50)
        win.close()
    elif (float(clickPoint[0]) >= 350 and float(clickPoint[0]) <= 550) and (float(clickPoint[1]) >= 50 and float(clickPoint[1]) <= 200):
        sleepWin = GraphWin("Nutrition Record", 50, 50)
        win.close()
    elif (float(clickPoint[0]) >= 50 and float(clickPoint[0]) <= 250) and (float(clickPoint[1]) >= 300 and float(clickPoint[1]) <= 450):
        sleepWin = GraphWin("Grades Input", 50, 50)
        win.close()
    elif (float(clickPoint[0]) >= 350 and float(clickPoint[0]) <= 550) and (float(clickPoint[1]) >= 300 and float(clickPoint[1]) <= 450):
        sleepWin = GraphWin("Extra-Curricular Record", 50, 50)
        win.close()
    else:
        mainClk(formClk(mainWin), win)
    
# MAIN
def main():
    
    mainWin = GraphWin("Project", 800, 600)

    # sleepBut
    SleepBut = Rectangle(Point(50,50), Point(250,200))
    SleepBut.draw(mainWin)

    # nutriBut
    NutriBut = Rectangle(Point(350,50), Point(550, 200))
    NutriBut.draw(mainWin)

    # gradesBut
    gradesBut = Rectangle(Point(50,300), Point(250,450))
    gradesBut.draw(mainWin)

    # EcBut
    EcBut = Rectangle(Point(350,300), Point(550,450))
    EcBut.draw(mainWin)

    clickLoc = formClk(mainWin)
    mainClk(clickLoc, mainWin)

main()



