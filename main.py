from art import tprint
import re

def after_input(used_tool):
    print(" ")
    print("[0] Use a tool again")
    print("[1] Select a different tool")
    print("[2] Exit")

    action = input("Select an option: ")
    if(not action.isnumeric()):
        print("Got string, expected a number")
        after_input(used_tool)
    else:
        action = int(action)
        if action < 0:
            print("Got negative number, expected positive")
            after_input(used_tool)
        else:
            if action == 0:
                run(used_tool)
            elif action == 1:
                ask()

def run(tool):
    if tool == "Furnace calculator":
         miners = int(input("Please enter the amount of miners: "))
         def furnace_calculate(m, boost_percentage):
            if len(boost_percentage) == 0:
                boost_percentage = 0
            else:
                boost_percentage = int(boost_percentage)
            y = m * 0.5
            z = y + (y * (boost_percentage/100))
            v = z * 1.6
            print("You will need " + str(round(v)) + " furnaces")
            after_input(tool)
         def ask_boost_percentage():
            boost_percentages = ["none", "20%", "30%", "40%", "50%", "60%", "70%"]
            count = 0
            for percentage in boost_percentages:
                if percentage != "none":
                    percentage = "+ " + percentage
                print("[" + str(count) + "] " + percentage)
                count = count + 1

            boost_percentage_input = input("Please select mining productivity: ")
            if(not boost_percentage_input.isnumeric()):
                print("Got string, expected a number")
                ask_boost_percentage()
            else:
                boost_percentage_input = int(boost_percentage_input)
                if(boost_percentage_input < 0):
                    print("Got negative number, expected positive")
                    ask_boost_percentage()
                else:
                    if boost_percentage_input < len(boost_percentages) - 1:
                        furnace_calculate(miners, re.sub(r"[^\d]", "", boost_percentages[boost_percentage_input]))
                    else:
                        print("Invalid percentage")
                        ask_boost_percentage()

         ask_boost_percentage()
    elif tool == "Belt calculator":
         miners = int(input("Please enter the amount of miners: "))
         def belt_calculate(miners, boost_percentage):
            if len(boost_percentage) == 0:
                boost_percentage = 0
            else:
                boost_percentage = int(boost_percentage)
            z = miners / 2
            z = z + (z * (boost_percentage/100))

            if z > 90:
                print("You wil need more than 2 belts")
            else:
                print("You will need maximum of 2 belts")
            after_input(tool)
         def ask_boost_percentage():
            boost_percentages = ["none", "20%", "30%", "40%", "50%", "60%", "70%"]
            count = 0
            for percentage in boost_percentages:
                if percentage != "none":
                    percentage = "+ " + percentage
                print("[" + str(count) + "] " + percentage)
                count = count + 1

            boost_percentage_input = input("Please select mining productivity: ")
            if(not boost_percentage_input.isnumeric()):
                print("Got string, expected a number")
                ask_boost_percentage()
            else:
                boost_percentage_input = int(boost_percentage_input)
                if(boost_percentage_input < 0):
                    print("Got negative number, expected positive")
                    ask_boost_percentage()
                else:
                    if boost_percentage_input < len(boost_percentages) - 1:
                        belt_calculate(miners, re.sub(r"[^\d]", "", boost_percentages[boost_percentage_input]))
                    else:
                        print("Invalid percentage")
                        ask_boost_percentage()
         ask_boost_percentage()
 
        

tools = ["Furnace calculator", "Belt calculator"]

tprint("Factoolrio")
def ask():
    print(" ")
    count = 0
    for tool in tools:
        print("[" + str(count) + "] " + tools[count])
        count = count + 1
    print(" ")
    input_tool = input("Please select a tool:")
    if(not input_tool.isnumeric()):
        print("Got string, expected a number")
        ask()
    else:
        input_tool = int(input_tool)
        if(input_tool < 0):
            print("Got negative number, expected positive")
            ask()
        else:
            if len(tools) > input_tool - 1:
                print("Running " + tools[input_tool] + "....")
                run(tools[input_tool])
            else:
                print("Invalid tool")
                ask()
ask()
