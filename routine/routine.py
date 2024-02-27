from datetime import datetime

today = datetime.now().strftime('%d/%m/%Y') # %H:%M

frequency_list = {"monday_to_friday":"5", "weekend":"2", "week":"7", "fifteen":"15", "month":"30"}

def frequency_choice(freq_choice):
    if freq_choice == '1' or "monday_to_friday":
        return frequency_list["monday_to_friday"]
    elif freq_choice == '2' or "weekend":
        return frequency_list["weekend"]
    elif freq_choice == '3' or "week":
        return frequency_list["week"]
    elif freq_choice == '4' or "fifteen":
        return frequency_list["fifteen"]
    elif freq_choice == '4' or "month":
        return frequency_list["month"]


class Activity(object):
    def __init__(self, name, freq_routine):
        self.name = name
        self.freq_routine = freq_routine
        self.check = False


class Activities:
    def __init__(self):
        self.activities = []

    def add_activity(self, new_activity):
        self.activities.append(new_activity)
        decision_choices("add_activity")

    def show_all_activities(self):
        #print(f"ATIVIDADES DE HOJE - {today}")
        while True:
            for activity in self.activities:
                if not activity.check:
                    print(f"[ ] {activity.name}")
                else:
                    print(f"[X] {activity.name}")

                decision_choices("show_all_activities")
            else:
                print("There aren't activities")
                break


def menu():
    activities = Activities()
    while True:
        print("1-ADD ACTIVITIES")
        print("2-SHOW ACTIVITIES")
        print("0-EXIT\n\n")
        
        choice = input("Enter your option: ")
        if choice == '1':

            name_activity = input("Enter activity name: ")
            for i,freq in enumerate(frequency_list, start=1):
                print(f"{i}-{freq}")
            freq_routine = input("Select activity frequency: ")
            frequency_choice(freq_routine)

            activity = Activity(name_activity, freq_routine)
            #print(f"{activity.name} - {activity.freq_routine} - {activity.check}")
            activities.add_activity(activity)

        elif choice == '2':

            activities.show_all_activities()

        elif choice == '0':
            print("\n\nFinished!")
            exit()
        else:
            print("Invalid option")


def decision_choices(previous_method):
    activities = Activities()
    print("\n\n(y) to continue\n(b) to back menu\n(e) to exit\n\n")
    while True:
        choice = input("Enter your option: ")
        if choice == 'y':

            if previous_method == "show_all_activities":
                activities.show_all_activities()
            elif previous_method == "add_activity":
                activities.add_activity()

        elif choice == 'b':
            menu()
        elif choice == 'e' or choice == '0':
            print("\n\nFinished!")
            exit()
        else:
            print("Invalid option")


def main():
    #activity1 = Activity("leitura", frequency_list["monday_to_friday"])
    menu()


if __name__ == "__main__":
    main()