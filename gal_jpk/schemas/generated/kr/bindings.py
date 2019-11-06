# /home/maciek/odoo-dev/gal/galicea/gal_jpk/schemas/generated/kr/bindings.py
# -*- coding: utf-8 -*-
# @generated
# PyXB bindings for NM:7c2e3df02e3712e0c0cc80dc782c78a13c626821
# Generated 2018-03-08 13:30:04.760522 by PyXB version 1.2.5 using Python 2.7.12.final.0
# Namespace http://jpk.mf.gov.pl/wzor/2016/03/09/03091/

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
from ..http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy_ import bindings as _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings
import pyxb.binding.datatypes
from ..http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2013_05_23_eD_KodyCECHKRAJOW_ import bindings as _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2013_05_23_eD_KodyCECHKRAJOW__bindings

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://jpk.mf.gov.pl/wzor/2016/03/09/03091/', create_if_missing=True)
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


# Atomic simple type: {http://jpk.mf.gov.pl/wzor/2016/03/09/03091/}TKodFormularza
class TKodFormularza (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Symbol wzoru formularza"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TKodFormularza')
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 5, 1)
    _Documentation = 'Symbol wzoru formularza'
TKodFormularza._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TKodFormularza, enum_prefix=None)
TKodFormularza.JPK_KR = TKodFormularza._CF_enumeration.addEnumeration(unicode_value='JPK_KR', tag='JPK_KR')
TKodFormularza._InitializeFacetMap(TKodFormularza._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'TKodFormularza', TKodFormularza)
_module_typeBindings.TKodFormularza = TKodFormularza

# Atomic simple type: {http://jpk.mf.gov.pl/wzor/2016/03/09/03091/}TCelZlozenia
class TCelZlozenia (pyxb.binding.datatypes.byte, pyxb.binding.basis.enumeration_mixin):

    """Określenie celu złożenia JPK"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TCelZlozenia')
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 13, 1)
    _Documentation = 'Okre\u015blenie celu z\u0142o\u017cenia JPK'
TCelZlozenia._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TCelZlozenia, enum_prefix=None)
TCelZlozenia._CF_enumeration.addEnumeration(unicode_value='1', tag=None)
TCelZlozenia._InitializeFacetMap(TCelZlozenia._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'TCelZlozenia', TCelZlozenia)
_module_typeBindings.TCelZlozenia = TCelZlozenia

# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.byte, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 41, 4)
    _Documentation = None
STD_ANON._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON, enum_prefix=None)
STD_ANON._CF_enumeration.addEnumeration(unicode_value='1', tag=None)
STD_ANON._InitializeFacetMap(STD_ANON._CF_enumeration)
_module_typeBindings.STD_ANON = STD_ANON

# Atomic simple type: {http://jpk.mf.gov.pl/wzor/2016/03/09/03091/}TKwotowy
class TKwotowy (pyxb.binding.datatypes.decimal):

    """Wartość numeryczna 18 znaków max, w tym 2 znaki po przecinku"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TKwotowy')
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 71, 1)
    _Documentation = 'Warto\u015b\u0107 numeryczna 18 znak\xf3w max, w tym 2 znaki po przecinku'
TKwotowy._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(2))
TKwotowy._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(18))
TKwotowy._InitializeFacetMap(TKwotowy._CF_fractionDigits,
   TKwotowy._CF_totalDigits)
Namespace.addCategoryObject('typeBinding', 'TKwotowy', TKwotowy)
_module_typeBindings.TKwotowy = TKwotowy

# Atomic simple type: {http://jpk.mf.gov.pl/wzor/2016/03/09/03091/}TZnakowyJPK
class TZnakowyJPK (pyxb.binding.datatypes.token):

    """Typ znakowy ograniczony do 256 znaków"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TZnakowyJPK')
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 88, 1)
    _Documentation = 'Typ znakowy ograniczony do 256 znak\xf3w'
TZnakowyJPK._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
TZnakowyJPK._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(256))
TZnakowyJPK._InitializeFacetMap(TZnakowyJPK._CF_minLength,
   TZnakowyJPK._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'TZnakowyJPK', TZnakowyJPK)
_module_typeBindings.TZnakowyJPK = TZnakowyJPK

# Atomic simple type: {http://jpk.mf.gov.pl/wzor/2016/03/09/03091/}TNaturalnyJPK
class TNaturalnyJPK (_ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TNaturalny):

    """Liczby naturalne większe od zera"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TNaturalnyJPK')
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 80, 1)
    _Documentation = 'Liczby naturalne wi\u0119ksze od zera'
TNaturalnyJPK._CF_minExclusive = pyxb.binding.facets.CF_minExclusive(value_datatype=_ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TNaturalny, value=pyxb.binding.datatypes.integer(0))
TNaturalnyJPK._InitializeFacetMap(TNaturalnyJPK._CF_minExclusive)
Namespace.addCategoryObject('typeBinding', 'TNaturalnyJPK', TNaturalnyJPK)
_module_typeBindings.TNaturalnyJPK = TNaturalnyJPK

# Complex type {http://jpk.mf.gov.pl/wzor/2016/03/09/03091/}TNaglowek with content type ELEMENT_ONLY
class TNaglowek (pyxb.binding.basis.complexTypeDefinition):
    """Nagłówek JPK_KR"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TNaglowek')
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 25, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03091/}KodFormularza uses Python identifier KodFormularza
    __KodFormularza = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'KodFormularza'), 'KodFormularza', '__httpjpk_mf_gov_plwzor2016030903091_TNaglowek_httpjpk_mf_gov_plwzor2016030903091KodFormularza', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 30, 3), )

    
    KodFormularza = property(__KodFormularza.value, __KodFormularza.set, None, None)

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03091/}WariantFormularza uses Python identifier WariantFormularza
    __WariantFormularza = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'WariantFormularza'), 'WariantFormularza', '__httpjpk_mf_gov_plwzor2016030903091_TNaglowek_httpjpk_mf_gov_plwzor2016030903091WariantFormularza', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 40, 3), )

    
    WariantFormularza = property(__WariantFormularza.value, __WariantFormularza.set, None, None)

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03091/}CelZlozenia uses Python identifier CelZlozenia
    __CelZlozenia = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CelZlozenia'), 'CelZlozenia', '__httpjpk_mf_gov_plwzor2016030903091_TNaglowek_httpjpk_mf_gov_plwzor2016030903091CelZlozenia', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 47, 3), )

    
    CelZlozenia = property(__CelZlozenia.value, __CelZlozenia.set, None, None)

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03091/}DataWytworzeniaJPK uses Python identifier DataWytworzeniaJPK
    __DataWytworzeniaJPK = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DataWytworzeniaJPK'), 'DataWytworzeniaJPK', '__httpjpk_mf_gov_plwzor2016030903091_TNaglowek_httpjpk_mf_gov_plwzor2016030903091DataWytworzeniaJPK', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 48, 3), )

    
    DataWytworzeniaJPK = property(__DataWytworzeniaJPK.value, __DataWytworzeniaJPK.set, None, 'Data i czas wytworzenia JPK_KR')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03091/}DataOd uses Python identifier DataOd
    __DataOd = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DataOd'), 'DataOd', '__httpjpk_mf_gov_plwzor2016030903091_TNaglowek_httpjpk_mf_gov_plwzor2016030903091DataOd', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 53, 3), )

    
    DataOd = property(__DataOd.value, __DataOd.set, None, 'Data pocz\u0105tkowa okresu, kt\xf3rego dotyczy JPK_KR')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03091/}DataDo uses Python identifier DataDo
    __DataDo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DataDo'), 'DataDo', '__httpjpk_mf_gov_plwzor2016030903091_TNaglowek_httpjpk_mf_gov_plwzor2016030903091DataDo', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 58, 3), )

    
    DataDo = property(__DataDo.value, __DataDo.set, None, 'Data ko\u0144cowa okresu, kt\xf3rego dotyczy JPK_KR')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03091/}DomyslnyKodWaluty uses Python identifier DomyslnyKodWaluty
    __DomyslnyKodWaluty = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DomyslnyKodWaluty'), 'DomyslnyKodWaluty', '__httpjpk_mf_gov_plwzor2016030903091_TNaglowek_httpjpk_mf_gov_plwzor2016030903091DomyslnyKodWaluty', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 63, 3), )

    
    DomyslnyKodWaluty = property(__DomyslnyKodWaluty.value, __DomyslnyKodWaluty.set, None, 'Trzyliterowy kod lokalnej waluty (ISO-4217), domy\u015blny dla wytworzonego JPK_KR')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03091/}KodUrzedu uses Python identifier KodUrzedu
    __KodUrzedu = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'KodUrzedu'), 'KodUrzedu', '__httpjpk_mf_gov_plwzor2016030903091_TNaglowek_httpjpk_mf_gov_plwzor2016030903091KodUrzedu', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 68, 3), )

    
    KodUrzedu = property(__KodUrzedu.value, __KodUrzedu.set, None, None)

    _ElementMap.update({
        __KodFormularza.name() : __KodFormularza,
        __WariantFormularza.name() : __WariantFormularza,
        __CelZlozenia.name() : __CelZlozenia,
        __DataWytworzeniaJPK.name() : __DataWytworzeniaJPK,
        __DataOd.name() : __DataOd,
        __DataDo.name() : __DataDo,
        __DomyslnyKodWaluty.name() : __DomyslnyKodWaluty,
        __KodUrzedu.name() : __KodUrzedu
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TNaglowek = TNaglowek
Namespace.addCategoryObject('typeBinding', 'TNaglowek', TNaglowek)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Jednolity plik kontrolny dla ksiąg rachunkowych"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 101, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03091/}Naglowek uses Python identifier Naglowek
    __Naglowek = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Naglowek'), 'Naglowek', '__httpjpk_mf_gov_plwzor2016030903091_CTD_ANON_httpjpk_mf_gov_plwzor2016030903091Naglowek', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 103, 4), )

    
    Naglowek = property(__Naglowek.value, __Naglowek.set, None, 'Nag\u0142\xf3wek JPK_KR')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03091/}Podmiot1 uses Python identifier Podmiot1
    __Podmiot1 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Podmiot1'), 'Podmiot1', '__httpjpk_mf_gov_plwzor2016030903091_CTD_ANON_httpjpk_mf_gov_plwzor2016030903091Podmiot1', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 108, 4), )

    
    Podmiot1 = property(__Podmiot1.value, __Podmiot1.set, None, None)

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03091/}ZOiS uses Python identifier ZOiS
    __ZOiS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ZOiS'), 'ZOiS', '__httpjpk_mf_gov_plwzor2016030903091_CTD_ANON_httpjpk_mf_gov_plwzor2016030903091ZOiS', True, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 124, 4), )

    
    ZOiS = property(__ZOiS.value, __ZOiS.set, None, 'Zestawienie obrot\xf3w i sald')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03091/}Dziennik uses Python identifier Dziennik
    __Dziennik = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Dziennik'), 'Dziennik', '__httpjpk_mf_gov_plwzor2016030903091_CTD_ANON_httpjpk_mf_gov_plwzor2016030903091Dziennik', True, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 219, 4), )

    
    Dziennik = property(__Dziennik.value, __Dziennik.set, None, 'Dziennik')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03091/}DziennikCtrl uses Python identifier DziennikCtrl
    __DziennikCtrl = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DziennikCtrl'), 'DziennikCtrl', '__httpjpk_mf_gov_plwzor2016030903091_CTD_ANON_httpjpk_mf_gov_plwzor2016030903091DziennikCtrl', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 284, 4), )

    
    DziennikCtrl = property(__DziennikCtrl.value, __DziennikCtrl.set, None, 'Sumy kontrolne dla tabeli Dziennik')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03091/}KontoZapis uses Python identifier KontoZapis
    __KontoZapis = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'KontoZapis'), 'KontoZapis', '__httpjpk_mf_gov_plwzor2016030903091_CTD_ANON_httpjpk_mf_gov_plwzor2016030903091KontoZapis', True, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 303, 4), )

    
    KontoZapis = property(__KontoZapis.value, __KontoZapis.set, None, 'Zapisy na kontach ksi\u0119gi g\u0142\xf3wnej i ksi\u0105g pomocniczych')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03091/}KontoZapisCtrl uses Python identifier KontoZapisCtrl
    __KontoZapisCtrl = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'KontoZapisCtrl'), 'KontoZapisCtrl', '__httpjpk_mf_gov_plwzor2016030903091_CTD_ANON_httpjpk_mf_gov_plwzor2016030903091KontoZapisCtrl', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 373, 4), )

    
    KontoZapisCtrl = property(__KontoZapisCtrl.value, __KontoZapisCtrl.set, None, 'Sumy kontrolne dla tabeli KontoZapis')

    _ElementMap.update({
        __Naglowek.name() : __Naglowek,
        __Podmiot1.name() : __Podmiot1,
        __ZOiS.name() : __ZOiS,
        __Dziennik.name() : __Dziennik,
        __DziennikCtrl.name() : __DziennikCtrl,
        __KontoZapis.name() : __KontoZapis,
        __KontoZapisCtrl.name() : __KontoZapisCtrl
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON = CTD_ANON


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 109, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03091/}IdentyfikatorPodmiotu uses Python identifier IdentyfikatorPodmiotu
    __IdentyfikatorPodmiotu = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'IdentyfikatorPodmiotu'), 'IdentyfikatorPodmiotu', '__httpjpk_mf_gov_plwzor2016030903091_CTD_ANON__httpjpk_mf_gov_plwzor2016030903091IdentyfikatorPodmiotu', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 111, 7), )

    
    IdentyfikatorPodmiotu = property(__IdentyfikatorPodmiotu.value, __IdentyfikatorPodmiotu.set, None, 'Dane identyfikuj\u0105ce podmiot')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03091/}AdresPodmiotu uses Python identifier AdresPodmiotu
    __AdresPodmiotu = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AdresPodmiotu'), 'AdresPodmiotu', '__httpjpk_mf_gov_plwzor2016030903091_CTD_ANON__httpjpk_mf_gov_plwzor2016030903091AdresPodmiotu', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 116, 7), )

    
    AdresPodmiotu = property(__AdresPodmiotu.value, __AdresPodmiotu.set, None, 'Adres podmiotu')

    _ElementMap.update({
        __IdentyfikatorPodmiotu.name() : __IdentyfikatorPodmiotu,
        __AdresPodmiotu.name() : __AdresPodmiotu
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_ = CTD_ANON_


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Zestawienie obrotów i sald"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 128, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03091/}KodKonta uses Python identifier KodKonta
    __KodKonta = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'KodKonta'), 'KodKonta', '__httpjpk_mf_gov_plwzor2016030903091_CTD_ANON_2_httpjpk_mf_gov_plwzor2016030903091KodKonta', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 130, 7), )

    
    KodKonta = property(__KodKonta.value, __KodKonta.set, None, 'Identyfikator konta ostatecznego zapisu (konta pomocniczego lub konta ksi\u0119gi g\u0142\xf3wnej, je\u017celi nie jest wymagany zapis na kontach pomocniczych)')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03091/}OpisKonta uses Python identifier OpisKonta
    __OpisKonta = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OpisKonta'), 'OpisKonta', '__httpjpk_mf_gov_plwzor2016030903091_CTD_ANON_2_httpjpk_mf_gov_plwzor2016030903091OpisKonta', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 135, 7), )

    
    OpisKonta = property(__OpisKonta.value, __OpisKonta.set, None, 'Nazwa konta')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03091/}TypKonta uses Python identifier TypKonta
    __TypKonta = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TypKonta'), 'TypKonta', '__httpjpk_mf_gov_plwzor2016030903091_CTD_ANON_2_httpjpk_mf_gov_plwzor2016030903091TypKonta', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 140, 7), )

    
    TypKonta = property(__TypKonta.value, __TypKonta.set, None, 'Typ konta (bilansowe, pozabilansowe, rozliczeniowe lub wynikowe)')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03091/}KodZespolu uses Python identifier KodZespolu
    __KodZespolu = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'KodZespolu'), 'KodZespolu', '__httpjpk_mf_gov_plwzor2016030903091_CTD_ANON_2_httpjpk_mf_gov_plwzor2016030903091KodZespolu', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 145, 7), )

    
    KodZespolu = property(__KodZespolu.value, __KodZespolu.set, None, 'Kod zespo\u0142u kont wg Wykazu Kont Syntetycznych (kont ksi\u0119gi g\u0142\xf3wnej)')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03091/}OpisZespolu uses Python identifier OpisZespolu
    __OpisZespolu = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OpisZespolu'), 'OpisZespolu', '__httpjpk_mf_gov_plwzor2016030903091_CTD_ANON_2_httpjpk_mf_gov_plwzor2016030903091OpisZespolu', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 150, 7), )

    
    OpisZespolu = property(__OpisZespolu.value, __OpisZespolu.set, None, 'Opis zespo\u0142u kont')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03091/}KodKategorii uses Python identifier KodKategorii
    __KodKategorii = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'KodKategorii'), 'KodKategorii', '__httpjpk_mf_gov_plwzor2016030903091_CTD_ANON_2_httpjpk_mf_gov_plwzor2016030903091KodKategorii', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 155, 7), )

    
    KodKategorii = property(__KodKategorii.value, __KodKategorii.set, None, 'Kod kategorii konta wed\u0142ug Zespo\u0142u Kont Syntetycznych (kont ksi\u0119gi g\u0142\xf3wnej)')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03091/}OpisKategorii uses Python identifier OpisKategorii
    __OpisKategorii = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OpisKategorii'), 'OpisKategorii', '__httpjpk_mf_gov_plwzor2016030903091_CTD_ANON_2_httpjpk_mf_gov_plwzor2016030903091OpisKategorii', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 160, 7), )

    
    OpisKategorii = property(__OpisKategorii.value, __OpisKategorii.set, None, 'Nazwa kategorii konta')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03091/}KodPodkategorii uses Python identifier KodPodkategorii
    __KodPodkategorii = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'KodPodkategorii'), 'KodPodkategorii', '__httpjpk_mf_gov_plwzor2016030903091_CTD_ANON_2_httpjpk_mf_gov_plwzor2016030903091KodPodkategorii', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 165, 7), )

    
    KodPodkategorii = property(__KodPodkategorii.value, __KodPodkategorii.set, None, 'Kod podkategorii konta ksi\u0105g pomocniczych w ramach poszczeg\xf3lnej kategorii Zespo\u0142u Kont Syntetycznych')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03091/}OpisPodkategorii uses Python identifier OpisPodkategorii
    __OpisPodkategorii = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OpisPodkategorii'), 'OpisPodkategorii', '__httpjpk_mf_gov_plwzor2016030903091_CTD_ANON_2_httpjpk_mf_gov_plwzor2016030903091OpisPodkategorii', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 170, 7), )

    
    OpisPodkategorii = property(__OpisPodkategorii.value, __OpisPodkategorii.set, None, 'Nazwa podkategorii konta')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03091/}BilansOtwarciaWinien uses Python identifier BilansOtwarciaWinien
    __BilansOtwarciaWinien = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BilansOtwarciaWinien'), 'BilansOtwarciaWinien', '__httpjpk_mf_gov_plwzor2016030903091_CTD_ANON_2_httpjpk_mf_gov_plwzor2016030903091BilansOtwarciaWinien', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 175, 7), )

    
    BilansOtwarciaWinien = property(__BilansOtwarciaWinien.value, __BilansOtwarciaWinien.set, None, 'Bilans otwarcia po stronie Winien w walucie polskiej')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03091/}BilansOtwarciaMa uses Python identifier BilansOtwarciaMa
    __BilansOtwarciaMa = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BilansOtwarciaMa'), 'BilansOtwarciaMa', '__httpjpk_mf_gov_plwzor2016030903091_CTD_ANON_2_httpjpk_mf_gov_plwzor2016030903091BilansOtwarciaMa', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 180, 7), )

    
    BilansOtwarciaMa = property(__BilansOtwarciaMa.value, __BilansOtwarciaMa.set, None, 'Bilans otwarcia po stronie Ma w walucie polskiej')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03091/}ObrotyWinien uses Python identifier ObrotyWinien
    __ObrotyWinien = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ObrotyWinien'), 'ObrotyWinien', '__httpjpk_mf_gov_plwzor2016030903091_CTD_ANON_2_httpjpk_mf_gov_plwzor2016030903091ObrotyWinien', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 185, 7), )

    
    ObrotyWinien = property(__ObrotyWinien.value, __ObrotyWinien.set, None, 'Obroty konta po stronie Winien, w okresie kt\xf3rego dotyczy JPK')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03091/}ObrotyMa uses Python identifier ObrotyMa
    __ObrotyMa = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ObrotyMa'), 'ObrotyMa', '__httpjpk_mf_gov_plwzor2016030903091_CTD_ANON_2_httpjpk_mf_gov_plwzor2016030903091ObrotyMa', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 190, 7), )

    
    ObrotyMa = property(__ObrotyMa.value, __ObrotyMa.set, None, 'Obroty konta po stronie Ma, w okresie kt\xf3rego dotyczy JPK')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03091/}ObrotyWinienNarast uses Python identifier ObrotyWinienNarast
    __ObrotyWinienNarast = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ObrotyWinienNarast'), 'ObrotyWinienNarast', '__httpjpk_mf_gov_plwzor2016030903091_CTD_ANON_2_httpjpk_mf_gov_plwzor2016030903091ObrotyWinienNarast', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 195, 7), )

    
    ObrotyWinienNarast = property(__ObrotyWinienNarast.value, __ObrotyWinienNarast.set, None, 'Obroty konta po stronie Winien, w okresie od otwarcia ksi\u0105g do daty ko\u0144cowej okresu, kt\xf3rego dotyczy JPK')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03091/}ObrotyMaNarast uses Python identifier ObrotyMaNarast
    __ObrotyMaNarast = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ObrotyMaNarast'), 'ObrotyMaNarast', '__httpjpk_mf_gov_plwzor2016030903091_CTD_ANON_2_httpjpk_mf_gov_plwzor2016030903091ObrotyMaNarast', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 200, 7), )

    
    ObrotyMaNarast = property(__ObrotyMaNarast.value, __ObrotyMaNarast.set, None, 'Obroty konta po stronie Ma, w okresie od otwarcia ksi\u0105g do daty ko\u0144cowej okresu, kt\xf3rego dotyczy JPK')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03091/}SaldoWinien uses Python identifier SaldoWinien
    __SaldoWinien = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SaldoWinien'), 'SaldoWinien', '__httpjpk_mf_gov_plwzor2016030903091_CTD_ANON_2_httpjpk_mf_gov_plwzor2016030903091SaldoWinien', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 205, 7), )

    
    SaldoWinien = property(__SaldoWinien.value, __SaldoWinien.set, None, 'Saldo po stronie Winien w walucie polskiej na dat\u0119 ko\u0144cow\u0105 okresu, kt\xf3rego dotyczy JPK z uwzgl\u0119dnieniem bilansu otwarcia')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03091/}SaldoMa uses Python identifier SaldoMa
    __SaldoMa = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SaldoMa'), 'SaldoMa', '__httpjpk_mf_gov_plwzor2016030903091_CTD_ANON_2_httpjpk_mf_gov_plwzor2016030903091SaldoMa', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 210, 7), )

    
    SaldoMa = property(__SaldoMa.value, __SaldoMa.set, None, 'Saldo po stronie Ma w walucie polskiej na dat\u0119 ko\u0144cow\u0105 okresu, kt\xf3rego dotyczy JPK z uwzl\u0119dnieniem bilansu otwarcia')

    
    # Attribute typ uses Python identifier typ
    __typ = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'typ'), 'typ', '__httpjpk_mf_gov_plwzor2016030903091_CTD_ANON_2_typ', pyxb.binding.datatypes.anySimpleType, fixed=True, unicode_default='G', required=True)
    __typ._DeclarationLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 216, 6)
    __typ._UseLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 216, 6)
    
    typ = property(__typ.value, __typ.set, None, None)

    _ElementMap.update({
        __KodKonta.name() : __KodKonta,
        __OpisKonta.name() : __OpisKonta,
        __TypKonta.name() : __TypKonta,
        __KodZespolu.name() : __KodZespolu,
        __OpisZespolu.name() : __OpisZespolu,
        __KodKategorii.name() : __KodKategorii,
        __OpisKategorii.name() : __OpisKategorii,
        __KodPodkategorii.name() : __KodPodkategorii,
        __OpisPodkategorii.name() : __OpisPodkategorii,
        __BilansOtwarciaWinien.name() : __BilansOtwarciaWinien,
        __BilansOtwarciaMa.name() : __BilansOtwarciaMa,
        __ObrotyWinien.name() : __ObrotyWinien,
        __ObrotyMa.name() : __ObrotyMa,
        __ObrotyWinienNarast.name() : __ObrotyWinienNarast,
        __ObrotyMaNarast.name() : __ObrotyMaNarast,
        __SaldoWinien.name() : __SaldoWinien,
        __SaldoMa.name() : __SaldoMa
    })
    _AttributeMap.update({
        __typ.name() : __typ
    })
_module_typeBindings.CTD_ANON_2 = CTD_ANON_2


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """Dziennik"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 223, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03091/}LpZapisuDziennika uses Python identifier LpZapisuDziennika
    __LpZapisuDziennika = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LpZapisuDziennika'), 'LpZapisuDziennika', '__httpjpk_mf_gov_plwzor2016030903091_CTD_ANON_3_httpjpk_mf_gov_plwzor2016030903091LpZapisuDziennika', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 225, 7), )

    
    LpZapisuDziennika = property(__LpZapisuDziennika.value, __LpZapisuDziennika.set, None, 'Numer kolejny zapisu dziennika')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03091/}NrZapisuDziennika uses Python identifier NrZapisuDziennika
    __NrZapisuDziennika = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NrZapisuDziennika'), 'NrZapisuDziennika', '__httpjpk_mf_gov_plwzor2016030903091_CTD_ANON_3_httpjpk_mf_gov_plwzor2016030903091NrZapisuDziennika', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 230, 7), )

    
    NrZapisuDziennika = property(__NrZapisuDziennika.value, __NrZapisuDziennika.set, None, 'Numer zapisu w dzienniku')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03091/}OpisDziennika uses Python identifier OpisDziennika
    __OpisDziennika = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OpisDziennika'), 'OpisDziennika', '__httpjpk_mf_gov_plwzor2016030903091_CTD_ANON_3_httpjpk_mf_gov_plwzor2016030903091OpisDziennika', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 235, 7), )

    
    OpisDziennika = property(__OpisDziennika.value, __OpisDziennika.set, None, 'Opis dziennika')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03091/}NrDowoduKsiegowego uses Python identifier NrDowoduKsiegowego
    __NrDowoduKsiegowego = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NrDowoduKsiegowego'), 'NrDowoduKsiegowego', '__httpjpk_mf_gov_plwzor2016030903091_CTD_ANON_3_httpjpk_mf_gov_plwzor2016030903091NrDowoduKsiegowego', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 240, 7), )

    
    NrDowoduKsiegowego = property(__NrDowoduKsiegowego.value, __NrDowoduKsiegowego.set, None, 'Numer dowodu ksi\u0119gowego (faktury, PK itp.)')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03091/}RodzajDowodu uses Python identifier RodzajDowodu
    __RodzajDowodu = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RodzajDowodu'), 'RodzajDowodu', '__httpjpk_mf_gov_plwzor2016030903091_CTD_ANON_3_httpjpk_mf_gov_plwzor2016030903091RodzajDowodu', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 245, 7), )

    
    RodzajDowodu = property(__RodzajDowodu.value, __RodzajDowodu.set, None, 'Rodzaj dowodu ksi\u0119gowego (np. faktura, PK, zestawienie, wyci\u0105g bankowy, raport kasowy, raport okresowy z kasy fiskalnej, zamkni\u0119cia kont, przeksi\u0119gowania techniczne i inne)')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03091/}DataOperacji uses Python identifier DataOperacji
    __DataOperacji = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DataOperacji'), 'DataOperacji', '__httpjpk_mf_gov_plwzor2016030903091_CTD_ANON_3_httpjpk_mf_gov_plwzor2016030903091DataOperacji', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 250, 7), )

    
    DataOperacji = property(__DataOperacji.value, __DataOperacji.set, None, 'Data dokonania operacji gospodarczej (np. data sprzeda\u017cy, zakupu)')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03091/}DataDowodu uses Python identifier DataDowodu
    __DataDowodu = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DataDowodu'), 'DataDowodu', '__httpjpk_mf_gov_plwzor2016030903091_CTD_ANON_3_httpjpk_mf_gov_plwzor2016030903091DataDowodu', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 255, 7), )

    
    DataDowodu = property(__DataDowodu.value, __DataDowodu.set, None, 'Data sporz\u0105dzenia dowodu ksi\u0119gowego')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03091/}DataKsiegowania uses Python identifier DataKsiegowania
    __DataKsiegowania = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DataKsiegowania'), 'DataKsiegowania', '__httpjpk_mf_gov_plwzor2016030903091_CTD_ANON_3_httpjpk_mf_gov_plwzor2016030903091DataKsiegowania', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 260, 7), )

    
    DataKsiegowania = property(__DataKsiegowania.value, __DataKsiegowania.set, None, 'Data, pod kt\xf3r\u0105 uj\u0119to dow\xf3d w ksi\u0119gach')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03091/}KodOperatora uses Python identifier KodOperatora
    __KodOperatora = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'KodOperatora'), 'KodOperatora', '__httpjpk_mf_gov_plwzor2016030903091_CTD_ANON_3_httpjpk_mf_gov_plwzor2016030903091KodOperatora', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 265, 7), )

    
    KodOperatora = property(__KodOperatora.value, __KodOperatora.set, None, 'Dane pozwalaj\u0105ce na ustalenie osoby odpowiedzialnej za tre\u015b\u0107 zapisu')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03091/}OpisOperacji uses Python identifier OpisOperacji
    __OpisOperacji = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OpisOperacji'), 'OpisOperacji', '__httpjpk_mf_gov_plwzor2016030903091_CTD_ANON_3_httpjpk_mf_gov_plwzor2016030903091OpisOperacji', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 270, 7), )

    
    OpisOperacji = property(__OpisOperacji.value, __OpisOperacji.set, None, 'Opis operacji w dzienniku')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03091/}DziennikKwotaOperacji uses Python identifier DziennikKwotaOperacji
    __DziennikKwotaOperacji = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DziennikKwotaOperacji'), 'DziennikKwotaOperacji', '__httpjpk_mf_gov_plwzor2016030903091_CTD_ANON_3_httpjpk_mf_gov_plwzor2016030903091DziennikKwotaOperacji', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 275, 7), )

    
    DziennikKwotaOperacji = property(__DziennikKwotaOperacji.value, __DziennikKwotaOperacji.set, None, 'Warto\u015b\u0107 operacji uj\u0119ta w Dzienniku')

    
    # Attribute typ uses Python identifier typ
    __typ = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'typ'), 'typ', '__httpjpk_mf_gov_plwzor2016030903091_CTD_ANON_3_typ', pyxb.binding.datatypes.anySimpleType, fixed=True, unicode_default='G', required=True)
    __typ._DeclarationLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 281, 6)
    __typ._UseLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 281, 6)
    
    typ = property(__typ.value, __typ.set, None, None)

    _ElementMap.update({
        __LpZapisuDziennika.name() : __LpZapisuDziennika,
        __NrZapisuDziennika.name() : __NrZapisuDziennika,
        __OpisDziennika.name() : __OpisDziennika,
        __NrDowoduKsiegowego.name() : __NrDowoduKsiegowego,
        __RodzajDowodu.name() : __RodzajDowodu,
        __DataOperacji.name() : __DataOperacji,
        __DataDowodu.name() : __DataDowodu,
        __DataKsiegowania.name() : __DataKsiegowania,
        __KodOperatora.name() : __KodOperatora,
        __OpisOperacji.name() : __OpisOperacji,
        __DziennikKwotaOperacji.name() : __DziennikKwotaOperacji
    })
    _AttributeMap.update({
        __typ.name() : __typ
    })
_module_typeBindings.CTD_ANON_3 = CTD_ANON_3


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """Sumy kontrolne dla tabeli Dziennik"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 288, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03091/}LiczbaWierszyDziennika uses Python identifier LiczbaWierszyDziennika
    __LiczbaWierszyDziennika = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LiczbaWierszyDziennika'), 'LiczbaWierszyDziennika', '__httpjpk_mf_gov_plwzor2016030903091_CTD_ANON_4_httpjpk_mf_gov_plwzor2016030903091LiczbaWierszyDziennika', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 290, 7), )

    
    LiczbaWierszyDziennika = property(__LiczbaWierszyDziennika.value, __LiczbaWierszyDziennika.set, None, 'Liczba wierszy Dziennika')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03091/}SumaKwotOperacji uses Python identifier SumaKwotOperacji
    __SumaKwotOperacji = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SumaKwotOperacji'), 'SumaKwotOperacji', '__httpjpk_mf_gov_plwzor2016030903091_CTD_ANON_4_httpjpk_mf_gov_plwzor2016030903091SumaKwotOperacji', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 295, 7), )

    
    SumaKwotOperacji = property(__SumaKwotOperacji.value, __SumaKwotOperacji.set, None, 'Suma warto\u015bci kwot operacji - (elementu KwotaOperacji)')

    _ElementMap.update({
        __LiczbaWierszyDziennika.name() : __LiczbaWierszyDziennika,
        __SumaKwotOperacji.name() : __SumaKwotOperacji
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_4 = CTD_ANON_4


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    """Zapisy na kontach księgi głównej i ksiąg pomocniczych"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 307, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03091/}LpZapisu uses Python identifier LpZapisu
    __LpZapisu = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LpZapisu'), 'LpZapisu', '__httpjpk_mf_gov_plwzor2016030903091_CTD_ANON_5_httpjpk_mf_gov_plwzor2016030903091LpZapisu', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 309, 7), )

    
    LpZapisu = property(__LpZapisu.value, __LpZapisu.set, None, 'Numer kolejny zapisu konta')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03091/}NrZapisu uses Python identifier NrZapisu
    __NrZapisu = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NrZapisu'), 'NrZapisu', '__httpjpk_mf_gov_plwzor2016030903091_CTD_ANON_5_httpjpk_mf_gov_plwzor2016030903091NrZapisu', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 314, 7), )

    
    NrZapisu = property(__NrZapisu.value, __NrZapisu.set, None, 'Numer (kod) zapisu na koncie pozwalaj\u0105cy na jego powi\u0105zanie z zapisem w Dzienniku (identyczny z elementem NrZapisuDziennika)')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03091/}KodKontaWinien uses Python identifier KodKontaWinien
    __KodKontaWinien = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'KodKontaWinien'), 'KodKontaWinien', '__httpjpk_mf_gov_plwzor2016030903091_CTD_ANON_5_httpjpk_mf_gov_plwzor2016030903091KodKontaWinien', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 319, 7), )

    
    KodKontaWinien = property(__KodKontaWinien.value, __KodKontaWinien.set, None, 'Identyfikator konta zapisu (konta pomocniczego lub konta ksi\u0119gi g\u0142\xf3wnej, je\u017celi nie jest wymagany zapis na kontach pomocniczych) dla zapisu po stronie Winien')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03091/}KwotaWinien uses Python identifier KwotaWinien
    __KwotaWinien = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'KwotaWinien'), 'KwotaWinien', '__httpjpk_mf_gov_plwzor2016030903091_CTD_ANON_5_httpjpk_mf_gov_plwzor2016030903091KwotaWinien', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 324, 7), )

    
    KwotaWinien = property(__KwotaWinien.value, __KwotaWinien.set, None, 'Kwota zapisu transakcji po stronie Winien')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03091/}KwotaWinienWaluta uses Python identifier KwotaWinienWaluta
    __KwotaWinienWaluta = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'KwotaWinienWaluta'), 'KwotaWinienWaluta', '__httpjpk_mf_gov_plwzor2016030903091_CTD_ANON_5_httpjpk_mf_gov_plwzor2016030903091KwotaWinienWaluta', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 329, 7), )

    
    KwotaWinienWaluta = property(__KwotaWinienWaluta.value, __KwotaWinienWaluta.set, None, 'Kwota zapisu transakcji po stronie Winien w walucie obcej dla operacji walutowych')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03091/}KodWalutyWinien uses Python identifier KodWalutyWinien
    __KodWalutyWinien = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'KodWalutyWinien'), 'KodWalutyWinien', '__httpjpk_mf_gov_plwzor2016030903091_CTD_ANON_5_httpjpk_mf_gov_plwzor2016030903091KodWalutyWinien', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 334, 7), )

    
    KodWalutyWinien = property(__KodWalutyWinien.value, __KodWalutyWinien.set, None, 'Kod waluty dla operacji walutowych dla ksi\u0119gowa\u0144 po stronie Winien')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03091/}OpisZapisuWinien uses Python identifier OpisZapisuWinien
    __OpisZapisuWinien = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OpisZapisuWinien'), 'OpisZapisuWinien', '__httpjpk_mf_gov_plwzor2016030903091_CTD_ANON_5_httpjpk_mf_gov_plwzor2016030903091OpisZapisuWinien', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 339, 7), )

    
    OpisZapisuWinien = property(__OpisZapisuWinien.value, __OpisZapisuWinien.set, None, 'Opis zapisu transakcji po stronie Winien')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03091/}KodKontaMa uses Python identifier KodKontaMa
    __KodKontaMa = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'KodKontaMa'), 'KodKontaMa', '__httpjpk_mf_gov_plwzor2016030903091_CTD_ANON_5_httpjpk_mf_gov_plwzor2016030903091KodKontaMa', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 344, 7), )

    
    KodKontaMa = property(__KodKontaMa.value, __KodKontaMa.set, None, 'Identyfikator konta zapisu (konta pomocniczego lub konta ksi\u0119gi g\u0142\xf3wnej, je\u017celi nie jest wymagany zapis na kontach pomocniczych) dla zapisu po stronie Ma')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03091/}KwotaMa uses Python identifier KwotaMa
    __KwotaMa = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'KwotaMa'), 'KwotaMa', '__httpjpk_mf_gov_plwzor2016030903091_CTD_ANON_5_httpjpk_mf_gov_plwzor2016030903091KwotaMa', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 349, 7), )

    
    KwotaMa = property(__KwotaMa.value, __KwotaMa.set, None, 'Kwota zapisu transakcji po stronie Ma')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03091/}KwotaMaWaluta uses Python identifier KwotaMaWaluta
    __KwotaMaWaluta = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'KwotaMaWaluta'), 'KwotaMaWaluta', '__httpjpk_mf_gov_plwzor2016030903091_CTD_ANON_5_httpjpk_mf_gov_plwzor2016030903091KwotaMaWaluta', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 354, 7), )

    
    KwotaMaWaluta = property(__KwotaMaWaluta.value, __KwotaMaWaluta.set, None, 'Kwota zapisu transakcji po stronie Ma w walucie obcej dla operacji walutowych')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03091/}KodWalutyMa uses Python identifier KodWalutyMa
    __KodWalutyMa = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'KodWalutyMa'), 'KodWalutyMa', '__httpjpk_mf_gov_plwzor2016030903091_CTD_ANON_5_httpjpk_mf_gov_plwzor2016030903091KodWalutyMa', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 359, 7), )

    
    KodWalutyMa = property(__KodWalutyMa.value, __KodWalutyMa.set, None, 'Kod waluty dla operacji walutowych ksi\u0119gowanych po stronie Ma')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03091/}OpisZapisuMa uses Python identifier OpisZapisuMa
    __OpisZapisuMa = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OpisZapisuMa'), 'OpisZapisuMa', '__httpjpk_mf_gov_plwzor2016030903091_CTD_ANON_5_httpjpk_mf_gov_plwzor2016030903091OpisZapisuMa', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 364, 7), )

    
    OpisZapisuMa = property(__OpisZapisuMa.value, __OpisZapisuMa.set, None, 'Opis zapisu transakcji po stronie Ma')

    
    # Attribute typ uses Python identifier typ
    __typ = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'typ'), 'typ', '__httpjpk_mf_gov_plwzor2016030903091_CTD_ANON_5_typ', pyxb.binding.datatypes.anySimpleType, fixed=True, unicode_default='G', required=True)
    __typ._DeclarationLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 370, 6)
    __typ._UseLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 370, 6)
    
    typ = property(__typ.value, __typ.set, None, None)

    _ElementMap.update({
        __LpZapisu.name() : __LpZapisu,
        __NrZapisu.name() : __NrZapisu,
        __KodKontaWinien.name() : __KodKontaWinien,
        __KwotaWinien.name() : __KwotaWinien,
        __KwotaWinienWaluta.name() : __KwotaWinienWaluta,
        __KodWalutyWinien.name() : __KodWalutyWinien,
        __OpisZapisuWinien.name() : __OpisZapisuWinien,
        __KodKontaMa.name() : __KodKontaMa,
        __KwotaMa.name() : __KwotaMa,
        __KwotaMaWaluta.name() : __KwotaMaWaluta,
        __KodWalutyMa.name() : __KodWalutyMa,
        __OpisZapisuMa.name() : __OpisZapisuMa
    })
    _AttributeMap.update({
        __typ.name() : __typ
    })
_module_typeBindings.CTD_ANON_5 = CTD_ANON_5


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_6 (pyxb.binding.basis.complexTypeDefinition):
    """Sumy kontrolne dla tabeli KontoZapis"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 377, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03091/}LiczbaWierszyKontoZapisj uses Python identifier LiczbaWierszyKontoZapisj
    __LiczbaWierszyKontoZapisj = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LiczbaWierszyKontoZapisj'), 'LiczbaWierszyKontoZapisj', '__httpjpk_mf_gov_plwzor2016030903091_CTD_ANON_6_httpjpk_mf_gov_plwzor2016030903091LiczbaWierszyKontoZapisj', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 379, 7), )

    
    LiczbaWierszyKontoZapisj = property(__LiczbaWierszyKontoZapisj.value, __LiczbaWierszyKontoZapisj.set, None, 'Liczba zapis\xf3w tabeli KontoZapis')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03091/}SumaWinien uses Python identifier SumaWinien
    __SumaWinien = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SumaWinien'), 'SumaWinien', '__httpjpk_mf_gov_plwzor2016030903091_CTD_ANON_6_httpjpk_mf_gov_plwzor2016030903091SumaWinien', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 384, 7), )

    
    SumaWinien = property(__SumaWinien.value, __SumaWinien.set, None, 'Suma warto\u015bci wierszy (zapis\xf3w) po stronie Winien (elementu KwotaWinien)')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03091/}SumaMa uses Python identifier SumaMa
    __SumaMa = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SumaMa'), 'SumaMa', '__httpjpk_mf_gov_plwzor2016030903091_CTD_ANON_6_httpjpk_mf_gov_plwzor2016030903091SumaMa', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 389, 7), )

    
    SumaMa = property(__SumaMa.value, __SumaMa.set, None, 'Suma warto\u015bci wierszy (zapis\xf3w) po stronie Ma (elementu KwotaMa)')

    _ElementMap.update({
        __LiczbaWierszyKontoZapisj.name() : __LiczbaWierszyKontoZapisj,
        __SumaWinien.name() : __SumaWinien,
        __SumaMa.name() : __SumaMa
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_6 = CTD_ANON_6


# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_7 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = TKodFormularza
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 31, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is TKodFormularza
    
    # Attribute kodSystemowy uses Python identifier kodSystemowy
    __kodSystemowy = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'kodSystemowy'), 'kodSystemowy', '__httpjpk_mf_gov_plwzor2016030903091_CTD_ANON_7_kodSystemowy', pyxb.binding.datatypes.string, fixed=True, unicode_default='JPK_KR (1)', required=True)
    __kodSystemowy._DeclarationLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 34, 7)
    __kodSystemowy._UseLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 34, 7)
    
    kodSystemowy = property(__kodSystemowy.value, __kodSystemowy.set, None, None)

    
    # Attribute wersjaSchemy uses Python identifier wersjaSchemy
    __wersjaSchemy = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'wersjaSchemy'), 'wersjaSchemy', '__httpjpk_mf_gov_plwzor2016030903091_CTD_ANON_7_wersjaSchemy', pyxb.binding.datatypes.string, fixed=True, unicode_default='1-0', required=True)
    __wersjaSchemy._DeclarationLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 35, 7)
    __wersjaSchemy._UseLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 35, 7)
    
    wersjaSchemy = property(__wersjaSchemy.value, __wersjaSchemy.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __kodSystemowy.name() : __kodSystemowy,
        __wersjaSchemy.name() : __wersjaSchemy
    })
_module_typeBindings.CTD_ANON_7 = CTD_ANON_7


JPK = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'JPK'), CTD_ANON, documentation='Jednolity plik kontrolny dla ksi\u0105g rachunkowych', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 97, 1))
Namespace.addCategoryObject('elementBinding', JPK.name().localName(), JPK)



TNaglowek._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'KodFormularza'), CTD_ANON_7, scope=TNaglowek, location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 30, 3)))

TNaglowek._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'WariantFormularza'), STD_ANON, scope=TNaglowek, location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 40, 3)))

TNaglowek._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CelZlozenia'), TCelZlozenia, scope=TNaglowek, location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 47, 3)))

TNaglowek._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataWytworzeniaJPK'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TDataCzas, scope=TNaglowek, documentation='Data i czas wytworzenia JPK_KR', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 48, 3)))

TNaglowek._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataOd'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TData, scope=TNaglowek, documentation='Data pocz\u0105tkowa okresu, kt\xf3rego dotyczy JPK_KR', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 53, 3)))

TNaglowek._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataDo'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TData, scope=TNaglowek, documentation='Data ko\u0144cowa okresu, kt\xf3rego dotyczy JPK_KR', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 58, 3)))

TNaglowek._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DomyslnyKodWaluty'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2013_05_23_eD_KodyCECHKRAJOW__bindings.currCode_Type, scope=TNaglowek, documentation='Trzyliterowy kod lokalnej waluty (ISO-4217), domy\u015blny dla wytworzonego JPK_KR', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 63, 3)))

TNaglowek._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'KodUrzedu'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TKodUS, scope=TNaglowek, location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 68, 3)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TNaglowek._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'KodFormularza')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 30, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TNaglowek._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'WariantFormularza')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 40, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TNaglowek._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CelZlozenia')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 47, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TNaglowek._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataWytworzeniaJPK')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 48, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TNaglowek._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataOd')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 53, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TNaglowek._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataDo')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 58, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TNaglowek._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DomyslnyKodWaluty')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 63, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TNaglowek._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'KodUrzedu')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 68, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TNaglowek._Automaton = _BuildAutomaton()




CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Naglowek'), TNaglowek, scope=CTD_ANON, documentation='Nag\u0142\xf3wek JPK_KR', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 103, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Podmiot1'), CTD_ANON_, scope=CTD_ANON, location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 108, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ZOiS'), CTD_ANON_2, scope=CTD_ANON, documentation='Zestawienie obrot\xf3w i sald', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 124, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Dziennik'), CTD_ANON_3, scope=CTD_ANON, documentation='Dziennik', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 219, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DziennikCtrl'), CTD_ANON_4, scope=CTD_ANON, documentation='Sumy kontrolne dla tabeli Dziennik', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 284, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'KontoZapis'), CTD_ANON_5, scope=CTD_ANON, documentation='Zapisy na kontach ksi\u0119gi g\u0142\xf3wnej i ksi\u0105g pomocniczych', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 303, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'KontoZapisCtrl'), CTD_ANON_6, scope=CTD_ANON, documentation='Sumy kontrolne dla tabeli KontoZapis', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 373, 4)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Naglowek')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 103, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Podmiot1')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 108, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ZOiS')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 124, 4))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Dziennik')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 219, 4))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DziennikCtrl')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 284, 4))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'KontoZapis')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 303, 4))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'KontoZapisCtrl')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 373, 4))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton_()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'IdentyfikatorPodmiotu'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TIdentyfikatorOsobyNiefizycznej, scope=CTD_ANON_, documentation='Dane identyfikuj\u0105ce podmiot', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 111, 7)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AdresPodmiotu'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TAdresPolski, scope=CTD_ANON_, documentation='Adres podmiotu', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 116, 7)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'IdentyfikatorPodmiotu')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 111, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AdresPodmiotu')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 116, 7))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_2()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'KodKonta'), TZnakowyJPK, scope=CTD_ANON_2, documentation='Identyfikator konta ostatecznego zapisu (konta pomocniczego lub konta ksi\u0119gi g\u0142\xf3wnej, je\u017celi nie jest wymagany zapis na kontach pomocniczych)', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 130, 7)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OpisKonta'), TZnakowyJPK, scope=CTD_ANON_2, documentation='Nazwa konta', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 135, 7)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TypKonta'), TZnakowyJPK, scope=CTD_ANON_2, documentation='Typ konta (bilansowe, pozabilansowe, rozliczeniowe lub wynikowe)', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 140, 7)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'KodZespolu'), TZnakowyJPK, scope=CTD_ANON_2, documentation='Kod zespo\u0142u kont wg Wykazu Kont Syntetycznych (kont ksi\u0119gi g\u0142\xf3wnej)', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 145, 7)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OpisZespolu'), TZnakowyJPK, scope=CTD_ANON_2, documentation='Opis zespo\u0142u kont', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 150, 7)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'KodKategorii'), TZnakowyJPK, scope=CTD_ANON_2, documentation='Kod kategorii konta wed\u0142ug Zespo\u0142u Kont Syntetycznych (kont ksi\u0119gi g\u0142\xf3wnej)', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 155, 7)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OpisKategorii'), TZnakowyJPK, scope=CTD_ANON_2, documentation='Nazwa kategorii konta', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 160, 7)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'KodPodkategorii'), TZnakowyJPK, scope=CTD_ANON_2, documentation='Kod podkategorii konta ksi\u0105g pomocniczych w ramach poszczeg\xf3lnej kategorii Zespo\u0142u Kont Syntetycznych', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 165, 7)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OpisPodkategorii'), TZnakowyJPK, scope=CTD_ANON_2, documentation='Nazwa podkategorii konta', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 170, 7)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BilansOtwarciaWinien'), TKwotowy, scope=CTD_ANON_2, documentation='Bilans otwarcia po stronie Winien w walucie polskiej', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 175, 7)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BilansOtwarciaMa'), TKwotowy, scope=CTD_ANON_2, documentation='Bilans otwarcia po stronie Ma w walucie polskiej', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 180, 7)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ObrotyWinien'), TKwotowy, scope=CTD_ANON_2, documentation='Obroty konta po stronie Winien, w okresie kt\xf3rego dotyczy JPK', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 185, 7)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ObrotyMa'), TKwotowy, scope=CTD_ANON_2, documentation='Obroty konta po stronie Ma, w okresie kt\xf3rego dotyczy JPK', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 190, 7)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ObrotyWinienNarast'), TKwotowy, scope=CTD_ANON_2, documentation='Obroty konta po stronie Winien, w okresie od otwarcia ksi\u0105g do daty ko\u0144cowej okresu, kt\xf3rego dotyczy JPK', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 195, 7)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ObrotyMaNarast'), TKwotowy, scope=CTD_ANON_2, documentation='Obroty konta po stronie Ma, w okresie od otwarcia ksi\u0105g do daty ko\u0144cowej okresu, kt\xf3rego dotyczy JPK', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 200, 7)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SaldoWinien'), TKwotowy, scope=CTD_ANON_2, documentation='Saldo po stronie Winien w walucie polskiej na dat\u0119 ko\u0144cow\u0105 okresu, kt\xf3rego dotyczy JPK z uwzgl\u0119dnieniem bilansu otwarcia', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 205, 7)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SaldoMa'), TKwotowy, scope=CTD_ANON_2, documentation='Saldo po stronie Ma w walucie polskiej na dat\u0119 ko\u0144cow\u0105 okresu, kt\xf3rego dotyczy JPK z uwzl\u0119dnieniem bilansu otwarcia', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 210, 7)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 165, 7))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 170, 7))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'KodKonta')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 130, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OpisKonta')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 135, 7))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TypKonta')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 140, 7))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'KodZespolu')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 145, 7))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OpisZespolu')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 150, 7))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'KodKategorii')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 155, 7))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OpisKategorii')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 160, 7))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'KodPodkategorii')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 165, 7))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OpisPodkategorii')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 170, 7))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BilansOtwarciaWinien')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 175, 7))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BilansOtwarciaMa')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 180, 7))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ObrotyWinien')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 185, 7))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ObrotyMa')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 190, 7))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ObrotyWinienNarast')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 195, 7))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ObrotyMaNarast')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 200, 7))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SaldoWinien')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 205, 7))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SaldoMa')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 210, 7))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
         ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
         ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
         ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
         ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
         ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
         ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
         ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    st_16._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_3()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LpZapisuDziennika'), TNaturalnyJPK, scope=CTD_ANON_3, documentation='Numer kolejny zapisu dziennika', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 225, 7)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NrZapisuDziennika'), TZnakowyJPK, scope=CTD_ANON_3, documentation='Numer zapisu w dzienniku', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 230, 7)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OpisDziennika'), TZnakowyJPK, scope=CTD_ANON_3, documentation='Opis dziennika', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 235, 7)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NrDowoduKsiegowego'), TZnakowyJPK, scope=CTD_ANON_3, documentation='Numer dowodu ksi\u0119gowego (faktury, PK itp.)', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 240, 7)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RodzajDowodu'), TZnakowyJPK, scope=CTD_ANON_3, documentation='Rodzaj dowodu ksi\u0119gowego (np. faktura, PK, zestawienie, wyci\u0105g bankowy, raport kasowy, raport okresowy z kasy fiskalnej, zamkni\u0119cia kont, przeksi\u0119gowania techniczne i inne)', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 245, 7)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataOperacji'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TData, scope=CTD_ANON_3, documentation='Data dokonania operacji gospodarczej (np. data sprzeda\u017cy, zakupu)', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 250, 7)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataDowodu'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TData, scope=CTD_ANON_3, documentation='Data sporz\u0105dzenia dowodu ksi\u0119gowego', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 255, 7)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataKsiegowania'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TData, scope=CTD_ANON_3, documentation='Data, pod kt\xf3r\u0105 uj\u0119to dow\xf3d w ksi\u0119gach', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 260, 7)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'KodOperatora'), TZnakowyJPK, scope=CTD_ANON_3, documentation='Dane pozwalaj\u0105ce na ustalenie osoby odpowiedzialnej za tre\u015b\u0107 zapisu', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 265, 7)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OpisOperacji'), TZnakowyJPK, scope=CTD_ANON_3, documentation='Opis operacji w dzienniku', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 270, 7)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DziennikKwotaOperacji'), TKwotowy, scope=CTD_ANON_3, documentation='Warto\u015b\u0107 operacji uj\u0119ta w Dzienniku', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 275, 7)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LpZapisuDziennika')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 225, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NrZapisuDziennika')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 230, 7))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OpisDziennika')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 235, 7))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NrDowoduKsiegowego')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 240, 7))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RodzajDowodu')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 245, 7))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataOperacji')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 250, 7))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataDowodu')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 255, 7))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataKsiegowania')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 260, 7))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'KodOperatora')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 265, 7))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OpisOperacji')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 270, 7))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DziennikKwotaOperacji')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 275, 7))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
         ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
         ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    st_10._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton_4()




CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LiczbaWierszyDziennika'), TNaturalnyJPK, scope=CTD_ANON_4, documentation='Liczba wierszy Dziennika', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 290, 7)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SumaKwotOperacji'), TKwotowy, scope=CTD_ANON_4, documentation='Suma warto\u015bci kwot operacji - (elementu KwotaOperacji)', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 295, 7)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LiczbaWierszyDziennika')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 290, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SumaKwotOperacji')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 295, 7))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_5()




CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LpZapisu'), TNaturalnyJPK, scope=CTD_ANON_5, documentation='Numer kolejny zapisu konta', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 309, 7)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NrZapisu'), TZnakowyJPK, scope=CTD_ANON_5, documentation='Numer (kod) zapisu na koncie pozwalaj\u0105cy na jego powi\u0105zanie z zapisem w Dzienniku (identyczny z elementem NrZapisuDziennika)', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 314, 7)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'KodKontaWinien'), TZnakowyJPK, scope=CTD_ANON_5, documentation='Identyfikator konta zapisu (konta pomocniczego lub konta ksi\u0119gi g\u0142\xf3wnej, je\u017celi nie jest wymagany zapis na kontach pomocniczych) dla zapisu po stronie Winien', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 319, 7), unicode_default='null'))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'KwotaWinien'), TKwotowy, scope=CTD_ANON_5, documentation='Kwota zapisu transakcji po stronie Winien', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 324, 7)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'KwotaWinienWaluta'), TKwotowy, scope=CTD_ANON_5, documentation='Kwota zapisu transakcji po stronie Winien w walucie obcej dla operacji walutowych', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 329, 7)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'KodWalutyWinien'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2013_05_23_eD_KodyCECHKRAJOW__bindings.currCode_Type, scope=CTD_ANON_5, documentation='Kod waluty dla operacji walutowych dla ksi\u0119gowa\u0144 po stronie Winien', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 334, 7)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OpisZapisuWinien'), TZnakowyJPK, scope=CTD_ANON_5, documentation='Opis zapisu transakcji po stronie Winien', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 339, 7)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'KodKontaMa'), TZnakowyJPK, scope=CTD_ANON_5, documentation='Identyfikator konta zapisu (konta pomocniczego lub konta ksi\u0119gi g\u0142\xf3wnej, je\u017celi nie jest wymagany zapis na kontach pomocniczych) dla zapisu po stronie Ma', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 344, 7), unicode_default='null'))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'KwotaMa'), TKwotowy, scope=CTD_ANON_5, documentation='Kwota zapisu transakcji po stronie Ma', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 349, 7)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'KwotaMaWaluta'), TKwotowy, scope=CTD_ANON_5, documentation='Kwota zapisu transakcji po stronie Ma w walucie obcej dla operacji walutowych', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 354, 7)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'KodWalutyMa'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2013_05_23_eD_KodyCECHKRAJOW__bindings.currCode_Type, scope=CTD_ANON_5, documentation='Kod waluty dla operacji walutowych ksi\u0119gowanych po stronie Ma', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 359, 7)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OpisZapisuMa'), TZnakowyJPK, scope=CTD_ANON_5, documentation='Opis zapisu transakcji po stronie Ma', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 364, 7)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 329, 7))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 334, 7))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 339, 7))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 354, 7))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 359, 7))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 364, 7))
    counters.add(cc_5)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LpZapisu')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 309, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NrZapisu')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 314, 7))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'KodKontaWinien')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 319, 7))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'KwotaWinien')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 324, 7))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'KwotaWinienWaluta')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 329, 7))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'KodWalutyWinien')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 334, 7))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OpisZapisuWinien')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 339, 7))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'KodKontaMa')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 344, 7))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'KwotaMa')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 349, 7))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'KwotaMaWaluta')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 354, 7))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'KodWalutyMa')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 359, 7))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OpisZapisuMa')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 364, 7))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_11._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_5._Automaton = _BuildAutomaton_6()




CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LiczbaWierszyKontoZapisj'), TNaturalnyJPK, scope=CTD_ANON_6, documentation='Liczba zapis\xf3w tabeli KontoZapis', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 379, 7)))

CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SumaWinien'), TKwotowy, scope=CTD_ANON_6, documentation='Suma warto\u015bci wierszy (zapis\xf3w) po stronie Winien (elementu KwotaWinien)', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 384, 7)))

CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SumaMa'), TKwotowy, scope=CTD_ANON_6, documentation='Suma warto\u015bci wierszy (zapis\xf3w) po stronie Ma (elementu KwotaMa)', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 389, 7)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LiczbaWierszyKontoZapisj')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 379, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SumaWinien')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 384, 7))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SumaMa')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd', 389, 7))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_6._Automaton = _BuildAutomaton_7()

