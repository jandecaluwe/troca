# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import re
from distutils.version import StrictVersion
import urubu

urubu_version_required = "0.3"

urubu_version_error = """\
Urubu version should be >= {}
Upgrade with: "pip install --upgrade urubu"
""".format(urubu_version_required)

if StrictVersion(urubu.__version__) < StrictVersion(urubu_version_required):
    raise AssertionError(urubu_version_error) 

undefined_key = "'{}' not defined in '{}'"

def check_keys(item, keys):
    for key in keys:    
        if key not in item:
            raise KeyError(undefined_key.format(key, item['id']))

mailinfo = re.compile(r'<.*>') 

def validate_default(item):
    pass 

champagne = '#F7E7CE'
white = '#E4D96F'
sweet = '#FFFF00'
ox = '#FFD700'
red = '#9F1D35'

champagne_re = re.compile(r'(petil|mous|sprankelend)', re.I)
white_re = re.compile(r'(wit|blanc|bianco)', re.I)
ox_re = re.compile(r'(ox)', re.I)
sweet_re = re.compile(r'(zoet|moel|tendre|demi.sec)', re.I)
red_re = re.compile(r'(rood|rouge|rosso)', re.I)

prijs_re = re.compile(r'(\d+\.\d+|\d+)', re.I)
        
def validate_wijnhuis(item):
    check_keys(item, ['wijnen'])
    for wijn in item['wijnen']:
        if not 'type' in wijn:
            continue
        color = 'inherit' 
        tipe = wijn['type']
        if champagne_re.search(tipe):
            color = champagne
        elif ox_re.search(tipe):
            color = ox
        elif sweet_re.search(tipe):
            color = sweet
        elif white_re.search(tipe):
            color = white
        elif red_re.search(tipe):
            color = red
        wijn['color'] = color 
    for wijn in item['wijnen']:
        if not 'prijs' in wijn:
            continue
        prijs = wijn['prijs']
        m = prijs_re.search(prijs)  
        if m:
            prijs = float(m.group(0))
            prijs = round((prijs * 1.21), 2)
            prijs = "{:.2f}".format(prijs)
            wijn['prijs'] = prijs


validators= {}

validators['wijnhuis'] = validate_wijnhuis 

