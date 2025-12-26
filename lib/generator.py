import numpy as np

def generate_binary_signal(Rb=10_000, frame_length=1000, seed=12345, samples_per_bit=20):
    """
    Generuje náhodný binární signál a jeho polar NRZ reprezentaci (-1/+1).

    Parametry:
    - Rb : bitová rychlost [b/s]
    - frame_length : počet bitů
    - seed : RNG seed
    - samples_per_bit : počet vzorků na bit

    Vrací:
    bits, nrz, t, fs, Rb
    """

    rng = np.random.default_rng(seed)
    bits = rng.integers(0, 2, frame_length)

    fs = samples_per_bit * Rb
    nrz = np.repeat(bits, samples_per_bit)

    # Převod na polar NRZ (-1/+1)
    nrz = 2 * nrz - 1

    t = np.arange(len(nrz)) / fs
    return bits, nrz, t, fs, Rb



