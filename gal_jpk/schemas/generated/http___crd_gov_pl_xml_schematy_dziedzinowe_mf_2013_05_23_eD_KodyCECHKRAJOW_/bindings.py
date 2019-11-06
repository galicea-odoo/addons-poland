# /home/maciek/odoo-dev/gal/galicea/gal_jpk/schemas/generated/http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2013_05_23_eD_KodyCECHKRAJOW_/bindings.py
# -*- coding: utf-8 -*-
# @generated
# PyXB bindings for NM:eb466b6f202dcea373f2ad7978c8048d57aff74a
# Generated 2018-03-08 13:30:04.720092 by PyXB version 1.2.5 using Python 2.7.12.final.0
# Namespace http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2013/05/23/eD/KodyCECHKRAJOW/ [xmlns:kck]

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six
# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:6998c690-22cc-11e8-9d15-8c705ac2b4bc')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.5'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2013/05/23/eD/KodyCECHKRAJOW/', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2013/05/23/eD/KodyCECHKRAJOW/}CountryCodeExMS_Type
class CountryCodeExMS_Type (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
			The appropriate country code from the ISO 3166 two-byte alpha version for the state in which the party concerned is a resident. Omit this only if  no data is available.
			This list excludes Member States of the European Union
The following entries must not be used:
	- AN --  NETHERLANDS ANTILLES
Valid entries are:
	- AF --  AFGHANISTAN 
	- AX --  ÅLAND ISLANDS
	- AL --  ALBANIA 
	- DZ --  ALGERIA 
	- AS --  AMERICAN SAMOA 
	- AD --  ANDORRA 
	- AO --  ANGOLA 
	- AI --  ANGUILLA 
	- AQ --  ANTARCTICA 
	- AG --  ANTIGUA AND BARBUDA 
	- AR --  ARGENTINA 
	- AM --  ARMENIA 
	- AW --  ARUBA 
	- AU --  AUSTRALIA 
	- AZ --  AZERBAIJAN 
	- BS --  BAHAMAS 
	- BH --  BAHRAIN 
	- BD --  BANGLADESH 
	- BB --  BARBADOS 
	- BY --  BELARUS 
	- BZ --  BELIZE 
	- BJ --  BENIN 
	- BM --  BERMUDA 
	- BT --  BHUTAN 
	- BO --  BOLIVIA 
	- BA --  BOSNIA AND HERZEGOVINA 
	- BW --  BOTSWANA 
	- BV --  BOUVET ISLAND 
	- BR --  BRAZIL 
	- IO --  BRITISH INDIAN OCEAN TERRITORY 
	- BN --  BRUNEI DARUSSALAM 
	- BF --  BURKINA FASO 
	- BI --  BURUNDI 
	- KH --  CAMBODIA 
	- CM --  CAMEROON 
	- CA --  CANADA 
	- CV --  CAPE VERDE 
	- KY --  CAYMAN ISLANDS 
	- CF --  CENTRAL AFRICAN REPUBLIC 
	- TD --  CHAD 
	- CL --  CHILE 
	- CN --  CHINA 
	- CX --  CHRISTMAS ISLAND 
	- CC --  COCOS (KEELING) ISLANDS 
	- CO --  COLOMBIA 
	- KM --  COMOROS 
	- CG --  CONGO 
	- CD --  CONGO, THE DEMOCRATIC REPUBLIC OF THE 
	- CK --  COOK ISLANDS 
	- CR --  COSTA RICA 
	- CI --  COTE D'IVOIRE 
	- CU --  CUBA 
	- DJ --  DJIBOUTI 
	- DM --  DOMINICA 
	- DO --  DOMINICAN REPUBLIC 
	- EC --  ECUADOR 
	- EG --  EGYPT 
	- SV --  EL SALVADOR 
	- GQ --  EQUATORIAL GUINEA 
	- ER --  ERITREA 
	- ET --  ETHIOPIA 
	- FK --  FALKLAND ISLANDS (MALVINAS) 
	- FO --  FAROE ISLANDS 
	- FJ --  FIJI 
	- GF --  FRENCH GUIANA 
	- PF --  FRENCH POLYNESIA 
	- TF --  FRENCH SOUTHERN TERRITORIES 
	- GA --  GABON 
	- GM --  GAMBIA 
	- GE --  GEORGIA 
	- GH --  GHANA 
	- GI --  GIBRALTAR 
	- GL --  GREENLAND 
	- GD --  GRENADA 
	- GP --  GUADELOUPE 
	- GU --  GUAM 
	- GT --  GUATEMALA 
	- GG --  GUERNSEY
	- GN --  GUINEA 
	- GW --  GUINEA-BISSAU 
	- GY --  GUYANA 
	- HT --  HAITI 
	- HM --  HEARD ISLAND AND MCDONALD ISLANDS 
	- VA --  HOLY SEE (VATICAN CITY STATE) 
	- HN --  HONDURAS 
	- HK --  HONG KONG 
	- IS --  ICELAND 
	- IN --  INDIA 
	- ID --  INDONESIA 
	- IR --  IRAN, ISLAMIC REPUBLIC OF 
	- IQ --  IRAQ 
	- IM --  ISLE OF MAN
	- IL --  ISRAEL 
	- JM --  JAMAICA 
	- JP --  JAPAN 
	- JE --	 JERSEY
	- JO --  JORDAN 
	- KZ --  KAZAKHSTAN 
	- KE --  KENYA 
	- KI --  KIRIBATI 
	- KP --  KOREA, DEMOCRATIC PEOPLE'S REPUBLIC OF 
	- KR --  KOREA, REPUBLIC OF 
	- KW --  KUWAIT 
	- KG --  KYRGYZSTAN 
	- LA --  LAO PEOPLE'S DEMOCRATIC REPUBLIC 
	- LB --  LEBANON 
	- LS --  LESOTHO 
	- LR --  LIBERIA 
	- LY --  LIBYAN ARAB JAMAHIRIYA 
	- LI --  LIECHTENSTEIN 
	- MO --  MACAO 
	- MK --  MACEDONIA, THE FORMER YUGOSLAV REPUBLIC OF 
	- MG --  MADAGASCAR 
	- MW --  MALAWI 
	- MY --  MALAYSIA 
	- MV --  MALDIVES 
	- ML --  MALI 
	- MH --  MARSHALL ISLANDS 
	- MQ --  MARTINIQUE 
	- MR --  MAURITANIA 
	- MU --  MAURITIUS 
	- YT --  MAYOTTE 
	- MX --  MEXICO 
	- FM --  MICRONESIA, FEDERATED STATES OF 
	- MD --  MOLDOVA, REPUBLIC OF 
	- MN --  MONGOLIA 
	- ME --  MONTENEGRO
	- MS --  MONTSERRAT 
	- MA --  MOROCCO 
	- MZ --  MOZAMBIQUE 
	- MM --  MYANMAR 
	- NA --  NAMIBIA 
	- NR --  NAURU 
	- NP --  NEPAL 
	- AN --  NETHERLANDS ANTILLES 
	- NC --  NEW CALEDONIA 
	- NZ --  NEW ZEALAND 
	- NI --  NICARAGUA 
	- NE --  NIGER 
	- NG --  NIGERIA 
	- NU --  NIUE 
	- NF --  NORFOLK ISLAND 
	- MP --  NORTHERN MARIANA ISLANDS 
	- NO --  NORWAY 
	- OM --  OMAN 
	- PK --  PAKISTAN 
	- PW --  PALAU 
	- PS --  PALESTINIAN TERRITORY, OCCUPIED 
	- PA --  PANAMA 
	- PG --  PAPUA NEW GUINEA 
	- PY --  PARAGUAY 
	- PE --  PERU 
	- PH --  PHILIPPINES 
	- PN --  PITCAIRN 
	- PR --  PUERTO RICO 
	- QA --  QATAR 
	- RE --  REUNION 
	- RU --  RUSSIAN FEDERATION 
	- RW --  RWANDA 
	- BL --  SAINT BARTHÉLEMY
	- SH --  SAINT HELENA 
	- KN --  SAINT KITTS AND NEVIS 
	- LC --  SAINT LUCIA 
	- MF --  SAINT MARTIN
	- PM --  SAINT PIERRE AND MIQUELON 
	- VC --  SAINT VINCENT AND THE GRENADINES 
	- WS --  SAMOA 
	- SM --  SAN MARINO 
	- ST --  SAO TOME AND PRINCIPE 
	- SA --  SAUDI ARABIA 
	- SN --  SENEGAL 
	- RS --  SERBIA
	- SC --  SEYCHELLES 
	- SL --  SIERRA LEONE 
	- SG --  SINGAPORE 
	- SB --  SOLOMON ISLANDS 
	- SO --  SOMALIA 
	- ZA --  SOUTH AFRICA 
	- GS --  SOUTH GEORGIA AND THE SOUTH SANDWICH ISLANDS 
	- LK --  SRI LANKA 
	- SD --  SUDAN 
	- SR --  SURINAME 
	- SJ --  SVALBARD AND JAN MAYEN 
	- SZ --  SWAZILAND 
	- CH --  SWITZERLAND 
	- SY --  SYRIAN ARAB REPUBLIC 
	- TW --  TAIWAN, PROVINCE OF CHINA 
	- TJ --  TAJIKISTAN 
	- TZ --  TANZANIA, UNITED REPUBLIC OF 
	- TH --  THAILAND 
	- TL --  TIMOR-LESTE 
	- TG --  TOGO 
	- TK --  TOKELAU 
	- TO --  TONGA 
	- TT --  TRINIDAD AND TOBAGO 
	- TN --  TUNISIA 
	- TR --  TURKEY 
	- TM --  TURKMENISTAN 
	- TC --  TURKS AND CAICOS ISLANDS 
	- TV --  TUVALU 
	- UG --  UGANDA 
	- UA --  UKRAINE 
	- AE --  UNITED ARAB EMIRATES 
	- US --  UNITED STATES 
	- UM --  UNITED STATES MINOR OUTLYING ISLANDS 
	- UY --  URUGUAY 
	- UZ --  UZBEKISTAN 
	- VU --  VANUATU 
	- VE --  VENEZUELA, BOLIVARIAN REPUBLIC OF
	- VN --  VIET NAM 
	- VG --  VIRGIN ISLANDS, BRITISH 
	- VI --  VIRGIN ISLANDS, U.S. 
	- WF --  WALLIS AND FUTUNA 
	- EH --  WESTERN SAHARA 
	- YE --  YEMEN 
	- ZM --  ZAMBIA 
	- ZW --  ZIMBABWE 
	- CW --  CURACAO
	- NM --  SAINT MARTIN (DUTCH PART) - invalidated
	- SX --  SAINT MARTIN (DUTCH PART)
	- BQ --  BONAIRE, SAINT EUSTATIUS AND SABA
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CountryCodeExMS_Type')
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2013/05/23/eD/KodyCECHKRAJOW/KodyCechKrajow_v3-0E.xsd', 7, 1)
    _Documentation = "\n\t\t\tThe appropriate country code from the ISO 3166 two-byte alpha version for the state in which the party concerned is a resident. Omit this only if  no data is available.\n\t\t\tThis list excludes Member States of the European Union\nThe following entries must not be used:\n\t- AN --  NETHERLANDS ANTILLES\nValid entries are:\n\t- AF --  AFGHANISTAN \n\t- AX --  \xc5LAND ISLANDS\n\t- AL --  ALBANIA \n\t- DZ --  ALGERIA \n\t- AS --  AMERICAN SAMOA \n\t- AD --  ANDORRA \n\t- AO --  ANGOLA \n\t- AI --  ANGUILLA \n\t- AQ --  ANTARCTICA \n\t- AG --  ANTIGUA AND BARBUDA \n\t- AR --  ARGENTINA \n\t- AM --  ARMENIA \n\t- AW --  ARUBA \n\t- AU --  AUSTRALIA \n\t- AZ --  AZERBAIJAN \n\t- BS --  BAHAMAS \n\t- BH --  BAHRAIN \n\t- BD --  BANGLADESH \n\t- BB --  BARBADOS \n\t- BY --  BELARUS \n\t- BZ --  BELIZE \n\t- BJ --  BENIN \n\t- BM --  BERMUDA \n\t- BT --  BHUTAN \n\t- BO --  BOLIVIA \n\t- BA --  BOSNIA AND HERZEGOVINA \n\t- BW --  BOTSWANA \n\t- BV --  BOUVET ISLAND \n\t- BR --  BRAZIL \n\t- IO --  BRITISH INDIAN OCEAN TERRITORY \n\t- BN --  BRUNEI DARUSSALAM \n\t- BF --  BURKINA FASO \n\t- BI --  BURUNDI \n\t- KH --  CAMBODIA \n\t- CM --  CAMEROON \n\t- CA --  CANADA \n\t- CV --  CAPE VERDE \n\t- KY --  CAYMAN ISLANDS \n\t- CF --  CENTRAL AFRICAN REPUBLIC \n\t- TD --  CHAD \n\t- CL --  CHILE \n\t- CN --  CHINA \n\t- CX --  CHRISTMAS ISLAND \n\t- CC --  COCOS (KEELING) ISLANDS \n\t- CO --  COLOMBIA \n\t- KM --  COMOROS \n\t- CG --  CONGO \n\t- CD --  CONGO, THE DEMOCRATIC REPUBLIC OF THE \n\t- CK --  COOK ISLANDS \n\t- CR --  COSTA RICA \n\t- CI --  COTE D'IVOIRE \n\t- CU --  CUBA \n\t- DJ --  DJIBOUTI \n\t- DM --  DOMINICA \n\t- DO --  DOMINICAN REPUBLIC \n\t- EC --  ECUADOR \n\t- EG --  EGYPT \n\t- SV --  EL SALVADOR \n\t- GQ --  EQUATORIAL GUINEA \n\t- ER --  ERITREA \n\t- ET --  ETHIOPIA \n\t- FK --  FALKLAND ISLANDS (MALVINAS) \n\t- FO --  FAROE ISLANDS \n\t- FJ --  FIJI \n\t- GF --  FRENCH GUIANA \n\t- PF --  FRENCH POLYNESIA \n\t- TF --  FRENCH SOUTHERN TERRITORIES \n\t- GA --  GABON \n\t- GM --  GAMBIA \n\t- GE --  GEORGIA \n\t- GH --  GHANA \n\t- GI --  GIBRALTAR \n\t- GL --  GREENLAND \n\t- GD --  GRENADA \n\t- GP --  GUADELOUPE \n\t- GU --  GUAM \n\t- GT --  GUATEMALA \n\t- GG --  GUERNSEY\n\t- GN --  GUINEA \n\t- GW --  GUINEA-BISSAU \n\t- GY --  GUYANA \n\t- HT --  HAITI \n\t- HM --  HEARD ISLAND AND MCDONALD ISLANDS \n\t- VA --  HOLY SEE (VATICAN CITY STATE) \n\t- HN --  HONDURAS \n\t- HK --  HONG KONG \n\t- IS --  ICELAND \n\t- IN --  INDIA \n\t- ID --  INDONESIA \n\t- IR --  IRAN, ISLAMIC REPUBLIC OF \n\t- IQ --  IRAQ \n\t- IM --  ISLE OF MAN\n\t- IL --  ISRAEL \n\t- JM --  JAMAICA \n\t- JP --  JAPAN \n\t- JE --\t JERSEY\n\t- JO --  JORDAN \n\t- KZ --  KAZAKHSTAN \n\t- KE --  KENYA \n\t- KI --  KIRIBATI \n\t- KP --  KOREA, DEMOCRATIC PEOPLE'S REPUBLIC OF \n\t- KR --  KOREA, REPUBLIC OF \n\t- KW --  KUWAIT \n\t- KG --  KYRGYZSTAN \n\t- LA --  LAO PEOPLE'S DEMOCRATIC REPUBLIC \n\t- LB --  LEBANON \n\t- LS --  LESOTHO \n\t- LR --  LIBERIA \n\t- LY --  LIBYAN ARAB JAMAHIRIYA \n\t- LI --  LIECHTENSTEIN \n\t- MO --  MACAO \n\t- MK --  MACEDONIA, THE FORMER YUGOSLAV REPUBLIC OF \n\t- MG --  MADAGASCAR \n\t- MW --  MALAWI \n\t- MY --  MALAYSIA \n\t- MV --  MALDIVES \n\t- ML --  MALI \n\t- MH --  MARSHALL ISLANDS \n\t- MQ --  MARTINIQUE \n\t- MR --  MAURITANIA \n\t- MU --  MAURITIUS \n\t- YT --  MAYOTTE \n\t- MX --  MEXICO \n\t- FM --  MICRONESIA, FEDERATED STATES OF \n\t- MD --  MOLDOVA, REPUBLIC OF \n\t- MN --  MONGOLIA \n\t- ME --  MONTENEGRO\n\t- MS --  MONTSERRAT \n\t- MA --  MOROCCO \n\t- MZ --  MOZAMBIQUE \n\t- MM --  MYANMAR \n\t- NA --  NAMIBIA \n\t- NR --  NAURU \n\t- NP --  NEPAL \n\t- AN --  NETHERLANDS ANTILLES \n\t- NC --  NEW CALEDONIA \n\t- NZ --  NEW ZEALAND \n\t- NI --  NICARAGUA \n\t- NE --  NIGER \n\t- NG --  NIGERIA \n\t- NU --  NIUE \n\t- NF --  NORFOLK ISLAND \n\t- MP --  NORTHERN MARIANA ISLANDS \n\t- NO --  NORWAY \n\t- OM --  OMAN \n\t- PK --  PAKISTAN \n\t- PW --  PALAU \n\t- PS --  PALESTINIAN TERRITORY, OCCUPIED \n\t- PA --  PANAMA \n\t- PG --  PAPUA NEW GUINEA \n\t- PY --  PARAGUAY \n\t- PE --  PERU \n\t- PH --  PHILIPPINES \n\t- PN --  PITCAIRN \n\t- PR --  PUERTO RICO \n\t- QA --  QATAR \n\t- RE --  REUNION \n\t- RU --  RUSSIAN FEDERATION \n\t- RW --  RWANDA \n\t- BL --  SAINT BARTH\xc9LEMY\n\t- SH --  SAINT HELENA \n\t- KN --  SAINT KITTS AND NEVIS \n\t- LC --  SAINT LUCIA \n\t- MF --  SAINT MARTIN\n\t- PM --  SAINT PIERRE AND MIQUELON \n\t- VC --  SAINT VINCENT AND THE GRENADINES \n\t- WS --  SAMOA \n\t- SM --  SAN MARINO \n\t- ST --  SAO TOME AND PRINCIPE \n\t- SA --  SAUDI ARABIA \n\t- SN --  SENEGAL \n\t- RS --  SERBIA\n\t- SC --  SEYCHELLES \n\t- SL --  SIERRA LEONE \n\t- SG --  SINGAPORE \n\t- SB --  SOLOMON ISLANDS \n\t- SO --  SOMALIA \n\t- ZA --  SOUTH AFRICA \n\t- GS --  SOUTH GEORGIA AND THE SOUTH SANDWICH ISLANDS \n\t- LK --  SRI LANKA \n\t- SD --  SUDAN \n\t- SR --  SURINAME \n\t- SJ --  SVALBARD AND JAN MAYEN \n\t- SZ --  SWAZILAND \n\t- CH --  SWITZERLAND \n\t- SY --  SYRIAN ARAB REPUBLIC \n\t- TW --  TAIWAN, PROVINCE OF CHINA \n\t- TJ --  TAJIKISTAN \n\t- TZ --  TANZANIA, UNITED REPUBLIC OF \n\t- TH --  THAILAND \n\t- TL --  TIMOR-LESTE \n\t- TG --  TOGO \n\t- TK --  TOKELAU \n\t- TO --  TONGA \n\t- TT --  TRINIDAD AND TOBAGO \n\t- TN --  TUNISIA \n\t- TR --  TURKEY \n\t- TM --  TURKMENISTAN \n\t- TC --  TURKS AND CAICOS ISLANDS \n\t- TV --  TUVALU \n\t- UG --  UGANDA \n\t- UA --  UKRAINE \n\t- AE --  UNITED ARAB EMIRATES \n\t- US --  UNITED STATES \n\t- UM --  UNITED STATES MINOR OUTLYING ISLANDS \n\t- UY --  URUGUAY \n\t- UZ --  UZBEKISTAN \n\t- VU --  VANUATU \n\t- VE --  VENEZUELA, BOLIVARIAN REPUBLIC OF\n\t- VN --  VIET NAM \n\t- VG --  VIRGIN ISLANDS, BRITISH \n\t- VI --  VIRGIN ISLANDS, U.S. \n\t- WF --  WALLIS AND FUTUNA \n\t- EH --  WESTERN SAHARA \n\t- YE --  YEMEN \n\t- ZM --  ZAMBIA \n\t- ZW --  ZIMBABWE \n\t- CW --  CURACAO\n\t- NM --  SAINT MARTIN (DUTCH PART) - invalidated\n\t- SX --  SAINT MARTIN (DUTCH PART)\n\t- BQ --  BONAIRE, SAINT EUSTATIUS AND SABA\n\t\t\t"
CountryCodeExMS_Type._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=CountryCodeExMS_Type, enum_prefix=None)
CountryCodeExMS_Type.AF = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='AF', tag='AF')
CountryCodeExMS_Type.AX = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='AX', tag='AX')
CountryCodeExMS_Type.AL = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='AL', tag='AL')
CountryCodeExMS_Type.DZ = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='DZ', tag='DZ')
CountryCodeExMS_Type.AS = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='AS', tag='AS')
CountryCodeExMS_Type.AD = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='AD', tag='AD')
CountryCodeExMS_Type.AO = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='AO', tag='AO')
CountryCodeExMS_Type.AI = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='AI', tag='AI')
CountryCodeExMS_Type.AQ = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='AQ', tag='AQ')
CountryCodeExMS_Type.AG = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='AG', tag='AG')
CountryCodeExMS_Type.AR = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='AR', tag='AR')
CountryCodeExMS_Type.AM = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='AM', tag='AM')
CountryCodeExMS_Type.AW = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='AW', tag='AW')
CountryCodeExMS_Type.AU = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='AU', tag='AU')
CountryCodeExMS_Type.AZ = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='AZ', tag='AZ')
CountryCodeExMS_Type.BS = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='BS', tag='BS')
CountryCodeExMS_Type.BH = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='BH', tag='BH')
CountryCodeExMS_Type.BD = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='BD', tag='BD')
CountryCodeExMS_Type.BB = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='BB', tag='BB')
CountryCodeExMS_Type.BY = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='BY', tag='BY')
CountryCodeExMS_Type.BZ = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='BZ', tag='BZ')
CountryCodeExMS_Type.BJ = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='BJ', tag='BJ')
CountryCodeExMS_Type.BM = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='BM', tag='BM')
CountryCodeExMS_Type.BT = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='BT', tag='BT')
CountryCodeExMS_Type.BO = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='BO', tag='BO')
CountryCodeExMS_Type.BA = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='BA', tag='BA')
CountryCodeExMS_Type.BW = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='BW', tag='BW')
CountryCodeExMS_Type.BV = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='BV', tag='BV')
CountryCodeExMS_Type.BR = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='BR', tag='BR')
CountryCodeExMS_Type.IO = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='IO', tag='IO')
CountryCodeExMS_Type.BN = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='BN', tag='BN')
CountryCodeExMS_Type.BF = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='BF', tag='BF')
CountryCodeExMS_Type.BI = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='BI', tag='BI')
CountryCodeExMS_Type.KH = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='KH', tag='KH')
CountryCodeExMS_Type.CM = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='CM', tag='CM')
CountryCodeExMS_Type.CA = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='CA', tag='CA')
CountryCodeExMS_Type.CV = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='CV', tag='CV')
CountryCodeExMS_Type.KY = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='KY', tag='KY')
CountryCodeExMS_Type.CF = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='CF', tag='CF')
CountryCodeExMS_Type.TD = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='TD', tag='TD')
CountryCodeExMS_Type.CL = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='CL', tag='CL')
CountryCodeExMS_Type.CN = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='CN', tag='CN')
CountryCodeExMS_Type.CX = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='CX', tag='CX')
CountryCodeExMS_Type.CC = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='CC', tag='CC')
CountryCodeExMS_Type.CO = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='CO', tag='CO')
CountryCodeExMS_Type.KM = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='KM', tag='KM')
CountryCodeExMS_Type.CG = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='CG', tag='CG')
CountryCodeExMS_Type.CD = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='CD', tag='CD')
CountryCodeExMS_Type.CK = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='CK', tag='CK')
CountryCodeExMS_Type.CR = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='CR', tag='CR')
CountryCodeExMS_Type.CI = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='CI', tag='CI')
CountryCodeExMS_Type.CU = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='CU', tag='CU')
CountryCodeExMS_Type.DJ = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='DJ', tag='DJ')
CountryCodeExMS_Type.DM = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='DM', tag='DM')
CountryCodeExMS_Type.DO = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='DO', tag='DO')
CountryCodeExMS_Type.EC = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='EC', tag='EC')
CountryCodeExMS_Type.EG = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='EG', tag='EG')
CountryCodeExMS_Type.SV = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='SV', tag='SV')
CountryCodeExMS_Type.GQ = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='GQ', tag='GQ')
CountryCodeExMS_Type.ER = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='ER', tag='ER')
CountryCodeExMS_Type.ET = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='ET', tag='ET')
CountryCodeExMS_Type.FK = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='FK', tag='FK')
CountryCodeExMS_Type.FO = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='FO', tag='FO')
CountryCodeExMS_Type.FJ = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='FJ', tag='FJ')
CountryCodeExMS_Type.GF = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='GF', tag='GF')
CountryCodeExMS_Type.PF = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='PF', tag='PF')
CountryCodeExMS_Type.TF = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='TF', tag='TF')
CountryCodeExMS_Type.GA = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='GA', tag='GA')
CountryCodeExMS_Type.GM = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='GM', tag='GM')
CountryCodeExMS_Type.GE = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='GE', tag='GE')
CountryCodeExMS_Type.GH = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='GH', tag='GH')
CountryCodeExMS_Type.GI = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='GI', tag='GI')
CountryCodeExMS_Type.GL = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='GL', tag='GL')
CountryCodeExMS_Type.GD = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='GD', tag='GD')
CountryCodeExMS_Type.GP = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='GP', tag='GP')
CountryCodeExMS_Type.GU = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='GU', tag='GU')
CountryCodeExMS_Type.GT = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='GT', tag='GT')
CountryCodeExMS_Type.GG = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='GG', tag='GG')
CountryCodeExMS_Type.GN = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='GN', tag='GN')
CountryCodeExMS_Type.GW = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='GW', tag='GW')
CountryCodeExMS_Type.GY = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='GY', tag='GY')
CountryCodeExMS_Type.HT = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='HT', tag='HT')
CountryCodeExMS_Type.HM = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='HM', tag='HM')
CountryCodeExMS_Type.VA = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='VA', tag='VA')
CountryCodeExMS_Type.HN = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='HN', tag='HN')
CountryCodeExMS_Type.HK = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='HK', tag='HK')
CountryCodeExMS_Type.IS = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='IS', tag='IS')
CountryCodeExMS_Type.IN = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='IN', tag='IN')
CountryCodeExMS_Type.ID = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='ID', tag='ID')
CountryCodeExMS_Type.IR = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='IR', tag='IR')
CountryCodeExMS_Type.IQ = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='IQ', tag='IQ')
CountryCodeExMS_Type.IM = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='IM', tag='IM')
CountryCodeExMS_Type.IL = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='IL', tag='IL')
CountryCodeExMS_Type.JM = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='JM', tag='JM')
CountryCodeExMS_Type.JP = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='JP', tag='JP')
CountryCodeExMS_Type.JE = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='JE', tag='JE')
CountryCodeExMS_Type.JO = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='JO', tag='JO')
CountryCodeExMS_Type.KZ = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='KZ', tag='KZ')
CountryCodeExMS_Type.KE = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='KE', tag='KE')
CountryCodeExMS_Type.KI = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='KI', tag='KI')
CountryCodeExMS_Type.KP = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='KP', tag='KP')
CountryCodeExMS_Type.KR = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='KR', tag='KR')
CountryCodeExMS_Type.KW = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='KW', tag='KW')
CountryCodeExMS_Type.KG = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='KG', tag='KG')
CountryCodeExMS_Type.LA = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='LA', tag='LA')
CountryCodeExMS_Type.LB = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='LB', tag='LB')
CountryCodeExMS_Type.LS = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='LS', tag='LS')
CountryCodeExMS_Type.LR = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='LR', tag='LR')
CountryCodeExMS_Type.LY = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='LY', tag='LY')
CountryCodeExMS_Type.LI = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='LI', tag='LI')
CountryCodeExMS_Type.MO = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='MO', tag='MO')
CountryCodeExMS_Type.MK = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='MK', tag='MK')
CountryCodeExMS_Type.MG = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='MG', tag='MG')
CountryCodeExMS_Type.MW = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='MW', tag='MW')
CountryCodeExMS_Type.MY = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='MY', tag='MY')
CountryCodeExMS_Type.MV = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='MV', tag='MV')
CountryCodeExMS_Type.ML = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='ML', tag='ML')
CountryCodeExMS_Type.MH = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='MH', tag='MH')
CountryCodeExMS_Type.MQ = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='MQ', tag='MQ')
CountryCodeExMS_Type.MR = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='MR', tag='MR')
CountryCodeExMS_Type.MU = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='MU', tag='MU')
CountryCodeExMS_Type.YT = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='YT', tag='YT')
CountryCodeExMS_Type.MX = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='MX', tag='MX')
CountryCodeExMS_Type.FM = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='FM', tag='FM')
CountryCodeExMS_Type.MD = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='MD', tag='MD')
CountryCodeExMS_Type.MN = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='MN', tag='MN')
CountryCodeExMS_Type.ME = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='ME', tag='ME')
CountryCodeExMS_Type.MS = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='MS', tag='MS')
CountryCodeExMS_Type.MA = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='MA', tag='MA')
CountryCodeExMS_Type.MZ = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='MZ', tag='MZ')
CountryCodeExMS_Type.MM = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='MM', tag='MM')
CountryCodeExMS_Type.NA = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='NA', tag='NA')
CountryCodeExMS_Type.NR = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='NR', tag='NR')
CountryCodeExMS_Type.NP = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='NP', tag='NP')
CountryCodeExMS_Type.AN = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='AN', tag='AN')
CountryCodeExMS_Type.NC = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='NC', tag='NC')
CountryCodeExMS_Type.NZ = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='NZ', tag='NZ')
CountryCodeExMS_Type.NI = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='NI', tag='NI')
CountryCodeExMS_Type.NE = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='NE', tag='NE')
CountryCodeExMS_Type.NG = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='NG', tag='NG')
CountryCodeExMS_Type.NU = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='NU', tag='NU')
CountryCodeExMS_Type.NF = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='NF', tag='NF')
CountryCodeExMS_Type.MP = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='MP', tag='MP')
CountryCodeExMS_Type.NO = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='NO', tag='NO')
CountryCodeExMS_Type.OM = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='OM', tag='OM')
CountryCodeExMS_Type.PK = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='PK', tag='PK')
CountryCodeExMS_Type.PW = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='PW', tag='PW')
CountryCodeExMS_Type.PS = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='PS', tag='PS')
CountryCodeExMS_Type.PA = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='PA', tag='PA')
CountryCodeExMS_Type.PG = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='PG', tag='PG')
CountryCodeExMS_Type.PY = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='PY', tag='PY')
CountryCodeExMS_Type.PE = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='PE', tag='PE')
CountryCodeExMS_Type.PH = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='PH', tag='PH')
CountryCodeExMS_Type.PN = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='PN', tag='PN')
CountryCodeExMS_Type.PR = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='PR', tag='PR')
CountryCodeExMS_Type.QA = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='QA', tag='QA')
CountryCodeExMS_Type.RE = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='RE', tag='RE')
CountryCodeExMS_Type.RU = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='RU', tag='RU')
CountryCodeExMS_Type.RW = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='RW', tag='RW')
CountryCodeExMS_Type.BL = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='BL', tag='BL')
CountryCodeExMS_Type.SH = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='SH', tag='SH')
CountryCodeExMS_Type.KN = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='KN', tag='KN')
CountryCodeExMS_Type.LC = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='LC', tag='LC')
CountryCodeExMS_Type.MF = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='MF', tag='MF')
CountryCodeExMS_Type.PM = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='PM', tag='PM')
CountryCodeExMS_Type.VC = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='VC', tag='VC')
CountryCodeExMS_Type.WS = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='WS', tag='WS')
CountryCodeExMS_Type.SM = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='SM', tag='SM')
CountryCodeExMS_Type.ST = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='ST', tag='ST')
CountryCodeExMS_Type.SA = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='SA', tag='SA')
CountryCodeExMS_Type.SN = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='SN', tag='SN')
CountryCodeExMS_Type.RS = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='RS', tag='RS')
CountryCodeExMS_Type.SC = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='SC', tag='SC')
CountryCodeExMS_Type.SL = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='SL', tag='SL')
CountryCodeExMS_Type.SG = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='SG', tag='SG')
CountryCodeExMS_Type.SB = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='SB', tag='SB')
CountryCodeExMS_Type.SO = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='SO', tag='SO')
CountryCodeExMS_Type.ZA = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='ZA', tag='ZA')
CountryCodeExMS_Type.GS = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='GS', tag='GS')
CountryCodeExMS_Type.LK = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='LK', tag='LK')
CountryCodeExMS_Type.SD = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='SD', tag='SD')
CountryCodeExMS_Type.SR = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='SR', tag='SR')
CountryCodeExMS_Type.SJ = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='SJ', tag='SJ')
CountryCodeExMS_Type.SZ = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='SZ', tag='SZ')
CountryCodeExMS_Type.CH = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='CH', tag='CH')
CountryCodeExMS_Type.SY = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='SY', tag='SY')
CountryCodeExMS_Type.TW = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='TW', tag='TW')
CountryCodeExMS_Type.TJ = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='TJ', tag='TJ')
CountryCodeExMS_Type.TZ = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='TZ', tag='TZ')
CountryCodeExMS_Type.TH = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='TH', tag='TH')
CountryCodeExMS_Type.TL = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='TL', tag='TL')
CountryCodeExMS_Type.TG = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='TG', tag='TG')
CountryCodeExMS_Type.TK = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='TK', tag='TK')
CountryCodeExMS_Type.TO = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='TO', tag='TO')
CountryCodeExMS_Type.TT = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='TT', tag='TT')
CountryCodeExMS_Type.TN = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='TN', tag='TN')
CountryCodeExMS_Type.TR = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='TR', tag='TR')
CountryCodeExMS_Type.TM = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='TM', tag='TM')
CountryCodeExMS_Type.TC = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='TC', tag='TC')
CountryCodeExMS_Type.TV = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='TV', tag='TV')
CountryCodeExMS_Type.UG = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='UG', tag='UG')
CountryCodeExMS_Type.UA = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='UA', tag='UA')
CountryCodeExMS_Type.AE = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='AE', tag='AE')
CountryCodeExMS_Type.US = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='US', tag='US')
CountryCodeExMS_Type.UM = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='UM', tag='UM')
CountryCodeExMS_Type.UY = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='UY', tag='UY')
CountryCodeExMS_Type.UZ = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='UZ', tag='UZ')
CountryCodeExMS_Type.VU = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='VU', tag='VU')
CountryCodeExMS_Type.VE = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='VE', tag='VE')
CountryCodeExMS_Type.VN = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='VN', tag='VN')
CountryCodeExMS_Type.VG = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='VG', tag='VG')
CountryCodeExMS_Type.VI = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='VI', tag='VI')
CountryCodeExMS_Type.WF = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='WF', tag='WF')
CountryCodeExMS_Type.EH = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='EH', tag='EH')
CountryCodeExMS_Type.YE = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='YE', tag='YE')
CountryCodeExMS_Type.ZM = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='ZM', tag='ZM')
CountryCodeExMS_Type.ZW = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='ZW', tag='ZW')
CountryCodeExMS_Type.CW = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='CW', tag='CW')
CountryCodeExMS_Type.NM = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='NM', tag='NM')
CountryCodeExMS_Type.SX = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='SX', tag='SX')
CountryCodeExMS_Type.BQ = CountryCodeExMS_Type._CF_enumeration.addEnumeration(unicode_value='BQ', tag='BQ')
CountryCodeExMS_Type._InitializeFacetMap(CountryCodeExMS_Type._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'CountryCodeExMS_Type', CountryCodeExMS_Type)
_module_typeBindings.CountryCodeExMS_Type = CountryCodeExMS_Type

# Atomic simple type: {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2013/05/23/eD/KodyCECHKRAJOW/}MSCountryCode_Type
class MSCountryCode_Type (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
			The appropriate country code from the ISO 3166 two-byte alpha version for the state in which the party concerned is a resident. Omit this only if  no data is available.
			This list includes only Member States of the European Union
Valid entries are:
  - AT --  AUSTRIA 
  - BE --  BELGIUM 
  - BG --  BULGARIA 
  - HR --  CROATIA 
  - CY --  CYPRUS 
  - CZ --  CZECH REPUBLIC 
  - DK --  DENMARK 
  - EE --  ESTONIA 
  - FI --  FINLAND 
  - FR --  FRANCE 
  - DE --  GERMANY 
  - EL --  GREECE 
  - HU --  HUNGARY 
  - IE --  IRELAND 
  - IT --  ITALY 
  - LV --  LATVIA 
  - LT --  LITHUANIA 
  - LU --  LUXEMBOURG 
  - MT --  MALTA 
  - NL --  NETHERLANDS 
  - PL --  POLAND 
  - PT --  PORTUGAL 
  - RO --  ROMANIA 
  - SK --  SLOVAKIA 
  - SI --  SLOVENIA 
  - ES --  SPAIN 
  - SE --  SWEDEN 
  - GB --  UNITED KINGDOM 
  - IC --  CANARY ISLANDS
  - XI --  CEUTA
  - XJ --  MELILLA
  - MC --  MONACO 
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MSCountryCode_Type')
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2013/05/23/eD/KodyCECHKRAJOW/KodyCechKrajow_v3-0E.xsd', 462, 1)
    _Documentation = '\n\t\t\tThe appropriate country code from the ISO 3166 two-byte alpha version for the state in which the party concerned is a resident. Omit this only if  no data is available.\n\t\t\tThis list includes only Member States of the European Union\nValid entries are:\n  - AT --  AUSTRIA \n  - BE --  BELGIUM \n  - BG --  BULGARIA \n  - HR --  CROATIA \n  - CY --  CYPRUS \n  - CZ --  CZECH REPUBLIC \n  - DK --  DENMARK \n  - EE --  ESTONIA \n  - FI --  FINLAND \n  - FR --  FRANCE \n  - DE --  GERMANY \n  - EL --  GREECE \n  - HU --  HUNGARY \n  - IE --  IRELAND \n  - IT --  ITALY \n  - LV --  LATVIA \n  - LT --  LITHUANIA \n  - LU --  LUXEMBOURG \n  - MT --  MALTA \n  - NL --  NETHERLANDS \n  - PL --  POLAND \n  - PT --  PORTUGAL \n  - RO --  ROMANIA \n  - SK --  SLOVAKIA \n  - SI --  SLOVENIA \n  - ES --  SPAIN \n  - SE --  SWEDEN \n  - GB --  UNITED KINGDOM \n  - IC --  CANARY ISLANDS\n  - XI --  CEUTA\n  - XJ --  MELILLA\n  - MC --  MONACO \n\t\t\t'
MSCountryCode_Type._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MSCountryCode_Type, enum_prefix=None)
MSCountryCode_Type.AT = MSCountryCode_Type._CF_enumeration.addEnumeration(unicode_value='AT', tag='AT')
MSCountryCode_Type.BE = MSCountryCode_Type._CF_enumeration.addEnumeration(unicode_value='BE', tag='BE')
MSCountryCode_Type.BG = MSCountryCode_Type._CF_enumeration.addEnumeration(unicode_value='BG', tag='BG')
MSCountryCode_Type.CY = MSCountryCode_Type._CF_enumeration.addEnumeration(unicode_value='CY', tag='CY')
MSCountryCode_Type.CZ = MSCountryCode_Type._CF_enumeration.addEnumeration(unicode_value='CZ', tag='CZ')
MSCountryCode_Type.DK = MSCountryCode_Type._CF_enumeration.addEnumeration(unicode_value='DK', tag='DK')
MSCountryCode_Type.EE = MSCountryCode_Type._CF_enumeration.addEnumeration(unicode_value='EE', tag='EE')
MSCountryCode_Type.FI = MSCountryCode_Type._CF_enumeration.addEnumeration(unicode_value='FI', tag='FI')
MSCountryCode_Type.FR = MSCountryCode_Type._CF_enumeration.addEnumeration(unicode_value='FR', tag='FR')
MSCountryCode_Type.DE = MSCountryCode_Type._CF_enumeration.addEnumeration(unicode_value='DE', tag='DE')
MSCountryCode_Type.EL = MSCountryCode_Type._CF_enumeration.addEnumeration(unicode_value='EL', tag='EL')
MSCountryCode_Type.HR = MSCountryCode_Type._CF_enumeration.addEnumeration(unicode_value='HR', tag='HR')
MSCountryCode_Type.HU = MSCountryCode_Type._CF_enumeration.addEnumeration(unicode_value='HU', tag='HU')
MSCountryCode_Type.IE = MSCountryCode_Type._CF_enumeration.addEnumeration(unicode_value='IE', tag='IE')
MSCountryCode_Type.IT = MSCountryCode_Type._CF_enumeration.addEnumeration(unicode_value='IT', tag='IT')
MSCountryCode_Type.LV = MSCountryCode_Type._CF_enumeration.addEnumeration(unicode_value='LV', tag='LV')
MSCountryCode_Type.LT = MSCountryCode_Type._CF_enumeration.addEnumeration(unicode_value='LT', tag='LT')
MSCountryCode_Type.LU = MSCountryCode_Type._CF_enumeration.addEnumeration(unicode_value='LU', tag='LU')
MSCountryCode_Type.MT = MSCountryCode_Type._CF_enumeration.addEnumeration(unicode_value='MT', tag='MT')
MSCountryCode_Type.NL = MSCountryCode_Type._CF_enumeration.addEnumeration(unicode_value='NL', tag='NL')
MSCountryCode_Type.PL = MSCountryCode_Type._CF_enumeration.addEnumeration(unicode_value='PL', tag='PL')
MSCountryCode_Type.PT = MSCountryCode_Type._CF_enumeration.addEnumeration(unicode_value='PT', tag='PT')
MSCountryCode_Type.RO = MSCountryCode_Type._CF_enumeration.addEnumeration(unicode_value='RO', tag='RO')
MSCountryCode_Type.SK = MSCountryCode_Type._CF_enumeration.addEnumeration(unicode_value='SK', tag='SK')
MSCountryCode_Type.SI = MSCountryCode_Type._CF_enumeration.addEnumeration(unicode_value='SI', tag='SI')
MSCountryCode_Type.ES = MSCountryCode_Type._CF_enumeration.addEnumeration(unicode_value='ES', tag='ES')
MSCountryCode_Type.SE = MSCountryCode_Type._CF_enumeration.addEnumeration(unicode_value='SE', tag='SE')
MSCountryCode_Type.GB = MSCountryCode_Type._CF_enumeration.addEnumeration(unicode_value='GB', tag='GB')
MSCountryCode_Type.IC = MSCountryCode_Type._CF_enumeration.addEnumeration(unicode_value='IC', tag='IC')
MSCountryCode_Type.XI = MSCountryCode_Type._CF_enumeration.addEnumeration(unicode_value='XI', tag='XI')
MSCountryCode_Type.XJ = MSCountryCode_Type._CF_enumeration.addEnumeration(unicode_value='XJ', tag='XJ')
MSCountryCode_Type.MC = MSCountryCode_Type._CF_enumeration.addEnumeration(unicode_value='MC', tag='MC')
MSCountryCode_Type._InitializeFacetMap(MSCountryCode_Type._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'MSCountryCode_Type', MSCountryCode_Type)
_module_typeBindings.MSCountryCode_Type = MSCountryCode_Type

# Atomic simple type: {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2013/05/23/eD/KodyCECHKRAJOW/}currCode_Type
class currCode_Type (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
			The appropriate currency code from the ISO 4217 three-byte alpha version for the currency in which a monetary amount is expressed. 
Valid entries are:
AED United Arab Emirates, Dirhams 
AFN Afghanistan, Afghanis 
ALL Albania, Leke 
AMD Armenia, Drams 
ANG Netherlands Antilles, Guilders 
AOA Angola, Kwanza 
ARS Argentina, Pesos 
AUD Australia, Dollars 
AWG Aruba, Guilders 
AZN Azerbaijan, Manats 
BAM Bosnia and Herzegovina, Convertible Marka 
BBD Barbados, Dollars 
BDT Bangladesh, Taka 
BGN Bulgaria, Leva 
BHD Bahrain, Dinars 
BIF Burundi, Francs 
BMD Bermuda, Dollars 
BND Brunei Darussalam, Dollars 
BOB Bolivia, Bolivianos 
BOV Bolivia, Mvdol
BRL Brazil, Brazil Real 
BSD Bahamas, Dollars 
BTN Bhutan, Ngultrum 
BWP Botswana, Pulas 
BYR Belarus, Rubles 
BZD Belize, Dollars 
CAD Canada, Dollars 
CDF Congo/Kinshasa, Congolese Francs 
CHF Switzerland, Francs 
CLF Chile, Unidades de fomento 
CLP Chile, Pesos 
CNY China, Yuan Renminbi 
COP Colombia, Pesos 
COU Colombia, Unidad de Valor Real
CRC Costa Rica, Colones 
CUC Cuba, Convertible Pesos 
CUP Cuba, Pesos 
CVE Cape Verde, Escudos 
CZK Czech Republic, Koruny 
DJF Djibouti, Francs 
DKK Denmark, Kroner 
DOP Dominican Republic, Pesos 
DZD Algeria, Algeria Dinars 
EEK Estonia, Krooni 
EGP Egypt, Pounds 
ERN Eritrea, Nakfa 
ETB Ethiopia, Birr 
EUR Euro Member Countries, Euro 
FJD Fiji, Dollars 
FKP Falkland Islands (Malvinas), Pounds 
GBP United Kingdom, Pounds 
GEL Georgia, Lari 
GHS Ghana, Cedis 
GIP Gibraltar, Pounds 
GMD Gambia, Dalasi 
GNF Guinea, Francs 
GTQ Guatemala, Quetzales 
GWP Guinea-Bissau Peso
GYD Guyana, Dollars 
HKD Hong Kong, Dollars 
HNL Honduras, Lempiras 
HRK Croatia, Kuna 
HTG Haiti, Gourdes 
HUF Hungary, Forint 
IDR Indonesia, Rupiahs 
ILS Israel, New Shekels 
INR India, Rupees 
IQD Iraq, Dinars 
IRR Iran, Rials 
ISK Iceland, Kronur  
JMD Jamaica, Dollars 
JOD Jordan, Dinars 
JPY Japan, Yen 
KES Kenya, Shillings 
KGS Kyrgyzstan, Soms 
KHR Cambodia, Riels 
KMF Comoros, Francs 
KPW Korea (North), Won 
KRW Korea (South), Won 
KWD Kuwait, Dinars 
KYD Cayman Islands, Dollars 
KZT Kazakstan, Tenge 
LAK Laos, Kips 
LBP Lebanon, Pounds 
LKR Sri Lanka, Rupees 
LRD Liberia, Dollars 
LSL Lesotho, Maloti 
LTL Lithuania, Litai 
LVL Latvia, Lati 
LYD Libya, Dinars 
MAD Morocco, Dirhams 
MDL Moldova, Lei 
MGA Madagascar, Malagasy Ariary 
MKD Macedonia, Denars 
MMK Myanmar (Burma), Kyats 
MNT Mongolia, Tugriks 
MOP Macau, Patacas 
MRO Mauritania, Ouguiyas 
MTL Malta, Liri 
MUR Mauritius, Rupees 
MVR Maldives (Maldive Islands), Rufiyaa 
MWK Malawi, Kwachas 
MXN Mexico, Pesos 
MXV Mexico, Mexican Unidad de Inversion
MYR Malaysia, Ringgits 
MZN Mozambique, Meticais 
NAD Namibia, Dollars 
NGN Nigeria, Nairas 
NIO Nicaragua, Gold Cordobas 
NOK Norway, Krone 
NPR Nepal, Nepal Rupees 
NZD New Zealand, Dollars 
OMR Oman, Rials 
PAB Panama, Balboa 
PEN Peru, Nuevos Soles 
PGK Papua New Guinea, Kina 
PHP Philippines, Pesos 
PKR Pakistan, Rupees 
PLN Poland, Zlotych 
PYG Paraguay, Guarani 
QAR Qatar, Rials 
RON Romania, New Lei 
RSD Serbian Dinar
RUB Russia, Rubles 
RWF Rwanda, Rwanda Francs 
SAR Saudi Arabia, Riyals 
SBD Solomon Islands, Dollars 
SCR Seychelles, Rupees 
SDG Sudan, Dinars 
SEK Sweden, Kronor 
SGD Singapore, Dollars 
SHP Saint Helena, Pounds 
SLL Sierra Leone, Leones 
SOS Somalia, Shillings 
SRD Suriname, Dollar 
STD São Tome and Principe, Dobras 
SVC El Salvador, Colones 
SYP Syria, Pounds 
SZL Swaziland, Emalangeni 
THB Thailand, Baht 
TJS Tajikistan, Somoni 
TMT Turkmenistan, Manats 
TND Tunisia, Dinars 
TOP Tonga, Pa'anga 
TRY Turkey, Liras 
TTD Trinidad and Tobago, Dollars 
TWD Taiwan, New Dollars 
TZS Tanzania, Shillings 
UAH Ukraine, Hryvnia 
UGX Uganda, Shillings 
USD United States of America, Dollars 
UYU Uruguay, Pesos 
UZS Uzbekistan, Sums 
VEF Venezuela, Bolivares 
VND Viet Nam, Dong 
VUV Vanuatu, Vatu 
WST Samoa, Tala 
XAF Communauté Financière Africaine BEAC, Francs 
XCD East Caribbean Dollars 
XOF Communauté Financière Africaine BCEAO, Francs 
XPD Palladium Ounces 
XPF Comptoirs Français du Pacifique Francs 
YER Yemen, Rials 
ZAR South Africa, Rand 
ZMK Zambia, Kwacha 
ZWL Zimbabwe, Zimbabwe Dollars 
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'currCode_Type')
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2013/05/23/eD/KodyCECHKRAJOW/KodyCechKrajow_v3-0E.xsd', 538, 1)
    _Documentation = "\n\t\t\tThe appropriate currency code from the ISO 4217 three-byte alpha version for the currency in which a monetary amount is expressed. \nValid entries are:\nAED United Arab Emirates, Dirhams \nAFN Afghanistan, Afghanis \nALL Albania, Leke \nAMD Armenia, Drams \nANG Netherlands Antilles, Guilders \nAOA Angola, Kwanza \nARS Argentina, Pesos \nAUD Australia, Dollars \nAWG Aruba, Guilders \nAZN Azerbaijan, Manats \nBAM Bosnia and Herzegovina, Convertible Marka \nBBD Barbados, Dollars \nBDT Bangladesh, Taka \nBGN Bulgaria, Leva \nBHD Bahrain, Dinars \nBIF Burundi, Francs \nBMD Bermuda, Dollars \nBND Brunei Darussalam, Dollars \nBOB Bolivia, Bolivianos \nBOV Bolivia, Mvdol\nBRL Brazil, Brazil Real \nBSD Bahamas, Dollars \nBTN Bhutan, Ngultrum \nBWP Botswana, Pulas \nBYR Belarus, Rubles \nBZD Belize, Dollars \nCAD Canada, Dollars \nCDF Congo/Kinshasa, Congolese Francs \nCHF Switzerland, Francs \nCLF Chile, Unidades de fomento \nCLP Chile, Pesos \nCNY China, Yuan Renminbi \nCOP Colombia, Pesos \nCOU Colombia, Unidad de Valor Real\nCRC Costa Rica, Colones \nCUC Cuba, Convertible Pesos \nCUP Cuba, Pesos \nCVE Cape Verde, Escudos \nCZK Czech Republic, Koruny \nDJF Djibouti, Francs \nDKK Denmark, Kroner \nDOP Dominican Republic, Pesos \nDZD Algeria, Algeria Dinars \nEEK Estonia, Krooni \nEGP Egypt, Pounds \nERN Eritrea, Nakfa \nETB Ethiopia, Birr \nEUR Euro Member Countries, Euro \nFJD Fiji, Dollars \nFKP Falkland Islands (Malvinas), Pounds \nGBP United Kingdom, Pounds \nGEL Georgia, Lari \nGHS Ghana, Cedis \nGIP Gibraltar, Pounds \nGMD Gambia, Dalasi \nGNF Guinea, Francs \nGTQ Guatemala, Quetzales \nGWP Guinea-Bissau Peso\nGYD Guyana, Dollars \nHKD Hong Kong, Dollars \nHNL Honduras, Lempiras \nHRK Croatia, Kuna \nHTG Haiti, Gourdes \nHUF Hungary, Forint \nIDR Indonesia, Rupiahs \nILS Israel, New Shekels \nINR India, Rupees \nIQD Iraq, Dinars \nIRR Iran, Rials \nISK Iceland, Kronur  \nJMD Jamaica, Dollars \nJOD Jordan, Dinars \nJPY Japan, Yen \nKES Kenya, Shillings \nKGS Kyrgyzstan, Soms \nKHR Cambodia, Riels \nKMF Comoros, Francs \nKPW Korea (North), Won \nKRW Korea (South), Won \nKWD Kuwait, Dinars \nKYD Cayman Islands, Dollars \nKZT Kazakstan, Tenge \nLAK Laos, Kips \nLBP Lebanon, Pounds \nLKR Sri Lanka, Rupees \nLRD Liberia, Dollars \nLSL Lesotho, Maloti \nLTL Lithuania, Litai \nLVL Latvia, Lati \nLYD Libya, Dinars \nMAD Morocco, Dirhams \nMDL Moldova, Lei \nMGA Madagascar, Malagasy Ariary \nMKD Macedonia, Denars \nMMK Myanmar (Burma), Kyats \nMNT Mongolia, Tugriks \nMOP Macau, Patacas \nMRO Mauritania, Ouguiyas \nMTL Malta, Liri \nMUR Mauritius, Rupees \nMVR Maldives (Maldive Islands), Rufiyaa \nMWK Malawi, Kwachas \nMXN Mexico, Pesos \nMXV Mexico, Mexican Unidad de Inversion\nMYR Malaysia, Ringgits \nMZN Mozambique, Meticais \nNAD Namibia, Dollars \nNGN Nigeria, Nairas \nNIO Nicaragua, Gold Cordobas \nNOK Norway, Krone \nNPR Nepal, Nepal Rupees \nNZD New Zealand, Dollars \nOMR Oman, Rials \nPAB Panama, Balboa \nPEN Peru, Nuevos Soles \nPGK Papua New Guinea, Kina \nPHP Philippines, Pesos \nPKR Pakistan, Rupees \nPLN Poland, Zlotych \nPYG Paraguay, Guarani \nQAR Qatar, Rials \nRON Romania, New Lei \nRSD Serbian Dinar\nRUB Russia, Rubles \nRWF Rwanda, Rwanda Francs \nSAR Saudi Arabia, Riyals \nSBD Solomon Islands, Dollars \nSCR Seychelles, Rupees \nSDG Sudan, Dinars \nSEK Sweden, Kronor \nSGD Singapore, Dollars \nSHP Saint Helena, Pounds \nSLL Sierra Leone, Leones \nSOS Somalia, Shillings \nSRD Suriname, Dollar \nSTD S\xe3o Tome and Principe, Dobras \nSVC El Salvador, Colones \nSYP Syria, Pounds \nSZL Swaziland, Emalangeni \nTHB Thailand, Baht \nTJS Tajikistan, Somoni \nTMT Turkmenistan, Manats \nTND Tunisia, Dinars \nTOP Tonga, Pa'anga \nTRY Turkey, Liras \nTTD Trinidad and Tobago, Dollars \nTWD Taiwan, New Dollars \nTZS Tanzania, Shillings \nUAH Ukraine, Hryvnia \nUGX Uganda, Shillings \nUSD United States of America, Dollars \nUYU Uruguay, Pesos \nUZS Uzbekistan, Sums \nVEF Venezuela, Bolivares \nVND Viet Nam, Dong \nVUV Vanuatu, Vatu \nWST Samoa, Tala \nXAF Communaut\xe9 Financi\xe8re Africaine BEAC, Francs \nXCD East Caribbean Dollars \nXOF Communaut\xe9 Financi\xe8re Africaine BCEAO, Francs \nXPD Palladium Ounces \nXPF Comptoirs Fran\xe7ais du Pacifique Francs \nYER Yemen, Rials \nZAR South Africa, Rand \nZMK Zambia, Kwacha \nZWL Zimbabwe, Zimbabwe Dollars \n\t\t\t"
currCode_Type._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=currCode_Type, enum_prefix=None)
currCode_Type.AED = currCode_Type._CF_enumeration.addEnumeration(unicode_value='AED', tag='AED')
currCode_Type.AFN = currCode_Type._CF_enumeration.addEnumeration(unicode_value='AFN', tag='AFN')
currCode_Type.ALL = currCode_Type._CF_enumeration.addEnumeration(unicode_value='ALL', tag='ALL')
currCode_Type.AMD = currCode_Type._CF_enumeration.addEnumeration(unicode_value='AMD', tag='AMD')
currCode_Type.ANG = currCode_Type._CF_enumeration.addEnumeration(unicode_value='ANG', tag='ANG')
currCode_Type.AOA = currCode_Type._CF_enumeration.addEnumeration(unicode_value='AOA', tag='AOA')
currCode_Type.ARS = currCode_Type._CF_enumeration.addEnumeration(unicode_value='ARS', tag='ARS')
currCode_Type.AUD = currCode_Type._CF_enumeration.addEnumeration(unicode_value='AUD', tag='AUD')
currCode_Type.AWG = currCode_Type._CF_enumeration.addEnumeration(unicode_value='AWG', tag='AWG')
currCode_Type.AZN = currCode_Type._CF_enumeration.addEnumeration(unicode_value='AZN', tag='AZN')
currCode_Type.BAM = currCode_Type._CF_enumeration.addEnumeration(unicode_value='BAM', tag='BAM')
currCode_Type.BBD = currCode_Type._CF_enumeration.addEnumeration(unicode_value='BBD', tag='BBD')
currCode_Type.BDT = currCode_Type._CF_enumeration.addEnumeration(unicode_value='BDT', tag='BDT')
currCode_Type.BGN = currCode_Type._CF_enumeration.addEnumeration(unicode_value='BGN', tag='BGN')
currCode_Type.BHD = currCode_Type._CF_enumeration.addEnumeration(unicode_value='BHD', tag='BHD')
currCode_Type.BIF = currCode_Type._CF_enumeration.addEnumeration(unicode_value='BIF', tag='BIF')
currCode_Type.BMD = currCode_Type._CF_enumeration.addEnumeration(unicode_value='BMD', tag='BMD')
currCode_Type.BND = currCode_Type._CF_enumeration.addEnumeration(unicode_value='BND', tag='BND')
currCode_Type.BOB = currCode_Type._CF_enumeration.addEnumeration(unicode_value='BOB', tag='BOB')
currCode_Type.BOV = currCode_Type._CF_enumeration.addEnumeration(unicode_value='BOV', tag='BOV')
currCode_Type.BRL = currCode_Type._CF_enumeration.addEnumeration(unicode_value='BRL', tag='BRL')
currCode_Type.BSD = currCode_Type._CF_enumeration.addEnumeration(unicode_value='BSD', tag='BSD')
currCode_Type.BTN = currCode_Type._CF_enumeration.addEnumeration(unicode_value='BTN', tag='BTN')
currCode_Type.BWP = currCode_Type._CF_enumeration.addEnumeration(unicode_value='BWP', tag='BWP')
currCode_Type.BYR = currCode_Type._CF_enumeration.addEnumeration(unicode_value='BYR', tag='BYR')
currCode_Type.BZD = currCode_Type._CF_enumeration.addEnumeration(unicode_value='BZD', tag='BZD')
currCode_Type.CAD = currCode_Type._CF_enumeration.addEnumeration(unicode_value='CAD', tag='CAD')
currCode_Type.CDF = currCode_Type._CF_enumeration.addEnumeration(unicode_value='CDF', tag='CDF')
currCode_Type.CHF = currCode_Type._CF_enumeration.addEnumeration(unicode_value='CHF', tag='CHF')
currCode_Type.CLF = currCode_Type._CF_enumeration.addEnumeration(unicode_value='CLF', tag='CLF')
currCode_Type.CLP = currCode_Type._CF_enumeration.addEnumeration(unicode_value='CLP', tag='CLP')
currCode_Type.CNY = currCode_Type._CF_enumeration.addEnumeration(unicode_value='CNY', tag='CNY')
currCode_Type.COP = currCode_Type._CF_enumeration.addEnumeration(unicode_value='COP', tag='COP')
currCode_Type.COU = currCode_Type._CF_enumeration.addEnumeration(unicode_value='COU', tag='COU')
currCode_Type.CRC = currCode_Type._CF_enumeration.addEnumeration(unicode_value='CRC', tag='CRC')
currCode_Type.CUC = currCode_Type._CF_enumeration.addEnumeration(unicode_value='CUC', tag='CUC')
currCode_Type.CUP = currCode_Type._CF_enumeration.addEnumeration(unicode_value='CUP', tag='CUP')
currCode_Type.CVE = currCode_Type._CF_enumeration.addEnumeration(unicode_value='CVE', tag='CVE')
currCode_Type.CZK = currCode_Type._CF_enumeration.addEnumeration(unicode_value='CZK', tag='CZK')
currCode_Type.DJF = currCode_Type._CF_enumeration.addEnumeration(unicode_value='DJF', tag='DJF')
currCode_Type.DKK = currCode_Type._CF_enumeration.addEnumeration(unicode_value='DKK', tag='DKK')
currCode_Type.DOP = currCode_Type._CF_enumeration.addEnumeration(unicode_value='DOP', tag='DOP')
currCode_Type.DZD = currCode_Type._CF_enumeration.addEnumeration(unicode_value='DZD', tag='DZD')
currCode_Type.EEK = currCode_Type._CF_enumeration.addEnumeration(unicode_value='EEK', tag='EEK')
currCode_Type.EGP = currCode_Type._CF_enumeration.addEnumeration(unicode_value='EGP', tag='EGP')
currCode_Type.ERN = currCode_Type._CF_enumeration.addEnumeration(unicode_value='ERN', tag='ERN')
currCode_Type.ETB = currCode_Type._CF_enumeration.addEnumeration(unicode_value='ETB', tag='ETB')
currCode_Type.EUR = currCode_Type._CF_enumeration.addEnumeration(unicode_value='EUR', tag='EUR')
currCode_Type.FJD = currCode_Type._CF_enumeration.addEnumeration(unicode_value='FJD', tag='FJD')
currCode_Type.FKP = currCode_Type._CF_enumeration.addEnumeration(unicode_value='FKP', tag='FKP')
currCode_Type.GBP = currCode_Type._CF_enumeration.addEnumeration(unicode_value='GBP', tag='GBP')
currCode_Type.GEL = currCode_Type._CF_enumeration.addEnumeration(unicode_value='GEL', tag='GEL')
currCode_Type.GHS = currCode_Type._CF_enumeration.addEnumeration(unicode_value='GHS', tag='GHS')
currCode_Type.GIP = currCode_Type._CF_enumeration.addEnumeration(unicode_value='GIP', tag='GIP')
currCode_Type.GMD = currCode_Type._CF_enumeration.addEnumeration(unicode_value='GMD', tag='GMD')
currCode_Type.GNF = currCode_Type._CF_enumeration.addEnumeration(unicode_value='GNF', tag='GNF')
currCode_Type.GTQ = currCode_Type._CF_enumeration.addEnumeration(unicode_value='GTQ', tag='GTQ')
currCode_Type.GWP = currCode_Type._CF_enumeration.addEnumeration(unicode_value='GWP', tag='GWP')
currCode_Type.GYD = currCode_Type._CF_enumeration.addEnumeration(unicode_value='GYD', tag='GYD')
currCode_Type.HKD = currCode_Type._CF_enumeration.addEnumeration(unicode_value='HKD', tag='HKD')
currCode_Type.HNL = currCode_Type._CF_enumeration.addEnumeration(unicode_value='HNL', tag='HNL')
currCode_Type.HRK = currCode_Type._CF_enumeration.addEnumeration(unicode_value='HRK', tag='HRK')
currCode_Type.HTG = currCode_Type._CF_enumeration.addEnumeration(unicode_value='HTG', tag='HTG')
currCode_Type.HUF = currCode_Type._CF_enumeration.addEnumeration(unicode_value='HUF', tag='HUF')
currCode_Type.IDR = currCode_Type._CF_enumeration.addEnumeration(unicode_value='IDR', tag='IDR')
currCode_Type.ILS = currCode_Type._CF_enumeration.addEnumeration(unicode_value='ILS', tag='ILS')
currCode_Type.INR = currCode_Type._CF_enumeration.addEnumeration(unicode_value='INR', tag='INR')
currCode_Type.IQD = currCode_Type._CF_enumeration.addEnumeration(unicode_value='IQD', tag='IQD')
currCode_Type.IRR = currCode_Type._CF_enumeration.addEnumeration(unicode_value='IRR', tag='IRR')
currCode_Type.ISK = currCode_Type._CF_enumeration.addEnumeration(unicode_value='ISK', tag='ISK')
currCode_Type.JMD = currCode_Type._CF_enumeration.addEnumeration(unicode_value='JMD', tag='JMD')
currCode_Type.JOD = currCode_Type._CF_enumeration.addEnumeration(unicode_value='JOD', tag='JOD')
currCode_Type.JPY = currCode_Type._CF_enumeration.addEnumeration(unicode_value='JPY', tag='JPY')
currCode_Type.KES = currCode_Type._CF_enumeration.addEnumeration(unicode_value='KES', tag='KES')
currCode_Type.KGS = currCode_Type._CF_enumeration.addEnumeration(unicode_value='KGS', tag='KGS')
currCode_Type.KHR = currCode_Type._CF_enumeration.addEnumeration(unicode_value='KHR', tag='KHR')
currCode_Type.KMF = currCode_Type._CF_enumeration.addEnumeration(unicode_value='KMF', tag='KMF')
currCode_Type.KPW = currCode_Type._CF_enumeration.addEnumeration(unicode_value='KPW', tag='KPW')
currCode_Type.KRW = currCode_Type._CF_enumeration.addEnumeration(unicode_value='KRW', tag='KRW')
currCode_Type.KWD = currCode_Type._CF_enumeration.addEnumeration(unicode_value='KWD', tag='KWD')
currCode_Type.KYD = currCode_Type._CF_enumeration.addEnumeration(unicode_value='KYD', tag='KYD')
currCode_Type.KZT = currCode_Type._CF_enumeration.addEnumeration(unicode_value='KZT', tag='KZT')
currCode_Type.LAK = currCode_Type._CF_enumeration.addEnumeration(unicode_value='LAK', tag='LAK')
currCode_Type.LBP = currCode_Type._CF_enumeration.addEnumeration(unicode_value='LBP', tag='LBP')
currCode_Type.LKR = currCode_Type._CF_enumeration.addEnumeration(unicode_value='LKR', tag='LKR')
currCode_Type.LRD = currCode_Type._CF_enumeration.addEnumeration(unicode_value='LRD', tag='LRD')
currCode_Type.LSL = currCode_Type._CF_enumeration.addEnumeration(unicode_value='LSL', tag='LSL')
currCode_Type.LTL = currCode_Type._CF_enumeration.addEnumeration(unicode_value='LTL', tag='LTL')
currCode_Type.LVL = currCode_Type._CF_enumeration.addEnumeration(unicode_value='LVL', tag='LVL')
currCode_Type.LYD = currCode_Type._CF_enumeration.addEnumeration(unicode_value='LYD', tag='LYD')
currCode_Type.MAD = currCode_Type._CF_enumeration.addEnumeration(unicode_value='MAD', tag='MAD')
currCode_Type.MDL = currCode_Type._CF_enumeration.addEnumeration(unicode_value='MDL', tag='MDL')
currCode_Type.MGA = currCode_Type._CF_enumeration.addEnumeration(unicode_value='MGA', tag='MGA')
currCode_Type.MKD = currCode_Type._CF_enumeration.addEnumeration(unicode_value='MKD', tag='MKD')
currCode_Type.MMK = currCode_Type._CF_enumeration.addEnumeration(unicode_value='MMK', tag='MMK')
currCode_Type.MNT = currCode_Type._CF_enumeration.addEnumeration(unicode_value='MNT', tag='MNT')
currCode_Type.MOP = currCode_Type._CF_enumeration.addEnumeration(unicode_value='MOP', tag='MOP')
currCode_Type.MRO = currCode_Type._CF_enumeration.addEnumeration(unicode_value='MRO', tag='MRO')
currCode_Type.MUR = currCode_Type._CF_enumeration.addEnumeration(unicode_value='MUR', tag='MUR')
currCode_Type.MVR = currCode_Type._CF_enumeration.addEnumeration(unicode_value='MVR', tag='MVR')
currCode_Type.MWK = currCode_Type._CF_enumeration.addEnumeration(unicode_value='MWK', tag='MWK')
currCode_Type.MXN = currCode_Type._CF_enumeration.addEnumeration(unicode_value='MXN', tag='MXN')
currCode_Type.MXV = currCode_Type._CF_enumeration.addEnumeration(unicode_value='MXV', tag='MXV')
currCode_Type.MYR = currCode_Type._CF_enumeration.addEnumeration(unicode_value='MYR', tag='MYR')
currCode_Type.MZN = currCode_Type._CF_enumeration.addEnumeration(unicode_value='MZN', tag='MZN')
currCode_Type.NAD = currCode_Type._CF_enumeration.addEnumeration(unicode_value='NAD', tag='NAD')
currCode_Type.NGN = currCode_Type._CF_enumeration.addEnumeration(unicode_value='NGN', tag='NGN')
currCode_Type.NIO = currCode_Type._CF_enumeration.addEnumeration(unicode_value='NIO', tag='NIO')
currCode_Type.NOK = currCode_Type._CF_enumeration.addEnumeration(unicode_value='NOK', tag='NOK')
currCode_Type.NPR = currCode_Type._CF_enumeration.addEnumeration(unicode_value='NPR', tag='NPR')
currCode_Type.NZD = currCode_Type._CF_enumeration.addEnumeration(unicode_value='NZD', tag='NZD')
currCode_Type.OMR = currCode_Type._CF_enumeration.addEnumeration(unicode_value='OMR', tag='OMR')
currCode_Type.PAB = currCode_Type._CF_enumeration.addEnumeration(unicode_value='PAB', tag='PAB')
currCode_Type.PEN = currCode_Type._CF_enumeration.addEnumeration(unicode_value='PEN', tag='PEN')
currCode_Type.PGK = currCode_Type._CF_enumeration.addEnumeration(unicode_value='PGK', tag='PGK')
currCode_Type.PHP = currCode_Type._CF_enumeration.addEnumeration(unicode_value='PHP', tag='PHP')
currCode_Type.PKR = currCode_Type._CF_enumeration.addEnumeration(unicode_value='PKR', tag='PKR')
currCode_Type.PLN = currCode_Type._CF_enumeration.addEnumeration(unicode_value='PLN', tag='PLN')
currCode_Type.PYG = currCode_Type._CF_enumeration.addEnumeration(unicode_value='PYG', tag='PYG')
currCode_Type.QAR = currCode_Type._CF_enumeration.addEnumeration(unicode_value='QAR', tag='QAR')
currCode_Type.RON = currCode_Type._CF_enumeration.addEnumeration(unicode_value='RON', tag='RON')
currCode_Type.RSD = currCode_Type._CF_enumeration.addEnumeration(unicode_value='RSD', tag='RSD')
currCode_Type.RUB = currCode_Type._CF_enumeration.addEnumeration(unicode_value='RUB', tag='RUB')
currCode_Type.RWF = currCode_Type._CF_enumeration.addEnumeration(unicode_value='RWF', tag='RWF')
currCode_Type.SAR = currCode_Type._CF_enumeration.addEnumeration(unicode_value='SAR', tag='SAR')
currCode_Type.SBD = currCode_Type._CF_enumeration.addEnumeration(unicode_value='SBD', tag='SBD')
currCode_Type.SCR = currCode_Type._CF_enumeration.addEnumeration(unicode_value='SCR', tag='SCR')
currCode_Type.SDG = currCode_Type._CF_enumeration.addEnumeration(unicode_value='SDG', tag='SDG')
currCode_Type.SEK = currCode_Type._CF_enumeration.addEnumeration(unicode_value='SEK', tag='SEK')
currCode_Type.SGD = currCode_Type._CF_enumeration.addEnumeration(unicode_value='SGD', tag='SGD')
currCode_Type.SHP = currCode_Type._CF_enumeration.addEnumeration(unicode_value='SHP', tag='SHP')
currCode_Type.SLL = currCode_Type._CF_enumeration.addEnumeration(unicode_value='SLL', tag='SLL')
currCode_Type.SOS = currCode_Type._CF_enumeration.addEnumeration(unicode_value='SOS', tag='SOS')
currCode_Type.SRD = currCode_Type._CF_enumeration.addEnumeration(unicode_value='SRD', tag='SRD')
currCode_Type.STD = currCode_Type._CF_enumeration.addEnumeration(unicode_value='STD', tag='STD')
currCode_Type.SVC = currCode_Type._CF_enumeration.addEnumeration(unicode_value='SVC', tag='SVC')
currCode_Type.SYP = currCode_Type._CF_enumeration.addEnumeration(unicode_value='SYP', tag='SYP')
currCode_Type.SZL = currCode_Type._CF_enumeration.addEnumeration(unicode_value='SZL', tag='SZL')
currCode_Type.THB = currCode_Type._CF_enumeration.addEnumeration(unicode_value='THB', tag='THB')
currCode_Type.TJS = currCode_Type._CF_enumeration.addEnumeration(unicode_value='TJS', tag='TJS')
currCode_Type.TMT = currCode_Type._CF_enumeration.addEnumeration(unicode_value='TMT', tag='TMT')
currCode_Type.TND = currCode_Type._CF_enumeration.addEnumeration(unicode_value='TND', tag='TND')
currCode_Type.TOP = currCode_Type._CF_enumeration.addEnumeration(unicode_value='TOP', tag='TOP')
currCode_Type.TRY = currCode_Type._CF_enumeration.addEnumeration(unicode_value='TRY', tag='TRY')
currCode_Type.TTD = currCode_Type._CF_enumeration.addEnumeration(unicode_value='TTD', tag='TTD')
currCode_Type.TVD = currCode_Type._CF_enumeration.addEnumeration(unicode_value='TVD', tag='TVD')
currCode_Type.TWD = currCode_Type._CF_enumeration.addEnumeration(unicode_value='TWD', tag='TWD')
currCode_Type.TZS = currCode_Type._CF_enumeration.addEnumeration(unicode_value='TZS', tag='TZS')
currCode_Type.UAH = currCode_Type._CF_enumeration.addEnumeration(unicode_value='UAH', tag='UAH')
currCode_Type.UGX = currCode_Type._CF_enumeration.addEnumeration(unicode_value='UGX', tag='UGX')
currCode_Type.USD = currCode_Type._CF_enumeration.addEnumeration(unicode_value='USD', tag='USD')
currCode_Type.UYU = currCode_Type._CF_enumeration.addEnumeration(unicode_value='UYU', tag='UYU')
currCode_Type.UZS = currCode_Type._CF_enumeration.addEnumeration(unicode_value='UZS', tag='UZS')
currCode_Type.VEF = currCode_Type._CF_enumeration.addEnumeration(unicode_value='VEF', tag='VEF')
currCode_Type.VND = currCode_Type._CF_enumeration.addEnumeration(unicode_value='VND', tag='VND')
currCode_Type.VUV = currCode_Type._CF_enumeration.addEnumeration(unicode_value='VUV', tag='VUV')
currCode_Type.WST = currCode_Type._CF_enumeration.addEnumeration(unicode_value='WST', tag='WST')
currCode_Type.XAF = currCode_Type._CF_enumeration.addEnumeration(unicode_value='XAF', tag='XAF')
currCode_Type.XCD = currCode_Type._CF_enumeration.addEnumeration(unicode_value='XCD', tag='XCD')
currCode_Type.XOF = currCode_Type._CF_enumeration.addEnumeration(unicode_value='XOF', tag='XOF')
currCode_Type.XPD = currCode_Type._CF_enumeration.addEnumeration(unicode_value='XPD', tag='XPD')
currCode_Type.XPF = currCode_Type._CF_enumeration.addEnumeration(unicode_value='XPF', tag='XPF')
currCode_Type.YER = currCode_Type._CF_enumeration.addEnumeration(unicode_value='YER', tag='YER')
currCode_Type.ZAR = currCode_Type._CF_enumeration.addEnumeration(unicode_value='ZAR', tag='ZAR')
currCode_Type.ZMK = currCode_Type._CF_enumeration.addEnumeration(unicode_value='ZMK', tag='ZMK')
currCode_Type.ZWL = currCode_Type._CF_enumeration.addEnumeration(unicode_value='ZWL', tag='ZWL')
currCode_Type._InitializeFacetMap(currCode_Type._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'currCode_Type', currCode_Type)
_module_typeBindings.currCode_Type = currCode_Type

# Atomic simple type: {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2013/05/23/eD/KodyCECHKRAJOW/}MSCurrCode_Type
class MSCurrCode_Type (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
			The appropriate currency code from the ISO 4217 three-byte alpha version for the currency in which a monetary amount is expressed. Currency codes are limited to those of Member States.
Valid entries are:
BGN Bulgaria, Leva 
CZK Czech Republic, Koruny 
DKK Denmark, Kroner 
EEK Estonia, Krooni 
EUR Euro Member Countries, Euro 
GBP United Kingdom, Pounds 
HRK Croatia, Kuna 
HUF Hungary, Forint 
LTL Lithuania, Litai 
LVL Latvia, Lati 
PLN Poland, Zlotych 
RON Romania, New Lei 
SEK Sweden, Kronor 
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MSCurrCode_Type')
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2013/05/23/eD/KodyCECHKRAJOW/KodyCechKrajow_v3-0E.xsd', 880, 1)
    _Documentation = '\n\t\t\tThe appropriate currency code from the ISO 4217 three-byte alpha version for the currency in which a monetary amount is expressed. Currency codes are limited to those of Member States.\nValid entries are:\nBGN Bulgaria, Leva \nCZK Czech Republic, Koruny \nDKK Denmark, Kroner \nEEK Estonia, Krooni \nEUR Euro Member Countries, Euro \nGBP United Kingdom, Pounds \nHRK Croatia, Kuna \nHUF Hungary, Forint \nLTL Lithuania, Litai \nLVL Latvia, Lati \nPLN Poland, Zlotych \nRON Romania, New Lei \nSEK Sweden, Kronor \n\t\t\t'
MSCurrCode_Type._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MSCurrCode_Type, enum_prefix=None)
MSCurrCode_Type.BGN = MSCurrCode_Type._CF_enumeration.addEnumeration(unicode_value='BGN', tag='BGN')
MSCurrCode_Type.CZK = MSCurrCode_Type._CF_enumeration.addEnumeration(unicode_value='CZK', tag='CZK')
MSCurrCode_Type.DKK = MSCurrCode_Type._CF_enumeration.addEnumeration(unicode_value='DKK', tag='DKK')
MSCurrCode_Type.EEK = MSCurrCode_Type._CF_enumeration.addEnumeration(unicode_value='EEK', tag='EEK')
MSCurrCode_Type.EUR = MSCurrCode_Type._CF_enumeration.addEnumeration(unicode_value='EUR', tag='EUR')
MSCurrCode_Type.GBP = MSCurrCode_Type._CF_enumeration.addEnumeration(unicode_value='GBP', tag='GBP')
MSCurrCode_Type.HRK = MSCurrCode_Type._CF_enumeration.addEnumeration(unicode_value='HRK', tag='HRK')
MSCurrCode_Type.HUF = MSCurrCode_Type._CF_enumeration.addEnumeration(unicode_value='HUF', tag='HUF')
MSCurrCode_Type.LTL = MSCurrCode_Type._CF_enumeration.addEnumeration(unicode_value='LTL', tag='LTL')
MSCurrCode_Type.LVL = MSCurrCode_Type._CF_enumeration.addEnumeration(unicode_value='LVL', tag='LVL')
MSCurrCode_Type.PLN = MSCurrCode_Type._CF_enumeration.addEnumeration(unicode_value='PLN', tag='PLN')
MSCurrCode_Type.RON = MSCurrCode_Type._CF_enumeration.addEnumeration(unicode_value='RON', tag='RON')
MSCurrCode_Type.SEK = MSCurrCode_Type._CF_enumeration.addEnumeration(unicode_value='SEK', tag='SEK')
MSCurrCode_Type._InitializeFacetMap(MSCurrCode_Type._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'MSCurrCode_Type', MSCurrCode_Type)
_module_typeBindings.MSCurrCode_Type = MSCurrCode_Type

# Atomic simple type: {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2013/05/23/eD/KodyCECHKRAJOW/}MSCurrCodeExPLN_Type
class MSCurrCodeExPLN_Type (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
			The appropriate currency code from the ISO 4217 three-byte alpha version for the currency in which a monetary amount is expressed. Currency codes are limited to those of Member States.
Valid entries are:
BGN Bulgaria, Leva 
CZK Czech Republic, Koruny 
DKK Denmark, Kroner 
EEK Estonia, Krooni 
EUR Euro Member Countries, Euro 
GBP United Kingdom, Pounds 
HRK Croatia, Kuna 
HUF Hungary, Forint 
LTL Lithuania, Litai 
LVL Latvia, Lati 
RON Romania, New Lei 
SEK Sweden, Kronor 
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MSCurrCodeExPLN_Type')
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2013/05/23/eD/KodyCECHKRAJOW/KodyCechKrajow_v3-0E.xsd', 916, 1)
    _Documentation = '\n\t\t\tThe appropriate currency code from the ISO 4217 three-byte alpha version for the currency in which a monetary amount is expressed. Currency codes are limited to those of Member States.\nValid entries are:\nBGN Bulgaria, Leva \nCZK Czech Republic, Koruny \nDKK Denmark, Kroner \nEEK Estonia, Krooni \nEUR Euro Member Countries, Euro \nGBP United Kingdom, Pounds \nHRK Croatia, Kuna \nHUF Hungary, Forint \nLTL Lithuania, Litai \nLVL Latvia, Lati \nRON Romania, New Lei \nSEK Sweden, Kronor \n\t\t\t'
MSCurrCodeExPLN_Type._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MSCurrCodeExPLN_Type, enum_prefix=None)
MSCurrCodeExPLN_Type.BGN = MSCurrCodeExPLN_Type._CF_enumeration.addEnumeration(unicode_value='BGN', tag='BGN')
MSCurrCodeExPLN_Type.CZK = MSCurrCodeExPLN_Type._CF_enumeration.addEnumeration(unicode_value='CZK', tag='CZK')
MSCurrCodeExPLN_Type.DKK = MSCurrCodeExPLN_Type._CF_enumeration.addEnumeration(unicode_value='DKK', tag='DKK')
MSCurrCodeExPLN_Type.EEK = MSCurrCodeExPLN_Type._CF_enumeration.addEnumeration(unicode_value='EEK', tag='EEK')
MSCurrCodeExPLN_Type.EUR = MSCurrCodeExPLN_Type._CF_enumeration.addEnumeration(unicode_value='EUR', tag='EUR')
MSCurrCodeExPLN_Type.GBP = MSCurrCodeExPLN_Type._CF_enumeration.addEnumeration(unicode_value='GBP', tag='GBP')
MSCurrCodeExPLN_Type.HRK = MSCurrCodeExPLN_Type._CF_enumeration.addEnumeration(unicode_value='HRK', tag='HRK')
MSCurrCodeExPLN_Type.HUF = MSCurrCodeExPLN_Type._CF_enumeration.addEnumeration(unicode_value='HUF', tag='HUF')
MSCurrCodeExPLN_Type.LTL = MSCurrCodeExPLN_Type._CF_enumeration.addEnumeration(unicode_value='LTL', tag='LTL')
MSCurrCodeExPLN_Type.LVL = MSCurrCodeExPLN_Type._CF_enumeration.addEnumeration(unicode_value='LVL', tag='LVL')
MSCurrCodeExPLN_Type.RON = MSCurrCodeExPLN_Type._CF_enumeration.addEnumeration(unicode_value='RON', tag='RON')
MSCurrCodeExPLN_Type.SEK = MSCurrCodeExPLN_Type._CF_enumeration.addEnumeration(unicode_value='SEK', tag='SEK')
MSCurrCodeExPLN_Type._InitializeFacetMap(MSCurrCodeExPLN_Type._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'MSCurrCodeExPLN_Type', MSCurrCodeExPLN_Type)
_module_typeBindings.MSCurrCodeExPLN_Type = MSCurrCodeExPLN_Type

# Atomic simple type: {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2013/05/23/eD/KodyCECHKRAJOW/}EULanguageCode_Type
class EULanguageCode_Type (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """ The list of official languages of the EU."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'EULanguageCode_Type')
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2013/05/23/eD/KodyCECHKRAJOW/KodyCechKrajow_v3-0E.xsd', 950, 1)
    _Documentation = ' The list of official languages of the EU.'
EULanguageCode_Type._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=EULanguageCode_Type, enum_prefix=None)
EULanguageCode_Type.bg = EULanguageCode_Type._CF_enumeration.addEnumeration(unicode_value='bg', tag='bg')
EULanguageCode_Type.cs = EULanguageCode_Type._CF_enumeration.addEnumeration(unicode_value='cs', tag='cs')
EULanguageCode_Type.da = EULanguageCode_Type._CF_enumeration.addEnumeration(unicode_value='da', tag='da')
EULanguageCode_Type.de = EULanguageCode_Type._CF_enumeration.addEnumeration(unicode_value='de', tag='de')
EULanguageCode_Type.el = EULanguageCode_Type._CF_enumeration.addEnumeration(unicode_value='el', tag='el')
EULanguageCode_Type.en = EULanguageCode_Type._CF_enumeration.addEnumeration(unicode_value='en', tag='en')
EULanguageCode_Type.es = EULanguageCode_Type._CF_enumeration.addEnumeration(unicode_value='es', tag='es')
EULanguageCode_Type.et = EULanguageCode_Type._CF_enumeration.addEnumeration(unicode_value='et', tag='et')
EULanguageCode_Type.fi = EULanguageCode_Type._CF_enumeration.addEnumeration(unicode_value='fi', tag='fi')
EULanguageCode_Type.fr = EULanguageCode_Type._CF_enumeration.addEnumeration(unicode_value='fr', tag='fr')
EULanguageCode_Type.ga = EULanguageCode_Type._CF_enumeration.addEnumeration(unicode_value='ga', tag='ga')
EULanguageCode_Type.hr = EULanguageCode_Type._CF_enumeration.addEnumeration(unicode_value='hr', tag='hr')
EULanguageCode_Type.hu = EULanguageCode_Type._CF_enumeration.addEnumeration(unicode_value='hu', tag='hu')
EULanguageCode_Type.it = EULanguageCode_Type._CF_enumeration.addEnumeration(unicode_value='it', tag='it')
EULanguageCode_Type.lt = EULanguageCode_Type._CF_enumeration.addEnumeration(unicode_value='lt', tag='lt')
EULanguageCode_Type.lv = EULanguageCode_Type._CF_enumeration.addEnumeration(unicode_value='lv', tag='lv')
EULanguageCode_Type.mt = EULanguageCode_Type._CF_enumeration.addEnumeration(unicode_value='mt', tag='mt')
EULanguageCode_Type.nl = EULanguageCode_Type._CF_enumeration.addEnumeration(unicode_value='nl', tag='nl')
EULanguageCode_Type.pl = EULanguageCode_Type._CF_enumeration.addEnumeration(unicode_value='pl', tag='pl')
EULanguageCode_Type.pt = EULanguageCode_Type._CF_enumeration.addEnumeration(unicode_value='pt', tag='pt')
EULanguageCode_Type.ro = EULanguageCode_Type._CF_enumeration.addEnumeration(unicode_value='ro', tag='ro')
EULanguageCode_Type.sk = EULanguageCode_Type._CF_enumeration.addEnumeration(unicode_value='sk', tag='sk')
EULanguageCode_Type.sl = EULanguageCode_Type._CF_enumeration.addEnumeration(unicode_value='sl', tag='sl')
EULanguageCode_Type.sv = EULanguageCode_Type._CF_enumeration.addEnumeration(unicode_value='sv', tag='sv')
EULanguageCode_Type.tr = EULanguageCode_Type._CF_enumeration.addEnumeration(unicode_value='tr', tag='tr')
EULanguageCode_Type._InitializeFacetMap(EULanguageCode_Type._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'EULanguageCode_Type', EULanguageCode_Type)
_module_typeBindings.EULanguageCode_Type = EULanguageCode_Type

# Union simple type: {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2013/05/23/eD/KodyCECHKRAJOW/}CountryCode_Type
# superclasses pyxb.binding.datatypes.anySimpleType
class CountryCode_Type (pyxb.binding.basis.STD_union):

    """Simple type that is a union of CountryCodeExMS_Type, MSCountryCode_Type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CountryCode_Type')
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2013/05/23/eD/KodyCECHKRAJOW/KodyCechKrajow_v3-0E.xsd', 3, 1)
    _Documentation = None

    _MemberTypes = ( CountryCodeExMS_Type, MSCountryCode_Type, )
CountryCode_Type._CF_pattern = pyxb.binding.facets.CF_pattern()
CountryCode_Type._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=CountryCode_Type)
CountryCode_Type.AF = 'AF'                        # originally CountryCodeExMS_Type.AF
CountryCode_Type.AX = 'AX'                        # originally CountryCodeExMS_Type.AX
CountryCode_Type.AL = 'AL'                        # originally CountryCodeExMS_Type.AL
CountryCode_Type.DZ = 'DZ'                        # originally CountryCodeExMS_Type.DZ
CountryCode_Type.AS = 'AS'                        # originally CountryCodeExMS_Type.AS
CountryCode_Type.AD = 'AD'                        # originally CountryCodeExMS_Type.AD
CountryCode_Type.AO = 'AO'                        # originally CountryCodeExMS_Type.AO
CountryCode_Type.AI = 'AI'                        # originally CountryCodeExMS_Type.AI
CountryCode_Type.AQ = 'AQ'                        # originally CountryCodeExMS_Type.AQ
CountryCode_Type.AG = 'AG'                        # originally CountryCodeExMS_Type.AG
CountryCode_Type.AR = 'AR'                        # originally CountryCodeExMS_Type.AR
CountryCode_Type.AM = 'AM'                        # originally CountryCodeExMS_Type.AM
CountryCode_Type.AW = 'AW'                        # originally CountryCodeExMS_Type.AW
CountryCode_Type.AU = 'AU'                        # originally CountryCodeExMS_Type.AU
CountryCode_Type.AZ = 'AZ'                        # originally CountryCodeExMS_Type.AZ
CountryCode_Type.BS = 'BS'                        # originally CountryCodeExMS_Type.BS
CountryCode_Type.BH = 'BH'                        # originally CountryCodeExMS_Type.BH
CountryCode_Type.BD = 'BD'                        # originally CountryCodeExMS_Type.BD
CountryCode_Type.BB = 'BB'                        # originally CountryCodeExMS_Type.BB
CountryCode_Type.BY = 'BY'                        # originally CountryCodeExMS_Type.BY
CountryCode_Type.BZ = 'BZ'                        # originally CountryCodeExMS_Type.BZ
CountryCode_Type.BJ = 'BJ'                        # originally CountryCodeExMS_Type.BJ
CountryCode_Type.BM = 'BM'                        # originally CountryCodeExMS_Type.BM
CountryCode_Type.BT = 'BT'                        # originally CountryCodeExMS_Type.BT
CountryCode_Type.BO = 'BO'                        # originally CountryCodeExMS_Type.BO
CountryCode_Type.BA = 'BA'                        # originally CountryCodeExMS_Type.BA
CountryCode_Type.BW = 'BW'                        # originally CountryCodeExMS_Type.BW
CountryCode_Type.BV = 'BV'                        # originally CountryCodeExMS_Type.BV
CountryCode_Type.BR = 'BR'                        # originally CountryCodeExMS_Type.BR
CountryCode_Type.IO = 'IO'                        # originally CountryCodeExMS_Type.IO
CountryCode_Type.BN = 'BN'                        # originally CountryCodeExMS_Type.BN
CountryCode_Type.BF = 'BF'                        # originally CountryCodeExMS_Type.BF
CountryCode_Type.BI = 'BI'                        # originally CountryCodeExMS_Type.BI
CountryCode_Type.KH = 'KH'                        # originally CountryCodeExMS_Type.KH
CountryCode_Type.CM = 'CM'                        # originally CountryCodeExMS_Type.CM
CountryCode_Type.CA = 'CA'                        # originally CountryCodeExMS_Type.CA
CountryCode_Type.CV = 'CV'                        # originally CountryCodeExMS_Type.CV
CountryCode_Type.KY = 'KY'                        # originally CountryCodeExMS_Type.KY
CountryCode_Type.CF = 'CF'                        # originally CountryCodeExMS_Type.CF
CountryCode_Type.TD = 'TD'                        # originally CountryCodeExMS_Type.TD
CountryCode_Type.CL = 'CL'                        # originally CountryCodeExMS_Type.CL
CountryCode_Type.CN = 'CN'                        # originally CountryCodeExMS_Type.CN
CountryCode_Type.CX = 'CX'                        # originally CountryCodeExMS_Type.CX
CountryCode_Type.CC = 'CC'                        # originally CountryCodeExMS_Type.CC
CountryCode_Type.CO = 'CO'                        # originally CountryCodeExMS_Type.CO
CountryCode_Type.KM = 'KM'                        # originally CountryCodeExMS_Type.KM
CountryCode_Type.CG = 'CG'                        # originally CountryCodeExMS_Type.CG
CountryCode_Type.CD = 'CD'                        # originally CountryCodeExMS_Type.CD
CountryCode_Type.CK = 'CK'                        # originally CountryCodeExMS_Type.CK
CountryCode_Type.CR = 'CR'                        # originally CountryCodeExMS_Type.CR
CountryCode_Type.CI = 'CI'                        # originally CountryCodeExMS_Type.CI
CountryCode_Type.CU = 'CU'                        # originally CountryCodeExMS_Type.CU
CountryCode_Type.DJ = 'DJ'                        # originally CountryCodeExMS_Type.DJ
CountryCode_Type.DM = 'DM'                        # originally CountryCodeExMS_Type.DM
CountryCode_Type.DO = 'DO'                        # originally CountryCodeExMS_Type.DO
CountryCode_Type.EC = 'EC'                        # originally CountryCodeExMS_Type.EC
CountryCode_Type.EG = 'EG'                        # originally CountryCodeExMS_Type.EG
CountryCode_Type.SV = 'SV'                        # originally CountryCodeExMS_Type.SV
CountryCode_Type.GQ = 'GQ'                        # originally CountryCodeExMS_Type.GQ
CountryCode_Type.ER = 'ER'                        # originally CountryCodeExMS_Type.ER
CountryCode_Type.ET = 'ET'                        # originally CountryCodeExMS_Type.ET
CountryCode_Type.FK = 'FK'                        # originally CountryCodeExMS_Type.FK
CountryCode_Type.FO = 'FO'                        # originally CountryCodeExMS_Type.FO
CountryCode_Type.FJ = 'FJ'                        # originally CountryCodeExMS_Type.FJ
CountryCode_Type.GF = 'GF'                        # originally CountryCodeExMS_Type.GF
CountryCode_Type.PF = 'PF'                        # originally CountryCodeExMS_Type.PF
CountryCode_Type.TF = 'TF'                        # originally CountryCodeExMS_Type.TF
CountryCode_Type.GA = 'GA'                        # originally CountryCodeExMS_Type.GA
CountryCode_Type.GM = 'GM'                        # originally CountryCodeExMS_Type.GM
CountryCode_Type.GE = 'GE'                        # originally CountryCodeExMS_Type.GE
CountryCode_Type.GH = 'GH'                        # originally CountryCodeExMS_Type.GH
CountryCode_Type.GI = 'GI'                        # originally CountryCodeExMS_Type.GI
CountryCode_Type.GL = 'GL'                        # originally CountryCodeExMS_Type.GL
CountryCode_Type.GD = 'GD'                        # originally CountryCodeExMS_Type.GD
CountryCode_Type.GP = 'GP'                        # originally CountryCodeExMS_Type.GP
CountryCode_Type.GU = 'GU'                        # originally CountryCodeExMS_Type.GU
CountryCode_Type.GT = 'GT'                        # originally CountryCodeExMS_Type.GT
CountryCode_Type.GG = 'GG'                        # originally CountryCodeExMS_Type.GG
CountryCode_Type.GN = 'GN'                        # originally CountryCodeExMS_Type.GN
CountryCode_Type.GW = 'GW'                        # originally CountryCodeExMS_Type.GW
CountryCode_Type.GY = 'GY'                        # originally CountryCodeExMS_Type.GY
CountryCode_Type.HT = 'HT'                        # originally CountryCodeExMS_Type.HT
CountryCode_Type.HM = 'HM'                        # originally CountryCodeExMS_Type.HM
CountryCode_Type.VA = 'VA'                        # originally CountryCodeExMS_Type.VA
CountryCode_Type.HN = 'HN'                        # originally CountryCodeExMS_Type.HN
CountryCode_Type.HK = 'HK'                        # originally CountryCodeExMS_Type.HK
CountryCode_Type.IS = 'IS'                        # originally CountryCodeExMS_Type.IS
CountryCode_Type.IN = 'IN'                        # originally CountryCodeExMS_Type.IN
CountryCode_Type.ID = 'ID'                        # originally CountryCodeExMS_Type.ID
CountryCode_Type.IR = 'IR'                        # originally CountryCodeExMS_Type.IR
CountryCode_Type.IQ = 'IQ'                        # originally CountryCodeExMS_Type.IQ
CountryCode_Type.IM = 'IM'                        # originally CountryCodeExMS_Type.IM
CountryCode_Type.IL = 'IL'                        # originally CountryCodeExMS_Type.IL
CountryCode_Type.JM = 'JM'                        # originally CountryCodeExMS_Type.JM
CountryCode_Type.JP = 'JP'                        # originally CountryCodeExMS_Type.JP
CountryCode_Type.JE = 'JE'                        # originally CountryCodeExMS_Type.JE
CountryCode_Type.JO = 'JO'                        # originally CountryCodeExMS_Type.JO
CountryCode_Type.KZ = 'KZ'                        # originally CountryCodeExMS_Type.KZ
CountryCode_Type.KE = 'KE'                        # originally CountryCodeExMS_Type.KE
CountryCode_Type.KI = 'KI'                        # originally CountryCodeExMS_Type.KI
CountryCode_Type.KP = 'KP'                        # originally CountryCodeExMS_Type.KP
CountryCode_Type.KR = 'KR'                        # originally CountryCodeExMS_Type.KR
CountryCode_Type.KW = 'KW'                        # originally CountryCodeExMS_Type.KW
CountryCode_Type.KG = 'KG'                        # originally CountryCodeExMS_Type.KG
CountryCode_Type.LA = 'LA'                        # originally CountryCodeExMS_Type.LA
CountryCode_Type.LB = 'LB'                        # originally CountryCodeExMS_Type.LB
CountryCode_Type.LS = 'LS'                        # originally CountryCodeExMS_Type.LS
CountryCode_Type.LR = 'LR'                        # originally CountryCodeExMS_Type.LR
CountryCode_Type.LY = 'LY'                        # originally CountryCodeExMS_Type.LY
CountryCode_Type.LI = 'LI'                        # originally CountryCodeExMS_Type.LI
CountryCode_Type.MO = 'MO'                        # originally CountryCodeExMS_Type.MO
CountryCode_Type.MK = 'MK'                        # originally CountryCodeExMS_Type.MK
CountryCode_Type.MG = 'MG'                        # originally CountryCodeExMS_Type.MG
CountryCode_Type.MW = 'MW'                        # originally CountryCodeExMS_Type.MW
CountryCode_Type.MY = 'MY'                        # originally CountryCodeExMS_Type.MY
CountryCode_Type.MV = 'MV'                        # originally CountryCodeExMS_Type.MV
CountryCode_Type.ML = 'ML'                        # originally CountryCodeExMS_Type.ML
CountryCode_Type.MH = 'MH'                        # originally CountryCodeExMS_Type.MH
CountryCode_Type.MQ = 'MQ'                        # originally CountryCodeExMS_Type.MQ
CountryCode_Type.MR = 'MR'                        # originally CountryCodeExMS_Type.MR
CountryCode_Type.MU = 'MU'                        # originally CountryCodeExMS_Type.MU
CountryCode_Type.YT = 'YT'                        # originally CountryCodeExMS_Type.YT
CountryCode_Type.MX = 'MX'                        # originally CountryCodeExMS_Type.MX
CountryCode_Type.FM = 'FM'                        # originally CountryCodeExMS_Type.FM
CountryCode_Type.MD = 'MD'                        # originally CountryCodeExMS_Type.MD
CountryCode_Type.MN = 'MN'                        # originally CountryCodeExMS_Type.MN
CountryCode_Type.ME = 'ME'                        # originally CountryCodeExMS_Type.ME
CountryCode_Type.MS = 'MS'                        # originally CountryCodeExMS_Type.MS
CountryCode_Type.MA = 'MA'                        # originally CountryCodeExMS_Type.MA
CountryCode_Type.MZ = 'MZ'                        # originally CountryCodeExMS_Type.MZ
CountryCode_Type.MM = 'MM'                        # originally CountryCodeExMS_Type.MM
CountryCode_Type.NA = 'NA'                        # originally CountryCodeExMS_Type.NA
CountryCode_Type.NR = 'NR'                        # originally CountryCodeExMS_Type.NR
CountryCode_Type.NP = 'NP'                        # originally CountryCodeExMS_Type.NP
CountryCode_Type.AN = 'AN'                        # originally CountryCodeExMS_Type.AN
CountryCode_Type.NC = 'NC'                        # originally CountryCodeExMS_Type.NC
CountryCode_Type.NZ = 'NZ'                        # originally CountryCodeExMS_Type.NZ
CountryCode_Type.NI = 'NI'                        # originally CountryCodeExMS_Type.NI
CountryCode_Type.NE = 'NE'                        # originally CountryCodeExMS_Type.NE
CountryCode_Type.NG = 'NG'                        # originally CountryCodeExMS_Type.NG
CountryCode_Type.NU = 'NU'                        # originally CountryCodeExMS_Type.NU
CountryCode_Type.NF = 'NF'                        # originally CountryCodeExMS_Type.NF
CountryCode_Type.MP = 'MP'                        # originally CountryCodeExMS_Type.MP
CountryCode_Type.NO = 'NO'                        # originally CountryCodeExMS_Type.NO
CountryCode_Type.OM = 'OM'                        # originally CountryCodeExMS_Type.OM
CountryCode_Type.PK = 'PK'                        # originally CountryCodeExMS_Type.PK
CountryCode_Type.PW = 'PW'                        # originally CountryCodeExMS_Type.PW
CountryCode_Type.PS = 'PS'                        # originally CountryCodeExMS_Type.PS
CountryCode_Type.PA = 'PA'                        # originally CountryCodeExMS_Type.PA
CountryCode_Type.PG = 'PG'                        # originally CountryCodeExMS_Type.PG
CountryCode_Type.PY = 'PY'                        # originally CountryCodeExMS_Type.PY
CountryCode_Type.PE = 'PE'                        # originally CountryCodeExMS_Type.PE
CountryCode_Type.PH = 'PH'                        # originally CountryCodeExMS_Type.PH
CountryCode_Type.PN = 'PN'                        # originally CountryCodeExMS_Type.PN
CountryCode_Type.PR = 'PR'                        # originally CountryCodeExMS_Type.PR
CountryCode_Type.QA = 'QA'                        # originally CountryCodeExMS_Type.QA
CountryCode_Type.RE = 'RE'                        # originally CountryCodeExMS_Type.RE
CountryCode_Type.RU = 'RU'                        # originally CountryCodeExMS_Type.RU
CountryCode_Type.RW = 'RW'                        # originally CountryCodeExMS_Type.RW
CountryCode_Type.BL = 'BL'                        # originally CountryCodeExMS_Type.BL
CountryCode_Type.SH = 'SH'                        # originally CountryCodeExMS_Type.SH
CountryCode_Type.KN = 'KN'                        # originally CountryCodeExMS_Type.KN
CountryCode_Type.LC = 'LC'                        # originally CountryCodeExMS_Type.LC
CountryCode_Type.MF = 'MF'                        # originally CountryCodeExMS_Type.MF
CountryCode_Type.PM = 'PM'                        # originally CountryCodeExMS_Type.PM
CountryCode_Type.VC = 'VC'                        # originally CountryCodeExMS_Type.VC
CountryCode_Type.WS = 'WS'                        # originally CountryCodeExMS_Type.WS
CountryCode_Type.SM = 'SM'                        # originally CountryCodeExMS_Type.SM
CountryCode_Type.ST = 'ST'                        # originally CountryCodeExMS_Type.ST
CountryCode_Type.SA = 'SA'                        # originally CountryCodeExMS_Type.SA
CountryCode_Type.SN = 'SN'                        # originally CountryCodeExMS_Type.SN
CountryCode_Type.RS = 'RS'                        # originally CountryCodeExMS_Type.RS
CountryCode_Type.SC = 'SC'                        # originally CountryCodeExMS_Type.SC
CountryCode_Type.SL = 'SL'                        # originally CountryCodeExMS_Type.SL
CountryCode_Type.SG = 'SG'                        # originally CountryCodeExMS_Type.SG
CountryCode_Type.SB = 'SB'                        # originally CountryCodeExMS_Type.SB
CountryCode_Type.SO = 'SO'                        # originally CountryCodeExMS_Type.SO
CountryCode_Type.ZA = 'ZA'                        # originally CountryCodeExMS_Type.ZA
CountryCode_Type.GS = 'GS'                        # originally CountryCodeExMS_Type.GS
CountryCode_Type.LK = 'LK'                        # originally CountryCodeExMS_Type.LK
CountryCode_Type.SD = 'SD'                        # originally CountryCodeExMS_Type.SD
CountryCode_Type.SR = 'SR'                        # originally CountryCodeExMS_Type.SR
CountryCode_Type.SJ = 'SJ'                        # originally CountryCodeExMS_Type.SJ
CountryCode_Type.SZ = 'SZ'                        # originally CountryCodeExMS_Type.SZ
CountryCode_Type.CH = 'CH'                        # originally CountryCodeExMS_Type.CH
CountryCode_Type.SY = 'SY'                        # originally CountryCodeExMS_Type.SY
CountryCode_Type.TW = 'TW'                        # originally CountryCodeExMS_Type.TW
CountryCode_Type.TJ = 'TJ'                        # originally CountryCodeExMS_Type.TJ
CountryCode_Type.TZ = 'TZ'                        # originally CountryCodeExMS_Type.TZ
CountryCode_Type.TH = 'TH'                        # originally CountryCodeExMS_Type.TH
CountryCode_Type.TL = 'TL'                        # originally CountryCodeExMS_Type.TL
CountryCode_Type.TG = 'TG'                        # originally CountryCodeExMS_Type.TG
CountryCode_Type.TK = 'TK'                        # originally CountryCodeExMS_Type.TK
CountryCode_Type.TO = 'TO'                        # originally CountryCodeExMS_Type.TO
CountryCode_Type.TT = 'TT'                        # originally CountryCodeExMS_Type.TT
CountryCode_Type.TN = 'TN'                        # originally CountryCodeExMS_Type.TN
CountryCode_Type.TR = 'TR'                        # originally CountryCodeExMS_Type.TR
CountryCode_Type.TM = 'TM'                        # originally CountryCodeExMS_Type.TM
CountryCode_Type.TC = 'TC'                        # originally CountryCodeExMS_Type.TC
CountryCode_Type.TV = 'TV'                        # originally CountryCodeExMS_Type.TV
CountryCode_Type.UG = 'UG'                        # originally CountryCodeExMS_Type.UG
CountryCode_Type.UA = 'UA'                        # originally CountryCodeExMS_Type.UA
CountryCode_Type.AE = 'AE'                        # originally CountryCodeExMS_Type.AE
CountryCode_Type.US = 'US'                        # originally CountryCodeExMS_Type.US
CountryCode_Type.UM = 'UM'                        # originally CountryCodeExMS_Type.UM
CountryCode_Type.UY = 'UY'                        # originally CountryCodeExMS_Type.UY
CountryCode_Type.UZ = 'UZ'                        # originally CountryCodeExMS_Type.UZ
CountryCode_Type.VU = 'VU'                        # originally CountryCodeExMS_Type.VU
CountryCode_Type.VE = 'VE'                        # originally CountryCodeExMS_Type.VE
CountryCode_Type.VN = 'VN'                        # originally CountryCodeExMS_Type.VN
CountryCode_Type.VG = 'VG'                        # originally CountryCodeExMS_Type.VG
CountryCode_Type.VI = 'VI'                        # originally CountryCodeExMS_Type.VI
CountryCode_Type.WF = 'WF'                        # originally CountryCodeExMS_Type.WF
CountryCode_Type.EH = 'EH'                        # originally CountryCodeExMS_Type.EH
CountryCode_Type.YE = 'YE'                        # originally CountryCodeExMS_Type.YE
CountryCode_Type.ZM = 'ZM'                        # originally CountryCodeExMS_Type.ZM
CountryCode_Type.ZW = 'ZW'                        # originally CountryCodeExMS_Type.ZW
CountryCode_Type.CW = 'CW'                        # originally CountryCodeExMS_Type.CW
CountryCode_Type.NM = 'NM'                        # originally CountryCodeExMS_Type.NM
CountryCode_Type.SX = 'SX'                        # originally CountryCodeExMS_Type.SX
CountryCode_Type.BQ = 'BQ'                        # originally CountryCodeExMS_Type.BQ
CountryCode_Type.AT = 'AT'                        # originally MSCountryCode_Type.AT
CountryCode_Type.BE = 'BE'                        # originally MSCountryCode_Type.BE
CountryCode_Type.BG = 'BG'                        # originally MSCountryCode_Type.BG
CountryCode_Type.CY = 'CY'                        # originally MSCountryCode_Type.CY
CountryCode_Type.CZ = 'CZ'                        # originally MSCountryCode_Type.CZ
CountryCode_Type.DK = 'DK'                        # originally MSCountryCode_Type.DK
CountryCode_Type.EE = 'EE'                        # originally MSCountryCode_Type.EE
CountryCode_Type.FI = 'FI'                        # originally MSCountryCode_Type.FI
CountryCode_Type.FR = 'FR'                        # originally MSCountryCode_Type.FR
CountryCode_Type.DE = 'DE'                        # originally MSCountryCode_Type.DE
CountryCode_Type.EL = 'EL'                        # originally MSCountryCode_Type.EL
CountryCode_Type.HR = 'HR'                        # originally MSCountryCode_Type.HR
CountryCode_Type.HU = 'HU'                        # originally MSCountryCode_Type.HU
CountryCode_Type.IE = 'IE'                        # originally MSCountryCode_Type.IE
CountryCode_Type.IT = 'IT'                        # originally MSCountryCode_Type.IT
CountryCode_Type.LV = 'LV'                        # originally MSCountryCode_Type.LV
CountryCode_Type.LT = 'LT'                        # originally MSCountryCode_Type.LT
CountryCode_Type.LU = 'LU'                        # originally MSCountryCode_Type.LU
CountryCode_Type.MT = 'MT'                        # originally MSCountryCode_Type.MT
CountryCode_Type.NL = 'NL'                        # originally MSCountryCode_Type.NL
CountryCode_Type.PL = 'PL'                        # originally MSCountryCode_Type.PL
CountryCode_Type.PT = 'PT'                        # originally MSCountryCode_Type.PT
CountryCode_Type.RO = 'RO'                        # originally MSCountryCode_Type.RO
CountryCode_Type.SK = 'SK'                        # originally MSCountryCode_Type.SK
CountryCode_Type.SI = 'SI'                        # originally MSCountryCode_Type.SI
CountryCode_Type.ES = 'ES'                        # originally MSCountryCode_Type.ES
CountryCode_Type.SE = 'SE'                        # originally MSCountryCode_Type.SE
CountryCode_Type.GB = 'GB'                        # originally MSCountryCode_Type.GB
CountryCode_Type.IC = 'IC'                        # originally MSCountryCode_Type.IC
CountryCode_Type.XI = 'XI'                        # originally MSCountryCode_Type.XI
CountryCode_Type.XJ = 'XJ'                        # originally MSCountryCode_Type.XJ
CountryCode_Type.MC = 'MC'                        # originally MSCountryCode_Type.MC
CountryCode_Type._InitializeFacetMap(CountryCode_Type._CF_pattern,
   CountryCode_Type._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'CountryCode_Type', CountryCode_Type)
_module_typeBindings.CountryCode_Type = CountryCode_Type
