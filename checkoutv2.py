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
                 
    if type(cost) == int:
        
        print('Would you like to add an insurance to your order')
        x = input()
        if x == 'yes':
            cost = cost + 5     
        else:
             cost = cost
                
        print('Would you like to sign up for the priority mail list')
        y = input()
        
        if y == 'yes':
            return 'The total price for your order is: ' + str(cost + 10)
        else:
            return 'The total price for your order is: ' + str(cost)