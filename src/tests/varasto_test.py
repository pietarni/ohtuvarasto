import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_negatiivinen_tilavuus_nollataan(self):
        new_varasto = Varasto(-10)
        self.assertAlmostEqual(new_varasto.tilavuus, 0)

    def test_negatiivinen_saldo_nollataan(self):
        new_varasto = Varasto(10,-10)
        self.assertAlmostEqual(new_varasto.saldo, 0)

    def test_saldo_yli_tilavuuden_tasataan(self):
        new_varasto = Varasto(10,100)
        self.assertAlmostEqual(new_varasto.saldo, 10)

    def test_negatiivisen_lisays_ei_muutoksia(self):
        alkuperainen_saldo = self.varasto.saldo
        self.varasto.lisaa_varastoon(-10)
        self.assertAlmostEqual(self.varasto.saldo, alkuperainen_saldo)

    def test_lisays_ei_mene_yli_tilavuuden(self):
        self.varasto.lisaa_varastoon(self.varasto.tilavuus+1)
        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_negatiivisen_ottaminen_ei_muutosta(self):
        alkuperainen_saldo = self.varasto.saldo
        self.varasto.ota_varastosta(-10)
        self.assertAlmostEqual(self.varasto.saldo, alkuperainen_saldo)

    def test_ottaminen_yli_saldon_palauttaa_koko_saldon(self):
        alkuperainen_saldo = self.varasto.saldo
        otettu = self.varasto.ota_varastosta(alkuperainen_saldo+100)
        self.assertAlmostEqual(otettu, alkuperainen_saldo)

    def test_str(self):
        self.assertAlmostEqual(str(self.varasto), f"saldo = {0}, vielä tilaa {100}")