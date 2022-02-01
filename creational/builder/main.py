from builders import HobbitHouseBuilder

if __name__ == "__main__":
    print("Let's build a house for Frodo!")
    hobit_house_builder = HobbitHouseBuilder()
    hobit_house_builder.set_materials(["wood", "rock", "Gandalf's magic"])
    hobit_house_builder.build_basement(20, 100).build_floors(2)
    hobit_house_builder.build_room(1, 10).build_room(1, 40)
    hobit_house_builder.build_roof(4, True)
    print(
        "Frodo just take a look : ({0})".format(hobit_house_builder.get_square())
        + str(hobit_house_builder.get_house())
    )

    print("Do you like it [Y/N]?")
    ans = input(">>> ")
    if ans == "Y":
        print("Call the builder next time then")
    elif ans == "N":
        print("Lets destroy then")
        hobit_house_builder.destroy()
        print(hobit_house_builder.get_house())
