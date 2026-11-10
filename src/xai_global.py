import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import shap
from xai_commun import m, Xte

Xs = Xte.sample(400, random_state=0)                    # 400 transactions de