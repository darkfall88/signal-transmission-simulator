# Projekt 1: Interaktivní simulace telegrafního a digitálního přenosu (Nyquistův a Shannon–Hartleyho teorém)

Úroveň: Bc., předmět Telekomunikace  
Jazyk: Python 3.12+  
Důraz: interaktivita, přístupnost, didaktičnost, jednoznačné hodnocení

## 1. Cíl

- Demonstrovat na interaktivní simulaci:
  - Nyquistův vzorkovací teorém (aliasing, rekonstrukce).
  - Nyquistovu limitu pro bezchybový přenos v pásmu omezeném kanálu.
  - Shannon–Hartleyho teorém (kapacita kanálu vs. šířka pásma a SNR).
- Porovnat telegrafní binární signál a alespoň jednu digitální modulaci (2-PAM/ASK nebo BPSK).
- Poskytnout srozumitelné vizualizace a intuitivní GUI vhodné do výuky.

## 2. Funkční požadavky (must-have)

1. Vstupy a GUI:

- Přepínače/posuvníky s jasnými popisy, jednotkami a rozsahy:
  - Typ signálu: Telegrafní (binární NRZ), 2-PAM/ASK nebo BPSK (min. 1 z digitálních).
  - Bitová rychlost Rb: 10 b/s – 200 kb/s.
  - Šířka pásma kanálu B: 100 Hz – 200 kHz.
  - Vzorkovací frekvence fs: 1 kHz – 2 MHz.
  - SNR (dB): −5 dB až 40 dB + přepínač AWGN on/off.
  - Délka rámce: 100 – 2000 bitů.
  - Seed RNG (pro reprodukovatelnost).
- Tlačítko „Reset na výukové defaulty“.

2. Generace a kanál:

- Generace náhodných binárních dat s mapováním na zvolenou modulaci.
- Pulsní tvar min. NRZ (obdélníkový).
- Kanál: ideální nízkopásmový filtr s nastavitelným B.
- AWGN s kalibrací podle výkonu signálu pro dosažení zadaného SNR.

3. Vzorkování, aliasing, rekonstrukce:

- Volitelné snížení fs pro demonstraci aliasingu.
- Zobrazení spektra (FFT) před/po kanálu a po vzorkování.
- Rekonstrukce signálu (ideální LPF) a symbolová detekce.

4. Měření a teorie:

- BER (Bit Error Rate) z detekovaných bitů.
- Teoretické limity:
  - Nyquistova rychlost: R_max = 2B (pro binární bez ISI, komentujte zjednodušení modelu).
  - Shannon–Hartley: C = B · log2(1 + SNR_linear).
- Vykreslení:
  - Časové průběhy: vysílaný, přijímaný, rekonstruovaný.
  - Oční diagram (eye diagram).
  - Spektrum |X(f)|.
  - Grafy: C vs. SNR, BER vs. SNR (simulovaná křivka).

5. Export a reprodukovatelnost:

- Export konfigurace do JSON.
- Export grafů do PNG a dat (např. BER křivky) do CSV.

## 3. Doporučené rozšíření (nice-to-have, nepovinné)

- Raised cosine puls s nastavitelným roll-off a demonstrace ISI.
- QPSK + ukázka vlivu chybné synchronizace.
- Interaktivní ilustrace kritéria Nyquista (nulování ISI).

## 4. Uživatelské rozhraní a přístupnost

- Stručné info-boxy (1–2 věty) u panelů: co graf/parametr ukazuje.
- Kontrastní barevné schéma, písmo min. 12–14 pt.
- Legendy, popisky os, jednotky, jasné názvy grafů.

## 5. Technické požadavky

- Python 3.12+.
- Doporučené knihovny: NumPy, SciPy, Matplotlib nebo Plotly, ipywidgets / Streamlit / Gradio.
- Struktura kódu do modulů: generator, channel, receiver, metrics, ui.
- Docstringy, typové anotace u veřejných funkcí, komentáře.

## 6. Odevzdání

- Zdrojové kódy + README (instalace, spuštění, popis parametrů).
- Jupyter notebook s demo scénářem (výukové ukázky) NEBO krátké textové PDF se scénářem a screenshoty.
- Sada JSON konfigurací pro reprodukci hodnoticích grafů.

## 7. Hodnocení (max. 50 bodů)

- Funkčnost must-have (20 b)
  - Generace signálu, kanál + AWGN, detekce, BER, teoretická kapacita, vizualizace čas/spektrum/oční diagram.
- Správnost a konzistence výpočtů (10 b)
  - Kalibrace SNR, chování BER vs. SNR a C vs. SNR odpovídá teorii pro rozumné parametry.
- Interaktivita a UX (8 b)
  - Intuitivní GUI, popisky, reset, přehledné grafy.
- Kvalita kódu a dokumentace (7 b)
  - Modularita, čitelnost, docstringy, README.
- Didaktičnost a přístupnost (5 b)
  - Info-boxy, srozumitelné výstupy, vhodné výchozí hodnoty.

## 8. Výchozí „výukové“ hodnoty (doporučení)

- Typ: BPSK.
- Rb = 10 kb/s, B = 10 kHz, fs = 500 kHz, SNR = 10 dB, délka rámce = 1000 bitů.
- Seed = 12345.
