# /home/maciek/odoo-dev/gal/galicea/gal_jpk/schemas/generated/http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_07_29_eD_VATZD_/bindings.py
# -*- coding: utf-8 -*-
# @generated
# PyXB bindings for NM:cac74e9c0376c4a70f91898d8c4a1f2d2b9e3182
# Generated 2018-03-08 13:30:04.759293 by PyXB version 1.2.5 using Python 2.7.12.final.0
# Namespace http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/07/29/eD/VATZD/ [xmlns:vzd]

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

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/07/29/eD/VATZD/', create_if_missing=True)
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
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/07/29/eD/VATZD/VAT-ZD(1)_v2-0E.xsd', 20, 4)
    _Documentation = None
STD_ANON._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON, enum_prefix=None)
STD_ANON._CF_enumeration.addEnumeration(unicode_value='1', tag=None)
STD_ANON._InitializeFacetMap(STD_ANON._CF_enumeration)
_module_typeBindings.STD_ANON = STD_ANON

# Atomic simple type: {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/07/29/eD/VATZD/}TKodFormularza_VAT-ZD
class TKodFormularza_VAT_ZD (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Symbol wzoru formularza"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TKodFormularza_VAT-ZD')
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/07/29/eD/VATZD/VAT-ZD(1)_v2-0E.xsd', 28, 1)
    _Documentation = 'Symbol wzoru formularza'
TKodFormularza_VAT_ZD._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TKodFormularza_VAT_ZD, enum_prefix=None)
TKodFormularza_VAT_ZD.VAT_ZD = TKodFormularza_VAT_ZD._CF_enumeration.addEnumeration(unicode_value='VAT-ZD', tag='VAT_ZD')
TKodFormularza_VAT_ZD._InitializeFacetMap(TKodFormularza_VAT_ZD._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'TKodFormularza_VAT-ZD', TKodFormularza_VAT_ZD)
_module_typeBindings.TKodFormularza_VAT_ZD = TKodFormularza_VAT_ZD

# Atomic simple type: [anonymous]
class STD_ANON_ (_ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TData):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/07/29/eD/VATZD/VAT-ZD(1)_v2-0E.xsd', 71, 11)
    _Documentation = None
STD_ANON_._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON_, value=pyxb.binding.datatypes.date('2011-01-01'))
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_minInclusive)
_module_typeBindings.STD_ANON_ = STD_ANON_

# Atomic simple type: [anonymous]
class STD_ANON_2 (_ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TData):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/07/29/eD/VATZD/VAT-ZD(1)_v2-0E.xsd', 81, 11)
    _Documentation = None
STD_ANON_2._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON_2, value=pyxb.binding.datatypes.date('2011-01-01'))
STD_ANON_2._InitializeFacetMap(STD_ANON_2._CF_minInclusive)
_module_typeBindings.STD_ANON_2 = STD_ANON_2

# Complex type {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/07/29/eD/VATZD/}TNaglowek_VAT-ZD with content type ELEMENT_ONLY
class TNaglowek_VAT_ZD (pyxb.binding.basis.complexTypeDefinition):
    """Nagłówek deklaracji"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TNaglowek_VAT-ZD')
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/07/29/eD/VATZD/VAT-ZD(1)_v2-0E.xsd', 4, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/07/29/eD/VATZD/}KodFormularza uses Python identifier KodFormularza
    __KodFormularza = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'KodFormularza'), 'KodFormularza', '__httpcrd_gov_plxmlschematydziedzinowemf20160729eDVATZD_TNaglowek_VAT_ZD_httpcrd_gov_plxmlschematydziedzinowemf20160729eDVATZDKodFormularza', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/07/29/eD/VATZD/VAT-ZD(1)_v2-0E.xsd', 9, 3), )

    
    KodFormularza = property(__KodFormularza.value, __KodFormularza.set, None, None)

    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/07/29/eD/VATZD/}WariantFormularza uses Python identifier WariantFormularza
    __WariantFormularza = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'WariantFormularza'), 'WariantFormularza', '__httpcrd_gov_plxmlschematydziedzinowemf20160729eDVATZD_TNaglowek_VAT_ZD_httpcrd_gov_plxmlschematydziedzinowemf20160729eDVATZDWariantFormularza', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/07/29/eD/VATZD/VAT-ZD(1)_v2-0E.xsd', 19, 3), )

    
    WariantFormularza = property(__WariantFormularza.value, __WariantFormularza.set, None, None)

    _ElementMap.update({
        __KodFormularza.name() : __KodFormularza,
        __WariantFormularza.name() : __WariantFormularza
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TNaglowek_VAT_ZD = TNaglowek_VAT_ZD
Namespace.addCategoryObject('typeBinding', 'TNaglowek_VAT-ZD', TNaglowek_VAT_ZD)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """ZAWIADOMIENIE O SKORYGOWANIU PODSTAWY OPODATKOWANIA ORAZ KWOTY PODATKU NALEŻNEGO"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/07/29/eD/VATZD/VAT-ZD(1)_v2-0E.xsd', 40, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/07/29/eD/VATZD/}Naglowek uses Python identifier Naglowek
    __Naglowek = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Naglowek'), 'Naglowek', '__httpcrd_gov_plxmlschematydziedzinowemf20160729eDVATZD_CTD_ANON_httpcrd_gov_plxmlschematydziedzinowemf20160729eDVATZDNaglowek', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/07/29/eD/VATZD/VAT-ZD(1)_v2-0E.xsd', 42, 4), )

    
    Naglowek = property(__Naglowek.value, __Naglowek.set, None, None)

    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/07/29/eD/VATZD/}PozycjeSzczegolowe uses Python identifier PozycjeSzczegolowe
    __PozycjeSzczegolowe = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PozycjeSzczegolowe'), 'PozycjeSzczegolowe', '__httpcrd_gov_plxmlschematydziedzinowemf20160729eDVATZD_CTD_ANON_httpcrd_gov_plxmlschematydziedzinowemf20160729eDVATZDPozycjeSzczegolowe', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/07/29/eD/VATZD/VAT-ZD(1)_v2-0E.xsd', 43, 4), )

    
    PozycjeSzczegolowe = property(__PozycjeSzczegolowe.value, __PozycjeSzczegolowe.set, None, 'Dane identyfikacyjne d\u0142u\u017cnika oraz informacje dotycz\u0105ce kwot korekty podstawy opodatkowania oraz podatku nale\u017cnego')

    _ElementMap.update({
        __Naglowek.name() : __Naglowek,
        __PozycjeSzczegolowe.name() : __PozycjeSzczegolowe
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON = CTD_ANON


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Dane identyfikacyjne dłużnika oraz informacje dotyczące kwot korekty podstawy opodatkowania oraz podatku należnego"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/07/29/eD/VATZD/VAT-ZD(1)_v2-0E.xsd', 47, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/07/29/eD/VATZD/}P_B uses Python identifier P_B
    __P_B = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_B'), 'P_B', '__httpcrd_gov_plxmlschematydziedzinowemf20160729eDVATZD_CTD_ANON__httpcrd_gov_plxmlschematydziedzinowemf20160729eDVATZDP_B', True, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/07/29/eD/VATZD/VAT-ZD(1)_v2-0E.xsd', 49, 7), )

    
    P_B = property(__P_B.value, __P_B.set, None, None)

    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/07/29/eD/VATZD/}P_10 uses Python identifier P_10
    __P_10 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_10'), 'P_10', '__httpcrd_gov_plxmlschematydziedzinowemf20160729eDVATZD_CTD_ANON__httpcrd_gov_plxmlschematydziedzinowemf20160729eDVATZDP_10', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/07/29/eD/VATZD/VAT-ZD(1)_v2-0E.xsd', 101, 7), )

    
    P_10 = property(__P_10.value, __P_10.set, None, 'Og\xf3\u0142em kwota korekty podstawy opodatkowania')

    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/07/29/eD/VATZD/}P_11 uses Python identifier P_11
    __P_11 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_11'), 'P_11', '__httpcrd_gov_plxmlschematydziedzinowemf20160729eDVATZD_CTD_ANON__httpcrd_gov_plxmlschematydziedzinowemf20160729eDVATZDP_11', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/07/29/eD/VATZD/VAT-ZD(1)_v2-0E.xsd', 106, 7), )

    
    P_11 = property(__P_11.value, __P_11.set, None, 'Og\xf3\u0142em kwota korekty podatku nale\u017cnego')

    _ElementMap.update({
        __P_B.name() : __P_B,
        __P_10.name() : __P_10,
        __P_11.name() : __P_11
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_ = CTD_ANON_


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/07/29/eD/VATZD/VAT-ZD(1)_v2-0E.xsd', 50, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/07/29/eD/VATZD/}P_BB uses Python identifier P_BB
    __P_BB = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_BB'), 'P_BB', '__httpcrd_gov_plxmlschematydziedzinowemf20160729eDVATZD_CTD_ANON_2_httpcrd_gov_plxmlschematydziedzinowemf20160729eDVATZDP_BB', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/07/29/eD/VATZD/VAT-ZD(1)_v2-0E.xsd', 52, 10), )

    
    P_BB = property(__P_BB.value, __P_BB.set, None, 'Nazwa podatnika (d\u0142u\u017cnika)')

    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/07/29/eD/VATZD/}P_BC uses Python identifier P_BC
    __P_BC = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_BC'), 'P_BC', '__httpcrd_gov_plxmlschematydziedzinowemf20160729eDVATZD_CTD_ANON_2_httpcrd_gov_plxmlschematydziedzinowemf20160729eDVATZDP_BC', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/07/29/eD/VATZD/VAT-ZD(1)_v2-0E.xsd', 57, 10), )

    
    P_BC = property(__P_BC.value, __P_BC.set, None, 'Identyfikator podatkowy NIP podatnika (d\u0142u\u017cnika)')

    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/07/29/eD/VATZD/}P_BD1 uses Python identifier P_BD1
    __P_BD1 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_BD1'), 'P_BD1', '__httpcrd_gov_plxmlschematydziedzinowemf20160729eDVATZD_CTD_ANON_2_httpcrd_gov_plxmlschematydziedzinowemf20160729eDVATZDP_BD1', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/07/29/eD/VATZD/VAT-ZD(1)_v2-0E.xsd', 62, 10), )

    
    P_BD1 = property(__P_BD1.value, __P_BD1.set, None, 'Nr faktury')

    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/07/29/eD/VATZD/}P_BD2 uses Python identifier P_BD2
    __P_BD2 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_BD2'), 'P_BD2', '__httpcrd_gov_plxmlschematydziedzinowemf20160729eDVATZD_CTD_ANON_2_httpcrd_gov_plxmlschematydziedzinowemf20160729eDVATZDP_BD2', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/07/29/eD/VATZD/VAT-ZD(1)_v2-0E.xsd', 67, 10), )

    
    P_BD2 = property(__P_BD2.value, __P_BD2.set, None, 'Data wystawienia faktury')

    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/07/29/eD/VATZD/}P_BE uses Python identifier P_BE
    __P_BE = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_BE'), 'P_BE', '__httpcrd_gov_plxmlschematydziedzinowemf20160729eDVATZD_CTD_ANON_2_httpcrd_gov_plxmlschematydziedzinowemf20160729eDVATZDP_BE', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/07/29/eD/VATZD/VAT-ZD(1)_v2-0E.xsd', 77, 10), )

    
    P_BE = property(__P_BE.value, __P_BE.set, None, 'Data up\u0142ywu terminu p\u0142atno\u015bci okre\u015blonego w fakturze lub umowie')

    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/07/29/eD/VATZD/}P_BF uses Python identifier P_BF
    __P_BF = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_BF'), 'P_BF', '__httpcrd_gov_plxmlschematydziedzinowemf20160729eDVATZD_CTD_ANON_2_httpcrd_gov_plxmlschematydziedzinowemf20160729eDVATZDP_BF', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/07/29/eD/VATZD/VAT-ZD(1)_v2-0E.xsd', 87, 10), )

    
    P_BF = property(__P_BF.value, __P_BF.set, None, 'Kwota korekty podstawy opodatkowania')

    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/07/29/eD/VATZD/}P_BG uses Python identifier P_BG
    __P_BG = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_BG'), 'P_BG', '__httpcrd_gov_plxmlschematydziedzinowemf20160729eDVATZD_CTD_ANON_2_httpcrd_gov_plxmlschematydziedzinowemf20160729eDVATZDP_BG', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/07/29/eD/VATZD/VAT-ZD(1)_v2-0E.xsd', 92, 10), )

    
    P_BG = property(__P_BG.value, __P_BG.set, None, 'Kwota korekty podatku nale\u017cnego')

    
    # Attribute typ uses Python identifier typ
    __typ = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'typ'), 'typ', '__httpcrd_gov_plxmlschematydziedzinowemf20160729eDVATZD_CTD_ANON_2_typ', pyxb.binding.datatypes.anySimpleType, fixed=True, unicode_default='G', required=True)
    __typ._DeclarationLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/07/29/eD/VATZD/VAT-ZD(1)_v2-0E.xsd', 98, 9)
    __typ._UseLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/07/29/eD/VATZD/VAT-ZD(1)_v2-0E.xsd', 98, 9)
    
    typ = property(__typ.value, __typ.set, None, None)

    _ElementMap.update({
        __P_BB.name() : __P_BB,
        __P_BC.name() : __P_BC,
        __P_BD1.name() : __P_BD1,
        __P_BD2.name() : __P_BD2,
        __P_BE.name() : __P_BE,
        __P_BF.name() : __P_BF,
        __P_BG.name() : __P_BG
    })
    _AttributeMap.update({
        __typ.name() : __typ
    })
_module_typeBindings.CTD_ANON_2 = CTD_ANON_2


# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = TKodFormularza_VAT_ZD
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/07/29/eD/VATZD/VAT-ZD(1)_v2-0E.xsd', 10, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is TKodFormularza_VAT_ZD
    
    # Attribute kodSystemowy uses Python identifier kodSystemowy
    __kodSystemowy = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'kodSystemowy'), 'kodSystemowy', '__httpcrd_gov_plxmlschematydziedzinowemf20160729eDVATZD_CTD_ANON_3_kodSystemowy', pyxb.binding.datatypes.string, fixed=True, unicode_default='VAT-ZD (1)', required=True)
    __kodSystemowy._DeclarationLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/07/29/eD/VATZD/VAT-ZD(1)_v2-0E.xsd', 13, 7)
    __kodSystemowy._UseLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/07/29/eD/VATZD/VAT-ZD(1)_v2-0E.xsd', 13, 7)
    
    kodSystemowy = property(__kodSystemowy.value, __kodSystemowy.set, None, None)

    
    # Attribute wersjaSchemy uses Python identifier wersjaSchemy
    __wersjaSchemy = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'wersjaSchemy'), 'wersjaSchemy', '__httpcrd_gov_plxmlschematydziedzinowemf20160729eDVATZD_CTD_ANON_3_wersjaSchemy', pyxb.binding.datatypes.string, fixed=True, unicode_default='2-0E', required=True)
    __wersjaSchemy._DeclarationLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/07/29/eD/VATZD/VAT-ZD(1)_v2-0E.xsd', 14, 7)
    __wersjaSchemy._UseLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/07/29/eD/VATZD/VAT-ZD(1)_v2-0E.xsd', 14, 7)
    
    wersjaSchemy = property(__wersjaSchemy.value, __wersjaSchemy.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __kodSystemowy.name() : __kodSystemowy,
        __wersjaSchemy.name() : __wersjaSchemy
    })
_module_typeBindings.CTD_ANON_3 = CTD_ANON_3


Wniosek_VAT_ZD = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Wniosek_VAT-ZD'), CTD_ANON, documentation='ZAWIADOMIENIE O SKORYGOWANIU PODSTAWY OPODATKOWANIA ORAZ KWOTY PODATKU NALE\u017bNEGO', location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/07/29/eD/VATZD/VAT-ZD(1)_v2-0E.xsd', 36, 1))
Namespace.addCategoryObject('elementBinding', Wniosek_VAT_ZD.name().localName(), Wniosek_VAT_ZD)



TNaglowek_VAT_ZD._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'KodFormularza'), CTD_ANON_3, scope=TNaglowek_VAT_ZD, location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/07/29/eD/VATZD/VAT-ZD(1)_v2-0E.xsd', 9, 3)))

TNaglowek_VAT_ZD._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'WariantFormularza'), STD_ANON, scope=TNaglowek_VAT_ZD, location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/07/29/eD/VATZD/VAT-ZD(1)_v2-0E.xsd', 19, 3)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TNaglowek_VAT_ZD._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'KodFormularza')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/07/29/eD/VATZD/VAT-ZD(1)_v2-0E.xsd', 9, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TNaglowek_VAT_ZD._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'WariantFormularza')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/07/29/eD/VATZD/VAT-ZD(1)_v2-0E.xsd', 19, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TNaglowek_VAT_ZD._Automaton = _BuildAutomaton()




CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Naglowek'), TNaglowek_VAT_ZD, scope=CTD_ANON, location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/07/29/eD/VATZD/VAT-ZD(1)_v2-0E.xsd', 42, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PozycjeSzczegolowe'), CTD_ANON_, scope=CTD_ANON, documentation='Dane identyfikacyjne d\u0142u\u017cnika oraz informacje dotycz\u0105ce kwot korekty podstawy opodatkowania oraz podatku nale\u017cnego', location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/07/29/eD/VATZD/VAT-ZD(1)_v2-0E.xsd', 43, 4)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Naglowek')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/07/29/eD/VATZD/VAT-ZD(1)_v2-0E.xsd', 42, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PozycjeSzczegolowe')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/07/29/eD/VATZD/VAT-ZD(1)_v2-0E.xsd', 43, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton_()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_B'), CTD_ANON_2, scope=CTD_ANON_, location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/07/29/eD/VATZD/VAT-ZD(1)_v2-0E.xsd', 49, 7)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_10'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TKwotaCNieujemna, scope=CTD_ANON_, documentation='Og\xf3\u0142em kwota korekty podstawy opodatkowania', location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/07/29/eD/VATZD/VAT-ZD(1)_v2-0E.xsd', 101, 7)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_11'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TKwotaCNieujemna, scope=CTD_ANON_, documentation='Og\xf3\u0142em kwota korekty podatku nale\u017cnego', location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/07/29/eD/VATZD/VAT-ZD(1)_v2-0E.xsd', 106, 7)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/07/29/eD/VATZD/VAT-ZD(1)_v2-0E.xsd', 49, 7))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_B')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/07/29/eD/VATZD/VAT-ZD(1)_v2-0E.xsd', 49, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_10')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/07/29/eD/VATZD/VAT-ZD(1)_v2-0E.xsd', 101, 7))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_11')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/07/29/eD/VATZD/VAT-ZD(1)_v2-0E.xsd', 106, 7))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_2()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_BB'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TZnakowy, scope=CTD_ANON_2, documentation='Nazwa podatnika (d\u0142u\u017cnika)', location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/07/29/eD/VATZD/VAT-ZD(1)_v2-0E.xsd', 52, 10)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_BC'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TNrNIP, scope=CTD_ANON_2, documentation='Identyfikator podatkowy NIP podatnika (d\u0142u\u017cnika)', location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/07/29/eD/VATZD/VAT-ZD(1)_v2-0E.xsd', 57, 10)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_BD1'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TZnakowy, scope=CTD_ANON_2, documentation='Nr faktury', location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/07/29/eD/VATZD/VAT-ZD(1)_v2-0E.xsd', 62, 10)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_BD2'), STD_ANON_, scope=CTD_ANON_2, documentation='Data wystawienia faktury', location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/07/29/eD/VATZD/VAT-ZD(1)_v2-0E.xsd', 67, 10)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_BE'), STD_ANON_2, scope=CTD_ANON_2, documentation='Data up\u0142ywu terminu p\u0142atno\u015bci okre\u015blonego w fakturze lub umowie', location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/07/29/eD/VATZD/VAT-ZD(1)_v2-0E.xsd', 77, 10)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_BF'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TKwota2Nieujemna, scope=CTD_ANON_2, documentation='Kwota korekty podstawy opodatkowania', location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/07/29/eD/VATZD/VAT-ZD(1)_v2-0E.xsd', 87, 10)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_BG'), _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TKwota2Nieujemna, scope=CTD_ANON_2, documentation='Kwota korekty podatku nale\u017cnego', location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/07/29/eD/VATZD/VAT-ZD(1)_v2-0E.xsd', 92, 10)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_BB')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/07/29/eD/VATZD/VAT-ZD(1)_v2-0E.xsd', 52, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_BC')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/07/29/eD/VATZD/VAT-ZD(1)_v2-0E.xsd', 57, 10))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_BD1')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/07/29/eD/VATZD/VAT-ZD(1)_v2-0E.xsd', 62, 10))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_BD2')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/07/29/eD/VATZD/VAT-ZD(1)_v2-0E.xsd', 67, 10))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_BE')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/07/29/eD/VATZD/VAT-ZD(1)_v2-0E.xsd', 77, 10))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_BF')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/07/29/eD/VATZD/VAT-ZD(1)_v2-0E.xsd', 87, 10))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_BG')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/07/29/eD/VATZD/VAT-ZD(1)_v2-0E.xsd', 92, 10))
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
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_3()

