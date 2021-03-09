# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 10:19:46 2021

@author: Julien
"""
from classes import Client
###############################################################################
######################   Enregistrement des constantes   ######################
###############################################################################
    
n_trucks = 4
truck_capacity = 25

nb_pop = 500
nb_generations = 2000

#Garder les 20 meilleurs individus
elitism = True
best_pop = 20

mutation_rate =0.7

top_gen = []

time_penalty = 100
quantity_penalty = 100


###############################################################################
########################   Enregistrement des villes   ########################
###############################################################################


time_matrix = [
        [0, 6, 9, 8, 7, 3, 6, 2, 3, 2, 6, 6, 4, 4, 5, 9, 7],
        [6, 0, 8, 3, 2, 6, 8, 4, 8, 8, 13, 7, 5, 8, 12, 10, 14],
        [9, 8, 0, 11, 10, 6, 3, 9, 5, 8, 4, 15, 14, 13, 9, 18, 9],
        [8, 3, 11, 0, 1, 7, 10, 6, 10, 10, 14, 6, 7, 9, 14, 6, 16],
        [7, 2, 10, 1, 0, 6, 9, 4, 8, 9, 13, 4, 6, 8, 12, 8, 14],
        [3, 6, 6, 7, 6, 0, 2, 3, 2, 2, 7, 9, 7, 7, 6, 12, 8],
        [6, 8, 3, 10, 9, 2, 0, 6, 2, 5, 4, 12, 10, 10, 6, 15, 5],
        [2, 4, 9, 6, 4, 3, 6, 0, 4, 4, 8, 5, 4, 3, 7, 8, 10],
        [3, 8, 5, 10, 8, 2, 2, 4, 0, 3, 4, 9, 8, 7, 3, 13, 6],
        [2, 8, 8, 10, 9, 2, 5, 4, 3, 0, 4, 6, 5, 4, 3, 9, 5],
        [6, 13, 4, 14, 13, 7, 4, 8, 4, 4, 0, 10, 9, 8, 4, 13, 4],
        [6, 7, 15, 6, 4, 9, 12, 5, 9, 6, 10, 0, 1, 3, 7, 3, 10],
        [4, 5, 14, 7, 6, 7, 10, 4, 8, 5, 9, 1, 0, 2, 6, 4, 8],
        [4, 8, 13, 9, 8, 7, 10, 3, 7, 4, 8, 3, 2, 0, 4, 5, 6],
        [5, 12, 9, 14, 12, 6, 6, 7, 3, 3, 4, 7, 6, 4, 0, 9, 2],
        [9, 10, 18, 6, 8, 12, 15, 8, 13, 9, 13, 3, 4, 5, 9, 0, 9],
        [7, 14, 9, 16, 14, 8, 5, 10, 6, 5, 4, 10, 8, 6, 2, 9, 0],
    ]

client_0 = Client(0,0,0,0,0,40)
client_1 = Client(1,-2,4,1,7,12)
client_2 = Client(2,4,4,1,10,15)
client_3 = Client(3,-4,3,3,16,18)
client_4 = Client(4,-3,3,4,10,13)
client_5 = Client(5,1,2,2,0,5)
client_6 = Client(6,3,2,4,5,10)
client_7 = Client(7,-1,1,8 ,0,4)
client_8 = Client(8,2,1,8,5,10)
client_9 = Client(9,1,-1,1,0,3)
client_10 = Client(10,4,-1,2,10,16)
client_11 = Client(11,-3,-2,1,10,15)
client_12 = Client(12,-2,-2,2,0,5)
client_13 = Client(13,-1,-3,14,5,10)
client_14 = Client(14,2,-3,4,7,8)
client_15 = Client(15,-4,-4,8,10,15)
client_16 = Client(16,3,-4,8,11,15)

clients=[ # [quantité à  livrer, de, à] 
        [0,0,1000],
        [1,7,12],
        [1,10,15],
        [3,16,18],
        [4,10,13],
        [2,0,5],
        [4,5,10],
        [8,0,4],
        [8,5,10],
        [1,0,3],
        [2,10,16],
        [1,10,15],
        [2,0,5],
        [14,5,10],
        [4,7,8],
        [8,10,15],
        [8,11,15]
        ]