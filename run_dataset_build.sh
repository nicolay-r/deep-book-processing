#!/bin/bash
python my_s3_dataset_compose.py
python my_s3_dataset_folding.py
python my_s4_char_spectrum_embed_features.py
python my_s5_char_save_spectrum_prompts.py
# python my_s5_parlai_dataset_0_stat.py
# python my_s5_parlai_dataset_1_stat.py
python my_s5_parlai_dataset_build_candidates.py
python my_s5_parlai_dataset_convert.py
