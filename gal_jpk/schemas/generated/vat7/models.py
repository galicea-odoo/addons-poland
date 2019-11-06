# Signature <<<5dc2f5fc>>>
# -*- coding: utf-8 -*-

import decimal
import datetime
from .bindings import Namespace
from xsd2xml import xmlgen
from ..http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_07_29_eD_VATZD_ import models as vzd
from ..http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_07_29_eD_VATZT_ import models as vzt
from ..http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_08_03_eD_VATZZ_ import models as vzz
from ..http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_02_05_eD_ORDZU_ import models as zzu
from ..http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy_ import models as etd
# vvv ONLY EDIT CODE BELOW THIS LINE vvv {imports}
# ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {ecf8427e}

class TNaglowek(object):
    """Nagłówek deklaracji"""
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TNaglowek}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getCelZlozenia(self):
        """@returns TNaglowek_CelZlozenia"""
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TNaglowek:getCelZlozenia}
        # TODO: Fill in the actual data
        return TNaglowek_CelZlozenia()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {f1107c65}

    def getKodFormularza(self):
        """@returns TNaglowek_KodFormularza"""
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TNaglowek:getKodFormularza}
        # TODO: Fill in the actual data
        return TNaglowek_KodFormularza()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {840267e6}

    def getKodUrzedu(self):
        """@returns string"""
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TNaglowek:getKodUrzedu}
        # TODO: Fill in the actual data
        return "0202"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {f770400d}

    def getMiesiac(self):
        """@returns int"""
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TNaglowek:getMiesiac}
        # TODO: Fill in the actual data
        return 1
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {3cc34dcd}

    def getRok(self):
        """@returns datetime.datetime"""
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TNaglowek:getRok}
        # TODO: Fill in the actual data
        return datetime.datetime.strptime('2016-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {fb6297fc}

    def getWariantFormularza(self):
        """@returns int"""
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TNaglowek:getWariantFormularza}
        # TODO: Fill in the actual data
        return 17
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c99a852a}


class TNaglowek_KodFormularza(object):
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TNaglowek_KodFormularza}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getContent(self):
        """XML Element Content

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TNaglowek_KodFormularza:getContent}
        # TODO: Fill in the actual data
        return "VAT-7"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {0aa36574}

    def getkodPodatku(self):
        """@returns string"""
        return "VAT"

    def getkodSystemowy(self):
        """@returns string"""
        return "VAT-7 (17)"

    def getrodzajZobowiazania(self):
        """@returns string"""
        return "Z"

    def getwersjaSchemy(self):
        """@returns string"""
        return "1-0E"


class TNaglowek_CelZlozenia(object):
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TNaglowek_CelZlozenia}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getContent(self):
        """XML Element Content

        @returns int
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TNaglowek_CelZlozenia:getContent}
        # TODO: Fill in the actual data
        return 1
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {3cc34dcd}

    def getpoz(self):
        """@returns string"""
        return "P_7"


class Element_Deklaracja(object):
    """DEKLARACJA DLA PODATKU OD TOWARÓW I USŁUG"""
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja}
    def __init__(self, document):
        """@param document odoo.addons.gal_jpk.models.Document"""
        self.document = document
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getNaglowek(self):
        """Nagłówek deklaracji

        @returns TNaglowek
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja:getNaglowek}
        # TODO: Fill in the actual data
        return TNaglowek()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {98f6a537}

    def getPodmiot1(self):
        """@returns Element_Deklaracja_Podmiot1"""
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja:getPodmiot1}
        # TODO: Fill in the actual data
        return Element_Deklaracja_Podmiot1()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {eff50b7f}

    def getPouczenia(self):
        """Wartość 1 oznacza potwierdzenie zapoznania się z treścią i akceptację
        poniższych pouczeń:
        								W przypadku niewpłacenia w obowiązującym terminie kwoty z poz.
        54 lub wpłacenia jej w niepełnej wysokości, niniejsza deklaracja stanowi
        podstawę do wystawienia tytułu wykonawczego zgodnie z przepisami ustawy
        z dnia 17 czerwca 1966 r. o postępowaniu egzekucyjnym w administracji
        (Dz. U. z 2016 r. poz. 599, z późn. zm.).

        Za podanie nieprawdy lub zatajenie prawdy i przez to narażenie podatku
        na uszczuplenie grozi odpowiedzialność przewidziana w Kodeksie karnym
        skarbowym.


        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja:getPouczenia}
        # TODO: Fill in the actual data
        return 1
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {3cc34dcd}

    def getPozycjeSzczegolowe(self):
        """@returns Element_Deklaracja_PozycjeSzczegolowe"""
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja:getPozycjeSzczegolowe}
        # TODO: Fill in the actual data
        return Element_Deklaracja_PozycjeSzczegolowe()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {8ce4aaaa}

    def getZalaczniki(self):
        """@returns Element_Deklaracja_Zalaczniki"""
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja:getZalaczniki}
        # TODO: Fill in the actual data
        return Element_Deklaracja_Zalaczniki()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {60bdc2de}

    def toXML(self):
        return xmlgen.bind(Namespace.elementBindings()['Deklaracja'], self).toxml()


class Element_Deklaracja_Zalaczniki(object):
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_Zalaczniki}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getWniosek_VAT_ZD(self):
        """ZAWIADOMIENIE O SKORYGOWANIU PODSTAWY OPODATKOWANIA ORAZ KWOTY
        PODATKU NALEŻNEGO

        @returns Element_Deklaracja_Zalaczniki_Wniosek_VAT_ZD
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_Zalaczniki:getWniosek_VAT_ZD}
        # TODO: Fill in the actual data
        return Element_Deklaracja_Zalaczniki_Wniosek_VAT_ZD()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {be916654}

    def getWniosek_VAT_ZT(self):
        """WNIOSEK O PRZYSPIESZENIE TERMINU ZWROTU PODATKU

        @returns Element_Deklaracja_Zalaczniki_Wniosek_VAT_ZT
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_Zalaczniki:getWniosek_VAT_ZT}
        # TODO: Fill in the actual data
        return Element_Deklaracja_Zalaczniki_Wniosek_VAT_ZT()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {75031beb}

    def getWniosek_VAT_ZZ(self):
        """WNIOSEK O ZWROT PODATKU VAT

        @returns Element_Deklaracja_Zalaczniki_Wniosek_VAT_ZZ
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_Zalaczniki:getWniosek_VAT_ZZ}
        # TODO: Fill in the actual data
        return Element_Deklaracja_Zalaczniki_Wniosek_VAT_ZZ()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {9faca786}

    def getZalacznik_ORD_ZU(self):
        """UZASADNIENIE PRZYCZYN KOREKTY DEKLARACJI

        @returns Element_Deklaracja_Zalaczniki_Zalacznik_ORD_ZU
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_Zalaczniki:getZalacznik_ORD_ZU}
        # TODO: Fill in the actual data
        return Element_Deklaracja_Zalaczniki_Zalacznik_ORD_ZU()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {16c48cea}


class Element_Deklaracja_Zalaczniki_Zalacznik_ORD_ZU(object):
    """UZASADNIENIE PRZYCZYN KOREKTY DEKLARACJI"""
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_Zalaczniki_Zalacznik_ORD_ZU}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getNaglowek(self):
        """@returns zzu.TNaglowek_ORD__ZU"""
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_Zalaczniki_Zalacznik_ORD_ZU:getNaglowek}
        # TODO: Fill in the actual data
        return zzu.TNaglowek_ORD__ZU()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {2b3911c0}

    def getPozycjeSzczegolowe(self):
        """@returns
        Element_Deklaracja_Zalaczniki_Zalacznik_ORD_ZU_PozycjeSzczegolowe
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_Zalaczniki_Zalacznik_ORD_ZU:getPozycjeSzczegolowe}
        # TODO: Fill in the actual data
        return Element_Deklaracja_Zalaczniki_Zalacznik_ORD_ZU_PozycjeSzczegolowe()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {8928cbd7}


class Element_Deklaracja_Zalaczniki_Zalacznik_ORD_ZU_PozycjeSzczegolowe(object):
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_Zalaczniki_Zalacznik_ORD_ZU_PozycjeSzczegolowe}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getP_13(self):
        """Treść uzasadnienia

        @returns
        Element_Deklaracja_Zalaczniki_Zalacznik_ORD_ZU_PozycjeSzczegolowe_P_13
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_Zalaczniki_Zalacznik_ORD_ZU_PozycjeSzczegolowe:getP_13}
        # TODO: Fill in the actual data
        return Element_Deklaracja_Zalaczniki_Zalacznik_ORD_ZU_PozycjeSzczegolowe_P_13()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {02fec15c}


class Element_Deklaracja_Zalaczniki_Zalacznik_ORD_ZU_PozycjeSzczegolowe_P_13(object):
    """Treść uzasadnienia"""
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_Zalaczniki_Zalacznik_ORD_ZU_PozycjeSzczegolowe_P_13}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getContent(self):
        """XML Element Content

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_Zalaczniki_Zalacznik_ORD_ZU_PozycjeSzczegolowe_P_13:getContent}
        # TODO: Fill in the actual data
        return "Element_Deklaracja_Zalaczniki_Zalacznik_ORD_ZU_PozycjeSzczegolowe_P_13"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {17b86701}


class Element_Deklaracja_Zalaczniki_Wniosek_VAT_ZZ(object):
    """WNIOSEK O ZWROT PODATKU VAT"""
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_Zalaczniki_Wniosek_VAT_ZZ}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getNaglowek(self):
        """@returns vzz.TNaglowek_VAT__ZZ"""
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_Zalaczniki_Wniosek_VAT_ZZ:getNaglowek}
        # TODO: Fill in the actual data
        return vzz.TNaglowek_VAT__ZZ()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {6e302235}

    def getPozycjeSzczegolowe(self):
        """@returns
        Element_Deklaracja_Zalaczniki_Wniosek_VAT_ZZ_PozycjeSzczegolowe
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_Zalaczniki_Wniosek_VAT_ZZ:getPozycjeSzczegolowe}
        # TODO: Fill in the actual data
        return Element_Deklaracja_Zalaczniki_Wniosek_VAT_ZZ_PozycjeSzczegolowe()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {3a8d5e07}


class Element_Deklaracja_Zalaczniki_Wniosek_VAT_ZZ_PozycjeSzczegolowe(object):
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_Zalaczniki_Wniosek_VAT_ZZ_PozycjeSzczegolowe}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getP_10(self):
        """Uzasadnienie złożenia wniosku

        @returns
        Element_Deklaracja_Zalaczniki_Wniosek_VAT_ZZ_PozycjeSzczegolowe_P_10
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_Zalaczniki_Wniosek_VAT_ZZ_PozycjeSzczegolowe:getP_10}
        # TODO: Fill in the actual data
        return Element_Deklaracja_Zalaczniki_Wniosek_VAT_ZZ_PozycjeSzczegolowe_P_10()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {f3f1f422}

    def getP_8(self):
        """Powód zwrotu

        @returns int
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_Zalaczniki_Wniosek_VAT_ZZ_PozycjeSzczegolowe:getP_8}
        # TODO: Fill in the actual data
        return 1
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {3cc34dcd}

    def getP_9(self):
        """Wnioskowana kwota podatku do zwrotu

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_Zalaczniki_Wniosek_VAT_ZZ_PozycjeSzczegolowe:getP_9}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}


class Element_Deklaracja_Zalaczniki_Wniosek_VAT_ZZ_PozycjeSzczegolowe_P_10(object):
    """Uzasadnienie złożenia wniosku"""
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_Zalaczniki_Wniosek_VAT_ZZ_PozycjeSzczegolowe_P_10}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getContent(self):
        """XML Element Content

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_Zalaczniki_Wniosek_VAT_ZZ_PozycjeSzczegolowe_P_10:getContent}
        # TODO: Fill in the actual data
        return "Element_Deklaracja_Zalaczniki_Wniosek_VAT_ZZ_PozycjeSzczegolowe_P_10"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {bdce0b46}


class Element_Deklaracja_Zalaczniki_Wniosek_VAT_ZT(object):
    """WNIOSEK O PRZYSPIESZENIE TERMINU ZWROTU PODATKU"""
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_Zalaczniki_Wniosek_VAT_ZT}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getNaglowek(self):
        """@returns vzt.TNaglowek_VAT__ZT"""
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_Zalaczniki_Wniosek_VAT_ZT:getNaglowek}
        # TODO: Fill in the actual data
        return vzt.TNaglowek_VAT__ZT()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {6f523ce4}

    def getPozycjeSzczegolowe(self):
        """@returns
        Element_Deklaracja_Zalaczniki_Wniosek_VAT_ZT_PozycjeSzczegolowe
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_Zalaczniki_Wniosek_VAT_ZT:getPozycjeSzczegolowe}
        # TODO: Fill in the actual data
        return Element_Deklaracja_Zalaczniki_Wniosek_VAT_ZT_PozycjeSzczegolowe()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {68ee57f3}


class Element_Deklaracja_Zalaczniki_Wniosek_VAT_ZT_PozycjeSzczegolowe(object):
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_Zalaczniki_Wniosek_VAT_ZT_PozycjeSzczegolowe}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getP_10(self):
        """Kwota do zwrotu w terminie 25 dni, o której przyspieszenie wnioskuje
        podatnik

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_Zalaczniki_Wniosek_VAT_ZT_PozycjeSzczegolowe:getP_10}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getP_11(self):
        """Uzasadnienie wniosku

        @returns
        Element_Deklaracja_Zalaczniki_Wniosek_VAT_ZT_PozycjeSzczegolowe_P_11
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_Zalaczniki_Wniosek_VAT_ZT_PozycjeSzczegolowe:getP_11}
        # TODO: Fill in the actual data
        return Element_Deklaracja_Zalaczniki_Wniosek_VAT_ZT_PozycjeSzczegolowe_P_11()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {2b238654}


class Element_Deklaracja_Zalaczniki_Wniosek_VAT_ZT_PozycjeSzczegolowe_P_11(object):
    """Uzasadnienie wniosku"""
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_Zalaczniki_Wniosek_VAT_ZT_PozycjeSzczegolowe_P_11}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getContent(self):
        """XML Element Content

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_Zalaczniki_Wniosek_VAT_ZT_PozycjeSzczegolowe_P_11:getContent}
        # TODO: Fill in the actual data
        return "Element_Deklaracja_Zalaczniki_Wniosek_VAT_ZT_PozycjeSzczegolowe_P_11"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {7475da0c}


class Element_Deklaracja_Zalaczniki_Wniosek_VAT_ZD(object):
    """ZAWIADOMIENIE O SKORYGOWANIU PODSTAWY OPODATKOWANIA ORAZ KWOTY PODATKU
    NALEŻNEGO
    """
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_Zalaczniki_Wniosek_VAT_ZD}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getNaglowek(self):
        """@returns vzd.TNaglowek_VAT__ZD"""
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_Zalaczniki_Wniosek_VAT_ZD:getNaglowek}
        # TODO: Fill in the actual data
        return vzd.TNaglowek_VAT__ZD()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {405c3647}

    def getPozycjeSzczegolowe(self):
        """Dane identyfikacyjne dłużnika oraz informacje dotyczące kwot korekty
        podstawy opodatkowania oraz podatku należnego

        @returns Element_Deklaracja_Zalaczniki_Wniosek_VAT_ZD_PozycjeSzczegolowe
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_Zalaczniki_Wniosek_VAT_ZD:getPozycjeSzczegolowe}
        # TODO: Fill in the actual data
        return Element_Deklaracja_Zalaczniki_Wniosek_VAT_ZD_PozycjeSzczegolowe()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {f5af3510}


class Element_Deklaracja_Zalaczniki_Wniosek_VAT_ZD_PozycjeSzczegolowe(object):
    """Dane identyfikacyjne dłużnika oraz informacje dotyczące kwot korekty
    podstawy opodatkowania oraz podatku należnego
    """
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_Zalaczniki_Wniosek_VAT_ZD_PozycjeSzczegolowe}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getP_10(self):
        """Ogółem kwota korekty podstawy opodatkowania

        @returns long
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_Zalaczniki_Wniosek_VAT_ZD_PozycjeSzczegolowe:getP_10}
        # TODO: Fill in the actual data
        return 0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {e3b5de26}

    def getP_11(self):
        """Ogółem kwota korekty podatku należnego

        @returns long
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_Zalaczniki_Wniosek_VAT_ZD_PozycjeSzczegolowe:getP_11}
        # TODO: Fill in the actual data
        return 0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {e3b5de26}

    def getP_B(self):
        """@returns
        Element_Deklaracja_Zalaczniki_Wniosek_VAT_ZD_PozycjeSzczegolowe_P_B[]
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_Zalaczniki_Wniosek_VAT_ZD_PozycjeSzczegolowe:getP_B}
        # TODO: Fill in the actual data
        return [Element_Deklaracja_Zalaczniki_Wniosek_VAT_ZD_PozycjeSzczegolowe_P_B(), Element_Deklaracja_Zalaczniki_Wniosek_VAT_ZD_PozycjeSzczegolowe_P_B()]
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {e29d00bc}


class Element_Deklaracja_Zalaczniki_Wniosek_VAT_ZD_PozycjeSzczegolowe_P_B(object):
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_Zalaczniki_Wniosek_VAT_ZD_PozycjeSzczegolowe_P_B}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getP_BB(self):
        """Nazwa podatnika (dłużnika)

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_Zalaczniki_Wniosek_VAT_ZD_PozycjeSzczegolowe_P_B:getP_BB}
        # TODO: Fill in the actual data
        return "P_BB"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {51fc8e0e}

    def getP_BC(self):
        """Identyfikator podatkowy NIP podatnika (dłużnika)

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_Zalaczniki_Wniosek_VAT_ZD_PozycjeSzczegolowe_P_B:getP_BC}
        # TODO: Fill in the actual data
        return "8424734595"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {fff228e5}

    def getP_BD1(self):
        """Nr faktury

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_Zalaczniki_Wniosek_VAT_ZD_PozycjeSzczegolowe_P_B:getP_BD1}
        # TODO: Fill in the actual data
        return "P_BD1"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {199d8f02}

    def getP_BD2(self):
        """Data wystawienia faktury

        @returns datetime.datetime
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_Zalaczniki_Wniosek_VAT_ZD_PozycjeSzczegolowe_P_B:getP_BD2}
        # TODO: Fill in the actual data
        return datetime.datetime.strptime('2011-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {7ec3083e}

    def getP_BE(self):
        """Data upływu terminu płatności określonego w fakturze lub umowie

        @returns datetime.datetime
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_Zalaczniki_Wniosek_VAT_ZD_PozycjeSzczegolowe_P_B:getP_BE}
        # TODO: Fill in the actual data
        return datetime.datetime.strptime('2011-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {7ec3083e}

    def getP_BF(self):
        """Kwota korekty podstawy opodatkowania

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_Zalaczniki_Wniosek_VAT_ZD_PozycjeSzczegolowe_P_B:getP_BF}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getP_BG(self):
        """Kwota korekty podatku należnego

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_Zalaczniki_Wniosek_VAT_ZD_PozycjeSzczegolowe_P_B:getP_BG}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def gettyp(self):
        """@returns string"""
        return "G"


class Element_Deklaracja_PozycjeSzczegolowe(object):
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_PozycjeSzczegolowe}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getP_10(self):
        """Podstawa opodatkowania - Dostawa towarów oraz świadczenie usług na
        terytorium kraju, zwolnione od podatku

        @returns long
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_PozycjeSzczegolowe:getP_10}
        # TODO: Fill in the actual data
        return 0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {e3b5de26}

    def getP_11(self):
        """Podstawa opodatkowania - Dostawa towarów oraz świadczenie usług poza
        terytorium kraju

        @returns long
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_PozycjeSzczegolowe:getP_11}
        # TODO: Fill in the actual data
        return 0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {e3b5de26}

    def getP_12(self):
        """Podstawa opodatkowania - w tym świadczenie usług, o których mowa w
        art. 100 ust. 1 pkt 4 ustawy

        @returns long
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_PozycjeSzczegolowe:getP_12}
        # TODO: Fill in the actual data
        return 0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {e3b5de26}

    def getP_13(self):
        """Podstawa opodatkowania - Dostawa towarów oraz świadczenie usług na
        terytorium kraju, opodatkowane stawką 0%

        @returns long
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_PozycjeSzczegolowe:getP_13}
        # TODO: Fill in the actual data
        return 0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {e3b5de26}

    def getP_14(self):
        """Podstawa opodatkowania - w tym dostawa towarów, o której mowa w art.
        129 ustawy

        @returns long
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_PozycjeSzczegolowe:getP_14}
        # TODO: Fill in the actual data
        return 0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {e3b5de26}

    def getP_15(self):
        """Podstawa opodatkowania - Dostawa towarów oraz świadczenie usług na
        terytorium kraju, opodatkowane stawką 5%

        @returns long
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_PozycjeSzczegolowe:getP_15}
        # TODO: Fill in the actual data
        return 0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {e3b5de26}

    def getP_16(self):
        """Podatek należny - Dostawa towarów oraz świadczenie usług na
        terytorium kraju, opodatkowane stawką 5%

        @returns long
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_PozycjeSzczegolowe:getP_16}
        # TODO: Fill in the actual data
        return 0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {e3b5de26}

    def getP_17(self):
        """Podstawa opodatkowania - Dostawa towarów oraz świadczenie usług na
        terytorium kraju, opodatkowane stawką 7% albo 8%

        @returns long
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_PozycjeSzczegolowe:getP_17}
        # TODO: Fill in the actual data
        return 0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {e3b5de26}

    def getP_18(self):
        """Podatek należny - Dostawa towarów oraz świadczenie usług na
        terytorium kraju, opodatkowane stawką 7% albo 8%

        @returns long
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_PozycjeSzczegolowe:getP_18}
        # TODO: Fill in the actual data
        return 0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {e3b5de26}

    def getP_19(self):
        """Podstawa opodatkowania - Dostawa towarów oraz świadczenie usług na
        terytorium kraju, opodatkowane stawką 22% albo 23%

        @returns long
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_PozycjeSzczegolowe:getP_19}
        # TODO: Fill in the actual data
        return 0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {e3b5de26}

    def getP_20(self):
        """Podatek należny - Dostawa towarów oraz świadczenie usług na
        terytorium kraju, opodatkowane stawką 22% albo 23%

        @returns long
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_PozycjeSzczegolowe:getP_20}
        # TODO: Fill in the actual data
        return 0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {e3b5de26}

    def getP_21(self):
        """Podstawa opodatkowania - Wewnątrzwspólnotowa dostawa towarów

        @returns long
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_PozycjeSzczegolowe:getP_21}
        # TODO: Fill in the actual data
        return 0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {e3b5de26}

    def getP_22(self):
        """Podstawa opodatkowania - Eksport towarów

        @returns long
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_PozycjeSzczegolowe:getP_22}
        # TODO: Fill in the actual data
        return 0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {e3b5de26}

    def getP_23(self):
        """Podstawa opodatkowania - Wewnątrzwspólnotowe nabycie towarów

        @returns long
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_PozycjeSzczegolowe:getP_23}
        # TODO: Fill in the actual data
        return 0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {e3b5de26}

    def getP_24(self):
        """Podatek należny - Wewnątrzwspólnotowe nabycie towarów

        @returns long
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_PozycjeSzczegolowe:getP_24}
        # TODO: Fill in the actual data
        return 0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {e3b5de26}

    def getP_25(self):
        """Podstawa opodatkowania - Import towarów podlegający rozliczeniu
        zgodnie z art. 33a ustawy

        @returns long
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_PozycjeSzczegolowe:getP_25}
        # TODO: Fill in the actual data
        return 0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {e3b5de26}

    def getP_26(self):
        """Podatek należny - Import towarów podlegający rozliczeniu zgodnie z
        art. 33a ustawy

        @returns long
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_PozycjeSzczegolowe:getP_26}
        # TODO: Fill in the actual data
        return 0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {e3b5de26}

    def getP_27(self):
        """Podstawa opodatkowania - Import usług z wyłączeniem usług nabywanych
        od podatników podatku od wartości dodanej, do których stosuje się art.
        28b ustawy

        @returns long
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_PozycjeSzczegolowe:getP_27}
        # TODO: Fill in the actual data
        return 0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {e3b5de26}

    def getP_28(self):
        """Podatek należny - Import usług z wyłączeniem usług nabywanych od
        podatników podatku od wartości dodanej, do których stosuje się art. 28b
        ustawy

        @returns long
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_PozycjeSzczegolowe:getP_28}
        # TODO: Fill in the actual data
        return 0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {e3b5de26}

    def getP_29(self):
        """Podstawa opodatkowania - Import usług nabywanych od podatników
        podatku od wartości dodanej, do których stosuje się art. 28b ustawy

        @returns long
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_PozycjeSzczegolowe:getP_29}
        # TODO: Fill in the actual data
        return 0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {e3b5de26}

    def getP_30(self):
        """Podatek należny - Import usług nabywanych od podatników podatku od
        wartości dodanej, do których stosuje się art. 28b ustawy

        @returns long
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_PozycjeSzczegolowe:getP_30}
        # TODO: Fill in the actual data
        return 0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {e3b5de26}

    def getP_31(self):
        """Podstawa opodatkowania - Dostawa towarów oraz świadczenie usług, dla
        których podatnikiem jest nabywca zgodnie z art. 17 ust. 1 pkt 7 lub 8
        ustawy (wypełnia dostawca)

        @returns long
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_PozycjeSzczegolowe:getP_31}
        # TODO: Fill in the actual data
        return 0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {e3b5de26}

    def getP_32(self):
        """Podstawa opodatkowania - Dostawa towarów, dla których podatnikiem
        jest nabywca zgodnie z art. 17 ust. 1 pkt 5 ustawy (wypełnia nabywca)

        @returns long
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_PozycjeSzczegolowe:getP_32}
        # TODO: Fill in the actual data
        return 0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {e3b5de26}

    def getP_33(self):
        """Podatek należny - Dostawa towarów, dla których podatnikiem jest
        nabywca zgodnie z art. 17 ust. 1 pkt 5 ustawy (wypełnia nabywca)

        @returns long
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_PozycjeSzczegolowe:getP_33}
        # TODO: Fill in the actual data
        return 0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {e3b5de26}

    def getP_34(self):
        """Podstawa opodatkowania - Dostawa towarów oraz świadczenie usług, dla
        których podatnikiem jest nabywca zgodnie z art. 17 ust. 1 pkt 7 lub 8
        ustawy (wypełnia nabywca)

        @returns long
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_PozycjeSzczegolowe:getP_34}
        # TODO: Fill in the actual data
        return 0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {e3b5de26}

    def getP_35(self):
        """Podatek należny - Dostawa towarów oraz świadczenie usług, dla których
        podatnikiem jest nabywca zgodnie z art. 17 ust. 1 pkt 7 lub 8 ustawy
        (wypełnia nabywca)

        @returns long
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_PozycjeSzczegolowe:getP_35}
        # TODO: Fill in the actual data
        return 0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {e3b5de26}

    def getP_36(self):
        """Kwota podatku należnego od towarów i usług objętych spisem z natury,
        o którym mowa w art. 14 ust. 5 ustawy

        @returns long
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_PozycjeSzczegolowe:getP_36}
        # TODO: Fill in the actual data
        return 0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {e3b5de26}

    def getP_37(self):
        """Zwrot odliczonej lub zwróconej kwoty wydatkowanej na zakup kas
        rejestrujących, o którym mowa w art. 111 ust. 6 ustawy

        @returns long
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_PozycjeSzczegolowe:getP_37}
        # TODO: Fill in the actual data
        return 0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {e3b5de26}

    def getP_38(self):
        """Kwota podatku należnego od wewnątrzwspólnotowego nabycia środków
        transportu, wykazanego w poz. 24, podlegająca wpłacie w terminie, o
        którym mowa w art. 103 ust. 3, w związku z ust. 4 ustawy

        @returns long
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_PozycjeSzczegolowe:getP_38}
        # TODO: Fill in the actual data
        return 0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {e3b5de26}

    def getP_39(self):
        """Kwota podatku od wewnątrzwspólnotowego nabycia paliw silnikowych,
        podlegająca wpłacie w terminach, o których mowa w art. 103 ust. 5a i 5b
        ustawy

        @returns long
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_PozycjeSzczegolowe:getP_39}
        # TODO: Fill in the actual data
        return 0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {e3b5de26}

    def getP_40(self):
        """Razem - Podstawa opodatkowania

        @returns long
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_PozycjeSzczegolowe:getP_40}
        # TODO: Fill in the actual data
        return 0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {e3b5de26}

    def getP_41(self):
        """Razem - Podatek należny

        @returns long
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_PozycjeSzczegolowe:getP_41}
        # TODO: Fill in the actual data
        return 0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {e3b5de26}

    def getP_42(self):
        """Kwota nadwyżki z poprzedniej deklaracji

        @returns long
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_PozycjeSzczegolowe:getP_42}
        # TODO: Fill in the actual data
        return 0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {e3b5de26}

    def getP_43(self):
        """Wartość netto - Nabycie towarów i usług zaliczanych u podatnika do
        środków trwałych

        @returns long
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_PozycjeSzczegolowe:getP_43}
        # TODO: Fill in the actual data
        return 0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {e3b5de26}

    def getP_44(self):
        """Podatek naliczony - Nabycie towarów i usług zaliczanych u podatnika
        do środków trwałych

        @returns long
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_PozycjeSzczegolowe:getP_44}
        # TODO: Fill in the actual data
        return 0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {e3b5de26}

    def getP_45(self):
        """Wartość netto - Nabycie towarów i usług pozostałych

        @returns long
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_PozycjeSzczegolowe:getP_45}
        # TODO: Fill in the actual data
        return 0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {e3b5de26}

    def getP_46(self):
        """Podatek naliczony - Nabycie towarów i usług pozostałych

        @returns long
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_PozycjeSzczegolowe:getP_46}
        # TODO: Fill in the actual data
        return 0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {e3b5de26}

    def getP_47(self):
        """Korekta podatku naliczonego od nabycia środków trwałych

        @returns long
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_PozycjeSzczegolowe:getP_47}
        # TODO: Fill in the actual data
        return 0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {e3b5de26}

    def getP_48(self):
        """Korekta podatku naliczonego od pozostałych nabyć

        @returns long
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_PozycjeSzczegolowe:getP_48}
        # TODO: Fill in the actual data
        return 0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {e3b5de26}

    def getP_49(self):
        """Korekta podatku naliczonego, o której mowa w art. 89b ust. 1 ustawy

        @returns long
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_PozycjeSzczegolowe:getP_49}
        # TODO: Fill in the actual data
        return 0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {e3b5de26}

    def getP_50(self):
        """Korekta podatku naliczonego, o której mowa w art. 89b ust. 4 ustawy

        @returns long
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_PozycjeSzczegolowe:getP_50}
        # TODO: Fill in the actual data
        return 0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {e3b5de26}

    def getP_51(self):
        """Razem kwota podatku naliczonego do odliczenia

        @returns long
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_PozycjeSzczegolowe:getP_51}
        # TODO: Fill in the actual data
        return 0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {e3b5de26}

    def getP_52(self):
        """Kwota wydatkowana na zakup kas rejestrujących, do odliczenia w danym
        okresie rozliczeniowym

        @returns long
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_PozycjeSzczegolowe:getP_52}
        # TODO: Fill in the actual data
        return 0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {e3b5de26}

    def getP_53(self):
        """Kwota podatku objęta zaniechaniem poboru

        @returns long
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_PozycjeSzczegolowe:getP_53}
        # TODO: Fill in the actual data
        return 0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {e3b5de26}

    def getP_54(self):
        """Kwota podatku podlegającego wpłacie do urzędu skarbowego

        @returns long
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_PozycjeSzczegolowe:getP_54}
        # TODO: Fill in the actual data
        return 0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {e3b5de26}

    def getP_55(self):
        """Kwota wydatkowana na zakup kas rejestrujących, przysługująca do
        zwrotu w danym okresie rozliczeniowym

        @returns long
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_PozycjeSzczegolowe:getP_55}
        # TODO: Fill in the actual data
        return 0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {e3b5de26}

    def getP_56(self):
        """Nadwyżka podatku naliczonego nad należnym

        @returns long
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_PozycjeSzczegolowe:getP_56}
        # TODO: Fill in the actual data
        return 0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {e3b5de26}

    def getP_57(self):
        """Kwota do zwrotu na rachunek bankowy wskazany przez podatnika

        @returns long
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_PozycjeSzczegolowe:getP_57}
        # TODO: Fill in the actual data
        return 0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {e3b5de26}

    def getP_58(self):
        """w tym kwota do zwrotu - w terminie 25 dni

        @returns long
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_PozycjeSzczegolowe:getP_58}
        # TODO: Fill in the actual data
        return 0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {e3b5de26}

    def getP_59(self):
        """w tym kwota do zwrotu - w terminie 60 dni

        @returns long
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_PozycjeSzczegolowe:getP_59}
        # TODO: Fill in the actual data
        return 0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {e3b5de26}

    def getP_60(self):
        """w tym kwota do zwrotu - w terminie 180 dni

        @returns long
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_PozycjeSzczegolowe:getP_60}
        # TODO: Fill in the actual data
        return 0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {e3b5de26}

    def getP_61(self):
        """Kwota do przeniesienia na następny okres rozliczeniowy

        @returns long
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_PozycjeSzczegolowe:getP_61}
        # TODO: Fill in the actual data
        return 0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {e3b5de26}

    def getP_62(self):
        """Podatnik wykonywał w okresie rozliczeniowym czynności, o których mowa
        w art. 119 ustawy

        @returns int
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_PozycjeSzczegolowe:getP_62}
        # TODO: Fill in the actual data
        return 1
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {3cc34dcd}

    def getP_63(self):
        """Podatnik wykonywał w okresie rozliczeniowym czynności, o których mowa
        w art. 120 ust. 4 lub 5 ustawy

        @returns int
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_PozycjeSzczegolowe:getP_63}
        # TODO: Fill in the actual data
        return 1
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {3cc34dcd}

    def getP_64(self):
        """Podatnik wykonywał w okresie rozliczeniowym czynności, o których mowa
        w art. 122 ustawy

        @returns int
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_PozycjeSzczegolowe:getP_64}
        # TODO: Fill in the actual data
        return 1
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {3cc34dcd}

    def getP_65(self):
        """Podatnik wykonywał w okresie rozliczeniowym czynności, o których mowa
        w art. 136 ustawy

        @returns int
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_PozycjeSzczegolowe:getP_65}
        # TODO: Fill in the actual data
        return 1
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {3cc34dcd}

    def getP_66(self):
        """Do niniejszej deklaracji dołączono Wniosek o zwrot podatku (VAT-ZZ):
        1 - tak, 2 - nie

        @returns int
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_PozycjeSzczegolowe:getP_66}
        # TODO: Fill in the actual data
        return 1
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {3cc34dcd}

    def getP_67(self):
        """Do niniejszej deklaracji dołączono Wniosek o przyspieszenie terminu
        zwrotu podatku (VAT-ZT): 1 - tak, 2 - nie

        @returns int
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_PozycjeSzczegolowe:getP_67}
        # TODO: Fill in the actual data
        return 1
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {3cc34dcd}

    def getP_68(self):
        """Do niniejszej deklaracji dołączono Zawiadomienie o skorygowaniu
        podstawy opodatkowania oraz kwoty podatku należnego (VAT-ZD): 1 - tak, 2
        - nie

        @returns int
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_PozycjeSzczegolowe:getP_68}
        # TODO: Fill in the actual data
        return 1
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {3cc34dcd}

    def getP_69(self):
        """Jeżeli w poz. 68 zaznaczono kwadrat nr 1, należy podać liczbę
        załączników VAT-ZD

        @returns int
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_PozycjeSzczegolowe:getP_69}
        # TODO: Fill in the actual data
        return 1
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {3cc34dcd}

    def getP_73(self):
        """Telefon kontaktowy

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_PozycjeSzczegolowe:getP_73}
        # TODO: Fill in the actual data
        return "P_73"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {ac5916ff}

    def getP_74(self):
        """Data wypełnienia

        @returns datetime.datetime
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_PozycjeSzczegolowe:getP_74}
        # TODO: Fill in the actual data
        return datetime.datetime.strptime('2016-08-01 00:00:00', '%Y-%m-%d %H:%M:%S')
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {15d9031f}


class Element_Deklaracja_Podmiot1(etd.TPodmiotDowolnyBezAdresu2):
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Deklaracja_Podmiot1}
    def __init__(self, *args, **kwargs):
        super(Element_Deklaracja_Podmiot1, self).__init__()
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {8cee6152}

    def getrola(self):
        """@returns string"""
        return "Podatnik"
