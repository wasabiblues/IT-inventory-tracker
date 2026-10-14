approved_models = ("Macbook pro", "Dell XPS","mouse","keyboard")
device_inventory = []
print("1. Add device")
print("2. Remove device")
print("3. View Inventory")
print("4. Exit")

while True:
    choice = input("Choose an Option.")
    if choice == "1":
        device = input("Type in the device name.")
        if device in approved_models:
            device_inventory.append(device)
            print("Device Added.")
        else:
            print("Error!")
    elif choice == "2":
        device = input("Type in the device you want to remove.")
        if device in device_inventory:
            device_inventory.remove(device)
            print("Device Removed.")
        else:
            print("Error!")
    elif choice == "3":
        print("Inventory:",device_inventory)

    elif choice == "4" :
        print("Exited.")
        break
    


