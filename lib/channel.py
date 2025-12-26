import numpy as np

def ideal_lowpass(signal, fs, B):
    """
    Ideální nízkopásmový filtr.

    signal : vstupní signál
    fs     : vzorkovací frekvence
    B      : šířka pásma [Hz]
    """

    N = len(signal)
    spectrum = np.fft.fft(signal)
    freqs = np.fft.fftfreq(N, d=1/fs)

    mask = np.abs(freqs) <= B
    spectrum_filtered = spectrum * mask

    filtered_signal = np.fft.ifft(spectrum_filtered).real
    return filtered_signal

def add_awgn(signal, snr_db, rng=None):
    if rng is None:
        rng = np.random.default_rng()

    signal_power = np.mean(signal**2)
    snr_linear = 10**(snr_db / 10)

    noise_power = signal_power / snr_linear
    noise_std = np.sqrt(noise_power)

    noise = rng.normal(0, noise_std, size=signal.shape)

    return signal + noise   # ⬅⬅⬅ KRITICKÉ


def apply_channel(
    signal,
    fs,
    B=10_000,
    snr_db=10,
    awgn_on=True,
    rng=None
):
    """
    Aplikuje kanál: LPF + AWGN
    """

    # omezení pásma
    out = ideal_lowpass(signal, fs, B)

    # přidání šumu
    if awgn_on:
        out = add_awgn(out, snr_db, rng)

    return out
