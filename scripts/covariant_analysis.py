import h5py
import numpy as np

def load_cmb_initial_conditions(path):
    """Load TFM relativistic CMB initial conditions."""
    with h5py.File(path, 'r') as f:
        T_plus = f['T_plus'][:]
        T_minus = f['T_minus'][:]
        gamma = f['gamma'][:]
        alpha = f.attrs['alpha']
        beta = f.attrs['beta']
        g_dirac = f.attrs['g_dirac']
    return T_plus, T_minus, gamma, alpha, beta, g_dirac

# Example usage:
T_plus, T_minus, gamma, alpha, beta, g_dirac = load_cmb_initial_conditions('data/cmb_initial_conditions.h5')
