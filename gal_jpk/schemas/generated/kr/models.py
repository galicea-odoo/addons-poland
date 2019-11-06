# Signature <<<184e4f7a>>>
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
    """Nagłówek JPK_KR"""
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
        """Data końcowa okresu, którego dotyczy JPK_KR

        @returns datetime.datetime
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TNaglowek:getDataDo}
        # TODO: Fill in the actual data
        return datetime.datetime.strptime('1900-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {dcc88bf3}

    def getDataOd(self):
        """Data początkowa okresu, którego dotyczy JPK_KR

        @returns datetime.datetime
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TNaglowek:getDataOd}
        # TODO: Fill in the actual data
        return datetime.datetime.strptime('1900-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {dcc88bf3}

    def getDataWytworzeniaJPK(self):
        """Data i czas wytworzenia JPK_KR

        @returns datetime.datetime
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {TNaglowek:getDataWytworzeniaJPK}
        # TODO: Fill in the actual data
        return datetime.datetime.strptime('2017-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {df3a3662}

    def getDomyslnyKodWaluty(self):
        """Trzyliterowy kod lokalnej waluty (ISO-4217), domyślny dla
        wytworzonego JPK_KR

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
        return "JPK_KR"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c72a095b}

    def getkodSystemowy(self):
        """@returns string"""
        return "JPK_KR (1)"

    def getwersjaSchemy(self):
        """@returns string"""
        return "1-0"


class Element_JPK(object):
    """Jednolity plik kontrolny dla ksiąg rachunkowych"""
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getDziennik(self):
        """Dziennik

        @returns Element_JPK_Dziennik[]
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK:getDziennik}
        # TODO: Fill in the actual data
        return [Element_JPK_Dziennik(), Element_JPK_Dziennik()]
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {1a385449}

    def getDziennikCtrl(self):
        """Sumy kontrolne dla tabeli Dziennik

        @returns Element_JPK_DziennikCtrl
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK:getDziennikCtrl}
        # TODO: Fill in the actual data
        return Element_JPK_DziennikCtrl()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c8186cd7}

    def getKontoZapis(self):
        """Zapisy na kontach księgi głównej i ksiąg pomocniczych

        @returns Element_JPK_KontoZapis[]
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK:getKontoZapis}
        # TODO: Fill in the actual data
        return [Element_JPK_KontoZapis(), Element_JPK_KontoZapis()]
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {618c7069}

    def getKontoZapisCtrl(self):
        """Sumy kontrolne dla tabeli KontoZapis

        @returns Element_JPK_KontoZapisCtrl
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK:getKontoZapisCtrl}
        # TODO: Fill in the actual data
        return Element_JPK_KontoZapisCtrl()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {37713252}

    def getNaglowek(self):
        """Nagłówek JPK_KR

        @returns TNaglowek
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK:getNaglowek}
        # TODO: Fill in the actual data
        return TNaglowek()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {98f6a537}

    def getPodmiot1(self):
        """@returns Element_JPK_Podmiot1"""
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK:getPodmiot1}
        # TODO: Fill in the actual data
        return Element_JPK_Podmiot1()
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {1be705e0}

    def getZOiS(self):
        """Zestawienie obrotów i sald

        @returns Element_JPK_ZOiS[]
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK:getZOiS}
        # TODO: Fill in the actual data
        return [Element_JPK_ZOiS(), Element_JPK_ZOiS()]
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {93602453}

    def toXML(self):
        return xmlgen.bind(Namespace.elementBindings()['JPK'], self).toxml()


class Element_JPK_ZOiS(object):
    """Zestawienie obrotów i sald"""
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_ZOiS}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getBilansOtwarciaMa(self):
        """Bilans otwarcia po stronie Ma w walucie polskiej

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_ZOiS:getBilansOtwarciaMa}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getBilansOtwarciaWinien(self):
        """Bilans otwarcia po stronie Winien w walucie polskiej

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_ZOiS:getBilansOtwarciaWinien}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getKodKategorii(self):
        """Kod kategorii konta według Zespołu Kont Syntetycznych (kont księgi
        głównej)

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_ZOiS:getKodKategorii}
        # TODO: Fill in the actual data
        return "KodKategorii"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {23be1bf2}

    def getKodKonta(self):
        """Identyfikator konta ostatecznego zapisu (konta pomocniczego lub konta
        księgi głównej, jeżeli nie jest wymagany zapis na kontach pomocniczych)

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_ZOiS:getKodKonta}
        # TODO: Fill in the actual data
        return "KodKonta"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {bb47d49b}

    def getKodPodkategorii(self):
        """Kod podkategorii konta ksiąg pomocniczych w ramach poszczególnej
        kategorii Zespołu Kont Syntetycznych

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_ZOiS:getKodPodkategorii}
        # TODO: Fill in the actual data
        return "KodPodkategorii"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c191f779}

    def getKodZespolu(self):
        """Kod zespołu kont wg Wykazu Kont Syntetycznych (kont księgi głównej)

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_ZOiS:getKodZespolu}
        # TODO: Fill in the actual data
        return "KodZespolu"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {1078fa88}

    def getObrotyMa(self):
        """Obroty konta po stronie Ma, w okresie którego dotyczy JPK

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_ZOiS:getObrotyMa}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getObrotyMaNarast(self):
        """Obroty konta po stronie Ma, w okresie od otwarcia ksiąg do daty
        końcowej okresu, którego dotyczy JPK

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_ZOiS:getObrotyMaNarast}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getObrotyWinien(self):
        """Obroty konta po stronie Winien, w okresie którego dotyczy JPK

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_ZOiS:getObrotyWinien}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getObrotyWinienNarast(self):
        """Obroty konta po stronie Winien, w okresie od otwarcia ksiąg do daty
        końcowej okresu, którego dotyczy JPK

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_ZOiS:getObrotyWinienNarast}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getOpisKategorii(self):
        """Nazwa kategorii konta

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_ZOiS:getOpisKategorii}
        # TODO: Fill in the actual data
        return "OpisKategorii"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {14115afb}

    def getOpisKonta(self):
        """Nazwa konta

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_ZOiS:getOpisKonta}
        # TODO: Fill in the actual data
        return "OpisKonta"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {adadb9e9}

    def getOpisPodkategorii(self):
        """Nazwa podkategorii konta

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_ZOiS:getOpisPodkategorii}
        # TODO: Fill in the actual data
        return "OpisPodkategorii"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {cdbf3331}

    def getOpisZespolu(self):
        """Opis zespołu kont

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_ZOiS:getOpisZespolu}
        # TODO: Fill in the actual data
        return "OpisZespolu"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b8c71176}

    def getSaldoMa(self):
        """Saldo po stronie Ma w walucie polskiej na datę końcową okresu,
        którego dotyczy JPK z uwzlędnieniem bilansu otwarcia

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_ZOiS:getSaldoMa}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getSaldoWinien(self):
        """Saldo po stronie Winien w walucie polskiej na datę końcową okresu,
        którego dotyczy JPK z uwzględnieniem bilansu otwarcia

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_ZOiS:getSaldoWinien}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getTypKonta(self):
        """Typ konta (bilansowe, pozabilansowe, rozliczeniowe lub wynikowe)

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_ZOiS:getTypKonta}
        # TODO: Fill in the actual data
        return "TypKonta"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {d361bb08}

    def gettyp(self):
        """@returns string"""
        return "G"


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


class Element_JPK_KontoZapisCtrl(object):
    """Sumy kontrolne dla tabeli KontoZapis"""
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_KontoZapisCtrl}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getLiczbaWierszyKontoZapisj(self):
        """Liczba zapisów tabeli KontoZapis

        @returns long
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_KontoZapisCtrl:getLiczbaWierszyKontoZapisj}
        # TODO: Fill in the actual data
        return 1
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {3cc34dcd}

    def getSumaMa(self):
        """Suma wartości wierszy (zapisów) po stronie Ma (elementu KwotaMa)

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_KontoZapisCtrl:getSumaMa}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getSumaWinien(self):
        """Suma wartości wierszy (zapisów) po stronie Winien (elementu
        KwotaWinien)

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_KontoZapisCtrl:getSumaWinien}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}


class Element_JPK_KontoZapis(object):
    """Zapisy na kontach księgi głównej i ksiąg pomocniczych"""
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_KontoZapis}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getKodKontaMa(self):
        """Identyfikator konta zapisu (konta pomocniczego lub konta księgi
        głównej, jeżeli nie jest wymagany zapis na kontach pomocniczych) dla
        zapisu po stronie Ma

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_KontoZapis:getKodKontaMa}
        # TODO: Fill in the actual data
        return "null"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {33ed6c48}

    def getKodKontaWinien(self):
        """Identyfikator konta zapisu (konta pomocniczego lub konta księgi
        głównej, jeżeli nie jest wymagany zapis na kontach pomocniczych) dla
        zapisu po stronie Winien

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_KontoZapis:getKodKontaWinien}
        # TODO: Fill in the actual data
        return "null"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {33ed6c48}

    def getKodWalutyMa(self):
        """Kod waluty dla operacji walutowych księgowanych po stronie Ma

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_KontoZapis:getKodWalutyMa}
        # TODO: Fill in the actual data
        return "AED"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {38f462e0}

    def getKodWalutyWinien(self):
        """Kod waluty dla operacji walutowych dla księgowań po stronie Winien

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_KontoZapis:getKodWalutyWinien}
        # TODO: Fill in the actual data
        return "AED"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {38f462e0}

    def getKwotaMa(self):
        """Kwota zapisu transakcji po stronie Ma

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_KontoZapis:getKwotaMa}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getKwotaMaWaluta(self):
        """Kwota zapisu transakcji po stronie Ma w walucie obcej dla operacji
        walutowych

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_KontoZapis:getKwotaMaWaluta}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getKwotaWinien(self):
        """Kwota zapisu transakcji po stronie Winien

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_KontoZapis:getKwotaWinien}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getKwotaWinienWaluta(self):
        """Kwota zapisu transakcji po stronie Winien w walucie obcej dla
        operacji walutowych

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_KontoZapis:getKwotaWinienWaluta}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getLpZapisu(self):
        """Numer kolejny zapisu konta

        @returns long
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_KontoZapis:getLpZapisu}
        # TODO: Fill in the actual data
        return 1
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {3cc34dcd}

    def getNrZapisu(self):
        """Numer (kod) zapisu na koncie pozwalający na jego powiązanie z zapisem
        w Dzienniku (identyczny z elementem NrZapisuDziennika)

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_KontoZapis:getNrZapisu}
        # TODO: Fill in the actual data
        return "NrZapisu"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {7bf37b0a}

    def getOpisZapisuMa(self):
        """Opis zapisu transakcji po stronie Ma

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_KontoZapis:getOpisZapisuMa}
        # TODO: Fill in the actual data
        return "OpisZapisuMa"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {071f014f}

    def getOpisZapisuWinien(self):
        """Opis zapisu transakcji po stronie Winien

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_KontoZapis:getOpisZapisuWinien}
        # TODO: Fill in the actual data
        return "OpisZapisuWinien"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {e3fd7c38}

    def gettyp(self):
        """@returns string"""
        return "G"


class Element_JPK_DziennikCtrl(object):
    """Sumy kontrolne dla tabeli Dziennik"""
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_DziennikCtrl}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getLiczbaWierszyDziennika(self):
        """Liczba wierszy Dziennika

        @returns long
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_DziennikCtrl:getLiczbaWierszyDziennika}
        # TODO: Fill in the actual data
        return 1
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {3cc34dcd}

    def getSumaKwotOperacji(self):
        """Suma wartości kwot operacji - (elementu KwotaOperacji)

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_DziennikCtrl:getSumaKwotOperacji}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}


class Element_JPK_Dziennik(object):
    """Dziennik"""
    # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_Dziennik}
    def __init__(self, *args, **kwargs):
        pass
    # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {c48c6d1d}

    def getDataDowodu(self):
        """Data sporządzenia dowodu księgowego

        @returns datetime.datetime
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_Dziennik:getDataDowodu}
        # TODO: Fill in the actual data
        return datetime.datetime.strptime('1900-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {dcc88bf3}

    def getDataKsiegowania(self):
        """Data, pod którą ujęto dowód w księgach

        @returns datetime.datetime
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_Dziennik:getDataKsiegowania}
        # TODO: Fill in the actual data
        return datetime.datetime.strptime('1900-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {dcc88bf3}

    def getDataOperacji(self):
        """Data dokonania operacji gospodarczej (np. data sprzedaży, zakupu)

        @returns datetime.datetime
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_Dziennik:getDataOperacji}
        # TODO: Fill in the actual data
        return datetime.datetime.strptime('1900-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {dcc88bf3}

    def getDziennikKwotaOperacji(self):
        """Wartość operacji ujęta w Dzienniku

        @returns decimal.Decimal/float
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_Dziennik:getDziennikKwotaOperacji}
        # TODO: Fill in the actual data
        return 0.0
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b966d58a}

    def getKodOperatora(self):
        """Dane pozwalające na ustalenie osoby odpowiedzialnej za treść zapisu

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_Dziennik:getKodOperatora}
        # TODO: Fill in the actual data
        return "KodOperatora"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {38cbed0b}

    def getLpZapisuDziennika(self):
        """Numer kolejny zapisu dziennika

        @returns long
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_Dziennik:getLpZapisuDziennika}
        # TODO: Fill in the actual data
        return 1
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {3cc34dcd}

    def getNrDowoduKsiegowego(self):
        """Numer dowodu księgowego (faktury, PK itp.)

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_Dziennik:getNrDowoduKsiegowego}
        # TODO: Fill in the actual data
        return "NrDowoduKsiegowego"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {2e413e55}

    def getNrZapisuDziennika(self):
        """Numer zapisu w dzienniku

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_Dziennik:getNrZapisuDziennika}
        # TODO: Fill in the actual data
        return "NrZapisuDziennika"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {b4192c23}

    def getOpisDziennika(self):
        """Opis dziennika

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_Dziennik:getOpisDziennika}
        # TODO: Fill in the actual data
        return "OpisDziennika"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {0a020c70}

    def getOpisOperacji(self):
        """Opis operacji w dzienniku

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_Dziennik:getOpisOperacji}
        # TODO: Fill in the actual data
        return "OpisOperacji"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {51ba20c3}

    def getRodzajDowodu(self):
        """Rodzaj dowodu księgowego (np. faktura, PK, zestawienie, wyciąg
        bankowy, raport kasowy, raport okresowy z kasy fiskalnej, zamknięcia
        kont, przeksięgowania techniczne i inne)

        @returns string
        """
        # vvv ONLY EDIT CODE BELOW THIS LINE vvv {Element_JPK_Dziennik:getRodzajDowodu}
        # TODO: Fill in the actual data
        return "RodzajDowodu"
        # ^^^ ONLY EDIT CODE ABOVE THIS LINE ^^^ {2a18e556}

    def gettyp(self):
        """@returns string"""
        return "G"
