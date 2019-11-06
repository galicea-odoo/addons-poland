# Signature <<<703247a5>>>
# -*- coding: utf-8 -*-

import decimal
import datetime
from .bindings import Namespace
from xsd2xml import xmlgen
from ..http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy_ import models as etd
# vvv ONLY EDIT CODE BELOW THIS LINE vvv {imports}
# ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {ecf8427e}

class TNaglowek_ORD__ZU(object):
    """Nagłówek deklaracji"""
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TNaglowek_ORD__ZU}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getKodFormularza(self):
        """@returns TNaglowek_ORD__ZU_KodFormularza"""
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TNaglowek_ORD__ZU:getKodFormularza}
        # TODO: Fill in the actual data
        return TNaglowek_ORD__ZU_KodFormularza()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {dfd58bb7}

    def getWariantFormularza(self):
        """@returns int"""
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TNaglowek_ORD__ZU:getWariantFormularza}
        # TODO: Fill in the actual data
        return 3
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {cf23ef9c}


class TNaglowek_ORD__ZU_KodFormularza(object):
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TNaglowek_ORD__ZU_KodFormularza}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getContent(self):
        """XML Element Content

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TNaglowek_ORD__ZU_KodFormularza:getContent}
        # TODO: Fill in the actual data
        return "ORD-ZU"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {3e1fe979}

    def getkodSystemowy(self):
        """@returns string"""
        return "ORD-ZU (3)"

    def getwersjaSchemy(self):
        """@returns string"""
        return "1-0E"


class Element_Zalacznik_ORD__ZU(object):
    """UZASADNIENIE PRZYCZYN KOREKTY DEKLARACJI"""
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Zalacznik_ORD__ZU}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getNaglowek(self):
        """@returns TNaglowek_ORD__ZU"""
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Zalacznik_ORD__ZU:getNaglowek}
        # TODO: Fill in the actual data
        return TNaglowek_ORD__ZU()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {6c1f451e}

    def getPozycjeSzczegolowe(self):
        """@returns Element_Zalacznik_ORD__ZU_PozycjeSzczegolowe"""
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Zalacznik_ORD__ZU:getPozycjeSzczegolowe}
        # TODO: Fill in the actual data
        return Element_Zalacznik_ORD__ZU_PozycjeSzczegolowe()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {83c037fb}

    def toXML(self):
        return xmlgen.bind(Namespace.elementBindings()['Zalacznik_ORD-ZU'], self).toxml()


class Element_Zalacznik_ORD__ZU_PozycjeSzczegolowe(object):
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Zalacznik_ORD__ZU_PozycjeSzczegolowe}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getP_13(self):
        """Treść uzasadnienia

        @returns Element_Zalacznik_ORD__ZU_PozycjeSzczegolowe_P_13
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Zalacznik_ORD__ZU_PozycjeSzczegolowe:getP_13}
        # TODO: Fill in the actual data
        return Element_Zalacznik_ORD__ZU_PozycjeSzczegolowe_P_13()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {ddcf4444}


class Element_Zalacznik_ORD__ZU_PozycjeSzczegolowe_P_13(object):
    """Treść uzasadnienia"""
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Zalacznik_ORD__ZU_PozycjeSzczegolowe_P_13}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getContent(self):
        """XML Element Content

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_Zalacznik_ORD__ZU_PozycjeSzczegolowe_P_13:getContent}
        # TODO: Fill in the actual data
        return "Element_Zalacznik_ORD__ZU_PozycjeSzczegolowe_P_13"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {cc0e5f78}
