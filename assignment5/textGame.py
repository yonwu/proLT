import sys
import argparse


class Stuff:
    def __init__(self, name, place):
        self.type = None
        self.name = name
        self.place = place

    def get_type(self):
        return self.type

    def get_name(self):
        return self.name


class StationaryStuff(Stuff):
    def __init__(self, name, place):
        super().__init__(name, place)
        self.type = "STATIONARY"


class MoveStuff(Stuff):
    def __init__(self, name, place):
        super().__init__(name, place)
        self.type = "MOVE"


class UseStuff(Stuff):
    def __init__(self, name, place, purpose):
        super().__init__(name, place)
        self.type = "USE"
        self.purpose = purpose


class Door:
    def __init__(self, room1, direct1, room2, direct2, status):
        self.door_side = {room1: direct1, room2: direct2}
        self.status = status


class Room:
    def __init__(self, room_name):
        self.doors = []
        self.item = []
        self.room_name = room_name

    def set_doors(self, doors):
        for door in doors:
            self.doors.append(door)

    def get_doors(self):
        return [x.door_side[self.room_name] for x in self.doors]

    def get_door(self, direct):
        for x in self.doors:
            if (self.room_name, direct) in x.door_side.items():
                return x

    def set_items(self, item):
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
    def __init__(self, start_room, room_list):
        self.item = []
        self.commands = ["go",
                         "take",
                         "release",
                         "open",
                         "show",
                         "commands",
                         "holding",
                         "quit",
                         "unlock",
                         "eat"]
        self.room = start_room
        self.room_list = room_list
        self.status = "tired"

    def go(self, direction):
        if self.status == "energetic":
            if direction in self.get_direct():

                door = self.room.get_door(direction)
                if door.status == "open":
                    print("Leave ", self.room.room_name)
                    current_room = self.room.room_name
                    for room in door.door_side.keys():
                        if room != current_room:
                            self.room = self.room_list[room]
                    print("(─‿‿─)")
                    print("Enter ", self.room.room_name)
                else:
                    print("(─‿‿─)")
                    print("The door is closed, please try to open it.")
                    print("ಥ_ಥ")
            else:
                print("(─‿‿─)")
                print("ಥ_ಥ There are no doors towards", direction)
        else:
            print("player's status is--", self.status, "--you cannot move at all")
            print("please eat something first")

    def take(self, stuff):
        if stuff in self.room.get_items():
            item = self.room.get_item(stuff)
            if item.get_type() == "STATIONARY":
                print("(─‿‿─)")
                print(item.get_name(), " is STATIONARY, it cannot be taken ಥ_ಥ ")
            else:
                self.item.append(item)
                self.room.remove_item(item)
                print("(─‿‿─)")
                print("you have taken the following item with you --", item.get_name())
                item.place = "player"
        else:
            print("no such stuff: ", stuff)

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
        self.room.add_item(item)
        item.place = self.room.room_name

    def check_key(self):
        for x in self.item:
            if x.purpose == "unlock":
                return True

    def check_food(self):
        for x in self.item:
            if x.purpose == "eat":
                return True

    def open(self, direction):
        if direction in self.get_direct():
            if self.room.get_door(direction).status == "closed" or self.room.get_door(direction).status == "unlocked":
                self.room.get_door(direction).status = "open"
                print("The door is open now, you can go through the door now")
            elif self.room.get_door(direction).status == "locked":
                print("The door is locked, try to find out the Key")
        else:
            print("no such door in this room: " ,direction)

    def unlock(self, direction):
        if direction in self.get_direct():
            if self.check_key():
                print("(─‿‿─)")
                print("Got the key")
                self.room.get_door(direction).status = "unlocked"
                print("The door is unlocked now, you can open it")
            else:
                print("(─‿‿─)")
                print("You dont have the key on you, try to find it")
        else:
            print("no such door in this room: ", direction)

    def get_commands(self):
        print("(─‿‿─)")
        print(self.commands)

    def get_direct(self):
        return self.room.get_doors()

    def show(self):
        print("(─‿‿─)")
        print("You are now in ROOM", self.room.room_name)
        print("Here are doors towords", self.get_direct())
        print("The following items are in this room,", self.room.get_items())

    def holding(self):
        print("(─‿‿─)")
        print([x.get_name() for x in self.item])

    def eat(self):
        if self.check_food():
            print("eating....")
            self.status = "energetic"
            print("the player's status is, ", self.status)
        else:
            print("no food at hand, please find some food")

    def take_action(self, command):
        action = command.split(" ")
        act = action[0].lower()
        if act == "quit":
            Game.quit_game()
        elif act == "go":
            self.go(action[1])
        elif act == "commands":
            self.get_commands()
        elif act == "holding":
            self.holding()
        elif act == "take":
            self.take(action[1])
        elif act == "show":
            self.show()
        elif act == "open":
            self.open(action[1])
        elif act == "release":
            self.release(action[1])
        elif act == "unlock":
            self.unlock(action[1])
        elif act == "eat":
            self.eat()


class Game:
    def __init__(self):
        pass

    @staticmethod
    def print_config(file):
        with open(file, 'r') as f:
            print(f.read())

    @staticmethod
    def quit_game():
        Game.print_config('GameOver.txt')
        sys.exit()

    @staticmethod
    def get_config_from_file(file):
        with open(file, "r") as infile:
            sents = infile.read().split("\n\n")
            if sents[-1] == "":
                sents = sents[:-1]
            game_config = {}
            for sent in sents:
                lines = sent.split("\n")
                for line in lines:
                    if line.startswith("#"):
                        key = line.strip("#")
                        game_config[key] = []
                        continue

                    line = line.strip().split("\t")
                    line = line[0].split(" ")[1:]
                    game_config[key].append(line)

        rooms_config = [x[0] for x in list(game_config.values())[0]]
        doors_config = list(game_config.values())[1]
        for x in doors_config:
            x[0] = x[0].split("-")

        items_config = list(game_config.values())[2]

        start_position = list(game_config.values())[3][0][0]

        return rooms_config, doors_config, items_config, start_position

    @staticmethod
    def init_game(file):
        rooms_config, doors_config, items_config, start_position = Game.get_config_from_file(file)

        room_list = {}

        for room in rooms_config:
            room_list[room] = Room(room)

        door_list = list()

        for door_config in doors_config:
            new_door = Door(room1=door_config[-2], direct1=door_config[0][0],
                            room2=door_config[-1], direct2=door_config[0][1], status=door_config[1])
            door_list.append(new_door)

        item_list = list()

        for item_config in items_config:
            if item_config[2] == "MOVE":
                new_item = MoveStuff(name=item_config[0], place=item_config[1])
            elif item_config[2] == "STATIONARY":
                new_item = StationaryStuff(name=item_config[0], place=item_config[1])
            elif item_config[2] == "USE":
                new_item = UseStuff(name=item_config[0], place=item_config[1], purpose=item_config[-1])
            item_list.append(new_item)

        for room in room_list.values():
            for door in door_list:
                if room.room_name in door.door_side.keys():
                    room.set_doors([door])
            for item in item_list:
                if room.room_name == item.place:
                    room.set_items([item])
            if room.room_name == start_position:
                start_room = room

        return room_list, start_room

    @staticmethod
    def start_game(file):
        room_list, start_room = Game.init_game(file)
        new_player = Player(start_room=start_room, room_list=room_list)

        print("(─‿‿─)")
        print("Please type some command：")
        while True:
            command = input()
            action = command.split(" ")

            if action[0].lower() in new_player.commands and len(action) < 3:
                new_player.take_action(command)
            else:
                print("I dont understand the command")
                continue


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Text Game  LOCKDOWN CORONA')
    parser.add_argument("file")
    args = parser.parse_args()
    file = args.file

    Game.print_config('startGame.txt')
    Game.start_game(file)
