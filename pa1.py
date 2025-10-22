#write a small program that allows people to add, drop, and change their mod 2 schedule

#function to add a class

#function to change a class

#function to drop (delete/pop) a class

#main function

#Write a program that allows people to add, drop, and change a mod schedule - All 7 mods

#Add functionality to loop this 7 times for whatever for D/E blocks), and give an option to make and display a full year schedule


def add_class(schedule):
    section = input("Would you like to add classes, d-blocks, or e-blocks? --> ")

    if section == "classes":
        mod = input ("what mod would you like to add classes to? choose: mod 1-7 --> ").strip().lower()
        if mod not in schedule["classes"]:
            print("Doesn't exist! Try again please")
            return schedule
        
        block = input("what block? a, b, or c? --> ").lower()
        if block not in schedule["classes"][mod]:
            print("That block does not exist")
            return schedule
        
        #I did this a bit differently (same for change and remove) everything I tried to use the .remove function or .append function it didn't work)

         
        if schedule["classes"][mod][block] != "": #!= "" means it's not equal to an empty string or more like it checks if there's something something in the variable 
            print(f"{mod} {block} block already has a class assigned: {schedule['classes'][mod][block]}") #tells python that there is already something in it
            return schedule


        new_class = input("Enter the name of the class that you want to have: ") #to add 
        schedule["classes"][mod][block]=new_class
        print(f"{new_class} has been added to your {mod}:{block}")
        return schedule


    elif section == "d-blocks":
        season = input("what season would you like to add your d-block in? choose Fall/Winter/Spring D-block --> ").strip().lower()
        if season not in schedule["d-blocks"]:
            print("Doesn't exist! Try again please")
            return schedule
        
        if len(schedule["d-blocks"][season]) >= 1: #len function and >= checks if theres 1 or more d-blocks in the season
            print(f"You already have 1 d-block in {season}. You can’t add more. Sorry")
            return schedule
        
        new_activity = input("Enter the name of the d-block that you want to have: ")
        schedule["d-blocks"][season].append(new_activity) #.append function
        print(f"{new_activity} has been added to your {season}")
      
      
    
    elif section == "e-blocks":
        if len(schedule["e-blocks"]) >= 3: 
            print(f"You already have 3 e-blocks. You can’t add more. Sorry")
            return schedule
         
        new_extra = input("enter your e-block: ").strip().lower()
        schedule["e-blocks"].append(new_extra)
        print(f"{new_extra} has been added to your e-blocks")
    

    else:
        print("Invalid section, please choose 'classes, 'd-blocks', or 'e-blocks'")
    return schedule


def remove_class(schedule):
    section = input("Would you like to change classes, d-blocks, or e-blocks? --> ") 

    if section == "classes":
        mod = input ("what mod would you like to change classes to? choose: mod 1-7 --> ").strip().lower()
        if mod not in schedule["classes"]:
            print("Doesn't exist! Try again please")
            return schedule
        
        block = input("what block? a, b, or c? --> ").lower()
        if block not in schedule["classes"][mod]:
            print("That block does not exist")
            return schedule
        
        if schedule["classes"][mod][block] == "": #== "" tells python to check if it is empty it will be true when there is nothing inside the variable
            print("No classes to remove in this block")
            return schedule
     
        print(f"Removed class from {block}")
        schedule["classes"][mod][block] = "" #= "" assigns an empty value (setting a value) or more like it makes the variable empty
        return schedule

    elif section == "d-blocks":
        season = input("what season would you to change your d-block in? choose Fall/Winter/Spring D-block --> ").strip().lower()
        if season not in schedule["d-blocks"]:
            print("Doesn't exist! Try again please")
            return schedule
        
        if not schedule["d-blocks"][season]:
            print(f"You don't have any classes in {season} to remove!")
            return schedule

        print(f"Your current d-blocks are {season}: {schedule['d-blocks'][season]}")
        activity_remove = input("Enter the name of the d-block that you want to remove: ").strip().lower()
        if activity_remove in schedule[season]["d-blocks"]:
            schedule["d-blocks"][season].remove(activity_remove) #.remove function
            print(f"{activity_remove} has been removed from your {season}")
        else:
            print("This activity isn't in your d-block")
    
    elif section == "e-blocks":

        if extra_remove not in schedule["e-blocks"]:
            print("Doesn't exist! Try again please")
            return schedule
        
        print(f"Your current e-blocks are: {schedule['e-blocks']}")
        extra_remove = input("Enter the e-block class you want to remove: ").strip().lower()
        if extra_remove in schedule["e-blocks"]:
            schedule["e-blocks"].remove(extra_remove)
            print(f"{extra_remove} has been removed from your e-blocks")
        else:
            print("That activity isnt in your e-block")

    else:
        print("Invalid section, try again")
    return schedule


def change_class(schedule): 
    section = input("Would you like to change classes, d-blocks, or e-blocks? ")

    if section == "classes":
        mod = input("what mod would you like to change? mod 1-7 --> ")
        if mod not in schedule["classes"]:
            print ("Doesn't exist! Try again")
            return schedule

        block = input("what block? a, b, or c? --> ").lower()
        if block not in schedule["classes"][mod]:
            print("That block does not exist")
            return schedule

        if schedule["classes"][mod][block] == "":
            print(f"You don't have any classes in {mod} to change!")
            return schedule
    

        print(f"Your current classes are {mod}: {schedule['classes'][mod][block]}")
        new_class = input(f"What class would you like to replace {schedule['classes'][mod][block]} with? ").strip()
        schedule["classes"][mod][block]=new_class
        print(f"Your class has been changed to {new_class} in {mod}:{block}.")
        return schedule

    elif section == "d-blocks":
        season = input("what season would you to change your d-block in? choose fall/winter/spring --> ").strip().lower()
        if season not in schedule["d-blocks"]:
            print("Doesn't exist! Try again please")
            return schedule
        
        if not schedule["d-blocks"][season]:
            print(f"You don't have any classes in {season} to remove!")
            return schedule
        
        print(f"Your current d-blocks are {season}: {schedule['d-blocks'][season]}")
        activity_change = input("Enter the name of the d-block that you want to change: ").strip().lower()

        if activity_change in schedule["d-blocks"][season]:
            new_activity = input(f"What would you like to replace {activity_change} with? ")
            new = schedule["d-blocks"][season].new(activity_change)
            schedule["d-blocks"][season][new] = new_activity
            print(f"{activity_change} has been changed from your {season} to {new_activity}" )
        
        else:
            print("This is not in your schedule")
        
    elif section == "e-blocks":

        if extra_change not in schedule["e-blocks"]:
            print("Doesn't exist! Try again please")
            return schedule
        
        print(f"Your current e-blocks are: {schedule['e-blocks']}")
        extra_change = input("Enter the e-block class you want to remove: ").strip().lower()

        if extra_change in schedule["e-blocks"][schedule]:
            new_extra = input(f"What would you like to replace {extra_change} with? ")
            schedule["e-blocks"].index(extra_change)
            schedule("e-blocks")[index] = new_extra
            print(f"{extra_change} has been changed from your e-blocks to {new_extra}")
        else:
            print("This activity isn't in your e-block")
    else:
        print("Invalid section")
    return schedule

def show_schedule(schedule): #def to show the schedule in the end
    print("\nHere's your full schedule! --> ")

    print("\nMods and Classes:")
    for mod, classes in schedule["classes"].items():
        print(f" {mod}: {classes if classes else 'No classes'}")

    print("\nD-blocks by Season:")
    for season, activities in schedule["d-blocks"].items():
        print(f" {season}: {activities if activities else 'No activities'}")

    print("\nE-blocks:")
    print(f"  {schedule['e-blocks'] if schedule['e-blocks'] else 'No activities'}")


def main():
    name = input("Hi! Please enter your name: ")
    print(f"Hello, {name}! Lets customize your schedule.")

    schedule = { #Schedule components
    "classes": {
        "mod 1": {"a": "", "b": "", "c": ""},
        "mod 2": {"a": "", "b": "", "c": ""},
        "mod 3": {"a": "", "b": "", "c": ""},
        "mod 4": {"a": "", "b": "", "c": ""},
        "mod 5": {"a": "", "b": "", "c": ""},
        "mod 6": {"a": "", "b": "", "c": ""},
        "mod 7": {"a": "", "b": "", "c": ""},
    },
    "d-blocks": {
        "fall": [],
        "winter": [],
        "spring": [],
    },
        "e-blocks": []
    }



    while True: 
        show_schedule(schedule)
        user_choice = input("\nWhat would you like to do? (add, drop, change, quit) --> ").lower().strip()
        
        if user_choice == "add":
            schedule = add_class(schedule)
        elif user_choice == "drop":
            schedule = remove_class(schedule)   
        elif user_choice == "change":
            schedule = change_class(schedule)
        elif user_choice == "quit":
            print(f"\nGoodbye, {name}! Your final schedule is: ")
            show_schedule(schedule)
            break
        else:
            print("Invalid input, please try again")

#To run the code
if __name__ == "__main__":
    main()