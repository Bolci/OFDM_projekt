import numpy as np
from dataclasses import dataclass

@dataclass
class QPSK_symbols:
    QPSK_symbols = np.asarray([1 + 1j, 1 - 1j, -1 + 1j, -1 - 1j])
    QPSK_max = np.sqrt(2)

@dataclass
class QAM_symbols:
    qam_symbols = np.asarray([3 + 3j,
                              3 + 1j,
                              3 - 3j,
                              3 - 1j,
                              1 + 3j,
                              1 + 1j,
                              1 - 3j,
                              1 - 1j,
                              -3 + 3j,
                              -3 + 1j,
                              -3 - 3j,
                              -3 - 1j,
                              -1 + 3j,
                              -1 + 1j,
                              -1 - 3j,
                              -1 - 1j])
    qam_aplitude = np.sqrt(18)
