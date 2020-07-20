import unittest
from main import Durak_game

class Testgame_unittest(unittest.TestCase):

    def setUp(self):
        self.game = Durak_game(3)
        print('Start test!')

    def tearDown(self):
        #self.game.current_throw = 0
        print('Test completed!')
        del self.game

#проверка что класс получил правильное количество игроков
    def test_init(self):
        self.assertEqual(self.game.col_players, 3)

    #проверка количество участников + 1 колода основная
    def test_col_colod(self):
        self.game.razdat_kolodu()
        self.assertEqual(len(self.game.game_baza), 4)

    #количество карт в колодах игрока и основной колоды
    def test_kol_kart(self):
        self.game.razdat_kolodu()
        self.assertEqual(len(self.game.game_baza[1]['koloda']), 6)
        self.assertEqual(len(self.game.game_baza[-1]['koloda']), 18)

    # первой карты хода  еще не существует в начале игры
    def test_pervaia_karta(self):
        with self.assertRaises(AttributeError): #AttributeError
            # Код, вызывающий данную ошибку!
            type(self.game.karta_zaprosa) is dict

    #Проверяем что переменные в классе отвечающие за очередь ходов имеют значения
    def test_kto_hodid(self):
        self.game.razdat_kolodu()
        self.game.nomer_act_igroka = 0
        self.game.nomer_otb_igroka = 1
        self.game.hod_brosok()
        self.assertTrue(type(self.game.karta_zaprosa), dict)