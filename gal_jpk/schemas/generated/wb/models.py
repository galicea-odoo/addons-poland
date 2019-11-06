# Signature <<<71b403f9>>>
# -*- coding: utf-8 -*-

import decimal
import datetime
from .bindings import Namespace
from xsd2xml import xmlgen
from ..http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy_ import models as etd
from ..http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2013_05_23_eD_KodyCECHKRAJOW_ import models as kck
# vvv ONLY EDIT CODE BELOW THIS LINE vvv {imports}
# ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {ecf8427e}

class TNaglowek(object):
    """Nagłówek JPK_WB"""
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TNaglowek}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getCelZlozenia(self):
        """@returns int"""
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TNaglowek:getCelZlozenia}
        # TODO: Fill in the actual data
        return 1
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {3cc34dcd}

    def getDataDo(self):
        """Data końcowa okresu, którego dotyczy JPK_WB

        @returns datetime.datetime
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TNaglowek:getDataDo}
        # TODO: Fill in the actual data
        return datetime.datetime.strptime('1900-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {dcc88bf3}

    def getDataOd(self):
        """Data początkowa okresu, którego dotyczy JPK_WB

        @returns datetime.datetime
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TNaglowek:getDataOd}
        # TODO: Fill in the actual data
        return datetime.datetime.strptime('1900-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {dcc88bf3}

    def getDataWytworzeniaJPK(self):
        """Data i czas wytworzenia JPK_WB

        @returns datetime.datetime
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TNaglowek:getDataWytworzeniaJPK}
        # TODO: Fill in the actual data
        return datetime.datetime.strptime('2017-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {df3a3662}

    def getDomyslnyKodWaluty(self):
        """Trzyliterowy kod lokalnej waluty (ISO-4217), domyślny dla
        wytworzonego JPK_WB

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TNaglowek:getDomyslnyKodWaluty}
        # TODO: Fill in the actual data
        return "AED"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {38f462e0}

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

    def getWariantFormularza(self):
        """@returns int"""
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TNaglowek:getWariantFormularza}
        # TODO: Fill in the actual data
        return 1
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {3cc34dcd}


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
        return "JPK_WB"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {611e244c}

    def getkodSystemowy(self):
        """@returns string"""
        return "JPK_WB (1)"

    def getwersjaSchemy(self):
        """@returns string"""
        return "1-0"


class Element_JPK(object):
    """Jednolity plik kontrolny dla wyciągu bankowego"""
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK}
    def __init__(self, document):
        """@param document odoo.addons.gal_jpk.models.Document"""
        self.document = document
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getNaglowek(self):
        """Nagłówek JPK_WB

        @returns TNaglowek
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK:getNaglowek}
        # TODO: Fill in the actual data
        return TNaglowek()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {98f6a537}

    def getNumerRachunku(self):
        """Numer IBAN rachunku, którego dotyczy wyciąg

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK:getNumerRachunku}
        # TODO: Fill in the actual data
        return "TK54AHLWIARM9WZTWBQWOG3FLWYHV9"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {67314a5f}

    def getPodmiot1(self):
        """@returns Element_JPK_Podmiot1"""
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK:getPodmiot1}
        # TODO: Fill in the actual data
        return Element_JPK_Podmiot1()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {1be705e0}

    def getSalda(self):
        """Salda wyciągu

        @returns Element_JPK_Salda
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK:getSalda}
        # TODO: Fill in the actual data
        return Element_JPK_Salda()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {ad4c5512}

    def getWyciagCtrl(self):
        """Sumy kontrolne dla wyciągu bankowego

        @returns Element_JPK_WyciagCtrl
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK:getWyciagCtrl}
        # TODO: Fill in the actual data
        return Element_JPK_WyciagCtrl()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {e43c80dc}

    def getWyciagWiersz(self):
        """Szczegółowe wiersze (zapisy) wyciągu bankowego

        @returns Element_JPK_WyciagWiersz[]
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK:getWyciagWiersz}
        # TODO: Fill in the actual data
        return [Element_JPK_WyciagWiersz(), Element_JPK_WyciagWiersz()]
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {00b2a706}

    def toXML(self):
        return xmlgen.bind(Namespace.elementBindings()['JPK'], self).toxml()


class Element_JPK_WyciagWiersz(object):
    """Szczegółowe wiersze (zapisy) wyciągu bankowego"""
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_WyciagWiersz}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getDataOperacji(self):
        """Data operacji

        @returns datetime.datetime
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_WyciagWiersz:getDataOperacji}
        # TODO: Fill in the actual data
        return datetime.datetime.strptime('1900-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {dcc88bf3}

    def getKwotaOperacji(self):
        """Kwota operacji

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_WyciagWiersz:getKwotaOperacji}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getNazwaPodmiotu(self):
        """Nazwa podmiotu będącego stroną operacji

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_WyciagWiersz:getNazwaPodmiotu}
        # TODO: Fill in the actual data
        return "NazwaPodmiotu"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {0fa186be}

    def getNumerWiersza(self):
        """Kolejny numer wiersza (zapisu) wyciągu

        @returns long
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_WyciagWiersz:getNumerWiersza}
        # TODO: Fill in the actual data
        return 1
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {3cc34dcd}

    def getOpisOperacji(self):
        """Opis operacji/transakcji

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_WyciagWiersz:getOpisOperacji}
        # TODO: Fill in the actual data
        return "OpisOperacji"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {51ba20c3}

    def getSaldoOperacji(self):
        """Saldo operacji

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_WyciagWiersz:getSaldoOperacji}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def gettyp(self):
        """@returns string"""
        return "G"


class Element_JPK_WyciagCtrl(object):
    """Sumy kontrolne dla wyciągu bankowego"""
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_WyciagCtrl}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getLiczbaWierszy(self):
        """Liczba wierszy wyciągu bankowego, w okresie którego dotyczy wyciąg

        @returns long
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_WyciagCtrl:getLiczbaWierszy}
        # TODO: Fill in the actual data
        return 1
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {3cc34dcd}

    def getSumaObciazen(self):
        """Suma kwot obciążeń rachunku w okresie, którego dotyczy wyciąg

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_WyciagCtrl:getSumaObciazen}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getSumaUznan(self):
        """Suma kwot uznań rachunku w okresie, którego dotyczy wyciąg

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_WyciagCtrl:getSumaUznan}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}


class Element_JPK_Salda(object):
    """Salda wyciągu"""
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_Salda}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getSaldoKoncowe(self):
        """Saldo końcowe wyciągu

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_Salda:getSaldoKoncowe}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getSaldoPoczatkowe(self):
        """Saldo początkowe wyciągu

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_Salda:getSaldoPoczatkowe}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}


class Element_JPK_Podmiot1(object):
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_Podmiot1}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getAdresPodmiotu(self):
        """Adres podmiotu

        @returns etd.TAdresPolski
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_Podmiot1:getAdresPodmiotu}
        # TODO: Fill in the actual data
        return etd.TAdresPolski()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {e38984d4}

    def getIdentyfikatorPodmiotu(self):
        """Dane identyfikujące podmiot

        @returns etd.TIdentyfikatorOsobyNiefizycznej
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_Podmiot1:getIdentyfikatorPodmiotu}
        # TODO: Fill in the actual data
        return etd.TIdentyfikatorOsobyNiefizycznej()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {429b9b00}
