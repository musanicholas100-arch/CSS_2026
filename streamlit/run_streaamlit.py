# -*- coding: utf-8 -*-
"""
Created on Wed Jan 28 21:22:27 2026

@author: Milan
"""

import subprocess

#file = "app.py"
#file = "app_plots.py"
file = "app_profiler.py"
#file = "app_profiler_menus.py"


subprocess.Popen(
    ["streamlit", "run", file], shell=True
)