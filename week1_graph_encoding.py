import numpy as np
import math
import scipy
try:
    import cirq
except ImportError:
    print("installing cirq...")
    
    import cirq
    print("installed cirq.")

import random
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings("ignore")

print("Libraries Imported Successfully!")


## MODIFY FOR CIRQ
def plot_results(result, satisfies_disagree_list):

  # Plotting results
  counts = result.circuit_results[0]
  plot = plot_histogram(counts, figsize=(int(6*len(counts.keys())**(1/2)), 8), sort='value_desc')
  ax = plot.gca()
  ax.tick_params(axis='x', which='major', labelsize=10)
  ax.set_xlabel("State", fontsize = 'x-large')
  ax.set_ylabel("Count", fontsize = 'x-large')

  # Marking correct (orange) vs. incorrect (blue) states

  correct_count = 0
  states = ax.xaxis.get_ticklabels()
  for i in range(len(states)):
    if satisfies_disagree_list(states[i].get_text()):
      ax.containers[i][0].set(color = 'orange')
      correct_count += 1
    else:
      ax.containers[i][0].set(color = 'blue')

  leg = plot.legend(['Incorrect (' + str(len(states) - correct_count) + ' counted)',
                     'Correct (' + str(correct_count) + ' counted)'],
                    fontsize = 'x-large',
                    loc = 'upper left')
  leg.legendHandles[0].set_color('blue')
  leg.legendHandles[1].set_color('orange')

  display(plot)


print("Libraries Imported Successfully!")