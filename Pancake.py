from simpleai.search import SearchProblem, astar
import random 



class PancakeProblem(SearchProblem):
    def __init__(self, initial):                                                  #Burada initial değerleri classın içine alıyoruz ve goal değerini sıralayıp küçükten büyüğe sıralıyoruz ve 
                                                                                #  pancake boyutunu len fonksiyonu ile alıyoruz
        super().__init__(initial)
        self.initial = tuple(initial)
        self.size = len(initial)
        self.goal = tuple(sorted(initial))
    

    def actions(self, state):                                                    #olabilecek aksiyonları bulan fonksiyon. Mesela 2 pancake çeviriyorsak aksiyon 2.
        possible_actions = []
        for i in range(2,self.size+1):
            possible_actions.append(i)
        return possible_actions


    def result(self, state, action):                                                          #Bu kısım aksiyonu state ile birleştirince çıkıcak sonucu gösterir.
        firstPart = state[:action]
        secondPart = state[action:self.size]                                           #Burdaki [action:self.size] kısmı state listesinin  2. elemanından size boyutundaki elemanına kadar 
                                                                                                        #olan kısmını alır.

        new_state = tuple(reversed(firstPart)) + secondPart

        return new_state


    def is_goal(self, state):                                                              # Sıralamamız hedefle aynı mı degilmi onu bulmak için.
        return state == self.goal


    def cost(self, c, state1, action, state2):  
        return c+1


    def heuristic(self, state):                                                               #Yanlış yerdeki pancakeleri ayırt edip döndürür.
        a = sum(s != g for (s, g) in zip(state, self.goal))
        return a


def main():

    n = int(input("Enter number of pancakes: "))

    arr = list()

    for i in range(n):
        arr.append(i)

    rand = input("Do you want to enter ordering?: yes/no ")

    if rand == "yes":
        ist = input("Enter top to bottom ordering between [0-{}], separated by spaces: ".format(n-1))
        arr = [int(item) for item in ist.split(" ")]
        print("Initial state: ", arr)
        print ("After Pancake Sorting: ")
        problem = PancakeProblem(arr)
        result = astar(problem)
        print(result.state)
        
    else:
        random.shuffle(arr)
        print("Initial state: ", arr)
        print ("After Pancake Sorting: ")
        problem = PancakeProblem(arr)
        result = astar(problem)
        print(result.state)


if __name__ == "__main__":
    main()
    
    






