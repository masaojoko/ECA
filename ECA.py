# Elementary Cellular Automaton(ECA) class
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
        self._crclr_flg = crclr_mode
        self._n_neighborhood = 3
        self._offset = 1
        
        canvas_rows = self._rows
        canvas_columns = self._columns if self._crclr_flg == 1 else self._columns + self._offset
        self._canvas = np.zeros([canvas_rows, canvas_columns], dtype=np.int64)        

    def _create_wolfram_rule(self, rule_number = 184): 
        """
        Parameters
        ----------
        rule_number: int
            from 0 to 255
        
        Returns
        -------
        out: dictionary 
            dictionary of str(ex. '010') and int(ex. 0)
        """
        self._rule_number = rule_number
        
        digits = 2 ** self._n_neighborhood

        in_pattern = []
        for i in range(digits):
            in_pattern.append(np.binary_repr(digits - 1 - i, width=self._n_neighborhood))
        out_pattern = np.array([int(x) for x in np.binary_repr(self._rule_number, width = digits)])
        
        return dict(zip(in_pattern, out_pattern))

    def set_init_condition(self, init_mode, n_node=1): 
        """
        Set a initial condition 

        Parameters
        ----------
        init_mode : {0, 1}
            0: only center node is 1
            1: random n nodes are 1
        n_node : int, optional
            defines the number of 1 in the initial condition
        """
        
        init_array = np.zeros(self._columns, dtype=np.int64)
        if init_mode == 0:
            init_array[int(self._columns/2) + 1] = 1
        elif init_mode == 1:
            init_array[random.sample(range(self._columns), k=n_node)] = 1
        else:
            pass

        self.set_init_array(init_array)

    def set_init_array(self, init_array):
        self._canvas[0,0:self._columns] = init_array

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
