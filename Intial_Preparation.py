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

Circuit= cirq.Circuit()
Qubits=cirq.NamedQubit.range(16, prefix='q')
Circuit.append([cirq.H.on_each(Qubits)])
print(Circuit)