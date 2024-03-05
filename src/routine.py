from datetime import datetime
import subprocess

today = datetime.now().strftime('%d/%m/%Y') # %H:%M

frequency_list = {"monday_to_friday":"5", "weekend":"2", "week":"7", "fifteen":"15", "month":"30"}

def frequency_choice(freq_choice):
    if freq_choice == '1' or freq_choice == "monday_to_friday":
        return frequency_list["monday_to_friday"]
    
    elif freq_choice == '2' or freq_choice == "weekend":
        return frequency_list["weekend"]
    
    elif freq_choice == '3' or freq_choice == "week":
        return frequency_list["week"]
    
    elif freq_choice == '4' or freq_choice == "fifteen":
        return frequency_list["fifteen"]
    
    elif freq_choice == '4' or freq_choice == "month":
        return frequency_list["month"]


class Activity(object):
    def __init__(self, name, freq):
        self.name = name
        self.freq = freq
        self.check = False


class InputInformation():
    def get_information_to_add_activity(self):
        input_name_activity = input("Enter activity name: ")
        for i,freq_list in enumerate(frequency_list, start=1):
            print(f"{i}-{freq_list}")
        input_freq_activity = input("Select activity frequency: ")
        freq = frequency_choice(input_freq_activity)

        return input_name_activity, freq


class Activities:
    def __init__(self):
        self.activities = []

    def add_activity(self, name_new_activity, freq_new_activity):
        new_activity = Activity(name_new_activity, freq_new_activity)
        self.activities.append(new_activity)
        
    def show_all_activities(self):
        if self.activities:
            print(f"ATIVIDADES DE HOJE - {today}")
            for activity in self.activities:
                if not activity.check:
                    print(f"[ ] {activity.name} {activity.freq}")
                else:
                    print(f"[X] {activity.name} {activity.freq}")
        else:
            print("There aren't activities")


def menu():
    manage_activities = Activities()
    manage_input_information = InputInformation()
    while True:
        print("1. ADD ACTIVITIES")
        print("2. SHOW ACTIVITIES")
        print("0. EXIT\n\n")
        choice = input("Enter your option: ")

        if choice == '1':
            name_activity, freq_activity = manage_input_information.get_information_to_add_activity()
            manage_activities.add_activity(name_activity, freq_activity)
        elif choice == '2':
            manage_activities.show_all_activities()
        elif choice == '0':
            print("\n\nFinished!")
            exit()
        else:
            print("Invalid option")


def main():
    menu()


if __name__ == "__main__":
    main()