import sys


class Stuff:
    def __init__(self, name):
        self.type = None
        self.name = name

    def get_type(self):
        return self.type

    def get_name(self):
        return self.name


class StationaryStuff(Stuff):
    def __init__(self, name):
        super().__init__(name)
        self.type = "STATIONARY"


class MoveStuff(Stuff):
    def __init__(self, name):
        super().__init__(name)
        self.type = "MOVE"


class UseStuff(Stuff):
    def __init__(self, name):
        super().__init__(name)
        self.type = "USE"


class Door:
    def __init__(self, room1, direct1, room2, direct2, status):
        self.door_side = {room1: direct1, room2: direct2}
        self.status = status


class Room:
    def __init__(self, room_name):
        self.doors = []
        self.item = []
        self.room_name = room_name

    def set_door(self, doors):
        for door in doors:
            self.doors.append(door)

    def get_doors(self):
        return [x.door_side[self.room_name] for x in self.doors]

    def get_door(self, direct):
        for x in self.doors:
            if (self.room_name, direct) in x.door_side.items():
                return x

    def set_item(self, item):
        for i in item:
            self.item.append(i)

    def get_items(self):
        return [x.get_name() for x in self.item]

    def get_item(self, stuff):
        for x in self.item:
            if x.get_name() == stuff:
                return x

    def remove_item(self, stuff):
        for x in self.item:
            if x.get_name() == stuff.get_name():
                self.item.remove(x)
                print("(─‿‿─)")
                print("the following item: %s has been taken from the room: %s" % (x.get_name(), self.room_name))

    def add_item(self, stuff):
        self.item.append(stuff)
        print("the following item: %s has been placed in this room : %s " % (stuff.get_name(), self.room_name))


class Player:
    def __init__(self):
        self.item = []
        self.commands = ["go",
                         "take",
                         "release",
                         "open",
                         "show",
                         "commands",
                         "holding",
                         "quit"]
        self.room = "LK"

    def go(self, direction):
        if direction in self.get_direct():

            door = eval(self.room).get_door(direction)
            if door.status == "open":
                print("Leave ", self.room)
                current_room = self.room
                for room in door.door_side.keys():
                    if room != current_room:
                        self.room = room
                print("(─‿‿─)")
                print("Enter ", self.room)
            else:
                print("(─‿‿─)")
                print("The door is closed, please use a key to open it.")
                print("ಥ_ಥ")
        else:
            print("(─‿‿─)")
            print("ಥ_ಥ There are no doors towards", direction)

    def take(self, stuff):
        item = eval(self.room).get_item(stuff)
        if item.get_type() == "STATIONARY":
            print("(─‿‿─)")
            print(item.get_name(), " is STATIONARY, it cannot be taken ಥ_ಥ ")
        else:
            self.item.append(item)
            eval(self.room).remove_item(item)
            print("(─‿‿─)")
            print("you have taken the following item with you --", item.get_name())

    def remove(self, stuff):
        for x in self.item:
            if x.get_name() == stuff.get_name():
                self.item.remove(x)
                print("(─‿‿─)")
                print("the following item has been release --", x.get_name())

    def get_item(self, stuff):
        for x in self.item:
            if x.get_name() == stuff:
                return x

    def release(self, stuff):
        item = self.get_item(stuff)
        self.remove(item)
        eval(self.room).add_item(item)

    def check_key(self):
        for x in [x.get_name() for x in self.item]:
            print(x)
            if x == "Key":
                return True

    def open(self, direction):
        if self.check_key():
            print("(─‿‿─)")
            print("Got the key")
            eval(self.room).get_door(direction).status = "open"
            self.go(direction)
        else:
            print("(─‿‿─)")
            print("try to find out the Key")

    def get_commands(self):
        print("(─‿‿─)")
        print(self.commands)

    def get_direct(self):
        return eval(self.room).get_doors()

    def show(self):
        print("(─‿‿─)")
        print("You are now in ROOM", self.room)
        print("Here are doors towords", self.get_direct())
        print("The following items are in this room,", eval(self.room).get_items())

    def holding(self):
        print("(─‿‿─)")
        print([x.get_name() for x in self.item])

    @staticmethod
    def quit_game():
        print_config('GameOver.txt')
        sys.exit()

    def take_action(self, command):
        action = command.split(" ")
        if action[0] == "quit":
            self.quit_game()
        elif action[0] == "go":
            self.go(action[1])
        elif action[0] == "commands":
            self.get_commands()
        elif action[0] == "holding":
            self.holding()
        elif action[0] == "take":
            self.take(action[1])
        elif action[0] == "show":
            self.show()
        elif action[0] == "open":
            self.open(action[1])
        elif action[0] == "release":
            self.release(action[1])


def print_config(file):
    with open(file, 'r') as f:
        print(f.read())


if __name__ == "__main__":
    print_config('gameConfiguration.txt')

    new_player = Player()

    Door_LK_Reading = Door("LK", "N1", "Reading_Room", "S", "open")
    Door_LK_BedRoom1 = Door("LK", "N2", "BedRoom1", "S", "open")
    Door_LK_BedRoom2 = Door("LK", "N3", "BedRoom2", "S", "closed")
    Door_LK_BathRoom = Door("LK", "E", "BathRoom", "W", "open")
    Door_LK_Balcony = Door("LK", "W", "Balcony", "E", "open")

    LK = Room("LK")
    LK.set_item([StationaryStuff("TV"), MoveStuff("Macbook"), UseStuff("Key")])
    LK.set_door([Door_LK_Reading, Door_LK_BedRoom1, Door_LK_BedRoom2, Door_LK_BathRoom, Door_LK_Balcony])

    Reading_Room = Room("Reading_Room")
    Reading_Room.set_door([Door_LK_Reading])

    BedRoom1 = Room("BedRoom1")
    BedRoom1.set_door([Door_LK_BedRoom1])

    BedRoom2 = Room("BedRoom2")
    BedRoom2.set_door([Door_LK_BedRoom2])

    BathRoom = Room("BathRoom")
    BathRoom.set_door([Door_LK_BathRoom])

    Balcony = Room("Balcony")
    Balcony.set_door([Door_LK_Balcony])

    print("(─‿‿─)")
    print("Please type some command：")
    while True:
        command = input()
        action = command.split(" ")

        if action[0] in new_player.commands and len(action) < 3:
            new_player.take_action(command)
        else:
            print("I dont understand the command")
            continue
