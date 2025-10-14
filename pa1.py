#write a small program that allows people to add, drop, and change their mod 2 schedule

#function to add a class

#function to change a class

#function to drop (delete/pop) a class

#main function

#Write a program that allows people to add, drop, and change a mod schedule - All 7 mods

#Add functionality to loop this 7 times for whatever for D/E blocks), and give an option to make and display a full year schedule


def add_class(schedule):
    section = input("Would you like to add classes, d-blocks, or e-blocks? --> ") #Change to section instead of mod

    if section == "classes":
        mod = input ("what mod would you like to add classes to? choose: mod 1-7 --> ").strip().lower()
        if mod not in schedule["classes"]:
            print("Doesn't exist! Try again please")
            return schedule
        
        new_class = input("Enter the name of the class that you want to have: ")
        schedule["classes"][mod].append(new_class)
        print(f"{new_class} has been added to your {mod}")
        return schedule

    elif section == "d-blocks":
        season = input("what season would you like to add your d-block in? choose Fall/Winter/Spring D-block --> ").strip().lower()
        if season not in schedule["d-blocks"]:
            print("Doesn't exist! Try again please")
            return schedule
    
        new_activity = input("Enter the name of the d-block that you want to have: ")
        schedule["d-blocks"][season].append(new_activity)
        print(f"{new_activity} has been added to your {season}")
      
    
    elif section == "e-blocks":
        new_extra = input("enter your e-block: ").strip().lower()
        schedule["e-blocks"].append(new_extra)
        print(f"{new_extra} has been added to your e-blocks")
    

    else:
        print("Invalid section, please choose 'classes, 'd-blocks', or 'e-blocks'")
    return schedule


def remove_class(schedule):
    section = input("Would you like to change classes, d-blocks, or e-blocks? --> ") #Change to section instead of mod

    if section == "classes":
        mod = input ("what mod would you like to change classes to? choose: mod 1-7 --> ").strip().lower()
        if mod not in schedule["classes"]:
            print("Doesn't exist! Try again please")
            return schedule
        
        if not schedule["classes"][mod]:
            print(f"You don't have any classes in {mod} to remove!")
            return schedule
     
        print(f"Your current classes are {mod}: {schedule['classes'][mod]}")
        class_to_remove = input("Enter the class you want to remove: ").strip().lower()

        if class_to_remove in schedule["classes"][mod]:
            schedule["classes"][mod].remove(class_to_remove) 
            print(f"{class_to_remove} has been removed from {mod}")

        else:
            print("This class is not in your schedule")

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
            schedule["d-blocks"][season].remove(activity_remove)
            print(f"{activity_remove} has been removed from your {season}")
        else:
            print("This activity isn't in your")
    
    elif section == "e-blocks":

        if extra_remove not in schedule["e-blocks"]:
            print("Doesn't exist! Try again please")
            return schedule
        
        print(f"Your current e-blocks are: {schedule['e-blocks']}")
        extra_remove = input("Enter the e-block class you want to remove: ").strip().lower()
        if extra_remove in schedule["e-blocks"]:
            schedule["e-blocks"].append(extra_remove)
            print(f"{extra_remove} has been removed from your e-blocks")
        else:
            print("That activity isnt in your e-block")

    else:
        print("Invalid section,try again")
    return schedule


def change_class(schedule): 
    section = input("Would you like to change classes, d-blocks, or e-blocks? ")

    if section == "classes":
        mod = input("what mod would you like to change? mod 1-7 --> ")
        if mod not in schedule["classes"]:
            print ("Doesn't exist! Try again")
            return schedule

        if not schedule["classes"][mod]:
            print(f"You don't have any classes in {mod} to change!")
            return schedule

        print(f"Your current classes are {mod}: {schedule['classes'][mod]}")
        class_to_change = input(f"Enter the class you want to change: ").strip().lower()

        if class_to_change in schedule["classes"][mod]:
            new_class = input(f"What class would you like to replace {class_to_change} with? ").strip()
            index = schedule["classes"][mod].index(class_to_change)
            schedule[mod][index] = new_class
            print(f"{class_to_change} has been changed to {new_class} in {mod}.")

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

def show_schedule(schedule):
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

    schedule = {
    "classes": {
        "mod 1": [],
        "mod 2": [],
        "mod 3": [],
        "mod 4": [],
        "mod 5": [],
        "mod 6": [],
        "mod 7": [],
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
        user_choice = input("\nWhat would you like to do? (add, drop, change, quit) --> ").lower()
        
        if user_choice == "add":
            schedule = add_class(schedule)
        elif user_choice == "drop":
            schedule = remove_class(schedule)   
        elif user_choice == "change":
            schedule = change_class(schedule)
        elif user_choice == "quit":
            print(f"\nGoodbye, {name}! Your final mod, schedule is: ")
            show_schedule(schedule)
            break
        else:
            print("Invalid input, please try again")

if __name__ == "__main__":
    main()