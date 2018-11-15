# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 19:17:38 2018

@author: edup_
"""

from checkoutv1 import checkout

def test_checkout_returns_cost():
    assert checkout(['Guitar']) == 1000
    assert checkout(['Guitar', 'Pick box']) == 1005
    assert checkout(['Guitar', 'Pick box', 'Guitar strings']) == 1015
    assert checkout(['Guitar strings']) == 10

def test_checkout_returns_error():
    assert checkout(['guitar']) == 'Error, product does not exist'
    assert checkout(['Bass guitar']) == 'Error, product does not exist'
    assert checkout(['Autotune']) == 'Error, product does not exist'

def test_checkout_empty_cart():
    assert checkout([]) == None
   
    