# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_data.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ajeffers <ajeffers@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/01 18:25:05 by ajeffers          #+#    #+#              #
#    Updated: 2026/03/01 18:25:07 by ajeffers         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant:
    def __init__(self, name:str, height:int, age:int):
        self.name = name
        self.height = height
        self.age = age

    def blueprinter(self):
        print(self.name.capitalize() + ": "+ str(self.height) +"cm, " + str(self.age) + " days old")

def main():
    print("=== Garden Plant Registry ===")
    plant1 = Plant("Rose", 25, 30)
    plant2 = Plant("Sunflower", 80, 45)
    plant3 = Plant("Cactus", 15, 120)
    plant1.blueprinter()
    plant2.blueprinter()
    plant3.blueprinter()

if __name__ == "__main__":
    main()
