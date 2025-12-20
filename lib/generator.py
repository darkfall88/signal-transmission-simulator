import matplotlib.pyplot as plt
import numpy as np
from IPython.display import clear_output


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


def plot_binary_signal(bits, nrz, t, Rb):
    """
    Zobrazí binární NRZ signál.
    """

    plt.figure(figsize=(12, 4))
    plt.step(t, nrz, where="post")
    plt.ylim(-1.2, 1.2)
    plt.xlabel("Čas [s]")
    plt.ylabel("Amplituda")
    plt.title(f"Telegrafní NRZ signál (Rb = {Rb/1e3:.1f} kb/s)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# ===== Funkce pro interaktivní volání =====
def interactive_plot(Rb, frame_length, seed):
    # generování signálu
    bits, nrz, t, fs, Rb_used = generate_binary_signal(
        Rb=int(Rb),
        frame_length=int(frame_length),
        seed=int(seed)
    )

    clear_output(wait=True)  # smaže předchozí grafy při změně
    plot_binary_signal(bits, nrz, t, Rb_used)

    # zobrazení parametrů
    print(f"Seed: {seed}")
    print(f"Vzorkovací frekvence fs = {fs / 1e3:.1f} kHz")
    print(f"Počet bitů = {len(bits)}")


