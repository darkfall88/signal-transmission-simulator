import numpy as np


def ber(bits_tx, bits_rx):
    """
    Výpočet Bit Error Rate (BER).

    bits_tx : vyslané bity (0/1)
    bits_rx : přijaté bity (0/1)

    Vrací:
    ber_value : float
    """

    N = min(len(bits_tx), len(bits_rx))
    if N == 0:
        return 0.0

    return np.mean(bits_tx[:N] != bits_rx[:N])

def shannon_capacity(B, snr_db):
    """
    Shannon–Hartleyho kapacita kanálu.

    B      : šířka pásma [Hz]
    snr_db : SNR [dB]

    Vrací:
    C : kapacita [bit/s]
    """

    snr_linear = 10 ** (snr_db / 10)
    return B * np.log2(1 + snr_linear)
