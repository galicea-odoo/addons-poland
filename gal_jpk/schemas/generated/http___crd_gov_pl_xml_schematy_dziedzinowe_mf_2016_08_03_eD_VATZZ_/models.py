# Signature <<<74091d2b>>>
# -*- coding: utf-8 -*-

import decimal
import datetime
from .bindings import Namespace
from xsd2xml import xmlgen
from ..http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy_ import models as etd
# vvv ONLY EDIT CODE BELOW THIS LINE vvv {imports}
# ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {ecf8427e}

class TNaglowek_VAT__ZZ(object):
    """Nagłówek deklaracji"""
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TNaglowek_VAT__ZZ}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getKodFormularza(self):
        """@returns TNaglowek_VAT__ZZ_KodFormularza"""
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TNaglowek_VAT__ZZ:getKodFormularza}
        # TODO: Fill in the actual data
        return TNaglowek_VAT__ZZ_KodFormularza()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {f0bc7b41}

    def getWariantFormularza(self):
        """@returns int"""
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TNaglowek_VAT__ZZ:getWariantFormularza}
        # TODO: Fill in the actual data
        return 5
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {3fb1756a}


class TNaglowek_VAT__ZZ_KodFormularza(object):
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TNaglowek_VAT__ZZ_KodFormularza}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getContent(self):
        """XML Element Content

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TNaglowek_VAT__ZZ_KodFormularza:getContent}
        # TODO: Fill in the actual data
        return "VAT-ZZ"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {feac6a68}

    def getkodSystemowy(self):
        """@returns string"""
        return "VAT-ZZ (5)"

    def getwersjaSchemy(self):
        """@returns string"""
        return "2-1E"


class Element_Wniosek_VAT__ZZ(object):
    """WNIOSEK O ZWROT PODATKU VAT"""
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Wniosek_VAT__ZZ}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getNaglowek(self):
        """@returns TNaglowek_VAT__ZZ"""
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Wniosek_VAT__ZZ:getNaglowek}
        # TODO: Fill in the actual data
        return TNaglowek_VAT__ZZ()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {47dcfe5b}

    def getPozycjeSzczegolowe(self):
        """@returns Element_Wniosek_VAT__ZZ_PozycjeSzczegolowe"""
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Wniosek_VAT__ZZ:getPozycjeSzczegolowe}
        # TODO: Fill in the actual data
        return Element_Wniosek_VAT__ZZ_PozycjeSzczegolowe()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {21a653c8}

    def toXML(self):
        return xmlgen.bind(Namespace.elementBindings()['Wniosek_VAT-ZZ'], self).toxml()


class Element_Wniosek_VAT__ZZ_PozycjeSzczegolowe(object):
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Wniosek_VAT__ZZ_PozycjeSzczegolowe}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getP_10(self):
        """Uzasadnienie złożenia wniosku

        @returns Element_Wniosek_VAT__ZZ_PozycjeSzczegolowe_P_10
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Wniosek_VAT__ZZ_PozycjeSzczegolowe:getP_10}
        # TODO: Fill in the actual data
        return Element_Wniosek_VAT__ZZ_PozycjeSzczegolowe_P_10()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b3182797}

    def getP_8(self):
        """Powód zwrotu

        @returns int
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Wniosek_VAT__ZZ_PozycjeSzczegolowe:getP_8}
        # TODO: Fill in the actual data
        return 1
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {3cc34dcd}

    def getP_9(self):
        """Wnioskowana kwota podatku do zwrotu

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Wniosek_VAT__ZZ_PozycjeSzczegolowe:getP_9}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}


class Element_Wniosek_VAT__ZZ_PozycjeSzczegolowe_P_10(object):
    """Uzasadnienie złożenia wniosku"""
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Wniosek_VAT__ZZ_PozycjeSzczegolowe_P_10}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getContent(self):
        """XML Element Content

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Wniosek_VAT__ZZ_PozycjeSzczegolowe_P_10:getContent}
        # TODO: Fill in the actual data
        return "Element_Wniosek_VAT__ZZ_PozycjeSzczegolowe_P_10"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {8bf4e427}
