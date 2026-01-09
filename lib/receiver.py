# receiver/receiver.py

import numpy as np


def sample_and_detect_nrz(
    signal,
    fs_internal,
    Rb,
    fs_rx=None
):

    # 1) ADC / převzorkování
    if fs_rx is not None and fs_rx < fs_internal:
        step_adc = max(int(fs_internal / fs_rx), 1)
        signal_rx = signal[::step_adc]
        fs_eff = fs_internal / step_adc
    else:
        signal_rx = signal
        fs_eff = fs_internal

    # 2) Symbolové vzorkování (i při fs_eff < Rb)
    samples_per_bit = fs_eff / Rb
    step = max(int(samples_per_bit), 1)

    sample_indices = np.arange(
        step // 2,
        len(signal_rx),
        step
    )

    samples = signal_rx[sample_indices]

    # 3) Detekce (práh = 0)
    bits_rx = (samples > 0).astype(int)

    return bits_rx, samples, signal_rx, fs_eff

# lib/receiver/reconstruction.py

import numpy as np


def reconstruct_zoh_from_rx(signal_rx, fs_rx, fs_internal):
    """
    Rekonstrukce signálu z ADC výstupu (ZOH DAC).
    """
    t_rx = np.arange(len(signal_rx)) / fs_rx
    t_rec = np.arange(0, t_rx[-1], 1 / fs_internal)

    # ZOH: držení poslední hodnoty
    signal_rec = np.zeros_like(t_rec)
    idx = 0
    for i, t in enumerate(t_rec):
        while idx + 1 < len(t_rx) and t_rx[idx + 1] <= t:
            idx += 1
        signal_rec[i] = signal_rx[idx]

    return t_rec, signal_rec


