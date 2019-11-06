# Signature <<<cfc193be>>>
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
    """Nagłówek JPK_MAG"""
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
        """Data końcowa okresu, którego dotyczy JPK_MAG

        @returns datetime.datetime
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TNaglowek:getDataDo}
        # TODO: Fill in the actual data
        return datetime.datetime.strptime('1900-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {dcc88bf3}

    def getDataOd(self):
        """Data początkowa okresu, którego dotyczy JPK_MAG

        @returns datetime.datetime
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TNaglowek:getDataOd}
        # TODO: Fill in the actual data
        return datetime.datetime.strptime('1900-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {dcc88bf3}

    def getDataWytworzeniaJPK(self):
        """Data i czas wytworzenia JPK_MAG

        @returns datetime.datetime
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TNaglowek:getDataWytworzeniaJPK}
        # TODO: Fill in the actual data
        return datetime.datetime.strptime('2017-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {df3a3662}

    def getDomyslnyKodWaluty(self):
        """Trzyliterowy kod lokalnej waluty (ISO-4217), domyślny dla
        wytworzonego JPK_MAG

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
        return "JPK_MAG"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b6e5e688}

    def getkodSystemowy(self):
        """@returns string"""
        return "JPK_MAG (1)"

    def getwersjaSchemy(self):
        """@returns string"""
        return "1-0"


class Element_JPK(object):
    """Jednolity plik kontrolny dla obrotu magazynowego"""
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK}
    def __init__(self, document):
        """@param document odoo.addons.gal_jpk.models.Document"""
        self.document = document
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getMM(self):
        """Przesunięcia międzymagazynowe

        @returns Element_JPK_MM
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK:getMM}
        # TODO: Fill in the actual data
        return Element_JPK_MM()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {17a145b0}

    def getMagazyn(self):
        """Oznaczenie magazynu

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK:getMagazyn}
        # TODO: Fill in the actual data
        return "Magazyn"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {004158c9}

    def getNaglowek(self):
        """Nagłówek JPK_MAG

        @returns TNaglowek
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK:getNaglowek}
        # TODO: Fill in the actual data
        return TNaglowek()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {98f6a537}

    def getPZ(self):
        """Przyjęcie z zewnątrz

        @returns Element_JPK_PZ
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK:getPZ}
        # TODO: Fill in the actual data
        return Element_JPK_PZ()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {42b14f0a}

    def getPodmiot1(self):
        """@returns Element_JPK_Podmiot1"""
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK:getPodmiot1}
        # TODO: Fill in the actual data
        return Element_JPK_Podmiot1()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {1be705e0}

    def getRW(self):
        """Rozchód wewnętrzny

        @returns Element_JPK_RW
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK:getRW}
        # TODO: Fill in the actual data
        return Element_JPK_RW()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {9698d5e2}

    def getWZ(self):
        """Wydanie na zewnątrz

        @returns Element_JPK_WZ
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK:getWZ}
        # TODO: Fill in the actual data
        return Element_JPK_WZ()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {f6a928dd}

    def toXML(self):
        return xmlgen.bind(Namespace.elementBindings()['JPK'], self).toxml()


class Element_JPK_WZ(object):
    """Wydanie na zewnątrz"""
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_WZ}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getWZCtrl(self):
        """WZ -sumy kontrolne

        @returns Element_JPK_WZ_WZCtrl
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_WZ:getWZCtrl}
        # TODO: Fill in the actual data
        return Element_JPK_WZ_WZCtrl()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {f685d041}

    def getWZWartosc(self):
        """Zestawienie dowodów WZ

        @returns Element_JPK_WZ_WZWartosc[]
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_WZ:getWZWartosc}
        # TODO: Fill in the actual data
        return [Element_JPK_WZ_WZWartosc(), Element_JPK_WZ_WZWartosc()]
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {cb692206}

    def getWZWiersz(self):
        """Szczegółowe pozycje dowodów WZ

        @returns Element_JPK_WZ_WZWiersz[]
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_WZ:getWZWiersz}
        # TODO: Fill in the actual data
        return [Element_JPK_WZ_WZWiersz(), Element_JPK_WZ_WZWiersz()]
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {10cfc565}


class Element_JPK_WZ_WZWiersz(object):
    """Szczegółowe pozycje dowodów WZ"""
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_WZ_WZWiersz}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getCenaJednWZ(self):
        """Cena towaru/materiału/opakowania

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_WZ_WZWiersz:getCenaJednWZ}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getIloscWydanaWZ(self):
        """Ilość wydana

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_WZ_WZWiersz:getIloscWydanaWZ}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getJednostkaMiaryWZ(self):
        """Jednostka miary

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_WZ_WZWiersz:getJednostkaMiaryWZ}
        # TODO: Fill in the actual data
        return "JednostkaMiaryWZ"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {6c5f6f04}

    def getKodTowaruWZ(self):
        """Kod towaru/materiału/opakowania

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_WZ_WZWiersz:getKodTowaruWZ}
        # TODO: Fill in the actual data
        return "KodTowaruWZ"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {6775fd68}

    def getNazwaTowaruWZ(self):
        """Nazwa towaru/materiału/opakowania

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_WZ_WZWiersz:getNazwaTowaruWZ}
        # TODO: Fill in the actual data
        return "NazwaTowaruWZ"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {a3aff752}

    def getNumer2WZ(self):
        """Numer dokumentu WZ

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_WZ_WZWiersz:getNumer2WZ}
        # TODO: Fill in the actual data
        return "Numer2WZ"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {82001101}

    def getWartoscPozycjiWZ(self):
        """Wartość towaru/materiału/opakowania

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_WZ_WZWiersz:getWartoscPozycjiWZ}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}


class Element_JPK_WZ_WZWartosc(object):
    """Zestawienie dowodów WZ"""
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_WZ_WZWartosc}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getDataFaWZ(self):
        """Data faktury lub specyfikacji dotyczącej wydanego towaru/materiału

        @returns datetime.datetime
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_WZ_WZWartosc:getDataFaWZ}
        # TODO: Fill in the actual data
        return datetime.datetime.strptime('1900-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {dcc88bf3}

    def getDataWZ(self):
        """Data dokumentu WZ

        @returns datetime.datetime
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_WZ_WZWartosc:getDataWZ}
        # TODO: Fill in the actual data
        return datetime.datetime.strptime('1900-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {dcc88bf3}

    def getDataWydaniaWZ(self):
        """Data wydania towaru/materiału

        @returns datetime.datetime
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_WZ_WZWartosc:getDataWydaniaWZ}
        # TODO: Fill in the actual data
        return datetime.datetime.strptime('1900-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {dcc88bf3}

    def getNumerFaWZ(self):
        """Numer faktury lub specyfikacji dotyczącej wydanego towaru/materiału

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_WZ_WZWartosc:getNumerFaWZ}
        # TODO: Fill in the actual data
        return "NumerFaWZ"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {56774572}

    def getNumerWZ(self):
        """Numer dokumentu WZ

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_WZ_WZWartosc:getNumerWZ}
        # TODO: Fill in the actual data
        return "NumerWZ"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {311509fe}

    def getOdbiorcaWZ(self):
        """Odbiorca towaru/materiału

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_WZ_WZWartosc:getOdbiorcaWZ}
        # TODO: Fill in the actual data
        return "OdbiorcaWZ"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {63604cb9}

    def getWartoscWZ(self):
        """Wartość dokumentu WZ

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_WZ_WZWartosc:getWartoscWZ}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}


class Element_JPK_WZ_WZCtrl(object):
    """WZ -sumy kontrolne"""
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_WZ_WZCtrl}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getLiczbaWZ(self):
        """Liczba dokumentów WZ

        @returns long
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_WZ_WZCtrl:getLiczbaWZ}
        # TODO: Fill in the actual data
        return 1
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {3cc34dcd}

    def getSumaWZ(self):
        """Wartość dokumentów WZ

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_WZ_WZCtrl:getSumaWZ}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}


class Element_JPK_RW(object):
    """Rozchód wewnętrzny"""
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_RW}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getRWCtrl(self):
        """RW -sumy kontrolne

        @returns Element_JPK_RW_RWCtrl
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_RW:getRWCtrl}
        # TODO: Fill in the actual data
        return Element_JPK_RW_RWCtrl()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {e31efe13}

    def getRWWartosc(self):
        """Zestawienie dowodów RW

        @returns Element_JPK_RW_RWWartosc[]
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_RW:getRWWartosc}
        # TODO: Fill in the actual data
        return [Element_JPK_RW_RWWartosc(), Element_JPK_RW_RWWartosc()]
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {85061d15}

    def getRWWiersz(self):
        """Szczegółowe pozycje dowodów RW

        @returns Element_JPK_RW_RWWiersz[]
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_RW:getRWWiersz}
        # TODO: Fill in the actual data
        return [Element_JPK_RW_RWWiersz(), Element_JPK_RW_RWWiersz()]
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {2669fc1f}


class Element_JPK_RW_RWWiersz(object):
    """Szczegółowe pozycje dowodów RW"""
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_RW_RWWiersz}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getCenaJednRW(self):
        """Cena towaru/materiału/opakowania

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_RW_RWWiersz:getCenaJednRW}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getIloscWydanaRW(self):
        """Ilość wydana

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_RW_RWWiersz:getIloscWydanaRW}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getJednostkaMiaryRW(self):
        """Jednostka miary

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_RW_RWWiersz:getJednostkaMiaryRW}
        # TODO: Fill in the actual data
        return "JednostkaMiaryRW"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {3e5dff7c}

    def getKodTowaruRW(self):
        """Kod towaru/materiału/opakowania

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_RW_RWWiersz:getKodTowaruRW}
        # TODO: Fill in the actual data
        return "KodTowaruRW"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b174ffa5}

    def getNazwaTowaruRW(self):
        """Nazwa towaru/materiału/opakowania

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_RW_RWWiersz:getNazwaTowaruRW}
        # TODO: Fill in the actual data
        return "NazwaTowaruRW"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {04e027e4}

    def getNumer2RW(self):
        """Numer dokumentu RW

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_RW_RWWiersz:getNumer2RW}
        # TODO: Fill in the actual data
        return "Numer2RW"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {47fe5361}

    def getWartoscPozycjiRW(self):
        """Wartość towaru/materiału/opakowania

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_RW_RWWiersz:getWartoscPozycjiRW}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}


class Element_JPK_RW_RWWartosc(object):
    """Zestawienie dowodów RW"""
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_RW_RWWartosc}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getDataRW(self):
        """Data dokumentu RW

        @returns datetime.datetime
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_RW_RWWartosc:getDataRW}
        # TODO: Fill in the actual data
        return datetime.datetime.strptime('1900-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {dcc88bf3}

    def getDataWydaniaRW(self):
        """Data wydania towaru/materiału

        @returns datetime.datetime
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_RW_RWWartosc:getDataWydaniaRW}
        # TODO: Fill in the actual data
        return datetime.datetime.strptime('1900-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {dcc88bf3}

    def getDokadRW(self):
        """Miejsce przeznacznienia towaru/materiału

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_RW_RWWartosc:getDokadRW}
        # TODO: Fill in the actual data
        return "DokadRW"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {25163717}

    def getNumerRW(self):
        """Numer dokumentu RW

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_RW_RWWartosc:getNumerRW}
        # TODO: Fill in the actual data
        return "NumerRW"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {51605d05}

    def getSkadRW(self):
        """Miejsce wydania towaru/materiału

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_RW_RWWartosc:getSkadRW}
        # TODO: Fill in the actual data
        return "SkadRW"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {06e59c59}

    def getWartoscRW(self):
        """Wartość dokumentu RW

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_RW_RWWartosc:getWartoscRW}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}


class Element_JPK_RW_RWCtrl(object):
    """RW -sumy kontrolne"""
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_RW_RWCtrl}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getLiczbaRW(self):
        """Liczba dokumentów RW

        @returns long
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_RW_RWCtrl:getLiczbaRW}
        # TODO: Fill in the actual data
        return 1
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {3cc34dcd}

    def getSumaRW(self):
        """Wartość dokumentów RW

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_RW_RWCtrl:getSumaRW}
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


class Element_JPK_PZ(object):
    """Przyjęcie z zewnątrz"""
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_PZ}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getPZCtrl(self):
        """PZ -sumy kontrolne

        @returns Element_JPK_PZ_PZCtrl
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_PZ:getPZCtrl}
        # TODO: Fill in the actual data
        return Element_JPK_PZ_PZCtrl()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {4cd4b026}

    def getPZWartosc(self):
        """Zestawienie dowodów PZ

        @returns Element_JPK_PZ_PZWartosc[]
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_PZ:getPZWartosc}
        # TODO: Fill in the actual data
        return [Element_JPK_PZ_PZWartosc(), Element_JPK_PZ_PZWartosc()]
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b9ae8513}

    def getPZWiersz(self):
        """Szczegółowe pozycje dowodów PZ

        @returns Element_JPK_PZ_PZWiersz[]
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_PZ:getPZWiersz}
        # TODO: Fill in the actual data
        return [Element_JPK_PZ_PZWiersz(), Element_JPK_PZ_PZWiersz()]
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {4a234ee8}


class Element_JPK_PZ_PZWiersz(object):
    """Szczegółowe pozycje dowodów PZ"""
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_PZ_PZWiersz}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getCenaJednPZ(self):
        """Cena towaru/materiału/opakowania

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_PZ_PZWiersz:getCenaJednPZ}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getIloscPrzyjetaPZ(self):
        """Ilość przyjęta

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_PZ_PZWiersz:getIloscPrzyjetaPZ}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getJednostkaMiaryPZ(self):
        """Jednostka miary

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_PZ_PZWiersz:getJednostkaMiaryPZ}
        # TODO: Fill in the actual data
        return "JednostkaMiaryPZ"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {3e2f314a}

    def getKodTowaruPZ(self):
        """Kod towaru/materiału/opakowania

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_PZ_PZWiersz:getKodTowaruPZ}
        # TODO: Fill in the actual data
        return "KodTowaruPZ"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {42557602}

    def getNazwaTowaruPZ(self):
        """Nazwa towaru/materiału/opakowania

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_PZ_PZWiersz:getNazwaTowaruPZ}
        # TODO: Fill in the actual data
        return "NazwaTowaruPZ"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {6883806d}

    def getNumer2PZ(self):
        """Numer dokumentu PZ

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_PZ_PZWiersz:getNumer2PZ}
        # TODO: Fill in the actual data
        return "Numer2PZ"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {987adbf2}

    def getWartoscPozycjiPZ(self):
        """Wartość towaru/materiału/opakowania

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_PZ_PZWiersz:getWartoscPozycjiPZ}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}


class Element_JPK_PZ_PZWartosc(object):
    """Zestawienie dowodów PZ"""
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_PZ_PZWartosc}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getDataFaPZ(self):
        """Data faktury lub specyfikacji dotyczącej przyjętego towaru/materiału

        @returns datetime.datetime
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_PZ_PZWartosc:getDataFaPZ}
        # TODO: Fill in the actual data
        return datetime.datetime.strptime('1900-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {dcc88bf3}

    def getDataOtrzymaniaPZ(self):
        """Data otrzymania towaru/materiału

        @returns datetime.datetime
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_PZ_PZWartosc:getDataOtrzymaniaPZ}
        # TODO: Fill in the actual data
        return datetime.datetime.strptime('1900-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {dcc88bf3}

    def getDataPZ(self):
        """Data dokumentu PZ

        @returns datetime.datetime
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_PZ_PZWartosc:getDataPZ}
        # TODO: Fill in the actual data
        return datetime.datetime.strptime('1900-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {dcc88bf3}

    def getDostawca(self):
        """Dostawca towaru/materiału

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_PZ_PZWartosc:getDostawca}
        # TODO: Fill in the actual data
        return "Dostawca"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {cab8adf7}

    def getNumerFaPZ(self):
        """Numer faktury lub specyfikacji dotyczącej przyjętego towaru/materiału

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_PZ_PZWartosc:getNumerFaPZ}
        # TODO: Fill in the actual data
        return "NumerFaPZ"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {596c3fb4}

    def getNumerPZ(self):
        """Numer dokumentu PZ

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_PZ_PZWartosc:getNumerPZ}
        # TODO: Fill in the actual data
        return "NumerPZ"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {488159c7}

    def getWartoscPZ(self):
        """Wartość ogólna dokumentu PZ

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_PZ_PZWartosc:getWartoscPZ}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}


class Element_JPK_PZ_PZCtrl(object):
    """PZ -sumy kontrolne"""
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_PZ_PZCtrl}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getLiczbaPZ(self):
        """Liczba dokumentów PZ

        @returns long
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_PZ_PZCtrl:getLiczbaPZ}
        # TODO: Fill in the actual data
        return 1
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {3cc34dcd}

    def getSumaPZ(self):
        """Wartość dokumentów PZ

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_PZ_PZCtrl:getSumaPZ}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}


class Element_JPK_MM(object):
    """Przesunięcia międzymagazynowe"""
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_MM}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getMMCtrl(self):
        """MM -sumy kontrolne

        @returns Element_JPK_MM_MMCtrl
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_MM:getMMCtrl}
        # TODO: Fill in the actual data
        return Element_JPK_MM_MMCtrl()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {f7e8fb9f}

    def getMMWartosc(self):
        """Zestawienie dowodów MM

        @returns Element_JPK_MM_MMWartosc[]
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_MM:getMMWartosc}
        # TODO: Fill in the actual data
        return [Element_JPK_MM_MMWartosc(), Element_JPK_MM_MMWartosc()]
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {004246d2}

    def getMMWiersz(self):
        """Szczegółowe pozycje dowodów MM

        @returns Element_JPK_MM_MMWiersz[]
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_MM:getMMWiersz}
        # TODO: Fill in the actual data
        return [Element_JPK_MM_MMWiersz(), Element_JPK_MM_MMWiersz()]
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {88df082d}


class Element_JPK_MM_MMWiersz(object):
    """Szczegółowe pozycje dowodów MM"""
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_MM_MMWiersz}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getCenaJednMM(self):
        """Cena towaru/materiału/opakowania

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_MM_MMWiersz:getCenaJednMM}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getIloscWydanaMM(self):
        """Ilość wydana

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_MM_MMWiersz:getIloscWydanaMM}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getJednostkaMiaryMM(self):
        """Jednostka miary

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_MM_MMWiersz:getJednostkaMiaryMM}
        # TODO: Fill in the actual data
        return "JednostkaMiaryMM"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {8b0394d9}

    def getKodTowaruMM(self):
        """Kod towaru/materiału/opakowania

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_MM_MMWiersz:getKodTowaruMM}
        # TODO: Fill in the actual data
        return "KodTowaruMM"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {30f41ff8}

    def getNazwaTowaruMM(self):
        """Nazwa towaru/materiału/opakowania

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_MM_MMWiersz:getNazwaTowaruMM}
        # TODO: Fill in the actual data
        return "NazwaTowaruMM"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {6cf5e2d5}

    def getNumer2MM(self):
        """Numer dokumentu MM

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_MM_MMWiersz:getNumer2MM}
        # TODO: Fill in the actual data
        return "Numer2MM"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {4a6dbc7d}

    def getWartoscPozycjiMM(self):
        """Wartość towaru/materiału/opakowania

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_MM_MMWiersz:getWartoscPozycjiMM}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}


class Element_JPK_MM_MMWartosc(object):
    """Zestawienie dowodów MM"""
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_MM_MMWartosc}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getDataMM(self):
        """Data dokumentu MM

        @returns datetime.datetime
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_MM_MMWartosc:getDataMM}
        # TODO: Fill in the actual data
        return datetime.datetime.strptime('1900-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {dcc88bf3}

    def getDataWydaniaMM(self):
        """Data wydania towaru/materiału

        @returns datetime.datetime
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_MM_MMWartosc:getDataWydaniaMM}
        # TODO: Fill in the actual data
        return datetime.datetime.strptime('1900-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {dcc88bf3}

    def getDokadMM(self):
        """Miejsce przeznacznienia towaru/materiału

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_MM_MMWartosc:getDokadMM}
        # TODO: Fill in the actual data
        return "DokadMM"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {ea741c04}

    def getNumerMM(self):
        """Numer dokumentu MM

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_MM_MMWartosc:getNumerMM}
        # TODO: Fill in the actual data
        return "NumerMM"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {668ad0e6}

    def getSkadMM(self):
        """Miejsce wydania towaru/materiału

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_MM_MMWartosc:getSkadMM}
        # TODO: Fill in the actual data
        return "SkadMM"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {3b0d3ca5}

    def getWartoscMM(self):
        """Wartość dokumentu MM

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_MM_MMWartosc:getWartoscMM}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}


class Element_JPK_MM_MMCtrl(object):
    """MM -sumy kontrolne"""
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_MM_MMCtrl}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getLiczbaMM(self):
        """Liczba dokumentów MM

        @returns long
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_MM_MMCtrl:getLiczbaMM}
        # TODO: Fill in the actual data
        return 1
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {3cc34dcd}

    def getSumaMM(self):
        """Wartość dokumentów MM

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_MM_MMCtrl:getSumaMM}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}
