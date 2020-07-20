import pytest
import main

class Testgame_pytest:

    def setup(self):
        self.game = main.Durak_game(3)
        print('Start test!')

    def teardown(self):
        #self.game.current_throw = 0
        print('Test completed!')

    #проверка что класс получил правильное количество игроков
    def test_init(self):
        assert self.game.col_players == 3

    #проверка количество участников + 1 колода основная
    def test_col_colod(self):
        self.game.razdat_kolodu()
        assert len(self.game.game_baza) == 4

    #количество карт в колодах игрока и основной колоды
    def test_kol_kart(self):
        self.game.razdat_kolodu()
        assert len(self.game.game_baza[1]['koloda']) == 6
        assert len(self.game.game_baza[-1]['koloda']) == 18

    # первой карты хода  еще не существует в начале игры
    def test_pervaia_karta(self):
        with pytest.raises(AttributeError): #AttributeError
            # Код, вызывающий данную ошибку!
            type(self.game.karta_zaprosa) is dict

    #Проверяем что переменные в классе отвечающие за очередь ходов имеют значения
    def test_kto_hodid(self):
        self.game.razdat_kolodu()
        self.game.nomer_act_igroka = 0
        self.game.nomer_otb_igroka = 1
        self.game.hod_brosok()
        assert type(self.game.karta_zaprosa) is dict