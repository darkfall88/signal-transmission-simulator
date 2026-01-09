import ipywidgets as widgets


# ======================
# Pomocné formátování
# ======================

def format_bandwidth(B):
    if B < 1_000:
        return f"{B:.0f} Hz"
    else:
        return f"{B/1e3:.1f} kHz"

# ======================================================
# UI pro GENERÁTOR
# ======================================================

def create_generator_ui():
    """
    Vytvoří UI prvky pro generátor binárního NRZ signálu.

    Vrací:
        ui (VBox),
        controls (dict)
    """

    Rb_slider = widgets.IntSlider(
        value=10_000,
        min=1_000,
        max=100_000,
        step=1_000,
        description="Rb [b/s]",
        continuous_update=True
    )

    frame_slider = widgets.IntSlider(
        value=100,
        min=10,
        max=2_000,
        step=10,
        description="Počet bitů",
        continuous_update=True
    )

    seed_text = widgets.IntText(
        value=12345,
        description="Seed"
    )

    random_seed_button = widgets.Button(
        description="Náhodný seed",
        button_style="info"
    )

    def randomize_seed(_):
        import numpy as np
        seed_text.value = int(np.random.randint(0, 1e9))

    random_seed_button.on_click(randomize_seed)

    ui = widgets.VBox([
        Rb_slider,
        frame_slider,
        seed_text,
        random_seed_button
    ])

    controls = {
        "Rb": Rb_slider,
        "frame_length": frame_slider,
        "seed": seed_text
    }

    return ui, controls



# ======================
# UI pro kanál
# ======================

def create_channel_ui():
    """
    Vytvoří UI prvky pro kanál (LPF + AWGN).
    Vrací:
        ui (VBox),
        controls (dict) – mapování názvů na widgety
    """

    B_slider = widgets.FloatLogSlider(
        value=10_000,
        base=10,
        min=2,      # 100 Hz
        max=5.3,    # ~200 kHz
        step=0.1,
        description="B",
        continuous_update=True
    )

    B_label = widgets.Label()
    B_label.value = f"Šířka pásma: {format_bandwidth(B_slider.value)}"

    def update_B_label(change):
        B_label.value = f"Šířka pásma: {format_bandwidth(change['new'])}"

    B_slider.observe(update_B_label, names="value")

    SNR_slider = widgets.FloatSlider(
        value=10,
        min=-5,
        max=40,
        step=1,
        description="SNR [dB]",
        continuous_update=True
    )

    awgn_checkbox = widgets.Checkbox(
        value=True,
        description="AWGN zapnuto"
    )

    show_noise_checkbox = widgets.Checkbox(
        value=False,
        description="Zobrazit šum"
    )

    zoom_bits_slider = widgets.IntSlider(
        value=5,
        min=1,
        max=20,
        step=1,
        description="Zoom [bity]"
    )

    ui = widgets.VBox([
        B_slider,
        B_label,
        SNR_slider,
        awgn_checkbox,
        zoom_bits_slider,
        show_noise_checkbox
    ])

    controls = {
        "B": B_slider,
        "snr_db": SNR_slider,
        "awgn_on": awgn_checkbox,
        "zoom_bits": zoom_bits_slider,
        "show_noise": show_noise_checkbox
    }

    return ui, controls

def create_receiver_ui():
    enable_adc = widgets.Checkbox(
        value=False,
        description="Snížit fs (ADC)"
    )

    fs_rx = widgets.FloatLogSlider(
        value=20_000,
        min=2,
        max=5,
        step=0.1,
        description="fs_rx [Hz]"
    )

    zoom_bits = widgets.IntSlider(
        value=10,
        min=1,
        max=100,
        step=1,
        description="Zoom [bitů]"
    )

    ui = widgets.VBox([
        enable_adc,
        fs_rx,
        zoom_bits
    ])

    controls = {
        "enable_adc": enable_adc,
        "fs_rx": fs_rx,
        "zoom_bits": zoom_bits
    }

    return ui, controls

