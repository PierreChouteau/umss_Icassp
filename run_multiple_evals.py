'''run evaluations on multiple models'''

import os

models_to_evaluate = [

    # model trained on BC1Song
    "UMSS_4s_satb_bc1song_mf0",
    "unet_4s_bc1song_mf0",
    "Sf-Sft_bc1song",
    "W-Up_bc1song",
    
    # model trained on BCBQ
    "UMSS_4s_satb_bc1song_mf0",
    "unet_4s_bc1song_mf0",
    "Sf-Sft_bcbq",
    "W-Up_bcbq",
]

eval_mode='default' # default evaluation
# eval_mode='fast' # fast evaluation
# eval_mode='robustness' # run many unique evaluations for each model, following different types of robustness tests
# eval_mode='robustness_vad' # run many unique evaluations for each model, with vad error tests only



for tag in models_to_evaluate:
    
    if eval_mode=='robustness_vad' :
        for i in range(5):
            command="python eval_robustness_tests.py --tag '{}' --f0-from-mix --test-set 'CSD' --teststocompute baseline_gtf0 gtf0_strict_error_percent --vadseed {}".format(tag,i)
            print(command)
            os.system(command)
    else:
        if eval_mode=='original_paper':
            command="python eval.py --tag '{}' --f0-from-mix --test-set 'CSD'".format(tag)
    
        elif eval_mode=='default':
            # mf0 extract with Crepe
            command="python eval.py --tag '{}' --test-set 'CSD' --show-progress --compute all".format(tag)
            # mf0 extract with Cuesta et al. (model 3) model
            # command="python eval.py --tag '{}' --f0-from-mix --test-set 'CSD' --show-progress --compute all".format(tag)
        
        elif eval_mode=='fast':
            command="python eval.py --tag '{}' --f0-from-mix --test-set 'CSD' --show-progress --compute SI-SDR_mask".format(tag)

        elif eval_mode=='robustness':
            command="python eval_robustness_tests.py --tag '{}' --f0-from-mix --test-set 'CSD' --teststocompute all".format(tag)

        elif eval_mode=='robustness_vad':
            command="python eval_robustness_tests.py --tag '{}' --f0-from-mix --test-set 'CSD' --teststocompute baseline_gtf0 gtf0_strict_error_percent --vadseed 0".format(tag)


        print(command)
        os.system(command)