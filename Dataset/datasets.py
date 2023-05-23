import torch.nn as nn
import numpy as np
from modulation_symbols import QPSK_symbols, QAM_symbols
import itertools

class OFDMDatasetBasic(nn.Module):
    def __init__(self, n_of_data: int, nfft: int =8, n_zeros: int =0, modulation_type:str ='qpsk', normalize: bool = False):
        super().__init__()

        self.n_of_data = n_of_data
        self.nfft = nfft
        self.n_zeros = n_zeros
        self.symbols = {'qpsk': QPSK_symbols, 'QAM': QAM_symbols}

        self.indexes = np.arange(len(self.symbols))


class OFDMDatasetUnique(OFDMDatasetBasic):
    def __init__(self, n_of_data: int, nfft: int =8, n_zeros: int =0, modulation_type: str = 'qpsk', normalize: bool = False):
        super().__init__(n_of_data, nfft, n_zeros, modulation_type, normalize)

        self.complex_numbers = np.asarray(list(itertools.product(symbols, repeat=nfft)))

class OFDM_dataset(OFDMDatasetBasic):
    def __init__(self, n_of_data: int, nfft: int =8, n_zeros: int =0, modulation_type: str = 'qpsk', normalize: bool = False):
        super().__init__(n_of_data, nfft, n_zeros, modulation_type, normalize)




        self.all_modulations = np.asarray([np.fft.ifft(np.asarray(x)) for x in self.complex_numbers])
        self.all_abs = np.abs(self.all_modulations)

        index =  np.unravel_index(np.argmax(self.all_abs), self.all_abs.shape)


        print(self.all_modulations)
        self.x = np.unique(self.all_abs)
        print(np.max(self.x))
        print(self.x)