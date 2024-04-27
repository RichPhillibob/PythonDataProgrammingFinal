from dataclasses import dataclass

@dataclass
class Player:
    PlayerID:int = 0
    batOrder:int = 0
    firstName:str = ''
    lastName:str = ''
    position:str = ''
    atBats:int = 0
    hits:int = 0

    @property
    def fullName(self):
        return f"{self.firstName} {self.lastName}"

    @property
    def battingAvg(self):
        try:
            avg = self.hits / self.atBats
            return round(avg, 3)
        except ZeroDivisionError:
            return 0.0
       
class Lineup:
    def __init__(self):
        self.__list = []

    def __len__(self):
        return len(self.__list)

    def add(self, player):
        return self.__list.append(player)

    def remove(self, number):
        return self.__list.pop(number - 1)

    def get(self, number):
        return self.__list[number - 1]

    def set(self, number, player):
        self.__list[number - 1] = player

    def move(self, oldNumber, newNumber):
        player = self.__list.pop(oldNumber - 1)
        self.__list.insert(newNumber - 1, player)

    def __iter__(self):
        for player in self.__list:
            yield player


def main():
    lineup = Lineup()
    lineup.add(Player(1, "Willie", "Mays", "CF", 100, 31))
    lineup.add(Player(2, "Hank", "Aaron", "RF", 100, 32))
    
    for player in lineup:
        print(player.batOrder, player.fullName, player.position,
              player.atBats, player.hits, player.battingAvg)
        
    print("Bye!")

if __name__ == "__main__":
    main()
