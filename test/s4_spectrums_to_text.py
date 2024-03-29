from core.spectrums.presets import PROMPT_PRESETS
from core.utils_npz import NpzUtils
from utils_fcp import FcpApi
from utils_my import MyAPI


X = NpzUtils.load(MyAPI.spectrum_features_norm)
prompts = PROMPT_PRESETS["most_imported_limited_5"](X, FcpApi())
print(prompts)
