#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 17:03:46 2018

@author: Javier
"""

#%%

class Product:
    
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Service:
    
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Tier:
    
    def __init__(self, tier, discount):
        self.tier = tier
        self.discount = discount
        
class ShoppingCart:
    
    list_products = []
    list_services = []
    
    def __init__(self):
        pass 
        
    def add_new_product(self, product):
        self.list_products.append(product)
        
    def add_new_service(self, service):
        if service not in self.list_services:
            self.list_services.append(service)
        else: 
            pass
        
    def checkout(self, tier):
        
        total_price = 0
        
        for service in self.list_services:
            if tier == gold:
                service.price *= tier.discount
                total_price += service.price         
            else:
                total_price += service.price
                
        for product in self.list_products:
        
            if tier == silver:
                for product in self.list_products:
                    product.price *= tier.discount
                    total_price += product.price
            if tier == gold:
                product.price *= tier.discount
                total_price += product.price
            if tier == normal:
                total_price += product.price
                    
        return total_price
        
cart1 = ShoppingCart()

#products:
guitar = Product("guitar", 1000)
pickbox = Product("pickbox", 5)
strings = Product("strings", 10)

#services: 
insurance = Service("insurance", 5)
priority_mail = Service("priority mail", 10)

#tiers:
normal = Tier("normal", 1)
silver = Tier("silver", 0.98)
gold = Tier("gold", 0.95)


cart1.add_new_product(guitar)
cart1.add_new_service(insurance)

#for i in cart1.list_products:
#    print(i.name)

#cart1.checkout(silver)
#cart1.checkout(gold)
#cart1.checkout(normal)