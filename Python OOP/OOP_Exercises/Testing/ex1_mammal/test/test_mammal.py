from unittest import TestCase, main
from project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self) -> None:
        self.mammal = Mammal('Rex', 'Dog', 'Bark')

    def test_correct_init(self):
        self.assertEqual('Rex', self.mammal.name)
        self.assertEqual('Dog', self.mammal.type)
        self.assertEqual('Bark', self.mammal.sound)
        self.assertEqual('animals', self.mammal.get_kingdom())

    def test_make_sound_return_string(self):
        expected_string = "Rex makes Bark"

        self.assertEqual(expected_string, self.mammal.make_sound())

    def test_info_expect_string(self):
        expected_string = 'Rex is of type Dog'

        self.assertEqual(expected_string, self.mammal.info())


if __name__ == '__main__':
    main()