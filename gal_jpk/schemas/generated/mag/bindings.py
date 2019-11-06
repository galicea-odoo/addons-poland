# /home/maciek/odoo-dev/gal/galicea/gal_jpk/schemas/generated/mag/bindings.py
# -*- coding: utf-8 -*-
# @generated
# PyXB bindings for NM:c8762978825ce240b473eb6cbcd2ae0230a5120d
# Generated 2018-03-08 13:30:04.761848 by PyXB version 1.2.5 using Python 2.7.12.final.0
# Namespace http://jpk.mf.gov.pl/wzor/2016/03/09/03093/

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
Namespace = pyxb.namespace.NamespaceForURI('http://jpk.mf.gov.pl/wzor/2016/03/09/03093/', create_if_missing=True)
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


# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.byte, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 21, 4)
    _Documentation = None
STD_ANON._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON, enum_prefix=None)
STD_ANON._CF_enumeration.addEnumeration(unicode_value='1', tag=None)
STD_ANON._InitializeFacetMap(STD_ANON._CF_enumeration)
_module_typeBindings.STD_ANON = STD_ANON

# Atomic simple type: {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}TKwotowy
class TKwotowy (pyxb.binding.datatypes.decimal):

    """Wartość numeryczna 18 znaków max, w tym 2 znaki po przecinku"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TKwotowy')
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 51, 1)
    _Documentation = 'Warto\u015b\u0107 numeryczna 18 znak\xf3w max, w tym 2 znaki po przecinku'
TKwotowy._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(2))
TKwotowy._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(18))
TKwotowy._InitializeFacetMap(TKwotowy._CF_fractionDigits,
   TKwotowy._CF_totalDigits)
Namespace.addCategoryObject('typeBinding', 'TKwotowy', TKwotowy)
_module_typeBindings.TKwotowy = TKwotowy

# Atomic simple type: {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}TZnakowyJPK
class TZnakowyJPK (pyxb.binding.datatypes.token):

    """Typ znakowy ograniczony do 256 znaków"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TZnakowyJPK')
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 68, 1)
    _Documentation = 'Typ znakowy ograniczony do 256 znak\xf3w'
TZnakowyJPK._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
TZnakowyJPK._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(256))
TZnakowyJPK._InitializeFacetMap(TZnakowyJPK._CF_minLength,
   TZnakowyJPK._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'TZnakowyJPK', TZnakowyJPK)
_module_typeBindings.TZnakowyJPK = TZnakowyJPK

# Atomic simple type: {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}TKodFormularza
class TKodFormularza (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Symbol wzoru formularza"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TKodFormularza')
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 77, 1)
    _Documentation = 'Symbol wzoru formularza'
TKodFormularza._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TKodFormularza, enum_prefix=None)
TKodFormularza.JPK_MAG = TKodFormularza._CF_enumeration.addEnumeration(unicode_value='JPK_MAG', tag='JPK_MAG')
TKodFormularza._InitializeFacetMap(TKodFormularza._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'TKodFormularza', TKodFormularza)
_module_typeBindings.TKodFormularza = TKodFormularza

# Atomic simple type: {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}TCelZlozenia
class TCelZlozenia (pyxb.binding.datatypes.byte, pyxb.binding.basis.enumeration_mixin):

    """Określenie celu złożenia JPK"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TCelZlozenia')
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 85, 1)
    _Documentation = 'Okre\u015blenie celu z\u0142o\u017cenia JPK'
TCelZlozenia._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TCelZlozenia, enum_prefix=None)
TCelZlozenia._CF_enumeration.addEnumeration(unicode_value='1', tag=None)
TCelZlozenia._InitializeFacetMap(TCelZlozenia._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'TCelZlozenia', TCelZlozenia)
_module_typeBindings.TCelZlozenia = TCelZlozenia

# Atomic simple type: {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}TIlosciJPK
class TIlosciJPK (pyxb.binding.datatypes.decimal):

    """Wykorzystywany do określenia ilości. Wartość numeryczna 22 znaki max, w tym 6 po przecinku."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TIlosciJPK')
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 97, 1)
    _Documentation = 'Wykorzystywany do okre\u015blenia ilo\u015bci. Warto\u015b\u0107 numeryczna 22 znaki max, w tym 6 po przecinku.'
TIlosciJPK._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(6))
TIlosciJPK._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(22))
TIlosciJPK._InitializeFacetMap(TIlosciJPK._CF_fractionDigits,
   TIlosciJPK._CF_totalDigits)
Namespace.addCategoryObject('typeBinding', 'TIlosciJPK', TIlosciJPK)
_module_typeBindings.TIlosciJPK = TIlosciJPK

# Atomic simple type: {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}TNaturalnyJPK
class TNaturalnyJPK (_ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TNaturalny):

    """Liczby naturalne większe od zera"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TNaturalnyJPK')
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 60, 1)
    _Documentation = 'Liczby naturalne wi\u0119ksze od zera'
TNaturalnyJPK._CF_minExclusive = pyxb.binding.facets.CF_minExclusive(value_datatype=_ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TNaturalny, value=pyxb.binding.datatypes.integer(0))
TNaturalnyJPK._InitializeFacetMap(TNaturalnyJPK._CF_minExclusive)
Namespace.addCategoryObject('typeBinding', 'TNaturalnyJPK', TNaturalnyJPK)
_module_typeBindings.TNaturalnyJPK = TNaturalnyJPK

# Complex type {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}TNaglowek with content type ELEMENT_ONLY
class TNaglowek (pyxb.binding.basis.complexTypeDefinition):
    """Nagłówek JPK_MAG"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TNaglowek')
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 5, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}KodFormularza uses Python identifier KodFormularza
    __KodFormularza = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'KodFormularza'), 'KodFormularza', '__httpjpk_mf_gov_plwzor2016030903093_TNaglowek_httpjpk_mf_gov_plwzor2016030903093KodFormularza', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 10, 3), )

    
    KodFormularza = property(__KodFormularza.value, __KodFormularza.set, None, None)

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}WariantFormularza uses Python identifier WariantFormularza
    __WariantFormularza = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'WariantFormularza'), 'WariantFormularza', '__httpjpk_mf_gov_plwzor2016030903093_TNaglowek_httpjpk_mf_gov_plwzor2016030903093WariantFormularza', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 20, 3), )

    
    WariantFormularza = property(__WariantFormularza.value, __WariantFormularza.set, None, None)

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}CelZlozenia uses Python identifier CelZlozenia
    __CelZlozenia = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CelZlozenia'), 'CelZlozenia', '__httpjpk_mf_gov_plwzor2016030903093_TNaglowek_httpjpk_mf_gov_plwzor2016030903093CelZlozenia', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 27, 3), )

    
    CelZlozenia = property(__CelZlozenia.value, __CelZlozenia.set, None, None)

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}DataWytworzeniaJPK uses Python identifier DataWytworzeniaJPK
    __DataWytworzeniaJPK = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DataWytworzeniaJPK'), 'DataWytworzeniaJPK', '__httpjpk_mf_gov_plwzor2016030903093_TNaglowek_httpjpk_mf_gov_plwzor2016030903093DataWytworzeniaJPK', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 28, 3), )

    
    DataWytworzeniaJPK = property(__DataWytworzeniaJPK.value, __DataWytworzeniaJPK.set, None, 'Data i czas wytworzenia JPK_MAG')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}DataOd uses Python identifier DataOd
    __DataOd = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DataOd'), 'DataOd', '__httpjpk_mf_gov_plwzor2016030903093_TNaglowek_httpjpk_mf_gov_plwzor2016030903093DataOd', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 33, 3), )

    
    DataOd = property(__DataOd.value, __DataOd.set, None, 'Data pocz\u0105tkowa okresu, kt\xf3rego dotyczy JPK_MAG')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}DataDo uses Python identifier DataDo
    __DataDo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DataDo'), 'DataDo', '__httpjpk_mf_gov_plwzor2016030903093_TNaglowek_httpjpk_mf_gov_plwzor2016030903093DataDo', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 38, 3), )

    
    DataDo = property(__DataDo.value, __DataDo.set, None, 'Data ko\u0144cowa okresu, kt\xf3rego dotyczy JPK_MAG')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}DomyslnyKodWaluty uses Python identifier DomyslnyKodWaluty
    __DomyslnyKodWaluty = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DomyslnyKodWaluty'), 'DomyslnyKodWaluty', '__httpjpk_mf_gov_plwzor2016030903093_TNaglowek_httpjpk_mf_gov_plwzor2016030903093DomyslnyKodWaluty', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 43, 3), )

    
    DomyslnyKodWaluty = property(__DomyslnyKodWaluty.value, __DomyslnyKodWaluty.set, None, 'Trzyliterowy kod lokalnej waluty (ISO-4217), domy\u015blny dla wytworzonego JPK_MAG')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}KodUrzedu uses Python identifier KodUrzedu
    __KodUrzedu = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'KodUrzedu'), 'KodUrzedu', '__httpjpk_mf_gov_plwzor2016030903093_TNaglowek_httpjpk_mf_gov_plwzor2016030903093KodUrzedu', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 48, 3), )

    
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
    """Jednolity plik kontrolny dla obrotu magazynowego"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 110, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}Naglowek uses Python identifier Naglowek
    __Naglowek = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Naglowek'), 'Naglowek', '__httpjpk_mf_gov_plwzor2016030903093_CTD_ANON_httpjpk_mf_gov_plwzor2016030903093Naglowek', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 112, 4), )

    
    Naglowek = property(__Naglowek.value, __Naglowek.set, None, 'Nag\u0142\xf3wek JPK_MAG')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}Podmiot1 uses Python identifier Podmiot1
    __Podmiot1 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Podmiot1'), 'Podmiot1', '__httpjpk_mf_gov_plwzor2016030903093_CTD_ANON_httpjpk_mf_gov_plwzor2016030903093Podmiot1', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 117, 4), )

    
    Podmiot1 = property(__Podmiot1.value, __Podmiot1.set, None, None)

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}Magazyn uses Python identifier Magazyn
    __Magazyn = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Magazyn'), 'Magazyn', '__httpjpk_mf_gov_plwzor2016030903093_CTD_ANON_httpjpk_mf_gov_plwzor2016030903093Magazyn', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 133, 4), )

    
    Magazyn = property(__Magazyn.value, __Magazyn.set, None, 'Oznaczenie magazynu')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}PZ uses Python identifier PZ
    __PZ = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PZ'), 'PZ', '__httpjpk_mf_gov_plwzor2016030903093_CTD_ANON_httpjpk_mf_gov_plwzor2016030903093PZ', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 138, 4), )

    
    PZ = property(__PZ.value, __PZ.set, None, 'Przyj\u0119cie z zewn\u0105trz')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}WZ uses Python identifier WZ
    __WZ = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'WZ'), 'WZ', '__httpjpk_mf_gov_plwzor2016030903093_CTD_ANON_httpjpk_mf_gov_plwzor2016030903093WZ', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 254, 4), )

    
    WZ = property(__WZ.value, __WZ.set, None, 'Wydanie na zewn\u0105trz')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}RW uses Python identifier RW
    __RW = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RW'), 'RW', '__httpjpk_mf_gov_plwzor2016030903093_CTD_ANON_httpjpk_mf_gov_plwzor2016030903093RW', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 370, 4), )

    
    RW = property(__RW.value, __RW.set, None, 'Rozch\xf3d wewn\u0119trzny')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}MM uses Python identifier MM
    __MM = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MM'), 'MM', '__httpjpk_mf_gov_plwzor2016030903093_CTD_ANON_httpjpk_mf_gov_plwzor2016030903093MM', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 481, 4), )

    
    MM = property(__MM.value, __MM.set, None, 'Przesuni\u0119cia mi\u0119dzymagazynowe')

    _ElementMap.update({
        __Naglowek.name() : __Naglowek,
        __Podmiot1.name() : __Podmiot1,
        __Magazyn.name() : __Magazyn,
        __PZ.name() : __PZ,
        __WZ.name() : __WZ,
        __RW.name() : __RW,
        __MM.name() : __MM
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
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 118, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}IdentyfikatorPodmiotu uses Python identifier IdentyfikatorPodmiotu
    __IdentyfikatorPodmiotu = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'IdentyfikatorPodmiotu'), 'IdentyfikatorPodmiotu', '__httpjpk_mf_gov_plwzor2016030903093_CTD_ANON__httpjpk_mf_gov_plwzor2016030903093IdentyfikatorPodmiotu', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 120, 7), )

    
    IdentyfikatorPodmiotu = property(__IdentyfikatorPodmiotu.value, __IdentyfikatorPodmiotu.set, None, 'Dane identyfikuj\u0105ce podmiot')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}AdresPodmiotu uses Python identifier AdresPodmiotu
    __AdresPodmiotu = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AdresPodmiotu'), 'AdresPodmiotu', '__httpjpk_mf_gov_plwzor2016030903093_CTD_ANON__httpjpk_mf_gov_plwzor2016030903093AdresPodmiotu', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 125, 7), )

    
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
    """Przyjęcie z zewnątrz"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 142, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}PZWartosc uses Python identifier PZWartosc
    __PZWartosc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PZWartosc'), 'PZWartosc', '__httpjpk_mf_gov_plwzor2016030903093_CTD_ANON_2_httpjpk_mf_gov_plwzor2016030903093PZWartosc', True, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 144, 7), )

    
    PZWartosc = property(__PZWartosc.value, __PZWartosc.set, None, 'Zestawienie dowod\xf3w PZ')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}PZWiersz uses Python identifier PZWiersz
    __PZWiersz = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PZWiersz'), 'PZWiersz', '__httpjpk_mf_gov_plwzor2016030903093_CTD_ANON_2_httpjpk_mf_gov_plwzor2016030903093PZWiersz', True, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 188, 7), )

    
    PZWiersz = property(__PZWiersz.value, __PZWiersz.set, None, 'Szczeg\xf3\u0142owe pozycje dowod\xf3w PZ')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}PZCtrl uses Python identifier PZCtrl
    __PZCtrl = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PZCtrl'), 'PZCtrl', '__httpjpk_mf_gov_plwzor2016030903093_CTD_ANON_2_httpjpk_mf_gov_plwzor2016030903093PZCtrl', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 232, 7), )

    
    PZCtrl = property(__PZCtrl.value, __PZCtrl.set, None, 'PZ -sumy kontrolne')

    _ElementMap.update({
        __PZWartosc.name() : __PZWartosc,
        __PZWiersz.name() : __PZWiersz,
        __PZCtrl.name() : __PZCtrl
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_2 = CTD_ANON_2


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """Zestawienie dowodów PZ"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 148, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}NumerPZ uses Python identifier NumerPZ
    __NumerPZ = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NumerPZ'), 'NumerPZ', '__httpjpk_mf_gov_plwzor2016030903093_CTD_ANON_3_httpjpk_mf_gov_plwzor2016030903093NumerPZ', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 150, 10), )

    
    NumerPZ = property(__NumerPZ.value, __NumerPZ.set, None, 'Numer dokumentu PZ')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}DataPZ uses Python identifier DataPZ
    __DataPZ = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DataPZ'), 'DataPZ', '__httpjpk_mf_gov_plwzor2016030903093_CTD_ANON_3_httpjpk_mf_gov_plwzor2016030903093DataPZ', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 155, 10), )

    
    DataPZ = property(__DataPZ.value, __DataPZ.set, None, 'Data dokumentu PZ')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}WartoscPZ uses Python identifier WartoscPZ
    __WartoscPZ = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'WartoscPZ'), 'WartoscPZ', '__httpjpk_mf_gov_plwzor2016030903093_CTD_ANON_3_httpjpk_mf_gov_plwzor2016030903093WartoscPZ', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 160, 10), )

    
    WartoscPZ = property(__WartoscPZ.value, __WartoscPZ.set, None, 'Warto\u015b\u0107 og\xf3lna dokumentu PZ')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}DataOtrzymaniaPZ uses Python identifier DataOtrzymaniaPZ
    __DataOtrzymaniaPZ = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DataOtrzymaniaPZ'), 'DataOtrzymaniaPZ', '__httpjpk_mf_gov_plwzor2016030903093_CTD_ANON_3_httpjpk_mf_gov_plwzor2016030903093DataOtrzymaniaPZ', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 165, 10), )

    
    DataOtrzymaniaPZ = property(__DataOtrzymaniaPZ.value, __DataOtrzymaniaPZ.set, None, 'Data otrzymania towaru/materia\u0142u')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}Dostawca uses Python identifier Dostawca
    __Dostawca = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Dostawca'), 'Dostawca', '__httpjpk_mf_gov_plwzor2016030903093_CTD_ANON_3_httpjpk_mf_gov_plwzor2016030903093Dostawca', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 170, 10), )

    
    Dostawca = property(__Dostawca.value, __Dostawca.set, None, 'Dostawca towaru/materia\u0142u')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}NumerFaPZ uses Python identifier NumerFaPZ
    __NumerFaPZ = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NumerFaPZ'), 'NumerFaPZ', '__httpjpk_mf_gov_plwzor2016030903093_CTD_ANON_3_httpjpk_mf_gov_plwzor2016030903093NumerFaPZ', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 175, 10), )

    
    NumerFaPZ = property(__NumerFaPZ.value, __NumerFaPZ.set, None, 'Numer faktury lub specyfikacji dotycz\u0105cej przyj\u0119tego towaru/materia\u0142u')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}DataFaPZ uses Python identifier DataFaPZ
    __DataFaPZ = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DataFaPZ'), 'DataFaPZ', '__httpjpk_mf_gov_plwzor2016030903093_CTD_ANON_3_httpjpk_mf_gov_plwzor2016030903093DataFaPZ', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 180, 10), )

    
    DataFaPZ = property(__DataFaPZ.value, __DataFaPZ.set, None, 'Data faktury lub specyfikacji dotycz\u0105cej przyj\u0119tego towaru/materia\u0142u')

    _ElementMap.update({
        __NumerPZ.name() : __NumerPZ,
        __DataPZ.name() : __DataPZ,
        __WartoscPZ.name() : __WartoscPZ,
        __DataOtrzymaniaPZ.name() : __DataOtrzymaniaPZ,
        __Dostawca.name() : __Dostawca,
        __NumerFaPZ.name() : __NumerFaPZ,
        __DataFaPZ.name() : __DataFaPZ
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_3 = CTD_ANON_3


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """Szczegółowe pozycje dowodów PZ"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 192, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}Numer2PZ uses Python identifier Numer2PZ
    __Numer2PZ = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Numer2PZ'), 'Numer2PZ', '__httpjpk_mf_gov_plwzor2016030903093_CTD_ANON_4_httpjpk_mf_gov_plwzor2016030903093Numer2PZ', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 194, 10), )

    
    Numer2PZ = property(__Numer2PZ.value, __Numer2PZ.set, None, 'Numer dokumentu PZ')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}KodTowaruPZ uses Python identifier KodTowaruPZ
    __KodTowaruPZ = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'KodTowaruPZ'), 'KodTowaruPZ', '__httpjpk_mf_gov_plwzor2016030903093_CTD_ANON_4_httpjpk_mf_gov_plwzor2016030903093KodTowaruPZ', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 199, 10), )

    
    KodTowaruPZ = property(__KodTowaruPZ.value, __KodTowaruPZ.set, None, 'Kod towaru/materia\u0142u/opakowania')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}NazwaTowaruPZ uses Python identifier NazwaTowaruPZ
    __NazwaTowaruPZ = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NazwaTowaruPZ'), 'NazwaTowaruPZ', '__httpjpk_mf_gov_plwzor2016030903093_CTD_ANON_4_httpjpk_mf_gov_plwzor2016030903093NazwaTowaruPZ', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 204, 10), )

    
    NazwaTowaruPZ = property(__NazwaTowaruPZ.value, __NazwaTowaruPZ.set, None, 'Nazwa towaru/materia\u0142u/opakowania')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}IloscPrzyjetaPZ uses Python identifier IloscPrzyjetaPZ
    __IloscPrzyjetaPZ = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'IloscPrzyjetaPZ'), 'IloscPrzyjetaPZ', '__httpjpk_mf_gov_plwzor2016030903093_CTD_ANON_4_httpjpk_mf_gov_plwzor2016030903093IloscPrzyjetaPZ', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 209, 10), )

    
    IloscPrzyjetaPZ = property(__IloscPrzyjetaPZ.value, __IloscPrzyjetaPZ.set, None, 'Ilo\u015b\u0107 przyj\u0119ta')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}JednostkaMiaryPZ uses Python identifier JednostkaMiaryPZ
    __JednostkaMiaryPZ = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'JednostkaMiaryPZ'), 'JednostkaMiaryPZ', '__httpjpk_mf_gov_plwzor2016030903093_CTD_ANON_4_httpjpk_mf_gov_plwzor2016030903093JednostkaMiaryPZ', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 214, 10), )

    
    JednostkaMiaryPZ = property(__JednostkaMiaryPZ.value, __JednostkaMiaryPZ.set, None, 'Jednostka miary')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}CenaJednPZ uses Python identifier CenaJednPZ
    __CenaJednPZ = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CenaJednPZ'), 'CenaJednPZ', '__httpjpk_mf_gov_plwzor2016030903093_CTD_ANON_4_httpjpk_mf_gov_plwzor2016030903093CenaJednPZ', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 219, 10), )

    
    CenaJednPZ = property(__CenaJednPZ.value, __CenaJednPZ.set, None, 'Cena towaru/materia\u0142u/opakowania')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}WartoscPozycjiPZ uses Python identifier WartoscPozycjiPZ
    __WartoscPozycjiPZ = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'WartoscPozycjiPZ'), 'WartoscPozycjiPZ', '__httpjpk_mf_gov_plwzor2016030903093_CTD_ANON_4_httpjpk_mf_gov_plwzor2016030903093WartoscPozycjiPZ', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 224, 10), )

    
    WartoscPozycjiPZ = property(__WartoscPozycjiPZ.value, __WartoscPozycjiPZ.set, None, 'Warto\u015b\u0107 towaru/materia\u0142u/opakowania')

    _ElementMap.update({
        __Numer2PZ.name() : __Numer2PZ,
        __KodTowaruPZ.name() : __KodTowaruPZ,
        __NazwaTowaruPZ.name() : __NazwaTowaruPZ,
        __IloscPrzyjetaPZ.name() : __IloscPrzyjetaPZ,
        __JednostkaMiaryPZ.name() : __JednostkaMiaryPZ,
        __CenaJednPZ.name() : __CenaJednPZ,
        __WartoscPozycjiPZ.name() : __WartoscPozycjiPZ
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_4 = CTD_ANON_4


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    """PZ -sumy kontrolne"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 236, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}LiczbaPZ uses Python identifier LiczbaPZ
    __LiczbaPZ = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LiczbaPZ'), 'LiczbaPZ', '__httpjpk_mf_gov_plwzor2016030903093_CTD_ANON_5_httpjpk_mf_gov_plwzor2016030903093LiczbaPZ', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 238, 10), )

    
    LiczbaPZ = property(__LiczbaPZ.value, __LiczbaPZ.set, None, 'Liczba dokument\xf3w PZ')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}SumaPZ uses Python identifier SumaPZ
    __SumaPZ = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SumaPZ'), 'SumaPZ', '__httpjpk_mf_gov_plwzor2016030903093_CTD_ANON_5_httpjpk_mf_gov_plwzor2016030903093SumaPZ', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 243, 10), )

    
    SumaPZ = property(__SumaPZ.value, __SumaPZ.set, None, 'Warto\u015b\u0107 dokument\xf3w PZ')

    _ElementMap.update({
        __LiczbaPZ.name() : __LiczbaPZ,
        __SumaPZ.name() : __SumaPZ
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_5 = CTD_ANON_5


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_6 (pyxb.binding.basis.complexTypeDefinition):
    """Wydanie na zewnątrz"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 258, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}WZWartosc uses Python identifier WZWartosc
    __WZWartosc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'WZWartosc'), 'WZWartosc', '__httpjpk_mf_gov_plwzor2016030903093_CTD_ANON_6_httpjpk_mf_gov_plwzor2016030903093WZWartosc', True, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 260, 7), )

    
    WZWartosc = property(__WZWartosc.value, __WZWartosc.set, None, 'Zestawienie dowod\xf3w WZ')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}WZWiersz uses Python identifier WZWiersz
    __WZWiersz = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'WZWiersz'), 'WZWiersz', '__httpjpk_mf_gov_plwzor2016030903093_CTD_ANON_6_httpjpk_mf_gov_plwzor2016030903093WZWiersz', True, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 304, 7), )

    
    WZWiersz = property(__WZWiersz.value, __WZWiersz.set, None, 'Szczeg\xf3\u0142owe pozycje dowod\xf3w WZ')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}WZCtrl uses Python identifier WZCtrl
    __WZCtrl = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'WZCtrl'), 'WZCtrl', '__httpjpk_mf_gov_plwzor2016030903093_CTD_ANON_6_httpjpk_mf_gov_plwzor2016030903093WZCtrl', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 348, 7), )

    
    WZCtrl = property(__WZCtrl.value, __WZCtrl.set, None, 'WZ -sumy kontrolne')

    _ElementMap.update({
        __WZWartosc.name() : __WZWartosc,
        __WZWiersz.name() : __WZWiersz,
        __WZCtrl.name() : __WZCtrl
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_6 = CTD_ANON_6


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_7 (pyxb.binding.basis.complexTypeDefinition):
    """Zestawienie dowodów WZ"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 264, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}NumerWZ uses Python identifier NumerWZ
    __NumerWZ = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NumerWZ'), 'NumerWZ', '__httpjpk_mf_gov_plwzor2016030903093_CTD_ANON_7_httpjpk_mf_gov_plwzor2016030903093NumerWZ', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 266, 10), )

    
    NumerWZ = property(__NumerWZ.value, __NumerWZ.set, None, 'Numer dokumentu WZ')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}DataWZ uses Python identifier DataWZ
    __DataWZ = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DataWZ'), 'DataWZ', '__httpjpk_mf_gov_plwzor2016030903093_CTD_ANON_7_httpjpk_mf_gov_plwzor2016030903093DataWZ', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 271, 10), )

    
    DataWZ = property(__DataWZ.value, __DataWZ.set, None, 'Data dokumentu WZ')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}WartoscWZ uses Python identifier WartoscWZ
    __WartoscWZ = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'WartoscWZ'), 'WartoscWZ', '__httpjpk_mf_gov_plwzor2016030903093_CTD_ANON_7_httpjpk_mf_gov_plwzor2016030903093WartoscWZ', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 276, 10), )

    
    WartoscWZ = property(__WartoscWZ.value, __WartoscWZ.set, None, 'Warto\u015b\u0107 dokumentu WZ')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}DataWydaniaWZ uses Python identifier DataWydaniaWZ
    __DataWydaniaWZ = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DataWydaniaWZ'), 'DataWydaniaWZ', '__httpjpk_mf_gov_plwzor2016030903093_CTD_ANON_7_httpjpk_mf_gov_plwzor2016030903093DataWydaniaWZ', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 281, 10), )

    
    DataWydaniaWZ = property(__DataWydaniaWZ.value, __DataWydaniaWZ.set, None, 'Data wydania towaru/materia\u0142u')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}OdbiorcaWZ uses Python identifier OdbiorcaWZ
    __OdbiorcaWZ = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OdbiorcaWZ'), 'OdbiorcaWZ', '__httpjpk_mf_gov_plwzor2016030903093_CTD_ANON_7_httpjpk_mf_gov_plwzor2016030903093OdbiorcaWZ', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 286, 10), )

    
    OdbiorcaWZ = property(__OdbiorcaWZ.value, __OdbiorcaWZ.set, None, 'Odbiorca towaru/materia\u0142u')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}NumerFaWZ uses Python identifier NumerFaWZ
    __NumerFaWZ = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NumerFaWZ'), 'NumerFaWZ', '__httpjpk_mf_gov_plwzor2016030903093_CTD_ANON_7_httpjpk_mf_gov_plwzor2016030903093NumerFaWZ', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 291, 10), )

    
    NumerFaWZ = property(__NumerFaWZ.value, __NumerFaWZ.set, None, 'Numer faktury lub specyfikacji dotycz\u0105cej wydanego towaru/materia\u0142u')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}DataFaWZ uses Python identifier DataFaWZ
    __DataFaWZ = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DataFaWZ'), 'DataFaWZ', '__httpjpk_mf_gov_plwzor2016030903093_CTD_ANON_7_httpjpk_mf_gov_plwzor2016030903093DataFaWZ', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 296, 10), )

    
    DataFaWZ = property(__DataFaWZ.value, __DataFaWZ.set, None, 'Data faktury lub specyfikacji dotycz\u0105cej wydanego towaru/materia\u0142u')

    _ElementMap.update({
        __NumerWZ.name() : __NumerWZ,
        __DataWZ.name() : __DataWZ,
        __WartoscWZ.name() : __WartoscWZ,
        __DataWydaniaWZ.name() : __DataWydaniaWZ,
        __OdbiorcaWZ.name() : __OdbiorcaWZ,
        __NumerFaWZ.name() : __NumerFaWZ,
        __DataFaWZ.name() : __DataFaWZ
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_7 = CTD_ANON_7


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_8 (pyxb.binding.basis.complexTypeDefinition):
    """Szczegółowe pozycje dowodów WZ"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 308, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}Numer2WZ uses Python identifier Numer2WZ
    __Numer2WZ = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Numer2WZ'), 'Numer2WZ', '__httpjpk_mf_gov_plwzor2016030903093_CTD_ANON_8_httpjpk_mf_gov_plwzor2016030903093Numer2WZ', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 310, 10), )

    
    Numer2WZ = property(__Numer2WZ.value, __Numer2WZ.set, None, 'Numer dokumentu WZ')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}KodTowaruWZ uses Python identifier KodTowaruWZ
    __KodTowaruWZ = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'KodTowaruWZ'), 'KodTowaruWZ', '__httpjpk_mf_gov_plwzor2016030903093_CTD_ANON_8_httpjpk_mf_gov_plwzor2016030903093KodTowaruWZ', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 315, 10), )

    
    KodTowaruWZ = property(__KodTowaruWZ.value, __KodTowaruWZ.set, None, 'Kod towaru/materia\u0142u/opakowania')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}NazwaTowaruWZ uses Python identifier NazwaTowaruWZ
    __NazwaTowaruWZ = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NazwaTowaruWZ'), 'NazwaTowaruWZ', '__httpjpk_mf_gov_plwzor2016030903093_CTD_ANON_8_httpjpk_mf_gov_plwzor2016030903093NazwaTowaruWZ', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 320, 10), )

    
    NazwaTowaruWZ = property(__NazwaTowaruWZ.value, __NazwaTowaruWZ.set, None, 'Nazwa towaru/materia\u0142u/opakowania')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}IloscWydanaWZ uses Python identifier IloscWydanaWZ
    __IloscWydanaWZ = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'IloscWydanaWZ'), 'IloscWydanaWZ', '__httpjpk_mf_gov_plwzor2016030903093_CTD_ANON_8_httpjpk_mf_gov_plwzor2016030903093IloscWydanaWZ', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 325, 10), )

    
    IloscWydanaWZ = property(__IloscWydanaWZ.value, __IloscWydanaWZ.set, None, 'Ilo\u015b\u0107 wydana')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}JednostkaMiaryWZ uses Python identifier JednostkaMiaryWZ
    __JednostkaMiaryWZ = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'JednostkaMiaryWZ'), 'JednostkaMiaryWZ', '__httpjpk_mf_gov_plwzor2016030903093_CTD_ANON_8_httpjpk_mf_gov_plwzor2016030903093JednostkaMiaryWZ', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 330, 10), )

    
    JednostkaMiaryWZ = property(__JednostkaMiaryWZ.value, __JednostkaMiaryWZ.set, None, 'Jednostka miary')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}CenaJednWZ uses Python identifier CenaJednWZ
    __CenaJednWZ = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CenaJednWZ'), 'CenaJednWZ', '__httpjpk_mf_gov_plwzor2016030903093_CTD_ANON_8_httpjpk_mf_gov_plwzor2016030903093CenaJednWZ', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 335, 10), )

    
    CenaJednWZ = property(__CenaJednWZ.value, __CenaJednWZ.set, None, 'Cena towaru/materia\u0142u/opakowania')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}WartoscPozycjiWZ uses Python identifier WartoscPozycjiWZ
    __WartoscPozycjiWZ = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'WartoscPozycjiWZ'), 'WartoscPozycjiWZ', '__httpjpk_mf_gov_plwzor2016030903093_CTD_ANON_8_httpjpk_mf_gov_plwzor2016030903093WartoscPozycjiWZ', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 340, 10), )

    
    WartoscPozycjiWZ = property(__WartoscPozycjiWZ.value, __WartoscPozycjiWZ.set, None, 'Warto\u015b\u0107 towaru/materia\u0142u/opakowania')

    _ElementMap.update({
        __Numer2WZ.name() : __Numer2WZ,
        __KodTowaruWZ.name() : __KodTowaruWZ,
        __NazwaTowaruWZ.name() : __NazwaTowaruWZ,
        __IloscWydanaWZ.name() : __IloscWydanaWZ,
        __JednostkaMiaryWZ.name() : __JednostkaMiaryWZ,
        __CenaJednWZ.name() : __CenaJednWZ,
        __WartoscPozycjiWZ.name() : __WartoscPozycjiWZ
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_8 = CTD_ANON_8


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_9 (pyxb.binding.basis.complexTypeDefinition):
    """WZ -sumy kontrolne"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 352, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}LiczbaWZ uses Python identifier LiczbaWZ
    __LiczbaWZ = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LiczbaWZ'), 'LiczbaWZ', '__httpjpk_mf_gov_plwzor2016030903093_CTD_ANON_9_httpjpk_mf_gov_plwzor2016030903093LiczbaWZ', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 354, 10), )

    
    LiczbaWZ = property(__LiczbaWZ.value, __LiczbaWZ.set, None, 'Liczba dokument\xf3w WZ')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}SumaWZ uses Python identifier SumaWZ
    __SumaWZ = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SumaWZ'), 'SumaWZ', '__httpjpk_mf_gov_plwzor2016030903093_CTD_ANON_9_httpjpk_mf_gov_plwzor2016030903093SumaWZ', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 359, 10), )

    
    SumaWZ = property(__SumaWZ.value, __SumaWZ.set, None, 'Warto\u015b\u0107 dokument\xf3w WZ')

    _ElementMap.update({
        __LiczbaWZ.name() : __LiczbaWZ,
        __SumaWZ.name() : __SumaWZ
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_9 = CTD_ANON_9


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_10 (pyxb.binding.basis.complexTypeDefinition):
    """Rozchód wewnętrzny"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 374, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}RWWartosc uses Python identifier RWWartosc
    __RWWartosc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RWWartosc'), 'RWWartosc', '__httpjpk_mf_gov_plwzor2016030903093_CTD_ANON_10_httpjpk_mf_gov_plwzor2016030903093RWWartosc', True, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 376, 7), )

    
    RWWartosc = property(__RWWartosc.value, __RWWartosc.set, None, 'Zestawienie dowod\xf3w RW')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}RWWiersz uses Python identifier RWWiersz
    __RWWiersz = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RWWiersz'), 'RWWiersz', '__httpjpk_mf_gov_plwzor2016030903093_CTD_ANON_10_httpjpk_mf_gov_plwzor2016030903093RWWiersz', True, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 415, 7), )

    
    RWWiersz = property(__RWWiersz.value, __RWWiersz.set, None, 'Szczeg\xf3\u0142owe pozycje dowod\xf3w RW')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}RWCtrl uses Python identifier RWCtrl
    __RWCtrl = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RWCtrl'), 'RWCtrl', '__httpjpk_mf_gov_plwzor2016030903093_CTD_ANON_10_httpjpk_mf_gov_plwzor2016030903093RWCtrl', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 459, 7), )

    
    RWCtrl = property(__RWCtrl.value, __RWCtrl.set, None, 'RW -sumy kontrolne')

    _ElementMap.update({
        __RWWartosc.name() : __RWWartosc,
        __RWWiersz.name() : __RWWiersz,
        __RWCtrl.name() : __RWCtrl
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_10 = CTD_ANON_10


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_11 (pyxb.binding.basis.complexTypeDefinition):
    """Zestawienie dowodów RW"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 380, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}NumerRW uses Python identifier NumerRW
    __NumerRW = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NumerRW'), 'NumerRW', '__httpjpk_mf_gov_plwzor2016030903093_CTD_ANON_11_httpjpk_mf_gov_plwzor2016030903093NumerRW', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 382, 10), )

    
    NumerRW = property(__NumerRW.value, __NumerRW.set, None, 'Numer dokumentu RW')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}DataRW uses Python identifier DataRW
    __DataRW = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DataRW'), 'DataRW', '__httpjpk_mf_gov_plwzor2016030903093_CTD_ANON_11_httpjpk_mf_gov_plwzor2016030903093DataRW', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 387, 10), )

    
    DataRW = property(__DataRW.value, __DataRW.set, None, 'Data dokumentu RW')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}WartoscRW uses Python identifier WartoscRW
    __WartoscRW = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'WartoscRW'), 'WartoscRW', '__httpjpk_mf_gov_plwzor2016030903093_CTD_ANON_11_httpjpk_mf_gov_plwzor2016030903093WartoscRW', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 392, 10), )

    
    WartoscRW = property(__WartoscRW.value, __WartoscRW.set, None, 'Warto\u015b\u0107 dokumentu RW')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}DataWydaniaRW uses Python identifier DataWydaniaRW
    __DataWydaniaRW = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DataWydaniaRW'), 'DataWydaniaRW', '__httpjpk_mf_gov_plwzor2016030903093_CTD_ANON_11_httpjpk_mf_gov_plwzor2016030903093DataWydaniaRW', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 397, 10), )

    
    DataWydaniaRW = property(__DataWydaniaRW.value, __DataWydaniaRW.set, None, 'Data wydania towaru/materia\u0142u')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}SkadRW uses Python identifier SkadRW
    __SkadRW = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SkadRW'), 'SkadRW', '__httpjpk_mf_gov_plwzor2016030903093_CTD_ANON_11_httpjpk_mf_gov_plwzor2016030903093SkadRW', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 402, 10), )

    
    SkadRW = property(__SkadRW.value, __SkadRW.set, None, 'Miejsce wydania towaru/materia\u0142u')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}DokadRW uses Python identifier DokadRW
    __DokadRW = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DokadRW'), 'DokadRW', '__httpjpk_mf_gov_plwzor2016030903093_CTD_ANON_11_httpjpk_mf_gov_plwzor2016030903093DokadRW', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 407, 10), )

    
    DokadRW = property(__DokadRW.value, __DokadRW.set, None, 'Miejsce przeznacznienia towaru/materia\u0142u')

    _ElementMap.update({
        __NumerRW.name() : __NumerRW,
        __DataRW.name() : __DataRW,
        __WartoscRW.name() : __WartoscRW,
        __DataWydaniaRW.name() : __DataWydaniaRW,
        __SkadRW.name() : __SkadRW,
        __DokadRW.name() : __DokadRW
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_11 = CTD_ANON_11


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_12 (pyxb.binding.basis.complexTypeDefinition):
    """Szczegółowe pozycje dowodów RW"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 419, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}Numer2RW uses Python identifier Numer2RW
    __Numer2RW = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Numer2RW'), 'Numer2RW', '__httpjpk_mf_gov_plwzor2016030903093_CTD_ANON_12_httpjpk_mf_gov_plwzor2016030903093Numer2RW', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 421, 10), )

    
    Numer2RW = property(__Numer2RW.value, __Numer2RW.set, None, 'Numer dokumentu RW')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}KodTowaruRW uses Python identifier KodTowaruRW
    __KodTowaruRW = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'KodTowaruRW'), 'KodTowaruRW', '__httpjpk_mf_gov_plwzor2016030903093_CTD_ANON_12_httpjpk_mf_gov_plwzor2016030903093KodTowaruRW', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 426, 10), )

    
    KodTowaruRW = property(__KodTowaruRW.value, __KodTowaruRW.set, None, 'Kod towaru/materia\u0142u/opakowania')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}NazwaTowaruRW uses Python identifier NazwaTowaruRW
    __NazwaTowaruRW = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NazwaTowaruRW'), 'NazwaTowaruRW', '__httpjpk_mf_gov_plwzor2016030903093_CTD_ANON_12_httpjpk_mf_gov_plwzor2016030903093NazwaTowaruRW', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 431, 10), )

    
    NazwaTowaruRW = property(__NazwaTowaruRW.value, __NazwaTowaruRW.set, None, 'Nazwa towaru/materia\u0142u/opakowania')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}IloscWydanaRW uses Python identifier IloscWydanaRW
    __IloscWydanaRW = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'IloscWydanaRW'), 'IloscWydanaRW', '__httpjpk_mf_gov_plwzor2016030903093_CTD_ANON_12_httpjpk_mf_gov_plwzor2016030903093IloscWydanaRW', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 436, 10), )

    
    IloscWydanaRW = property(__IloscWydanaRW.value, __IloscWydanaRW.set, None, 'Ilo\u015b\u0107 wydana')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}JednostkaMiaryRW uses Python identifier JednostkaMiaryRW
    __JednostkaMiaryRW = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'JednostkaMiaryRW'), 'JednostkaMiaryRW', '__httpjpk_mf_gov_plwzor2016030903093_CTD_ANON_12_httpjpk_mf_gov_plwzor2016030903093JednostkaMiaryRW', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 441, 10), )

    
    JednostkaMiaryRW = property(__JednostkaMiaryRW.value, __JednostkaMiaryRW.set, None, 'Jednostka miary')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}CenaJednRW uses Python identifier CenaJednRW
    __CenaJednRW = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CenaJednRW'), 'CenaJednRW', '__httpjpk_mf_gov_plwzor2016030903093_CTD_ANON_12_httpjpk_mf_gov_plwzor2016030903093CenaJednRW', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 446, 10), )

    
    CenaJednRW = property(__CenaJednRW.value, __CenaJednRW.set, None, 'Cena towaru/materia\u0142u/opakowania')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}WartoscPozycjiRW uses Python identifier WartoscPozycjiRW
    __WartoscPozycjiRW = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'WartoscPozycjiRW'), 'WartoscPozycjiRW', '__httpjpk_mf_gov_plwzor2016030903093_CTD_ANON_12_httpjpk_mf_gov_plwzor2016030903093WartoscPozycjiRW', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 451, 10), )

    
    WartoscPozycjiRW = property(__WartoscPozycjiRW.value, __WartoscPozycjiRW.set, None, 'Warto\u015b\u0107 towaru/materia\u0142u/opakowania')

    _ElementMap.update({
        __Numer2RW.name() : __Numer2RW,
        __KodTowaruRW.name() : __KodTowaruRW,
        __NazwaTowaruRW.name() : __NazwaTowaruRW,
        __IloscWydanaRW.name() : __IloscWydanaRW,
        __JednostkaMiaryRW.name() : __JednostkaMiaryRW,
        __CenaJednRW.name() : __CenaJednRW,
        __WartoscPozycjiRW.name() : __WartoscPozycjiRW
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_12 = CTD_ANON_12


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_13 (pyxb.binding.basis.complexTypeDefinition):
    """RW -sumy kontrolne"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 463, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}LiczbaRW uses Python identifier LiczbaRW
    __LiczbaRW = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LiczbaRW'), 'LiczbaRW', '__httpjpk_mf_gov_plwzor2016030903093_CTD_ANON_13_httpjpk_mf_gov_plwzor2016030903093LiczbaRW', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 465, 10), )

    
    LiczbaRW = property(__LiczbaRW.value, __LiczbaRW.set, None, 'Liczba dokument\xf3w RW')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}SumaRW uses Python identifier SumaRW
    __SumaRW = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SumaRW'), 'SumaRW', '__httpjpk_mf_gov_plwzor2016030903093_CTD_ANON_13_httpjpk_mf_gov_plwzor2016030903093SumaRW', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 470, 10), )

    
    SumaRW = property(__SumaRW.value, __SumaRW.set, None, 'Warto\u015b\u0107 dokument\xf3w RW')

    _ElementMap.update({
        __LiczbaRW.name() : __LiczbaRW,
        __SumaRW.name() : __SumaRW
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_13 = CTD_ANON_13


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_14 (pyxb.binding.basis.complexTypeDefinition):
    """Przesunięcia międzymagazynowe"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 485, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}MMWartosc uses Python identifier MMWartosc
    __MMWartosc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MMWartosc'), 'MMWartosc', '__httpjpk_mf_gov_plwzor2016030903093_CTD_ANON_14_httpjpk_mf_gov_plwzor2016030903093MMWartosc', True, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 487, 7), )

    
    MMWartosc = property(__MMWartosc.value, __MMWartosc.set, None, 'Zestawienie dowod\xf3w MM')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}MMWiersz uses Python identifier MMWiersz
    __MMWiersz = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MMWiersz'), 'MMWiersz', '__httpjpk_mf_gov_plwzor2016030903093_CTD_ANON_14_httpjpk_mf_gov_plwzor2016030903093MMWiersz', True, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 526, 7), )

    
    MMWiersz = property(__MMWiersz.value, __MMWiersz.set, None, 'Szczeg\xf3\u0142owe pozycje dowod\xf3w MM')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}MMCtrl uses Python identifier MMCtrl
    __MMCtrl = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MMCtrl'), 'MMCtrl', '__httpjpk_mf_gov_plwzor2016030903093_CTD_ANON_14_httpjpk_mf_gov_plwzor2016030903093MMCtrl', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 570, 7), )

    
    MMCtrl = property(__MMCtrl.value, __MMCtrl.set, None, 'MM -sumy kontrolne')

    _ElementMap.update({
        __MMWartosc.name() : __MMWartosc,
        __MMWiersz.name() : __MMWiersz,
        __MMCtrl.name() : __MMCtrl
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_14 = CTD_ANON_14


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_15 (pyxb.binding.basis.complexTypeDefinition):
    """Zestawienie dowodów MM"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 491, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}NumerMM uses Python identifier NumerMM
    __NumerMM = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NumerMM'), 'NumerMM', '__httpjpk_mf_gov_plwzor2016030903093_CTD_ANON_15_httpjpk_mf_gov_plwzor2016030903093NumerMM', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 493, 10), )

    
    NumerMM = property(__NumerMM.value, __NumerMM.set, None, 'Numer dokumentu MM')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}DataMM uses Python identifier DataMM
    __DataMM = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DataMM'), 'DataMM', '__httpjpk_mf_gov_plwzor2016030903093_CTD_ANON_15_httpjpk_mf_gov_plwzor2016030903093DataMM', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 498, 10), )

    
    DataMM = property(__DataMM.value, __DataMM.set, None, 'Data dokumentu MM')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}WartoscMM uses Python identifier WartoscMM
    __WartoscMM = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'WartoscMM'), 'WartoscMM', '__httpjpk_mf_gov_plwzor2016030903093_CTD_ANON_15_httpjpk_mf_gov_plwzor2016030903093WartoscMM', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 503, 10), )

    
    WartoscMM = property(__WartoscMM.value, __WartoscMM.set, None, 'Warto\u015b\u0107 dokumentu MM')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}DataWydaniaMM uses Python identifier DataWydaniaMM
    __DataWydaniaMM = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DataWydaniaMM'), 'DataWydaniaMM', '__httpjpk_mf_gov_plwzor2016030903093_CTD_ANON_15_httpjpk_mf_gov_plwzor2016030903093DataWydaniaMM', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 508, 10), )

    
    DataWydaniaMM = property(__DataWydaniaMM.value, __DataWydaniaMM.set, None, 'Data wydania towaru/materia\u0142u')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}SkadMM uses Python identifier SkadMM
    __SkadMM = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SkadMM'), 'SkadMM', '__httpjpk_mf_gov_plwzor2016030903093_CTD_ANON_15_httpjpk_mf_gov_plwzor2016030903093SkadMM', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 513, 10), )

    
    SkadMM = property(__SkadMM.value, __SkadMM.set, None, 'Miejsce wydania towaru/materia\u0142u')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}DokadMM uses Python identifier DokadMM
    __DokadMM = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DokadMM'), 'DokadMM', '__httpjpk_mf_gov_plwzor2016030903093_CTD_ANON_15_httpjpk_mf_gov_plwzor2016030903093DokadMM', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 518, 10), )

    
    DokadMM = property(__DokadMM.value, __DokadMM.set, None, 'Miejsce przeznacznienia towaru/materia\u0142u')

    _ElementMap.update({
        __NumerMM.name() : __NumerMM,
        __DataMM.name() : __DataMM,
        __WartoscMM.name() : __WartoscMM,
        __DataWydaniaMM.name() : __DataWydaniaMM,
        __SkadMM.name() : __SkadMM,
        __DokadMM.name() : __DokadMM
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_15 = CTD_ANON_15


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_16 (pyxb.binding.basis.complexTypeDefinition):
    """Szczegółowe pozycje dowodów MM"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 530, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}Numer2MM uses Python identifier Numer2MM
    __Numer2MM = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Numer2MM'), 'Numer2MM', '__httpjpk_mf_gov_plwzor2016030903093_CTD_ANON_16_httpjpk_mf_gov_plwzor2016030903093Numer2MM', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 532, 10), )

    
    Numer2MM = property(__Numer2MM.value, __Numer2MM.set, None, 'Numer dokumentu MM')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}KodTowaruMM uses Python identifier KodTowaruMM
    __KodTowaruMM = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'KodTowaruMM'), 'KodTowaruMM', '__httpjpk_mf_gov_plwzor2016030903093_CTD_ANON_16_httpjpk_mf_gov_plwzor2016030903093KodTowaruMM', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 537, 10), )

    
    KodTowaruMM = property(__KodTowaruMM.value, __KodTowaruMM.set, None, 'Kod towaru/materia\u0142u/opakowania')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}NazwaTowaruMM uses Python identifier NazwaTowaruMM
    __NazwaTowaruMM = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NazwaTowaruMM'), 'NazwaTowaruMM', '__httpjpk_mf_gov_plwzor2016030903093_CTD_ANON_16_httpjpk_mf_gov_plwzor2016030903093NazwaTowaruMM', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 542, 10), )

    
    NazwaTowaruMM = property(__NazwaTowaruMM.value, __NazwaTowaruMM.set, None, 'Nazwa towaru/materia\u0142u/opakowania')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}IloscWydanaMM uses Python identifier IloscWydanaMM
    __IloscWydanaMM = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'IloscWydanaMM'), 'IloscWydanaMM', '__httpjpk_mf_gov_plwzor2016030903093_CTD_ANON_16_httpjpk_mf_gov_plwzor2016030903093IloscWydanaMM', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 547, 10), )

    
    IloscWydanaMM = property(__IloscWydanaMM.value, __IloscWydanaMM.set, None, 'Ilo\u015b\u0107 wydana')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}JednostkaMiaryMM uses Python identifier JednostkaMiaryMM
    __JednostkaMiaryMM = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'JednostkaMiaryMM'), 'JednostkaMiaryMM', '__httpjpk_mf_gov_plwzor2016030903093_CTD_ANON_16_httpjpk_mf_gov_plwzor2016030903093JednostkaMiaryMM', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 552, 10), )

    
    JednostkaMiaryMM = property(__JednostkaMiaryMM.value, __JednostkaMiaryMM.set, None, 'Jednostka miary')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}CenaJednMM uses Python identifier CenaJednMM
    __CenaJednMM = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CenaJednMM'), 'CenaJednMM', '__httpjpk_mf_gov_plwzor2016030903093_CTD_ANON_16_httpjpk_mf_gov_plwzor2016030903093CenaJednMM', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 557, 10), )

    
    CenaJednMM = property(__CenaJednMM.value, __CenaJednMM.set, None, 'Cena towaru/materia\u0142u/opakowania')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}WartoscPozycjiMM uses Python identifier WartoscPozycjiMM
    __WartoscPozycjiMM = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'WartoscPozycjiMM'), 'WartoscPozycjiMM', '__httpjpk_mf_gov_plwzor2016030903093_CTD_ANON_16_httpjpk_mf_gov_plwzor2016030903093WartoscPozycjiMM', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 562, 10), )

    
    WartoscPozycjiMM = property(__WartoscPozycjiMM.value, __WartoscPozycjiMM.set, None, 'Warto\u015b\u0107 towaru/materia\u0142u/opakowania')

    _ElementMap.update({
        __Numer2MM.name() : __Numer2MM,
        __KodTowaruMM.name() : __KodTowaruMM,
        __NazwaTowaruMM.name() : __NazwaTowaruMM,
        __IloscWydanaMM.name() : __IloscWydanaMM,
        __JednostkaMiaryMM.name() : __JednostkaMiaryMM,
        __CenaJednMM.name() : __CenaJednMM,
        __WartoscPozycjiMM.name() : __WartoscPozycjiMM
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_16 = CTD_ANON_16


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_17 (pyxb.binding.basis.complexTypeDefinition):
    """MM -sumy kontrolne"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 574, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}LiczbaMM uses Python identifier LiczbaMM
    __LiczbaMM = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LiczbaMM'), 'LiczbaMM', '__httpjpk_mf_gov_plwzor2016030903093_CTD_ANON_17_httpjpk_mf_gov_plwzor2016030903093LiczbaMM', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 576, 10), )

    
    LiczbaMM = property(__LiczbaMM.value, __LiczbaMM.set, None, 'Liczba dokument\xf3w MM')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/03/09/03093/}SumaMM uses Python identifier SumaMM
    __SumaMM = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SumaMM'), 'SumaMM', '__httpjpk_mf_gov_plwzor2016030903093_CTD_ANON_17_httpjpk_mf_gov_plwzor2016030903093SumaMM', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 581, 10), )

    
    SumaMM = property(__SumaMM.value, __SumaMM.set, None, 'Warto\u015b\u0107 dokument\xf3w MM')

    _ElementMap.update({
        __LiczbaMM.name() : __LiczbaMM,
        __SumaMM.name() : __SumaMM
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_17 = CTD_ANON_17


# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_18 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = TKodFormularza
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 11, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is TKodFormularza
    
    # Attribute kodSystemowy uses Python identifier kodSystemowy
    __kodSystemowy = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'kodSystemowy'), 'kodSystemowy', '__httpjpk_mf_gov_plwzor2016030903093_CTD_ANON_18_kodSystemowy', pyxb.binding.datatypes.string, fixed=True, unicode_default='JPK_MAG (1)', required=True)
    __kodSystemowy._DeclarationLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 14, 7)
    __kodSystemowy._UseLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 14, 7)
    
    kodSystemowy = property(__kodSystemowy.value, __kodSystemowy.set, None, None)

    
    # Attribute wersjaSchemy uses Python identifier wersjaSchemy
    __wersjaSchemy = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'wersjaSchemy'), 'wersjaSchemy', '__httpjpk_mf_gov_plwzor2016030903093_CTD_ANON_18_wersjaSchemy', pyxb.binding.datatypes.string, fixed=True, unicode_default='1-0', required=True)
    __wersjaSchemy._DeclarationLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 15, 7)
    __wersjaSchemy._UseLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 15, 7)
    
    wersjaSchemy = property(__wersjaSchemy.value, __wersjaSchemy.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __kodSystemowy.name() : __kodSystemowy,
        __wersjaSchemy.name() : __wersjaSchemy
    })
_module_typeBindings.CTD_ANON_18 = CTD_ANON_18


JPK = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'JPK'), CTD_ANON, documentation='Jednolity plik kontrolny dla obrotu magazynowego', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 106, 1))
Namespace.addCategoryObject('elementBinding', JPK.name().localName(), JPK)



TNaglowek._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'KodFormularza'), CTD_ANON_18, scope=TNaglowek, location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 10, 3)))

TNaglowek._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'WariantFormularza'), STD_ANON, scope=TNaglowek, location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 20, 3)))

TNaglowek._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CelZlozenia'), TCelZlozenia, scope=TNaglowek, location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 27, 3)))

TNaglowek._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataWytworzeniaJPK'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TDataCzas, scope=TNaglowek, documentation='Data i czas wytworzenia JPK_MAG', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 28, 3)))

TNaglowek._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataOd'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TData, scope=TNaglowek, documentation='Data pocz\u0105tkowa okresu, kt\xf3rego dotyczy JPK_MAG', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 33, 3)))

TNaglowek._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataDo'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TData, scope=TNaglowek, documentation='Data ko\u0144cowa okresu, kt\xf3rego dotyczy JPK_MAG', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 38, 3)))

TNaglowek._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DomyslnyKodWaluty'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2013_05_23_eD_KodyCECHKRAJOW__bindings.currCode_Type, scope=TNaglowek, documentation='Trzyliterowy kod lokalnej waluty (ISO-4217), domy\u015blny dla wytworzonego JPK_MAG', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 43, 3)))

TNaglowek._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'KodUrzedu'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TKodUS, scope=TNaglowek, location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 48, 3)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TNaglowek._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'KodFormularza')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 10, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TNaglowek._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'WariantFormularza')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 20, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TNaglowek._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CelZlozenia')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 27, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TNaglowek._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataWytworzeniaJPK')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 28, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TNaglowek._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataOd')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 33, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TNaglowek._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataDo')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 38, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TNaglowek._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DomyslnyKodWaluty')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 43, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TNaglowek._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'KodUrzedu')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 48, 3))
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




CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Naglowek'), TNaglowek, scope=CTD_ANON, documentation='Nag\u0142\xf3wek JPK_MAG', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 112, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Podmiot1'), CTD_ANON_, scope=CTD_ANON, location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 117, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Magazyn'), TZnakowyJPK, scope=CTD_ANON, documentation='Oznaczenie magazynu', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 133, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PZ'), CTD_ANON_2, scope=CTD_ANON, documentation='Przyj\u0119cie z zewn\u0105trz', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 138, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'WZ'), CTD_ANON_6, scope=CTD_ANON, documentation='Wydanie na zewn\u0105trz', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 254, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RW'), CTD_ANON_10, scope=CTD_ANON, documentation='Rozch\xf3d wewn\u0119trzny', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 370, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MM'), CTD_ANON_14, scope=CTD_ANON, documentation='Przesuni\u0119cia mi\u0119dzymagazynowe', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 481, 4)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 138, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 254, 4))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 370, 4))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 481, 4))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Naglowek')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 112, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Podmiot1')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 117, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Magazyn')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 133, 4))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PZ')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 138, 4))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'WZ')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 254, 4))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RW')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 370, 4))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MM')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 481, 4))
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
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton_()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'IdentyfikatorPodmiotu'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TIdentyfikatorOsobyNiefizycznej, scope=CTD_ANON_, documentation='Dane identyfikuj\u0105ce podmiot', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 120, 7)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AdresPodmiotu'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TAdresPolski, scope=CTD_ANON_, documentation='Adres podmiotu', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 125, 7)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'IdentyfikatorPodmiotu')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 120, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AdresPodmiotu')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 125, 7))
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




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PZWartosc'), CTD_ANON_3, scope=CTD_ANON_2, documentation='Zestawienie dowod\xf3w PZ', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 144, 7)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PZWiersz'), CTD_ANON_4, scope=CTD_ANON_2, documentation='Szczeg\xf3\u0142owe pozycje dowod\xf3w PZ', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 188, 7)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PZCtrl'), CTD_ANON_5, scope=CTD_ANON_2, documentation='PZ -sumy kontrolne', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 232, 7)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PZWartosc')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 144, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PZWiersz')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 188, 7))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PZCtrl')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 232, 7))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_3()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NumerPZ'), TZnakowyJPK, scope=CTD_ANON_3, documentation='Numer dokumentu PZ', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 150, 10)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataPZ'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TData, scope=CTD_ANON_3, documentation='Data dokumentu PZ', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 155, 10)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'WartoscPZ'), TKwotowy, scope=CTD_ANON_3, documentation='Warto\u015b\u0107 og\xf3lna dokumentu PZ', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 160, 10)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataOtrzymaniaPZ'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TData, scope=CTD_ANON_3, documentation='Data otrzymania towaru/materia\u0142u', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 165, 10)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Dostawca'), TZnakowyJPK, scope=CTD_ANON_3, documentation='Dostawca towaru/materia\u0142u', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 170, 10)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NumerFaPZ'), TZnakowyJPK, scope=CTD_ANON_3, documentation='Numer faktury lub specyfikacji dotycz\u0105cej przyj\u0119tego towaru/materia\u0142u', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 175, 10)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataFaPZ'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TData, scope=CTD_ANON_3, documentation='Data faktury lub specyfikacji dotycz\u0105cej przyj\u0119tego towaru/materia\u0142u', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 180, 10)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 175, 10))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 180, 10))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NumerPZ')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 150, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataPZ')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 155, 10))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'WartoscPZ')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 160, 10))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataOtrzymaniaPZ')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 165, 10))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Dostawca')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 170, 10))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NumerFaPZ')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 175, 10))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataFaPZ')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 180, 10))
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
    transitions.append(fac.Transition(st_6, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton_4()




CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Numer2PZ'), TZnakowyJPK, scope=CTD_ANON_4, documentation='Numer dokumentu PZ', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 194, 10)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'KodTowaruPZ'), TZnakowyJPK, scope=CTD_ANON_4, documentation='Kod towaru/materia\u0142u/opakowania', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 199, 10)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NazwaTowaruPZ'), TZnakowyJPK, scope=CTD_ANON_4, documentation='Nazwa towaru/materia\u0142u/opakowania', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 204, 10)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'IloscPrzyjetaPZ'), TIlosciJPK, scope=CTD_ANON_4, documentation='Ilo\u015b\u0107 przyj\u0119ta', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 209, 10)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'JednostkaMiaryPZ'), TZnakowyJPK, scope=CTD_ANON_4, documentation='Jednostka miary', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 214, 10)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CenaJednPZ'), TKwotowy, scope=CTD_ANON_4, documentation='Cena towaru/materia\u0142u/opakowania', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 219, 10)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'WartoscPozycjiPZ'), TKwotowy, scope=CTD_ANON_4, documentation='Warto\u015b\u0107 towaru/materia\u0142u/opakowania', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 224, 10)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 199, 10))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Numer2PZ')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 194, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'KodTowaruPZ')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 199, 10))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NazwaTowaruPZ')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 204, 10))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'IloscPrzyjetaPZ')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 209, 10))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'JednostkaMiaryPZ')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 214, 10))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CenaJednPZ')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 219, 10))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'WartoscPozycjiPZ')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 224, 10))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
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
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_5()




CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LiczbaPZ'), TNaturalnyJPK, scope=CTD_ANON_5, documentation='Liczba dokument\xf3w PZ', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 238, 10)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SumaPZ'), TKwotowy, scope=CTD_ANON_5, documentation='Warto\u015b\u0107 dokument\xf3w PZ', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 243, 10)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LiczbaPZ')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 238, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SumaPZ')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 243, 10))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_5._Automaton = _BuildAutomaton_6()




CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'WZWartosc'), CTD_ANON_7, scope=CTD_ANON_6, documentation='Zestawienie dowod\xf3w WZ', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 260, 7)))

CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'WZWiersz'), CTD_ANON_8, scope=CTD_ANON_6, documentation='Szczeg\xf3\u0142owe pozycje dowod\xf3w WZ', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 304, 7)))

CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'WZCtrl'), CTD_ANON_9, scope=CTD_ANON_6, documentation='WZ -sumy kontrolne', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 348, 7)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'WZWartosc')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 260, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'WZWiersz')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 304, 7))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'WZCtrl')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 348, 7))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_6._Automaton = _BuildAutomaton_7()




CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NumerWZ'), TZnakowyJPK, scope=CTD_ANON_7, documentation='Numer dokumentu WZ', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 266, 10)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataWZ'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TData, scope=CTD_ANON_7, documentation='Data dokumentu WZ', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 271, 10)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'WartoscWZ'), TKwotowy, scope=CTD_ANON_7, documentation='Warto\u015b\u0107 dokumentu WZ', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 276, 10)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataWydaniaWZ'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TData, scope=CTD_ANON_7, documentation='Data wydania towaru/materia\u0142u', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 281, 10)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OdbiorcaWZ'), TZnakowyJPK, scope=CTD_ANON_7, documentation='Odbiorca towaru/materia\u0142u', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 286, 10)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NumerFaWZ'), TZnakowyJPK, scope=CTD_ANON_7, documentation='Numer faktury lub specyfikacji dotycz\u0105cej wydanego towaru/materia\u0142u', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 291, 10)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataFaWZ'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TData, scope=CTD_ANON_7, documentation='Data faktury lub specyfikacji dotycz\u0105cej wydanego towaru/materia\u0142u', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 296, 10)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 291, 10))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 296, 10))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NumerWZ')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 266, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataWZ')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 271, 10))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'WartoscWZ')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 276, 10))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataWydaniaWZ')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 281, 10))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OdbiorcaWZ')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 286, 10))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NumerFaWZ')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 291, 10))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataFaWZ')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 296, 10))
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
    transitions.append(fac.Transition(st_6, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_7._Automaton = _BuildAutomaton_8()




CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Numer2WZ'), TZnakowyJPK, scope=CTD_ANON_8, documentation='Numer dokumentu WZ', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 310, 10)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'KodTowaruWZ'), TZnakowyJPK, scope=CTD_ANON_8, documentation='Kod towaru/materia\u0142u/opakowania', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 315, 10)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NazwaTowaruWZ'), TZnakowyJPK, scope=CTD_ANON_8, documentation='Nazwa towaru/materia\u0142u/opakowania', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 320, 10)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'IloscWydanaWZ'), TIlosciJPK, scope=CTD_ANON_8, documentation='Ilo\u015b\u0107 wydana', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 325, 10)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'JednostkaMiaryWZ'), TZnakowyJPK, scope=CTD_ANON_8, documentation='Jednostka miary', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 330, 10)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CenaJednWZ'), TKwotowy, scope=CTD_ANON_8, documentation='Cena towaru/materia\u0142u/opakowania', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 335, 10)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'WartoscPozycjiWZ'), TKwotowy, scope=CTD_ANON_8, documentation='Warto\u015b\u0107 towaru/materia\u0142u/opakowania', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 340, 10)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 315, 10))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Numer2WZ')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 310, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'KodTowaruWZ')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 315, 10))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NazwaTowaruWZ')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 320, 10))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'IloscWydanaWZ')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 325, 10))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'JednostkaMiaryWZ')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 330, 10))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CenaJednWZ')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 335, 10))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'WartoscPozycjiWZ')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 340, 10))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
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
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_8._Automaton = _BuildAutomaton_9()




CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LiczbaWZ'), TNaturalnyJPK, scope=CTD_ANON_9, documentation='Liczba dokument\xf3w WZ', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 354, 10)))

CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SumaWZ'), TKwotowy, scope=CTD_ANON_9, documentation='Warto\u015b\u0107 dokument\xf3w WZ', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 359, 10)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LiczbaWZ')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 354, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SumaWZ')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 359, 10))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_9._Automaton = _BuildAutomaton_10()




CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RWWartosc'), CTD_ANON_11, scope=CTD_ANON_10, documentation='Zestawienie dowod\xf3w RW', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 376, 7)))

CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RWWiersz'), CTD_ANON_12, scope=CTD_ANON_10, documentation='Szczeg\xf3\u0142owe pozycje dowod\xf3w RW', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 415, 7)))

CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RWCtrl'), CTD_ANON_13, scope=CTD_ANON_10, documentation='RW -sumy kontrolne', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 459, 7)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RWWartosc')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 376, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RWWiersz')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 415, 7))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RWCtrl')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 459, 7))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_10._Automaton = _BuildAutomaton_11()




CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NumerRW'), TZnakowyJPK, scope=CTD_ANON_11, documentation='Numer dokumentu RW', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 382, 10)))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataRW'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TData, scope=CTD_ANON_11, documentation='Data dokumentu RW', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 387, 10)))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'WartoscRW'), TKwotowy, scope=CTD_ANON_11, documentation='Warto\u015b\u0107 dokumentu RW', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 392, 10)))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataWydaniaRW'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TData, scope=CTD_ANON_11, documentation='Data wydania towaru/materia\u0142u', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 397, 10)))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SkadRW'), TZnakowyJPK, scope=CTD_ANON_11, documentation='Miejsce wydania towaru/materia\u0142u', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 402, 10)))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DokadRW'), TZnakowyJPK, scope=CTD_ANON_11, documentation='Miejsce przeznacznienia towaru/materia\u0142u', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 407, 10)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 402, 10))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 407, 10))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NumerRW')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 382, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataRW')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 387, 10))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'WartoscRW')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 392, 10))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataWydaniaRW')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 397, 10))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SkadRW')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 402, 10))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DokadRW')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 407, 10))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
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
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_11._Automaton = _BuildAutomaton_12()




CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Numer2RW'), TZnakowyJPK, scope=CTD_ANON_12, documentation='Numer dokumentu RW', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 421, 10)))

CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'KodTowaruRW'), TZnakowyJPK, scope=CTD_ANON_12, documentation='Kod towaru/materia\u0142u/opakowania', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 426, 10)))

CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NazwaTowaruRW'), TZnakowyJPK, scope=CTD_ANON_12, documentation='Nazwa towaru/materia\u0142u/opakowania', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 431, 10)))

CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'IloscWydanaRW'), TIlosciJPK, scope=CTD_ANON_12, documentation='Ilo\u015b\u0107 wydana', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 436, 10)))

CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'JednostkaMiaryRW'), TZnakowyJPK, scope=CTD_ANON_12, documentation='Jednostka miary', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 441, 10)))

CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CenaJednRW'), TKwotowy, scope=CTD_ANON_12, documentation='Cena towaru/materia\u0142u/opakowania', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 446, 10)))

CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'WartoscPozycjiRW'), TKwotowy, scope=CTD_ANON_12, documentation='Warto\u015b\u0107 towaru/materia\u0142u/opakowania', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 451, 10)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 426, 10))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Numer2RW')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 421, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'KodTowaruRW')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 426, 10))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NazwaTowaruRW')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 431, 10))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'IloscWydanaRW')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 436, 10))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'JednostkaMiaryRW')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 441, 10))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CenaJednRW')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 446, 10))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'WartoscPozycjiRW')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 451, 10))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
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
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_12._Automaton = _BuildAutomaton_13()




CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LiczbaRW'), TNaturalnyJPK, scope=CTD_ANON_13, documentation='Liczba dokument\xf3w RW', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 465, 10)))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SumaRW'), TKwotowy, scope=CTD_ANON_13, documentation='Warto\u015b\u0107 dokument\xf3w RW', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 470, 10)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LiczbaRW')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 465, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SumaRW')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 470, 10))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_13._Automaton = _BuildAutomaton_14()




CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MMWartosc'), CTD_ANON_15, scope=CTD_ANON_14, documentation='Zestawienie dowod\xf3w MM', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 487, 7)))

CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MMWiersz'), CTD_ANON_16, scope=CTD_ANON_14, documentation='Szczeg\xf3\u0142owe pozycje dowod\xf3w MM', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 526, 7)))

CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MMCtrl'), CTD_ANON_17, scope=CTD_ANON_14, documentation='MM -sumy kontrolne', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 570, 7)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MMWartosc')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 487, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MMWiersz')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 526, 7))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MMCtrl')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 570, 7))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_14._Automaton = _BuildAutomaton_15()




CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NumerMM'), TZnakowyJPK, scope=CTD_ANON_15, documentation='Numer dokumentu MM', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 493, 10)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataMM'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TData, scope=CTD_ANON_15, documentation='Data dokumentu MM', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 498, 10)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'WartoscMM'), TKwotowy, scope=CTD_ANON_15, documentation='Warto\u015b\u0107 dokumentu MM', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 503, 10)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataWydaniaMM'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TData, scope=CTD_ANON_15, documentation='Data wydania towaru/materia\u0142u', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 508, 10)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SkadMM'), TZnakowyJPK, scope=CTD_ANON_15, documentation='Miejsce wydania towaru/materia\u0142u', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 513, 10)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DokadMM'), TZnakowyJPK, scope=CTD_ANON_15, documentation='Miejsce przeznacznienia towaru/materia\u0142u', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 518, 10)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 513, 10))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 518, 10))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NumerMM')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 493, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataMM')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 498, 10))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'WartoscMM')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 503, 10))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataWydaniaMM')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 508, 10))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SkadMM')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 513, 10))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DokadMM')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 518, 10))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
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
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_15._Automaton = _BuildAutomaton_16()




CTD_ANON_16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Numer2MM'), TZnakowyJPK, scope=CTD_ANON_16, documentation='Numer dokumentu MM', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 532, 10)))

CTD_ANON_16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'KodTowaruMM'), TZnakowyJPK, scope=CTD_ANON_16, documentation='Kod towaru/materia\u0142u/opakowania', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 537, 10)))

CTD_ANON_16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NazwaTowaruMM'), TZnakowyJPK, scope=CTD_ANON_16, documentation='Nazwa towaru/materia\u0142u/opakowania', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 542, 10)))

CTD_ANON_16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'IloscWydanaMM'), TIlosciJPK, scope=CTD_ANON_16, documentation='Ilo\u015b\u0107 wydana', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 547, 10)))

CTD_ANON_16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'JednostkaMiaryMM'), TZnakowyJPK, scope=CTD_ANON_16, documentation='Jednostka miary', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 552, 10)))

CTD_ANON_16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CenaJednMM'), TKwotowy, scope=CTD_ANON_16, documentation='Cena towaru/materia\u0142u/opakowania', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 557, 10)))

CTD_ANON_16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'WartoscPozycjiMM'), TKwotowy, scope=CTD_ANON_16, documentation='Warto\u015b\u0107 towaru/materia\u0142u/opakowania', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 562, 10)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 537, 10))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Numer2MM')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 532, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'KodTowaruMM')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 537, 10))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NazwaTowaruMM')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 542, 10))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'IloscWydanaMM')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 547, 10))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'JednostkaMiaryMM')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 552, 10))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CenaJednMM')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 557, 10))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'WartoscPozycjiMM')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 562, 10))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
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
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_16._Automaton = _BuildAutomaton_17()




CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LiczbaMM'), TNaturalnyJPK, scope=CTD_ANON_17, documentation='Liczba dokument\xf3w MM', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 576, 10)))

CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SumaMM'), TKwotowy, scope=CTD_ANON_17, documentation='Warto\u015b\u0107 dokument\xf3w MM', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 581, 10)))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LiczbaMM')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 576, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SumaMM')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd', 581, 10))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_17._Automaton = _BuildAutomaton_18()

