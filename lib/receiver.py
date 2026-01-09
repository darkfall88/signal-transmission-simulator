import numpy as np


def sample_and_detect_nrz(signal, fs, Rb, threshold=0.0):
    """
    Základní přijímač pro NRZ:
    - vzorkování ve středu bitu
    - prahová detekce

    Parametry:
    signal : vstupní signál po kanálu
    fs     : vzorkovací frekvence signálu
    Rb     : bitová rychlost
    threshold : rozhodovací práh

    Vrací:
    bits_rx : detekované bity (0/1)
    samples : použité vzorky
    """

    samples_per_bit = int(fs / Rb)
    if samples_per_bit < 1:
        raise ValueError("fs musí být >= Rb")

    # vzorkovací okamžiky – střed bitu
    sample_indices = np.arange(
        samples_per_bit // 2,
        len(signal),
        samples_per_bit
    )

    samples = signal[sample_indices]

    # prahová detekce
    bits_rx = (samples > threshold).astype(int)

    return bits_rx, samples
