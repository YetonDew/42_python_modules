# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_growth.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ajeffers <ajeffers@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/01 18:24:53 by ajeffers          #+#    #+#              #
#    Updated: 2026/03/01 18:24:55 by ajeffers         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from ex1.ft_garden_data import Plant as BasePlant

class Plant(BasePlant):
	def grow(self, days: int):
		self.height += days


	def age_up(self, days: int):
		self.age += days

	def get_info(self):
		self.blueprinter()

def main():
    days = int(input("Enter the amount of days you want to simulate: "))
    p = Plant("Rose", 25, 30)
    print("=== Day 1 ===")
    p.get_info()
    print("=== Day "+ str(days) +"===")
    p.grow(days)
    p.age_up(days)
    p.get_info()
    print("Growth this week: +"+str(days) +"cm")


if __name__ == "__main__":
    main()
