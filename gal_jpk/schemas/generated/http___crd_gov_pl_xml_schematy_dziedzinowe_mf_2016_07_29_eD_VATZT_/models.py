# Signature <<<e71ec65b>>>
# -*- coding: utf-8 -*-

import decimal
import datetime
from .bindings import Namespace
from xsd2xml import xmlgen
from ..http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy_ import models as etd
# vvv ONLY EDIT CODE BELOW THIS LINE vvv {imports}
# ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {ecf8427e}

class TNaglowek_VAT__ZT(object):
    """Nagłówek deklaracji"""
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TNaglowek_VAT__ZT}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getKodFormularza(self):
        """@returns TNaglowek_VAT__ZT_KodFormularza"""
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TNaglowek_VAT__ZT:getKodFormularza}
        # TODO: Fill in the actual data
        return TNaglowek_VAT__ZT_KodFormularza()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {6d621fd0}

    def getWariantFormularza(self):
        """@returns int"""
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TNaglowek_VAT__ZT:getWariantFormularza}
        # TODO: Fill in the actual data
        return 5
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {3fb1756a}


class TNaglowek_VAT__ZT_KodFormularza(object):
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TNaglowek_VAT__ZT_KodFormularza}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getContent(self):
        """XML Element Content

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TNaglowek_VAT__ZT_KodFormularza:getContent}
        # TODO: Fill in the actual data
        return "VAT-ZT"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c1e3626c}

    def getkodSystemowy(self):
        """@returns string"""
        return "VAT-ZT (5)"

    def getwersjaSchemy(self):
        """@returns string"""
        return "2-0E"


class Element_Wniosek_VAT__ZT(object):
    """WNIOSEK O PRZYSPIESZENIE TERMINU ZWROTU PODATKU"""
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Wniosek_VAT__ZT}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getNaglowek(self):
        """@returns TNaglowek_VAT__ZT"""
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Wniosek_VAT__ZT:getNaglowek}
        # TODO: Fill in the actual data
        return TNaglowek_VAT__ZT()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {0f87be10}

    def getPozycjeSzczegolowe(self):
        """@returns Element_Wniosek_VAT__ZT_PozycjeSzczegolowe"""
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Wniosek_VAT__ZT:getPozycjeSzczegolowe}
        # TODO: Fill in the actual data
        return Element_Wniosek_VAT__ZT_PozycjeSzczegolowe()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {6a17435b}

    def toXML(self):
        return xmlgen.bind(Namespace.elementBindings()['Wniosek_VAT-ZT'], self).toxml()


class Element_Wniosek_VAT__ZT_PozycjeSzczegolowe(object):
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Wniosek_VAT__ZT_PozycjeSzczegolowe}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getP_10(self):
        """Kwota do zwrotu w terminie 25 dni, o której przyspieszenie wnioskuje
        podatnik

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Wniosek_VAT__ZT_PozycjeSzczegolowe:getP_10}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getP_11(self):
        """Uzasadnienie wniosku

        @returns Element_Wniosek_VAT__ZT_PozycjeSzczegolowe_P_11
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Wniosek_VAT__ZT_PozycjeSzczegolowe:getP_11}
        # TODO: Fill in the actual data
        return Element_Wniosek_VAT__ZT_PozycjeSzczegolowe_P_11()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {f9efe2bf}


class Element_Wniosek_VAT__ZT_PozycjeSzczegolowe_P_11(object):
    """Uzasadnienie wniosku"""
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Wniosek_VAT__ZT_PozycjeSzczegolowe_P_11}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getContent(self):
        """XML Element Content

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Wniosek_VAT__ZT_PozycjeSzczegolowe_P_11:getContent}
        # TODO: Fill in the actual data
        return "Element_Wniosek_VAT__ZT_PozycjeSzczegolowe_P_11"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {7f72d749}
