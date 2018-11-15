# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 18:13:08 2018

@author: edup_
"""

products = {'Guitar':1000, 'Pick box':5, 'Guitar strings':10}

def checkout(shopping_cart):
    cost = 0
    
    for product in shopping_cart:
        
           if product in products:
               cost = cost + products[product]
           elif product not in products:
               return 'Error, product does not exist'
           
    if shopping_cart == []:
        cost = None
        print(" Your shopping cart is empty, cannot proceed with checkout")
                 

    return cost