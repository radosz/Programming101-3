import unittest
from panda_soc_network import Panda, PandaSocialNetwork


class TestPanda (unittest.TestCase):

    def setUp(self):
        self.sc = PandaSocialNetwork()
        self.Panda_male = Panda("rado", "radosz88@gmail.com", "male")
        self.Panda_female = Panda("Nina", "Nina@abv.bg", "female")

    def test_instance(self):
        self.assertTrue(isinstance(self.Panda_female, Panda))

    def test__eq__panda(self):
        self.assertFalse(self.Panda_female == self.Panda_male)

    def test_isMale_isFemale(self):
        self.assertTrue(self.Panda_male.isMale())
        self.assertTrue(self.Panda_female.isFemale())
        self.assertFalse(self.Panda_female.isMale())
        self.assertFalse(self.Panda_male.isFemale())

    def test_mail(self):
        self.assertTrue(self.Panda_female.isMail())
        wrong_mail = Panda("gosho", "mailaabv.com", "male")
        self.assertFalse(wrong_mail.isMail())

    def test_validate_gender(self):
        self.assertTrue(self.Panda_female.validate_gender())
        gender_test = Panda("gosho", "maila@abv.com", "idiot")
        self.assertFalse(gender_test.validate_gender())

    def test_panda_social_network_add(self):
        Panda1 = Panda("gosho", "maila@abv.com", "male")
        self.sc.add_panda(Panda1)
        self.assertTrue(len(self.sc.network) == 1)
        # Panda2 = Panda("gosho","maila@abv.com","male")
        # self.assertEqual(self.sc.add_panda(Panda1),PandaAlreadyThere)

    def test_panda_soc_network_has_panda(self):
        self.sc.add_panda(self.Panda_female)
        self.assertTrue(self.sc.has_panda(self.Panda_female))

    def test_make_friends(self):
        Panda3 = Panda("Maria", "marcheto_qka_panda@abv.bg", "female")
        self.sc.make_friends(self.Panda_male, Panda3)
        self.sc.make_friends(self.Panda_male, self.Panda_female)
        self.assertTrue(len(self.sc.network[self.Panda_male]) == 2)

        # print(self.sc)
    def test_are_friends(self):
        Panda3 = Panda("Maria", "marcheto_qka_panda@abv.bg", "female")
        self.sc.make_friends(self.Panda_male, Panda3)
        self.sc.make_friends(self.Panda_male, self.Panda_female)
        self.assertTrue(
            self.sc.are_friends(self.Panda_male, self.Panda_female))

    def test_friends_of_panda(self):
        Panda3 = Panda("Maria", "marcheto_qka_panda@abv.bg", "female")
        self.sc.make_friends(self.Panda_male, Panda3)
        self.sc.make_friends(self.Panda_male, self.Panda_female)
        self.assertTrue(self.Panda_female in self.sc.network[self.Panda_male])
        self.assertTrue(Panda3 in self.sc.network[self.Panda_male])

    def test_connection_level(self):
        Panda1 = Panda("Maria", "marcheto_qka_panda@abv.bg", "female")
        Panda2 = Panda("Blagoi", "marcheto_qka_panda@abv.bg", "male")
        Panda3 = Panda("Tonka", "marcheto_qka_panda@abv.bg", "female")
        Panda4 = Panda("Geri", "marcheto_qka_panda@abv.bg", "female")
        Panda5 = Panda("Ivan", "marcheto_qka_panda@abv.bg", "male")
        Panda7 = Panda("Hristo", "marcheto_qka_panda@abv.bg", "male")
        Panda8 = Panda("Penka", "marcheto_qka_panda@abv.bg", "female")
        Panda9 = Panda("Petq", "marcheto_qka_panda@abv.bg", "female")
        Panda10 = Panda("Kitodar", "marcheto_qka_panda@abv.bg", "female")

        self.sc.network = {
            Panda1: [Panda2, Panda3, Panda5],
            Panda2: [Panda1],
            Panda3: [Panda1, Panda4],
            Panda4: [Panda3],
            Panda5: [Panda1, Panda7, Panda8],
            Panda7: [Panda5],
            Panda8: [Panda9, Panda5],
            Panda9: [Panda8]
        }
        self.assertEqual(self.sc.connection_level(Panda1, Panda1), 0)
        self.assertEqual(self.sc.connection_level(Panda1, Panda2), 1)
        self.assertEqual(self.sc.connection_level(Panda1, Panda2), 1)
        self.assertEqual(self.sc.connection_level(Panda1, Panda3), 1)
        self.assertEqual(self.sc.connection_level(Panda3, Panda5), 2)
        self.assertEqual(self.sc.connection_level(Panda1, Panda9), 3)
        self.assertEqual(self.sc.connection_level(Panda1, Panda10), -1)

    def test_are_connected(self):
        self.sc.make_friends(self.Panda_male, self.Panda_female)

        self.assertTrue(
            self.sc.are_connected(self.Panda_male, self.Panda_female))

    def test_how_many_gender_in_network(self):
        Panda1 = Panda("Maria", "marcheto_qka_panda@abv.bg", "female")
        Panda2 = Panda("Blagoi", "marcheto_qka_panda@abv.bg", "male")
        Panda3 = Panda("Tonka", "marcheto_qka_panda@abv.bg", "female")
        Panda4 = Panda("Geri", "marcheto_qka_panda@abv.bg", "female")
        Panda5 = Panda("Ivan", "marcheto_qka_panda@abv.bg", "male")
        Panda7 = Panda("Hristo", "marcheto_qka_panda@abv.bg", "male")
        Panda8 = Panda("Penka", "marcheto_qka_panda@abv.bg", "female")
        Panda9 = Panda("Petq", "marcheto_qka_panda@abv.bg", "female")

        self.sc.network = {
            Panda1: [Panda2, Panda3, Panda5],
            Panda2: [Panda1],
            Panda3: [Panda1, Panda4],
            Panda4: [Panda3],
            Panda5: [Panda1, Panda7, Panda8],
            Panda7: [Panda5],
            Panda8: [Panda9, Panda5],
            Panda9: [Panda8]
        }
        self.assertEqual(
            self.sc.how_many_gender_in_network(1, Panda1, "male"), 2)
        self.assertEqual(
            self.sc.how_many_gender_in_network(2, Panda1, "female"), 3)
        self.assertEqual(
            self.sc.how_many_gender_in_network(2, Panda1, "male"), 3)
        self.assertEqual(
            self.sc.how_many_gender_in_network(3, Panda1, "female"), 4)
        print(self.sc.pandas_to_json())

if __name__ == '__main__':
    unittest.main()
