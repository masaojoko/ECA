# ECA demo
from ECA import ECA
import numpy as np

# set up
columns = 50
rows = 50
circular_mode = 0  # 1: circular, 0: not circular
rule_number = 184 # select 0-255 (ex. 30, 54, 102, 184)
init_mode = 1 # 0: only center node is 1, 1: random n nodes are 1
n_node = 20 # used only when init_mode = 1

# initialize
eca = ECA(columns, rows, circular_mode)
eca.set_rule(rule_number)
eca.set_init_condition(init_mode, n_node)

# execute 
eca.simulate()

# visualize
eca.visualize()
