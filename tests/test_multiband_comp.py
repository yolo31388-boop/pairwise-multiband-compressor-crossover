import pytest
import av.multiband_comp as mod

CASES = [
    ("lr_crossover_split", (1,)),
    ("envelope_link", (1,)),
    ("coeff_double_buffer", (1,)),
    ("sidechain_rate_convert", (1,)),
    ("total_gain_normalize", (1,)),
    ("bypass_crossfade", (1,)),
    ("load_compressor", (1,)),
    ("analyze_bands", (1,)),
    ("process_comp", (1,)),
    ("present_comp", (1,)),
    ("validate_comp", (1,)),
    ("metrics_comp", (1,)),
    ("audit_comp", (1,)),
    ("fallback_comp", (1,)),
    ("determinism_comp", (1,)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
