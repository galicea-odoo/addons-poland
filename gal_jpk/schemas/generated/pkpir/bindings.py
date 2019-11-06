# /home/maciek/odoo-dev/gal/galicea/gal_jpk/schemas/generated/pkpir/bindings.py
# -*- coding: utf-8 -*-
# @generated
# PyXB bindings for NM:30ffae5c4066cfc8cd81f77679a2522c2bf457f5
# Generated 2018-03-08 13:30:04.722086 by PyXB version 1.2.5 using Python 2.7.12.final.0
# Namespace http://jpk.mf.gov.pl/wzor/2016/10/26/10262/

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
Namespace = pyxb.namespace.NamespaceForURI('http://jpk.mf.gov.pl/wzor/2016/10/26/10262/', create_if_missing=True)
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


# Atomic simple type: {http://jpk.mf.gov.pl/wzor/2016/10/26/10262/}TKodFormularza
class TKodFormularza (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Symbol wzoru formularza"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TKodFormularza')
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 6, 1)
    _Documentation = 'Symbol wzoru formularza'
TKodFormularza._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TKodFormularza, enum_prefix=None)
TKodFormularza.JPK_PKPIR = TKodFormularza._CF_enumeration.addEnumeration(unicode_value='JPK_PKPIR', tag='JPK_PKPIR')
TKodFormularza._InitializeFacetMap(TKodFormularza._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'TKodFormularza', TKodFormularza)
_module_typeBindings.TKodFormularza = TKodFormularza

# Atomic simple type: {http://jpk.mf.gov.pl/wzor/2016/10/26/10262/}TCelZlozenia
class TCelZlozenia (pyxb.binding.datatypes.byte, pyxb.binding.basis.enumeration_mixin):

    """Określenie celu złożenia JPK"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TCelZlozenia')
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 14, 1)
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
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 42, 4)
    _Documentation = None
STD_ANON._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON, enum_prefix=None)
STD_ANON._CF_enumeration.addEnumeration(unicode_value='2', tag=None)
STD_ANON._InitializeFacetMap(STD_ANON._CF_enumeration)
_module_typeBindings.STD_ANON = STD_ANON

# Atomic simple type: {http://jpk.mf.gov.pl/wzor/2016/10/26/10262/}TKwotowy
class TKwotowy (pyxb.binding.datatypes.decimal):

    """Wartość numeryczna 18 znaków max, w tym 2 znaki po przecinku"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TKwotowy')
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 72, 1)
    _Documentation = 'Warto\u015b\u0107 numeryczna 18 znak\xf3w max, w tym 2 znaki po przecinku'
TKwotowy._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(2))
TKwotowy._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(18))
TKwotowy._InitializeFacetMap(TKwotowy._CF_fractionDigits,
   TKwotowy._CF_totalDigits)
Namespace.addCategoryObject('typeBinding', 'TKwotowy', TKwotowy)
_module_typeBindings.TKwotowy = TKwotowy

# Atomic simple type: {http://jpk.mf.gov.pl/wzor/2016/10/26/10262/}TZnakowyJPK
class TZnakowyJPK (pyxb.binding.datatypes.token):

    """Typ znakowy ograniczony do 256 znaków"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TZnakowyJPK')
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 89, 1)
    _Documentation = 'Typ znakowy ograniczony do 256 znak\xf3w'
TZnakowyJPK._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
TZnakowyJPK._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(256))
TZnakowyJPK._InitializeFacetMap(TZnakowyJPK._CF_minLength,
   TZnakowyJPK._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'TZnakowyJPK', TZnakowyJPK)
_module_typeBindings.TZnakowyJPK = TZnakowyJPK

# Atomic simple type: {http://jpk.mf.gov.pl/wzor/2016/10/26/10262/}TNaturalnyJPK
class TNaturalnyJPK (_ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TNaturalny):

    """Liczby naturalne większe od zera"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TNaturalnyJPK')
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 81, 1)
    _Documentation = 'Liczby naturalne wi\u0119ksze od zera'
TNaturalnyJPK._CF_minExclusive = pyxb.binding.facets.CF_minExclusive(value_datatype=_ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TNaturalny, value=pyxb.binding.datatypes.integer(0))
TNaturalnyJPK._InitializeFacetMap(TNaturalnyJPK._CF_minExclusive)
Namespace.addCategoryObject('typeBinding', 'TNaturalnyJPK', TNaturalnyJPK)
_module_typeBindings.TNaturalnyJPK = TNaturalnyJPK

# Complex type {http://jpk.mf.gov.pl/wzor/2016/10/26/10262/}TNaglowek with content type ELEMENT_ONLY
class TNaglowek (pyxb.binding.basis.complexTypeDefinition):
    """Nagłówek JPK_PKPIR"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TNaglowek')
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 26, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://jpk.mf.gov.pl/wzor/2016/10/26/10262/}KodFormularza uses Python identifier KodFormularza
    __KodFormularza = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'KodFormularza'), 'KodFormularza', '__httpjpk_mf_gov_plwzor2016102610262_TNaglowek_httpjpk_mf_gov_plwzor2016102610262KodFormularza', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 31, 3), )

    
    KodFormularza = property(__KodFormularza.value, __KodFormularza.set, None, None)

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/10/26/10262/}WariantFormularza uses Python identifier WariantFormularza
    __WariantFormularza = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'WariantFormularza'), 'WariantFormularza', '__httpjpk_mf_gov_plwzor2016102610262_TNaglowek_httpjpk_mf_gov_plwzor2016102610262WariantFormularza', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 41, 3), )

    
    WariantFormularza = property(__WariantFormularza.value, __WariantFormularza.set, None, None)

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/10/26/10262/}CelZlozenia uses Python identifier CelZlozenia
    __CelZlozenia = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CelZlozenia'), 'CelZlozenia', '__httpjpk_mf_gov_plwzor2016102610262_TNaglowek_httpjpk_mf_gov_plwzor2016102610262CelZlozenia', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 48, 3), )

    
    CelZlozenia = property(__CelZlozenia.value, __CelZlozenia.set, None, None)

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/10/26/10262/}DataWytworzeniaJPK uses Python identifier DataWytworzeniaJPK
    __DataWytworzeniaJPK = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DataWytworzeniaJPK'), 'DataWytworzeniaJPK', '__httpjpk_mf_gov_plwzor2016102610262_TNaglowek_httpjpk_mf_gov_plwzor2016102610262DataWytworzeniaJPK', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 49, 3), )

    
    DataWytworzeniaJPK = property(__DataWytworzeniaJPK.value, __DataWytworzeniaJPK.set, None, 'Data i czas wytworzenia JPK_PKPIR')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/10/26/10262/}DataOd uses Python identifier DataOd
    __DataOd = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DataOd'), 'DataOd', '__httpjpk_mf_gov_plwzor2016102610262_TNaglowek_httpjpk_mf_gov_plwzor2016102610262DataOd', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 54, 3), )

    
    DataOd = property(__DataOd.value, __DataOd.set, None, 'Data pocz\u0105tkowa okresu, kt\xf3rego dotyczy JPK_PKPIR')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/10/26/10262/}DataDo uses Python identifier DataDo
    __DataDo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DataDo'), 'DataDo', '__httpjpk_mf_gov_plwzor2016102610262_TNaglowek_httpjpk_mf_gov_plwzor2016102610262DataDo', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 59, 3), )

    
    DataDo = property(__DataDo.value, __DataDo.set, None, 'Data ko\u0144cowa okresu, kt\xf3rego dotyczy JPK_PKPIR')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/10/26/10262/}DomyslnyKodWaluty uses Python identifier DomyslnyKodWaluty
    __DomyslnyKodWaluty = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DomyslnyKodWaluty'), 'DomyslnyKodWaluty', '__httpjpk_mf_gov_plwzor2016102610262_TNaglowek_httpjpk_mf_gov_plwzor2016102610262DomyslnyKodWaluty', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 64, 3), )

    
    DomyslnyKodWaluty = property(__DomyslnyKodWaluty.value, __DomyslnyKodWaluty.set, None, 'Trzyliterowy kod lokalnej waluty (ISO-4217), domy\u015blny dla wytworzonego JPK_PKPIR')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/10/26/10262/}KodUrzedu uses Python identifier KodUrzedu
    __KodUrzedu = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'KodUrzedu'), 'KodUrzedu', '__httpjpk_mf_gov_plwzor2016102610262_TNaglowek_httpjpk_mf_gov_plwzor2016102610262KodUrzedu', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 69, 3), )

    
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


# Complex type {http://jpk.mf.gov.pl/wzor/2016/10/26/10262/}TAdresJPK with content type ELEMENT_ONLY
class TAdresJPK (pyxb.binding.basis.complexTypeDefinition):
    """Informacje opisujące adres"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TAdresJPK')
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 98, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://jpk.mf.gov.pl/wzor/2016/10/26/10262/}KodKraju uses Python identifier KodKraju
    __KodKraju = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'KodKraju'), 'KodKraju', '__httpjpk_mf_gov_plwzor2016102610262_TAdresJPK_httpjpk_mf_gov_plwzor2016102610262KodKraju', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 103, 3), )

    
    KodKraju = property(__KodKraju.value, __KodKraju.set, None, 'Kraj')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/10/26/10262/}Wojewodztwo uses Python identifier Wojewodztwo
    __Wojewodztwo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Wojewodztwo'), 'Wojewodztwo', '__httpjpk_mf_gov_plwzor2016102610262_TAdresJPK_httpjpk_mf_gov_plwzor2016102610262Wojewodztwo', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 108, 3), )

    
    Wojewodztwo = property(__Wojewodztwo.value, __Wojewodztwo.set, None, 'Wojew\xf3dztwo')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/10/26/10262/}Powiat uses Python identifier Powiat
    __Powiat = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Powiat'), 'Powiat', '__httpjpk_mf_gov_plwzor2016102610262_TAdresJPK_httpjpk_mf_gov_plwzor2016102610262Powiat', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 113, 3), )

    
    Powiat = property(__Powiat.value, __Powiat.set, None, 'Powiat')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/10/26/10262/}Gmina uses Python identifier Gmina
    __Gmina = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Gmina'), 'Gmina', '__httpjpk_mf_gov_plwzor2016102610262_TAdresJPK_httpjpk_mf_gov_plwzor2016102610262Gmina', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 118, 3), )

    
    Gmina = property(__Gmina.value, __Gmina.set, None, 'Gmina')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/10/26/10262/}Ulica uses Python identifier Ulica
    __Ulica = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Ulica'), 'Ulica', '__httpjpk_mf_gov_plwzor2016102610262_TAdresJPK_httpjpk_mf_gov_plwzor2016102610262Ulica', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 123, 3), )

    
    Ulica = property(__Ulica.value, __Ulica.set, None, 'Nazwa ulicy')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/10/26/10262/}NrDomu uses Python identifier NrDomu
    __NrDomu = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NrDomu'), 'NrDomu', '__httpjpk_mf_gov_plwzor2016102610262_TAdresJPK_httpjpk_mf_gov_plwzor2016102610262NrDomu', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 128, 3), )

    
    NrDomu = property(__NrDomu.value, __NrDomu.set, None, 'Numer budynku')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/10/26/10262/}NrLokalu uses Python identifier NrLokalu
    __NrLokalu = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NrLokalu'), 'NrLokalu', '__httpjpk_mf_gov_plwzor2016102610262_TAdresJPK_httpjpk_mf_gov_plwzor2016102610262NrLokalu', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 133, 3), )

    
    NrLokalu = property(__NrLokalu.value, __NrLokalu.set, None, 'Numer lokalu')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/10/26/10262/}Miejscowosc uses Python identifier Miejscowosc
    __Miejscowosc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Miejscowosc'), 'Miejscowosc', '__httpjpk_mf_gov_plwzor2016102610262_TAdresJPK_httpjpk_mf_gov_plwzor2016102610262Miejscowosc', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 138, 3), )

    
    Miejscowosc = property(__Miejscowosc.value, __Miejscowosc.set, None, 'Nazwa miejscowo\u015bci')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/10/26/10262/}KodPocztowy uses Python identifier KodPocztowy
    __KodPocztowy = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'KodPocztowy'), 'KodPocztowy', '__httpjpk_mf_gov_plwzor2016102610262_TAdresJPK_httpjpk_mf_gov_plwzor2016102610262KodPocztowy', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 143, 3), )

    
    KodPocztowy = property(__KodPocztowy.value, __KodPocztowy.set, None, 'Kod pocztowy')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/10/26/10262/}Poczta uses Python identifier Poczta
    __Poczta = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Poczta'), 'Poczta', '__httpjpk_mf_gov_plwzor2016102610262_TAdresJPK_httpjpk_mf_gov_plwzor2016102610262Poczta', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 148, 3), )

    
    Poczta = property(__Poczta.value, __Poczta.set, None, 'Nazwa urz\u0119du pocztowego')

    _ElementMap.update({
        __KodKraju.name() : __KodKraju,
        __Wojewodztwo.name() : __Wojewodztwo,
        __Powiat.name() : __Powiat,
        __Gmina.name() : __Gmina,
        __Ulica.name() : __Ulica,
        __NrDomu.name() : __NrDomu,
        __NrLokalu.name() : __NrLokalu,
        __Miejscowosc.name() : __Miejscowosc,
        __KodPocztowy.name() : __KodPocztowy,
        __Poczta.name() : __Poczta
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TAdresJPK = TAdresJPK
Namespace.addCategoryObject('typeBinding', 'TAdresJPK', TAdresJPK)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Jednolity plik kontrolny dla podatkowej księgi przychodów i rozchodów"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 159, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://jpk.mf.gov.pl/wzor/2016/10/26/10262/}Naglowek uses Python identifier Naglowek
    __Naglowek = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Naglowek'), 'Naglowek', '__httpjpk_mf_gov_plwzor2016102610262_CTD_ANON_httpjpk_mf_gov_plwzor2016102610262Naglowek', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 161, 4), )

    
    Naglowek = property(__Naglowek.value, __Naglowek.set, None, 'Nag\u0142\xf3wek JPK_PKPIR')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/10/26/10262/}Podmiot1 uses Python identifier Podmiot1
    __Podmiot1 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Podmiot1'), 'Podmiot1', '__httpjpk_mf_gov_plwzor2016102610262_CTD_ANON_httpjpk_mf_gov_plwzor2016102610262Podmiot1', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 166, 4), )

    
    Podmiot1 = property(__Podmiot1.value, __Podmiot1.set, None, None)

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/10/26/10262/}PKPIRInfo uses Python identifier PKPIRInfo
    __PKPIRInfo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PKPIRInfo'), 'PKPIRInfo', '__httpjpk_mf_gov_plwzor2016102610262_CTD_ANON_httpjpk_mf_gov_plwzor2016102610262PKPIRInfo', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 182, 4), )

    
    PKPIRInfo = property(__PKPIRInfo.value, __PKPIRInfo.set, None, 'Dane dotycz\u0105ce ustalenia dochodu w roku podatkowym')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/10/26/10262/}PKPIRSpis uses Python identifier PKPIRSpis
    __PKPIRSpis = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PKPIRSpis'), 'PKPIRSpis', '__httpjpk_mf_gov_plwzor2016102610262_CTD_ANON_httpjpk_mf_gov_plwzor2016102610262PKPIRSpis', True, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 211, 4), )

    
    PKPIRSpis = property(__PKPIRSpis.value, __PKPIRSpis.set, None, 'Spisy z natury sporz\u0105dzone w ci\u0105gu roku podatkowego')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/10/26/10262/}PKPIRWiersz uses Python identifier PKPIRWiersz
    __PKPIRWiersz = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PKPIRWiersz'), 'PKPIRWiersz', '__httpjpk_mf_gov_plwzor2016102610262_CTD_ANON_httpjpk_mf_gov_plwzor2016102610262PKPIRWiersz', True, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 231, 4), )

    
    PKPIRWiersz = property(__PKPIRWiersz.value, __PKPIRWiersz.set, None, 'Na podstawie za\u0142\u0105cznika do rozporz\u0105dzenia Ministra Finans\xf3w z dnia 26 sierpnia 2003 r. w sprawie prowadzenia podatkowej ksi\u0119gi przychod\xf3w i rozchod\xf3w (Dz. U. z 2014 r. poz. 1037, z p\xf3\u017an. zm.)')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/10/26/10262/}PKPIRCtrl uses Python identifier PKPIRCtrl
    __PKPIRCtrl = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PKPIRCtrl'), 'PKPIRCtrl', '__httpjpk_mf_gov_plwzor2016102610262_CTD_ANON_httpjpk_mf_gov_plwzor2016102610262PKPIRCtrl', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 334, 4), )

    
    PKPIRCtrl = property(__PKPIRCtrl.value, __PKPIRCtrl.set, None, 'Sumy kontrolne dla tabeli PKPIRWiersz')

    _ElementMap.update({
        __Naglowek.name() : __Naglowek,
        __Podmiot1.name() : __Podmiot1,
        __PKPIRInfo.name() : __PKPIRInfo,
        __PKPIRSpis.name() : __PKPIRSpis,
        __PKPIRWiersz.name() : __PKPIRWiersz,
        __PKPIRCtrl.name() : __PKPIRCtrl
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
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 167, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://jpk.mf.gov.pl/wzor/2016/10/26/10262/}IdentyfikatorPodmiotu uses Python identifier IdentyfikatorPodmiotu
    __IdentyfikatorPodmiotu = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'IdentyfikatorPodmiotu'), 'IdentyfikatorPodmiotu', '__httpjpk_mf_gov_plwzor2016102610262_CTD_ANON__httpjpk_mf_gov_plwzor2016102610262IdentyfikatorPodmiotu', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 169, 7), )

    
    IdentyfikatorPodmiotu = property(__IdentyfikatorPodmiotu.value, __IdentyfikatorPodmiotu.set, None, 'Dane identyfikuj\u0105ce podmiot')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/10/26/10262/}AdresPodmiotu uses Python identifier AdresPodmiotu
    __AdresPodmiotu = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AdresPodmiotu'), 'AdresPodmiotu', '__httpjpk_mf_gov_plwzor2016102610262_CTD_ANON__httpjpk_mf_gov_plwzor2016102610262AdresPodmiotu', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 174, 7), )

    
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
    """Dane dotyczące ustalenia dochodu w roku podatkowym"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 186, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://jpk.mf.gov.pl/wzor/2016/10/26/10262/}P_1 uses Python identifier P_1
    __P_1 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_1'), 'P_1', '__httpjpk_mf_gov_plwzor2016102610262_CTD_ANON_2_httpjpk_mf_gov_plwzor2016102610262P_1', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 188, 7), )

    
    P_1 = property(__P_1.value, __P_1.set, None, 'Warto\u015b\u0107 spisu z natury na pocz\u0105tek roku podatkowego')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/10/26/10262/}P_2 uses Python identifier P_2
    __P_2 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_2'), 'P_2', '__httpjpk_mf_gov_plwzor2016102610262_CTD_ANON_2_httpjpk_mf_gov_plwzor2016102610262P_2', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 193, 7), )

    
    P_2 = property(__P_2.value, __P_2.set, None, 'Warto\u015b\u0107 spisu z natury na koniec roku podatkowego')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/10/26/10262/}P_3 uses Python identifier P_3
    __P_3 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_3'), 'P_3', '__httpjpk_mf_gov_plwzor2016102610262_CTD_ANON_2_httpjpk_mf_gov_plwzor2016102610262P_3', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 198, 7), )

    
    P_3 = property(__P_3.value, __P_3.set, None, 'Razem koszty uzyskania przychodu, wg obja\u015bnie\u0144 do podatkowej ksi\u0119gi przychod\xf3w i rozchod\xf3w')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/10/26/10262/}P_4 uses Python identifier P_4
    __P_4 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_4'), 'P_4', '__httpjpk_mf_gov_plwzor2016102610262_CTD_ANON_2_httpjpk_mf_gov_plwzor2016102610262P_4', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 203, 7), )

    
    P_4 = property(__P_4.value, __P_4.set, None, 'Doch\xf3d osi\u0105gni\u0119ty w roku podatkowym, wg obja\u015bnie\u0144 do podatkowej ksi\u0119gi przychod\xf3w i rozchod\xf3w')

    _ElementMap.update({
        __P_1.name() : __P_1,
        __P_2.name() : __P_2,
        __P_3.name() : __P_3,
        __P_4.name() : __P_4
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_2 = CTD_ANON_2


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """Spisy z natury sporządzone w ciągu roku podatkowego"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 215, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://jpk.mf.gov.pl/wzor/2016/10/26/10262/}P_5A uses Python identifier P_5A
    __P_5A = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_5A'), 'P_5A', '__httpjpk_mf_gov_plwzor2016102610262_CTD_ANON_3_httpjpk_mf_gov_plwzor2016102610262P_5A', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 217, 7), )

    
    P_5A = property(__P_5A.value, __P_5A.set, None, 'Data spisu z natury sporz\u0105dzonego w ci\u0105gu roku podatkowego')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/10/26/10262/}P_5B uses Python identifier P_5B
    __P_5B = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_5B'), 'P_5B', '__httpjpk_mf_gov_plwzor2016102610262_CTD_ANON_3_httpjpk_mf_gov_plwzor2016102610262P_5B', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 222, 7), )

    
    P_5B = property(__P_5B.value, __P_5B.set, None, 'Warto\u015b\u0107 spisu z natury sporz\u0105dzonego w ci\u0105gu roku podatkowego')

    
    # Attribute typ uses Python identifier typ
    __typ = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'typ'), 'typ', '__httpjpk_mf_gov_plwzor2016102610262_CTD_ANON_3_typ', pyxb.binding.datatypes.anySimpleType, fixed=True, unicode_default='G', required=True)
    __typ._DeclarationLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 228, 6)
    __typ._UseLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 228, 6)
    
    typ = property(__typ.value, __typ.set, None, None)

    _ElementMap.update({
        __P_5A.name() : __P_5A,
        __P_5B.name() : __P_5B
    })
    _AttributeMap.update({
        __typ.name() : __typ
    })
_module_typeBindings.CTD_ANON_3 = CTD_ANON_3


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """Na podstawie załącznika do rozporządzenia Ministra Finansów z dnia 26 sierpnia 2003 r. w sprawie prowadzenia podatkowej księgi przychodów i rozchodów (Dz. U. z 2014 r. poz. 1037, z późn. zm.)"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 235, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://jpk.mf.gov.pl/wzor/2016/10/26/10262/}K_1 uses Python identifier K_1
    __K_1 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'K_1'), 'K_1', '__httpjpk_mf_gov_plwzor2016102610262_CTD_ANON_4_httpjpk_mf_gov_plwzor2016102610262K_1', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 237, 7), )

    
    K_1 = property(__K_1.value, __K_1.set, None, 'Lp.')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/10/26/10262/}K_2 uses Python identifier K_2
    __K_2 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'K_2'), 'K_2', '__httpjpk_mf_gov_plwzor2016102610262_CTD_ANON_4_httpjpk_mf_gov_plwzor2016102610262K_2', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 242, 7), )

    
    K_2 = property(__K_2.value, __K_2.set, None, 'Data zdarzenia gospodarczego')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/10/26/10262/}K_3 uses Python identifier K_3
    __K_3 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'K_3'), 'K_3', '__httpjpk_mf_gov_plwzor2016102610262_CTD_ANON_4_httpjpk_mf_gov_plwzor2016102610262K_3', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 247, 7), )

    
    K_3 = property(__K_3.value, __K_3.set, None, 'Nr dowodu ksi\u0119gowego')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/10/26/10262/}K_4 uses Python identifier K_4
    __K_4 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'K_4'), 'K_4', '__httpjpk_mf_gov_plwzor2016102610262_CTD_ANON_4_httpjpk_mf_gov_plwzor2016102610262K_4', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 252, 7), )

    
    K_4 = property(__K_4.value, __K_4.set, None, 'Kontrahent - imi\u0119 i nazwisko (firma)')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/10/26/10262/}K_5 uses Python identifier K_5
    __K_5 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'K_5'), 'K_5', '__httpjpk_mf_gov_plwzor2016102610262_CTD_ANON_4_httpjpk_mf_gov_plwzor2016102610262K_5', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 257, 7), )

    
    K_5 = property(__K_5.value, __K_5.set, None, 'Kontrahent- adres')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/10/26/10262/}K_6 uses Python identifier K_6
    __K_6 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'K_6'), 'K_6', '__httpjpk_mf_gov_plwzor2016102610262_CTD_ANON_4_httpjpk_mf_gov_plwzor2016102610262K_6', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 262, 7), )

    
    K_6 = property(__K_6.value, __K_6.set, None, 'Opis zdarzenia gospodarczego')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/10/26/10262/}K_7 uses Python identifier K_7
    __K_7 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'K_7'), 'K_7', '__httpjpk_mf_gov_plwzor2016102610262_CTD_ANON_4_httpjpk_mf_gov_plwzor2016102610262K_7', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 267, 7), )

    
    K_7 = property(__K_7.value, __K_7.set, None, 'Przych\xf3d - warto\u015b\u0107 sprzedanych towar\xf3w i us\u0142ug')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/10/26/10262/}K_8 uses Python identifier K_8
    __K_8 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'K_8'), 'K_8', '__httpjpk_mf_gov_plwzor2016102610262_CTD_ANON_4_httpjpk_mf_gov_plwzor2016102610262K_8', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 272, 7), )

    
    K_8 = property(__K_8.value, __K_8.set, None, 'Przych\xf3d - pozosta\u0142e przychody')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/10/26/10262/}K_9 uses Python identifier K_9
    __K_9 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'K_9'), 'K_9', '__httpjpk_mf_gov_plwzor2016102610262_CTD_ANON_4_httpjpk_mf_gov_plwzor2016102610262K_9', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 277, 7), )

    
    K_9 = property(__K_9.value, __K_9.set, None, 'Przych\xf3d - razem przych\xf3d (7+8)')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/10/26/10262/}K_10 uses Python identifier K_10
    __K_10 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'K_10'), 'K_10', '__httpjpk_mf_gov_plwzor2016102610262_CTD_ANON_4_httpjpk_mf_gov_plwzor2016102610262K_10', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 282, 7), )

    
    K_10 = property(__K_10.value, __K_10.set, None, 'Zakup towar\xf3w handlowych i materia\u0142\xf3w wg cen zakupu')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/10/26/10262/}K_11 uses Python identifier K_11
    __K_11 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'K_11'), 'K_11', '__httpjpk_mf_gov_plwzor2016102610262_CTD_ANON_4_httpjpk_mf_gov_plwzor2016102610262K_11', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 287, 7), )

    
    K_11 = property(__K_11.value, __K_11.set, None, 'Koszty uboczne zakupu')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/10/26/10262/}K_12 uses Python identifier K_12
    __K_12 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'K_12'), 'K_12', '__httpjpk_mf_gov_plwzor2016102610262_CTD_ANON_4_httpjpk_mf_gov_plwzor2016102610262K_12', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 292, 7), )

    
    K_12 = property(__K_12.value, __K_12.set, None, 'Wydatki (koszty) - wynagrodzenia w got\xf3wce i w naturze')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/10/26/10262/}K_13 uses Python identifier K_13
    __K_13 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'K_13'), 'K_13', '__httpjpk_mf_gov_plwzor2016102610262_CTD_ANON_4_httpjpk_mf_gov_plwzor2016102610262K_13', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 297, 7), )

    
    K_13 = property(__K_13.value, __K_13.set, None, 'Wydatki (koszty) - pozosta\u0142e wydatki')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/10/26/10262/}K_14 uses Python identifier K_14
    __K_14 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'K_14'), 'K_14', '__httpjpk_mf_gov_plwzor2016102610262_CTD_ANON_4_httpjpk_mf_gov_plwzor2016102610262K_14', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 302, 7), )

    
    K_14 = property(__K_14.value, __K_14.set, None, 'Wydatki (koszty) - razem wydatki (12+13)')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/10/26/10262/}K_15 uses Python identifier K_15
    __K_15 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'K_15'), 'K_15', '__httpjpk_mf_gov_plwzor2016102610262_CTD_ANON_4_httpjpk_mf_gov_plwzor2016102610262K_15', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 307, 7), )

    
    K_15 = property(__K_15.value, __K_15.set, None, 'Wydatki (koszty) - pole wolne')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/10/26/10262/}K_16A uses Python identifier K_16A
    __K_16A = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'K_16A'), 'K_16A', '__httpjpk_mf_gov_plwzor2016102610262_CTD_ANON_4_httpjpk_mf_gov_plwzor2016102610262K_16A', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 313, 8), )

    
    K_16A = property(__K_16A.value, __K_16A.set, None, 'Koszty dzia\u0142alno\u015bci badawczo\n-rozwojowej, o kt\xf3rych mowa w art. 26e ustawy o podatku dochodowym - opis kosztu')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/10/26/10262/}K_16B uses Python identifier K_16B
    __K_16B = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'K_16B'), 'K_16B', '__httpjpk_mf_gov_plwzor2016102610262_CTD_ANON_4_httpjpk_mf_gov_plwzor2016102610262K_16B', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 319, 8), )

    
    K_16B = property(__K_16B.value, __K_16B.set, None, 'Koszty dzia\u0142alno\u015bci badawczo-rozwojowej, o kt\xf3rych mowa w art. 26e ustawy o podatku dochodowym - warto\u015b\u0107')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/10/26/10262/}K_17 uses Python identifier K_17
    __K_17 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'K_17'), 'K_17', '__httpjpk_mf_gov_plwzor2016102610262_CTD_ANON_4_httpjpk_mf_gov_plwzor2016102610262K_17', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 325, 7), )

    
    K_17 = property(__K_17.value, __K_17.set, None, 'Uwagi')

    
    # Attribute typ uses Python identifier typ
    __typ = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'typ'), 'typ', '__httpjpk_mf_gov_plwzor2016102610262_CTD_ANON_4_typ', pyxb.binding.datatypes.anySimpleType, fixed=True, unicode_default='G', required=True)
    __typ._DeclarationLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 331, 6)
    __typ._UseLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 331, 6)
    
    typ = property(__typ.value, __typ.set, None, None)

    _ElementMap.update({
        __K_1.name() : __K_1,
        __K_2.name() : __K_2,
        __K_3.name() : __K_3,
        __K_4.name() : __K_4,
        __K_5.name() : __K_5,
        __K_6.name() : __K_6,
        __K_7.name() : __K_7,
        __K_8.name() : __K_8,
        __K_9.name() : __K_9,
        __K_10.name() : __K_10,
        __K_11.name() : __K_11,
        __K_12.name() : __K_12,
        __K_13.name() : __K_13,
        __K_14.name() : __K_14,
        __K_15.name() : __K_15,
        __K_16A.name() : __K_16A,
        __K_16B.name() : __K_16B,
        __K_17.name() : __K_17
    })
    _AttributeMap.update({
        __typ.name() : __typ
    })
_module_typeBindings.CTD_ANON_4 = CTD_ANON_4


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    """Sumy kontrolne dla tabeli PKPIRWiersz"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 338, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://jpk.mf.gov.pl/wzor/2016/10/26/10262/}LiczbaWierszy uses Python identifier LiczbaWierszy
    __LiczbaWierszy = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LiczbaWierszy'), 'LiczbaWierszy', '__httpjpk_mf_gov_plwzor2016102610262_CTD_ANON_5_httpjpk_mf_gov_plwzor2016102610262LiczbaWierszy', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 340, 7), )

    
    LiczbaWierszy = property(__LiczbaWierszy.value, __LiczbaWierszy.set, None, 'Liczba wierszy (zapis\xf3w) PKPIR, w okresie kt\xf3rego dotyczy JPK_PKPIR')

    
    # Element {http://jpk.mf.gov.pl/wzor/2016/10/26/10262/}SumaPrzychodow uses Python identifier SumaPrzychodow
    __SumaPrzychodow = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SumaPrzychodow'), 'SumaPrzychodow', '__httpjpk_mf_gov_plwzor2016102610262_CTD_ANON_5_httpjpk_mf_gov_plwzor2016102610262SumaPrzychodow', False, pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 345, 7), )

    
    SumaPrzychodow = property(__SumaPrzychodow.value, __SumaPrzychodow.set, None, '\u0141\u0105czna warto\u015b\u0107 przychod\xf3w razem (kol. 9) w PKPIR w okresie, kt\xf3rego dotyczy JPK_PKPIR')

    _ElementMap.update({
        __LiczbaWierszy.name() : __LiczbaWierszy,
        __SumaPrzychodow.name() : __SumaPrzychodow
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_5 = CTD_ANON_5


# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_6 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = TKodFormularza
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 32, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is TKodFormularza
    
    # Attribute kodSystemowy uses Python identifier kodSystemowy
    __kodSystemowy = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'kodSystemowy'), 'kodSystemowy', '__httpjpk_mf_gov_plwzor2016102610262_CTD_ANON_6_kodSystemowy', pyxb.binding.datatypes.string, fixed=True, unicode_default='JPK_PKPIR (2)', required=True)
    __kodSystemowy._DeclarationLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 35, 7)
    __kodSystemowy._UseLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 35, 7)
    
    kodSystemowy = property(__kodSystemowy.value, __kodSystemowy.set, None, None)

    
    # Attribute wersjaSchemy uses Python identifier wersjaSchemy
    __wersjaSchemy = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'wersjaSchemy'), 'wersjaSchemy', '__httpjpk_mf_gov_plwzor2016102610262_CTD_ANON_6_wersjaSchemy', pyxb.binding.datatypes.string, fixed=True, unicode_default='1-0', required=True)
    __wersjaSchemy._DeclarationLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 36, 7)
    __wersjaSchemy._UseLocation = pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 36, 7)
    
    wersjaSchemy = property(__wersjaSchemy.value, __wersjaSchemy.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __kodSystemowy.name() : __kodSystemowy,
        __wersjaSchemy.name() : __wersjaSchemy
    })
_module_typeBindings.CTD_ANON_6 = CTD_ANON_6


JPK = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'JPK'), CTD_ANON, documentation='Jednolity plik kontrolny dla podatkowej ksi\u0119gi przychod\xf3w i rozchod\xf3w', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 155, 1))
Namespace.addCategoryObject('elementBinding', JPK.name().localName(), JPK)



TNaglowek._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'KodFormularza'), CTD_ANON_6, scope=TNaglowek, location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 31, 3)))

TNaglowek._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'WariantFormularza'), STD_ANON, scope=TNaglowek, location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 41, 3)))

TNaglowek._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CelZlozenia'), TCelZlozenia, scope=TNaglowek, location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 48, 3)))

TNaglowek._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataWytworzeniaJPK'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TDataCzas, scope=TNaglowek, documentation='Data i czas wytworzenia JPK_PKPIR', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 49, 3)))

TNaglowek._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataOd'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TData, scope=TNaglowek, documentation='Data pocz\u0105tkowa okresu, kt\xf3rego dotyczy JPK_PKPIR', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 54, 3)))

TNaglowek._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataDo'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TData, scope=TNaglowek, documentation='Data ko\u0144cowa okresu, kt\xf3rego dotyczy JPK_PKPIR', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 59, 3)))

TNaglowek._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DomyslnyKodWaluty'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2013_05_23_eD_KodyCECHKRAJOW__bindings.currCode_Type, scope=TNaglowek, documentation='Trzyliterowy kod lokalnej waluty (ISO-4217), domy\u015blny dla wytworzonego JPK_PKPIR', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 64, 3)))

TNaglowek._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'KodUrzedu'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TKodUS, scope=TNaglowek, location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 69, 3)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TNaglowek._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'KodFormularza')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 31, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TNaglowek._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'WariantFormularza')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 41, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TNaglowek._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CelZlozenia')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 48, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TNaglowek._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataWytworzeniaJPK')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 49, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TNaglowek._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataOd')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 54, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TNaglowek._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataDo')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 59, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TNaglowek._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DomyslnyKodWaluty')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 64, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TNaglowek._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'KodUrzedu')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 69, 3))
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




TAdresJPK._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'KodKraju'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TKodKraju, scope=TAdresJPK, documentation='Kraj', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 103, 3)))

TAdresJPK._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Wojewodztwo'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TJednAdmin, scope=TAdresJPK, documentation='Wojew\xf3dztwo', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 108, 3)))

TAdresJPK._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Powiat'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TJednAdmin, scope=TAdresJPK, documentation='Powiat', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 113, 3)))

TAdresJPK._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Gmina'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TJednAdmin, scope=TAdresJPK, documentation='Gmina', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 118, 3)))

TAdresJPK._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Ulica'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TUlica, scope=TAdresJPK, documentation='Nazwa ulicy', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 123, 3)))

TAdresJPK._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NrDomu'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TNrBudynku, scope=TAdresJPK, documentation='Numer budynku', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 128, 3)))

TAdresJPK._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NrLokalu'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TNrLokalu, scope=TAdresJPK, documentation='Numer lokalu', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 133, 3)))

TAdresJPK._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Miejscowosc'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TMiejscowosc, scope=TAdresJPK, documentation='Nazwa miejscowo\u015bci', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 138, 3)))

TAdresJPK._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'KodPocztowy'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TKodPocztowy, scope=TAdresJPK, documentation='Kod pocztowy', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 143, 3)))

TAdresJPK._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Poczta'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TMiejscowosc, scope=TAdresJPK, documentation='Nazwa urz\u0119du pocztowego', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 148, 3)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 108, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 113, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 118, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 123, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 128, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 133, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 143, 3))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 148, 3))
    counters.add(cc_7)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TAdresJPK._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'KodKraju')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 103, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TAdresJPK._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Wojewodztwo')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 108, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TAdresJPK._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Powiat')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 113, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TAdresJPK._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Gmina')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 118, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TAdresJPK._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Ulica')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 123, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TAdresJPK._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NrDomu')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 128, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TAdresJPK._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NrLokalu')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 133, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TAdresJPK._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Miejscowosc')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 138, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(TAdresJPK._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'KodPocztowy')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 143, 3))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(TAdresJPK._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Poczta')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 148, 3))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, True) ]))
    st_9._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TAdresJPK._Automaton = _BuildAutomaton_()




CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Naglowek'), TNaglowek, scope=CTD_ANON, documentation='Nag\u0142\xf3wek JPK_PKPIR', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 161, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Podmiot1'), CTD_ANON_, scope=CTD_ANON, location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 166, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PKPIRInfo'), CTD_ANON_2, scope=CTD_ANON, documentation='Dane dotycz\u0105ce ustalenia dochodu w roku podatkowym', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 182, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PKPIRSpis'), CTD_ANON_3, scope=CTD_ANON, documentation='Spisy z natury sporz\u0105dzone w ci\u0105gu roku podatkowego', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 211, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PKPIRWiersz'), CTD_ANON_4, scope=CTD_ANON, documentation='Na podstawie za\u0142\u0105cznika do rozporz\u0105dzenia Ministra Finans\xf3w z dnia 26 sierpnia 2003 r. w sprawie prowadzenia podatkowej ksi\u0119gi przychod\xf3w i rozchod\xf3w (Dz. U. z 2014 r. poz. 1037, z p\xf3\u017an. zm.)', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 231, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PKPIRCtrl'), CTD_ANON_5, scope=CTD_ANON, documentation='Sumy kontrolne dla tabeli PKPIRWiersz', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 334, 4)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 211, 4))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Naglowek')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 161, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Podmiot1')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 166, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PKPIRInfo')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 182, 4))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PKPIRSpis')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 211, 4))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PKPIRWiersz')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 231, 4))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PKPIRCtrl')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 334, 4))
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
    transitions.append(fac.Transition(st_4, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton_2()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'IdentyfikatorPodmiotu'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TIdentyfikatorOsobyNiefizycznej, scope=CTD_ANON_, documentation='Dane identyfikuj\u0105ce podmiot', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 169, 7)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AdresPodmiotu'), TAdresJPK, scope=CTD_ANON_, documentation='Adres podmiotu', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 174, 7)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'IdentyfikatorPodmiotu')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 169, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AdresPodmiotu')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 174, 7))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_3()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_1'), TKwotowy, scope=CTD_ANON_2, documentation='Warto\u015b\u0107 spisu z natury na pocz\u0105tek roku podatkowego', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 188, 7)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_2'), TKwotowy, scope=CTD_ANON_2, documentation='Warto\u015b\u0107 spisu z natury na koniec roku podatkowego', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 193, 7)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_3'), TKwotowy, scope=CTD_ANON_2, documentation='Razem koszty uzyskania przychodu, wg obja\u015bnie\u0144 do podatkowej ksi\u0119gi przychod\xf3w i rozchod\xf3w', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 198, 7)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_4'), TKwotowy, scope=CTD_ANON_2, documentation='Doch\xf3d osi\u0105gni\u0119ty w roku podatkowym, wg obja\u015bnie\u0144 do podatkowej ksi\u0119gi przychod\xf3w i rozchod\xf3w', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 203, 7)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_1')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 188, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_2')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 193, 7))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_3')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 198, 7))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_4')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 203, 7))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
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
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_4()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_5A'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TData, scope=CTD_ANON_3, documentation='Data spisu z natury sporz\u0105dzonego w ci\u0105gu roku podatkowego', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 217, 7)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_5B'), TKwotowy, scope=CTD_ANON_3, documentation='Warto\u015b\u0107 spisu z natury sporz\u0105dzonego w ci\u0105gu roku podatkowego', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 222, 7)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 216, 6))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_5A')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 217, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_5B')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 222, 7))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton_5()




CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'K_1'), TNaturalnyJPK, scope=CTD_ANON_4, documentation='Lp.', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 237, 7)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'K_2'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TData, scope=CTD_ANON_4, documentation='Data zdarzenia gospodarczego', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 242, 7)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'K_3'), TZnakowyJPK, scope=CTD_ANON_4, documentation='Nr dowodu ksi\u0119gowego', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 247, 7)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'K_4'), TZnakowyJPK, scope=CTD_ANON_4, documentation='Kontrahent - imi\u0119 i nazwisko (firma)', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 252, 7)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'K_5'), TZnakowyJPK, scope=CTD_ANON_4, documentation='Kontrahent- adres', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 257, 7)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'K_6'), TZnakowyJPK, scope=CTD_ANON_4, documentation='Opis zdarzenia gospodarczego', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 262, 7)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'K_7'), TKwotowy, scope=CTD_ANON_4, documentation='Przych\xf3d - warto\u015b\u0107 sprzedanych towar\xf3w i us\u0142ug', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 267, 7)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'K_8'), TKwotowy, scope=CTD_ANON_4, documentation='Przych\xf3d - pozosta\u0142e przychody', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 272, 7)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'K_9'), TKwotowy, scope=CTD_ANON_4, documentation='Przych\xf3d - razem przych\xf3d (7+8)', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 277, 7)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'K_10'), TKwotowy, scope=CTD_ANON_4, documentation='Zakup towar\xf3w handlowych i materia\u0142\xf3w wg cen zakupu', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 282, 7)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'K_11'), TKwotowy, scope=CTD_ANON_4, documentation='Koszty uboczne zakupu', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 287, 7)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'K_12'), TKwotowy, scope=CTD_ANON_4, documentation='Wydatki (koszty) - wynagrodzenia w got\xf3wce i w naturze', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 292, 7)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'K_13'), TKwotowy, scope=CTD_ANON_4, documentation='Wydatki (koszty) - pozosta\u0142e wydatki', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 297, 7)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'K_14'), TKwotowy, scope=CTD_ANON_4, documentation='Wydatki (koszty) - razem wydatki (12+13)', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 302, 7)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'K_15'), TKwotowy, scope=CTD_ANON_4, documentation='Wydatki (koszty) - pole wolne', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 307, 7)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'K_16A'), TZnakowyJPK, scope=CTD_ANON_4, documentation='Koszty dzia\u0142alno\u015bci badawczo\n-rozwojowej, o kt\xf3rych mowa w art. 26e ustawy o podatku dochodowym - opis kosztu', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 313, 8)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'K_16B'), TKwotowy, scope=CTD_ANON_4, documentation='Koszty dzia\u0142alno\u015bci badawczo-rozwojowej, o kt\xf3rych mowa w art. 26e ustawy o podatku dochodowym - warto\u015b\u0107', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 319, 8)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'K_17'), TZnakowyJPK, scope=CTD_ANON_4, documentation='Uwagi', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 325, 7)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 312, 7))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 325, 7))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'K_1')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 237, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'K_2')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 242, 7))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'K_3')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 247, 7))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'K_4')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 252, 7))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'K_5')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 257, 7))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'K_6')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 262, 7))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'K_7')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 267, 7))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'K_8')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 272, 7))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'K_9')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 277, 7))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'K_10')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 282, 7))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'K_11')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 287, 7))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'K_12')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 292, 7))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'K_13')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 297, 7))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'K_14')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 302, 7))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'K_15')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 307, 7))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'K_16A')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 313, 8))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'K_16B')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 319, 8))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'K_17')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 325, 7))
    st_17 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
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
    transitions.append(fac.Transition(st_17, [
         ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
         ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_17._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_6()




CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LiczbaWierszy'), TNaturalnyJPK, scope=CTD_ANON_5, documentation='Liczba wierszy (zapis\xf3w) PKPIR, w okresie kt\xf3rego dotyczy JPK_PKPIR', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 340, 7)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SumaPrzychodow'), TKwotowy, scope=CTD_ANON_5, documentation='\u0141\u0105czna warto\u015b\u0107 przychod\xf3w razem (kol. 9) w PKPIR w okresie, kt\xf3rego dotyczy JPK_PKPIR', location=pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 345, 7)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LiczbaWierszy')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 340, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SumaPrzychodow')), pyxb.utils.utility.Location('http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd', 345, 7))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_5._Automaton = _BuildAutomaton_7()

