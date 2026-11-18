# DeepONet Reduced-Model Surrogate Report

- Data: `data\jump3_dataset_cal.csv`
- Samples: `240` (`192` train / `48` test)
- Device: `cuda`
- FEM labels: `not used`

## Test R2

- `Hcom_mm`: `0.999782`
- `vcom_mps`: `0.999773`
- `vtop_mps`: `0.999905`
- `spin_radms`: `0.999871`
- `Btrig_static_T`: `0.999924`
- `Btrig_lo_T`: `0.999930`
- `Btrig_hi_T`: `0.999931`

## Dataset Errors After Training

- `Hcom_mm`: MAE `0.0710625`, max abs `1.61612`
- `vcom_mps`: MAE `0.000521599`, max abs `0.0110441`
- `vtop_mps`: MAE `0.00143281`, max abs `0.0191035`
- `spin_radms`: MAE `0.000131538`, max abs `0.000617728`
- `Btrig_static_T`: MAE `0.00139326`, max abs `0.0084939`
- `Btrig_lo_T`: MAE `0.00199143`, max abs `0.012978`
- `Btrig_hi_T`: MAE `0.00252`, max abs `0.0167522`

## Scope

This model is a reduced-model operator surrogate. It is suitable for fast platform-side prediction and inverse-design proposal generation.
It is not a high-fidelity FEM operator and should not be presented as replacing Abaqus validation.
