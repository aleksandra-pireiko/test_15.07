class Tomato:
    # стадии созревания
    states = {0: "Томат посажен", 1: "Росток", 2: "Томат цветёт", 3: "Плоды зелёные", 4: "Плоды жёлтые", 5: "Томаты созрели"}

    def __init__(self, index):
        self._index = index
        self._state = 0

    def grow(self,):
        # переходим на следующую стадию созревания
        if self._state < 5:
            self._state += 1

    def is_ripe(self):
        # проверяем созревание
        if self._state == 5:
            return True
        else:
           return False

class TomatoBush:

    def __init__(self, kol_tomat):
        self.tomatoes = [] # контейнер для хранения объектов-томатов
        for i in range(kol_tomat):
            self.tomato = Tomato(i)
            self.tomatoes.append(self.tomato)

    def grow_all(self):
        # все томаты переходят на следующую стадию созревания
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        # проверяем созревание всех объектов
        if self.tomato.is_ripe():
            return True
        else:
            return False

    def give_away_all(self):
        # убираем урожай
        self.tomatoes = []
        self.tomato = 0


class Gardener:
    def __init__(self, name, plant):
        # закрепляем за определенным садовником объект класса TomatoBash
        self.name = name
        self._plant = plant

    def work(self):
        # увеличиваем стадии роста
        self._plant.grow_all()
        print("Садовник работает")

    def harvest(self):
        # уборка урожая, если растения созрели
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print("Растения убраны")
        else:
            print("Растения ещё не созрели")

    @staticmethod
    # выводит справку по садоводству
    def knowledge_base():
        print("Тома́т или помидóр (лат. Solánum lycopérsicum) — однолетнее или многолетнее травянистое растение, вид "
              "рода Паслён (Solanum) семейства Паслёновые (Solanaceae). ""\n""Возделывается как овощная культура; "
              "выращивается ради съедобных плодов — сочных многогнёздных ягод различной формы и окраски, также называемых "
              "томатами или помидорами.""\n""Томат — теплотребовательная культура, оптимальная температура для роста и "
              "развития растений составляет +22…+25 °C, при температуре ниже 15 °С не цветёт,""\n" "погибает при замерзании "
              "ниже 0° С, при температуре ниже +10 °C прекращается рост растений и пыльца в цветках не созревает "
              "и неоплодотворённая завязь отпадает.""\n""Томат плохо переносит повышенную влажность воздуха, но требует много "
              "воды для роста плодов. Растения томата требовательны к свету. При его недостатке задерживается" "\n""развитие "
              "растений, листья бледнеют, образовавшиеся бутоны опадают, стебли сильно вытягиваются. Томаты культивируют "
              "как в открытом грунте, так и в теплицах и парниках.")

# Тесты
Gardener.knowledge_base()
tomatoes = TomatoBush(6)
Vasya = Gardener("Vasya", tomatoes)
Vasya.work()
Vasya.harvest()
Vasya.work()
Vasya.work()
Vasya.work()
Vasya.work()
Vasya.harvest()