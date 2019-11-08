# Elementary Cellular Automaton(ECA) demo
import matplotlib.pyplot as plt
import numpy as np
import random

class ECA:
    """
    ECA simulator
    """

    def __init__(self, columns = 20, rows = 10, crclr_mode = 1):
        self._columns = columns
        self._rows = rows
        self._crclr_flg = crclr_mode # 1: circular, 0: not circular
        self._n_neighborhood = 3
        self._offset = 1
        
        canvas_rows = self._rows
        canvas_columns = self._columns if self._crclr_flg == 1 else self._columns + self._offset
        self._canvas = np.zeros([canvas_rows, canvas_columns], dtype=np.int64)        

    def _create_wolfram_rule(self, rule_number = 184): 
        self._rule_number = rule_number
        
        digits = 2 ** self._n_neighborhood

        in_pattern = []
        for i in range(digits):
            in_pattern.append(np.binary_repr(digits - 1 - i, width=self._n_neighborhood))
        out_pattern = np.array([int(x) for x in np.binary_repr(self._rule_number, width = digits)])
        
        return dict(zip(in_pattern, out_pattern))

    def set_initial_condition(self, initial_array):
        self._canvas[0,0:self._columns] = initial_array

    def set_rule(self, rule_number):
        self._rule = self._create_wolfram_rule(rule_number)
                
    def simulate(self):
        for i in np.arange(0, self._rows - 1):
            for j in np.arange(0, self._columns):
                neiborhood = ''.join(map(str,np.roll(self._canvas[i,:], self._offset-j)[0:self._n_neighborhood]))
                self._canvas[i+1, j] = self._rule[neiborhood]

    def visualize(self):
        plt.imshow(self._canvas[:, 0:self._columns], cmap = 'Greys', interpolation='nearest')
        plt.title('Elementary Celluar Automaton  (Rule {})'.format(self._rule_number))
        plt.show()



# Main -- 

# set up
columns = 50
rows = 50
circular_mode = 1
rule_number = 255 # select 0-255 (ex. 30, 54, 102, 184)

init_array = np.zeros(columns, dtype=np.int64)
# case 1: only center node is 1
init_array[int(columns/2) + 1] = 1 
# case 2: random n nodes are 1 (edit the parameter k)
# init_array[random.sample(range(columns), k=20)] = 1

# initialize
eca = ECA(columns, rows, circular_mode)
eca.set_rule(rule_number)
eca.set_initial_condition(init_array)

# execute 
eca.simulate()

# visualize
eca.visualize()
