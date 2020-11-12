class soccer_player :
    def __init__(self, name, height, weight, position):
        self.name = name
        self.height = height
        self.weight = weight
        self.position = position

    def info(self):
        print(f'선수이름: {self.name}')
        print(f'키: {self.height}')
        print(f'몸무게: {self.weight}')
        print(f'포지션: {self.position}')

    def where_to_go(self, position_num):
        print(self.position[position_num])

player1 = soccer_player('메시',170,72,['FW'])
player2 = soccer_player('호나우지뉴',181,83,['MF','FW'])
player3 = soccer_player('필립 람',170,66,['DF','MF'])
player4 = soccer_player('호날두',187,84,['FW'])

player1.info()
player2.info()
player3.info()
player4.info()

player1.where_to_go(0)
player2.where_to_go(1)
player3.where_to_go(1)
player4.where_to_go(0)