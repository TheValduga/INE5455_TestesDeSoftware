import unittest

from src.agencia import Agencia

class TestAgencia(unittest.TestCase):

    def setUp(self) -> None:
        self.agencia = Agencia("Kobrasol","0001","Bradesco")

    def test_cadastro_de_contas(self):
        # implicit fixture setup
        # inline fixture setup
        self.agencia.criar_conta("Lucas")
        self.agencia.criar_conta("Gabriela")
        # exercise sut
        contas = self.agencia.obter_contas()
        # result verification
        self.assertEqual(2, len(contas))

    def test_obter_conta_pelo_id(self):
        # implicit fixture setup
        # inline fixture setup
        self.agencia.criar_conta("Lucas")
        self.agencia.criar_conta("Gabriela")
        # exercise sut
        conta = self.agencia.obter_conta(2)
        titular = conta.titular()
        # result verification
        self.assertEqual("Gabriela", titular)


if __name__ == "__main__":
    unittest.main()