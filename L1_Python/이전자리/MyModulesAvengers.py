

class Unit():    # Unit(object) == Unit  *단, python3.x에서
    def __init__(self, ability, level):
        self.ability = ability
        self.level = level
        print('unit이 생성되었습니다.')
        
    def show_info(self):
        print('ability : {}'.format(self.ability))
        print('level : {}'.format(self.level))
            
class Hero(Unit):
    def __init__(self, ability, level, weapon):
        super().__init__(ability, level)
        self.weapon = weapon
        
    def show_info(self):
        super().show_info()
        print('weapon: {}'.format(self.weapon))
        
class AvengersHero(Hero):  #속성 += hometown
    def __init__(self, ability, level, weapon, hometown):
        super().__init__(ability, level, weapon)
        self.hometown = hometown
        
    def show_info(self):
        super().show_info()
        print('hometown : {}'.format(self.hometown))

        
if __name__ == '__main__':  #다른 파일에서 import 했을때는 해당 코드 실행 x        
    Thor = AvengersHero('thunder',9,'hammer','Asgard')
    Thor.show_info()

    print('AvengersHero class가 정상 작동합니다.')

    batman = Avengers.Hero('money', 7, 'car')
    batman.show_info()

    print('Hero class가 정상 작동합니다.')
