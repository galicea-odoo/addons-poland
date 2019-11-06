# Signature <<<eb985a96>>>
# -*- coding: utf-8 -*-

import decimal
import datetime
from .bindings import Namespace
from xsd2xml import xmlgen
from ..http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy_ import models as etd
# vvv ONLY EDIT CODE BELOW THIS LINE vvv {imports}
# ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {ecf8427e}

class TNaglowek_VAT__ZD(object):
    """Nagłówek deklaracji"""
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TNaglowek_VAT__ZD}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getKodFormularza(self):
        """@returns TNaglowek_VAT__ZD_KodFormularza"""
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TNaglowek_VAT__ZD:getKodFormularza}
        # TODO: Fill in the actual data
        return TNaglowek_VAT__ZD_KodFormularza()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {ed7d770f}

    def getWariantFormularza(self):
        """@returns int"""
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TNaglowek_VAT__ZD:getWariantFormularza}
        # TODO: Fill in the actual data
        return 1
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {3cc34dcd}


class TNaglowek_VAT__ZD_KodFormularza(object):
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TNaglowek_VAT__ZD_KodFormularza}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getContent(self):
        """XML Element Content

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TNaglowek_VAT__ZD_KodFormularza:getContent}
        # TODO: Fill in the actual data
        return "VAT-ZD"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {d4b4373a}

    def getkodSystemowy(self):
        """@returns string"""
        return "VAT-ZD (1)"

    def getwersjaSchemy(self):
        """@returns string"""
        return "2-0E"


class Element_Wniosek_VAT__ZD(object):
    """ZAWIADOMIENIE O SKORYGOWANIU PODSTAWY OPODATKOWANIA ORAZ KWOTY PODATKU
    NALEŻNEGO
    """
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Wniosek_VAT__ZD}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getNaglowek(self):
        """@returns TNaglowek_VAT__ZD"""
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Wniosek_VAT__ZD:getNaglowek}
        # TODO: Fill in the actual data
        return TNaglowek_VAT__ZD()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {ff38a6a6}

    def getPozycjeSzczegolowe(self):
        """Dane identyfikacyjne dłużnika oraz informacje dotyczące kwot korekty
        podstawy opodatkowania oraz podatku należnego

        @returns Element_Wniosek_VAT__ZD_PozycjeSzczegolowe
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Wniosek_VAT__ZD:getPozycjeSzczegolowe}
        # TODO: Fill in the actual data
        return Element_Wniosek_VAT__ZD_PozycjeSzczegolowe()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {8f51f1cb}

    def toXML(self):
        return xmlgen.bind(Namespace.elementBindings()['Wniosek_VAT-ZD'], self).toxml()


class Element_Wniosek_VAT__ZD_PozycjeSzczegolowe(object):
    """Dane identyfikacyjne dłużnika oraz informacje dotyczące kwot korekty
    podstawy opodatkowania oraz podatku należnego
    """
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Wniosek_VAT__ZD_PozycjeSzczegolowe}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getP_10(self):
        """Ogółem kwota korekty podstawy opodatkowania

        @returns long
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Wniosek_VAT__ZD_PozycjeSzczegolowe:getP_10}
        # TODO: Fill in the actual data
        return 0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {e3b5de26}

    def getP_11(self):
        """Ogółem kwota korekty podatku należnego

        @returns long
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Wniosek_VAT__ZD_PozycjeSzczegolowe:getP_11}
        # TODO: Fill in the actual data
        return 0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {e3b5de26}

    def getP_B(self):
        """@returns Element_Wniosek_VAT__ZD_PozycjeSzczegolowe_P_B[]"""
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Wniosek_VAT__ZD_PozycjeSzczegolowe:getP_B}
        # TODO: Fill in the actual data
        return [Element_Wniosek_VAT__ZD_PozycjeSzczegolowe_P_B(), Element_Wniosek_VAT__ZD_PozycjeSzczegolowe_P_B()]
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {be6a9baf}


class Element_Wniosek_VAT__ZD_PozycjeSzczegolowe_P_B(object):
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Wniosek_VAT__ZD_PozycjeSzczegolowe_P_B}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getP_BB(self):
        """Nazwa podatnika (dłużnika)

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Wniosek_VAT__ZD_PozycjeSzczegolowe_P_B:getP_BB}
        # TODO: Fill in the actual data
        return "P_BB"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {51fc8e0e}

    def getP_BC(self):
        """Identyfikator podatkowy NIP podatnika (dłużnika)

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Wniosek_VAT__ZD_PozycjeSzczegolowe_P_B:getP_BC}
        # TODO: Fill in the actual data
        return "8424734595"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {fff228e5}

    def getP_BD1(self):
        """Nr faktury

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Wniosek_VAT__ZD_PozycjeSzczegolowe_P_B:getP_BD1}
        # TODO: Fill in the actual data
        return "P_BD1"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {199d8f02}

    def getP_BD2(self):
        """Data wystawienia faktury

        @returns datetime.datetime
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Wniosek_VAT__ZD_PozycjeSzczegolowe_P_B:getP_BD2}
        # TODO: Fill in the actual data
        return datetime.datetime.strptime('2011-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {7ec3083e}

    def getP_BE(self):
        """Data upływu terminu płatności określonego w fakturze lub umowie

        @returns datetime.datetime
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Wniosek_VAT__ZD_PozycjeSzczegolowe_P_B:getP_BE}
        # TODO: Fill in the actual data
        return datetime.datetime.strptime('2011-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {7ec3083e}

    def getP_BF(self):
        """Kwota korekty podstawy opodatkowania

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Wniosek_VAT__ZD_PozycjeSzczegolowe_P_B:getP_BF}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getP_BG(self):
        """Kwota korekty podatku należnego

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Wniosek_VAT__ZD_PozycjeSzczegolowe_P_B:getP_BG}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def gettyp(self):
        """@returns string"""
        return "G"
