# Validation Guide for TFM Paper #19  
**Reproduce key results and figures:**  

---

## 1. Dirac Coupling Schematic (Figure 1)  
```bash  
python scripts/dirac_coupling.py  
```
**Output:** `figures/Dirac_Tpm_schematic.png`  

---

## 2. Muon g-2 Calculation (Figure 2)  
```bash  
python scripts/g2_calculation.py --m_tpm 100 --coupling_g 0.1  
```
Compare \( \Delta a_\mu \) output to **Section 4.1**.  

---

## 3. Higgs Decay Modification  
```bash  
python scripts/higgs_decays.py --input data/cmb_initial_conditions.h5  
```
Matches **Equation (4.2)** in the paper.  

---

## 4. Neutrino Mass Analysis  
```bash  
python scripts/neutrino_oscillations.py --lambda_nu 1e-5  
```
Tests **Equation (4.4)** predictions.  
