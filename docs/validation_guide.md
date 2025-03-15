# Validation Guide  
Reproduce key results from **Relativistic Quantum Fields in the Time Field Model** (Paper #19).  

---

## 1. Dirac Spinor Coupling to \(T^\pm\)  
**Script:** `scripts/dirac_coupling.py`  
**Output:** `figures/Dirac_Tpm_schematic.png` (Figure 1)  
**Steps:**  
1. Generate the Dirac-\(T^\pm\) coupling schematic:  
   ```bash  
   python scripts/dirac_coupling.py  
   ```
Compare the output to Figure 1 in the paper.  
Verify the vertex labels (incoming/outgoing muon, \(T^+\), \(T^-\)).  

---

## 2. Muon \( g-2 \) Contribution  
**Script:** `scripts/g2_calculation.py`  
**Output:** Terminal output of \( \Delta a_\mu \).  
**Steps:**  
1. Compute the TFM contribution to the muon’s anomalous magnetic moment:  
   ```bash  
   python scripts/g2_calculation.py --m_tpm 100 --coupling_g 0.1  
   ```
**Parameters:**  
- `--m_tpm`: Mass of \(T^\pm\) in GeV (default: 100 GeV).  
- `--coupling_g`: Coupling constant \( g \) (default: 0.1).  

**Expected output for default parameters:**  
```plaintext
TFM contribution to muon g-2: Δa_μ = 2.5e-9  
```
Compare with **Section 4.1** and **Equation (4.1)**.  

---

## 3. Higgs Decay Modifications  
**Script:** `scripts/higgs_decays.py`  
**Data:** `data/cmb_initial_conditions.h5`  
**Output:** Modified partial width \( \Gamma(h \to \gamma \gamma) \).  
**Steps:**  
1. Calculate the Higgs decay modification factor \( \delta_{TFM} \):  
   ```bash  
   python scripts/higgs_decays.py --input data/cmb_initial_conditions.h5  
   ```
The script returns \( \delta_{TFM} \), e.g., \( \sim 0.005 \) (5% shift).  
Match with **Equation (4.2)** and **Section 4.2**.  

---

## 4. Neutrino Oscillation Analysis  
**Script:** `scripts/neutrino_oscillations.py`  
**Parameters:** Coupling \( \lambda_\nu \) (default: \( 10^{-5} \)).  
**Output:** \( \Delta m_\nu^2 \) for neutrino flavors.  
**Steps:**  
1. Compute neutrino mass-squared differences:  
   ```bash  
   python scripts/neutrino_oscillations.py --lambda_nu 1e-5  
   ```
**Expected output (example):**  
```plaintext
Δm^2 (eV²): [2.4e-3, 7.5e-5]  
```
Compare with **Equation (4.4)** and **Section 4.4**.  

---

## 5. Hierarchy Problem (One-Loop Cancellation)  
**Script:** `scripts/hierarchy_rg.py`  
**Output:** Higgs mass correction \( \Delta m_h^2 \) from \(T^\pm\) loops.  
**Steps:**  
1. Run the one-loop cancellation analysis:  
   ```bash  
   python scripts/hierarchy_rg.py --m_tpm 1000 --coupling_g 0.2  
   ```
**Example output:**  
```plaintext
Δm_h^2 reduction: 38%  
```
Aligns with **Section 4.5** and **Appendix C**.  

---

## Notes  
- **Dependencies:** Install via `pip install -r requirements.txt` (NumPy, Matplotlib, h5py).  
- **Data Sources:**  
  - **Mock CMB data:** `data/cmb_initial_conditions.h5`.  
  - **For real CMB analysis,** substitute with Planck data: [Planck Archive](https://pla.esac.esa.int/).  
- **Issues?** Open a GitHub ticket or contact [alifayyaz@live.com](mailto:alifayyaz@live.com).  

---

## Reproducibility Checklist  
✅ Generate all figures and outputs using the scripts above.  
✅ Compare terminal/log outputs with paper predictions.  
✅ Replace mock data with observational datasets for real-world validation.  

---

**Key Features:**  
- Step-by-step replication of **Figures 1–2** and key equations.  
- Direct parameter inputs (e.g., \(m_{T^\pm}\), \(g\), \(\lambda_\nu\)).  
- Clear links to paper sections for cross-verification.  
