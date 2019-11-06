# -*- coding: utf-8 -*-
import os

schemas = {
    'kr': 'http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_KR%281%29_v1-0.xsd',
    'wb': 'http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_WB%281%29_v1-0.xsd',
    'mag': 'http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_MAG%281%29_v1-0.xsd',
    'vat': 'http://www.mf.gov.pl/documents/764034/6145258/Schemat_JPK_VAT%283%29_v1-1.xsd',
    'fa': 'http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_FA%281%29_v1-0.xsd',
    'pkpir': 'http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_PKPIR%282%29_v1-0.xsd',
    'ewp': 'http://www.mf.gov.pl/documents/764034/5134536/Schemat_JPK_EWP_v1-0.xsd',
    'vat7': 'http://crd.gov.pl/wzor/2016/08/05/3412/schemat.xsd',
}
target_directory = os.path.dirname(os.path.realpath(__file__))
