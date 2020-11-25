from plotterBase import BinnedAndIncl
from ROOT import *
import os
import sys
import subprocess

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from PlotObjects import binnedAndInclInputs as compare_input

# get root files
pwd = subprocess.check_output("echo $PWD", shell=True, encoding="utf-8")
pwd = pwd.rstrip("\n")
plotterBaseDir = pwd + "/" 
selectorOutput = pwd + "/../SelectorOutput/DrellYan/"
# inclusive first
file_names = compare_input.file_names
option = compare_input.option
hist_names = compare_input.observables
lumi = compare_input.lumi
output_path = compare_input.output_path


weights = compare_input.weights
params = compare_input.params

def make_hist():
    canvas = BinnedAndIncl(cvs_params)
    canvas.get_hists(hist_incl, hists_binned, hist_params)
    canvas.combine(info_params)
    canvas.save(output_path + "/" + hist_name + ".pdf")

root_files = {}
for name in file_names:
    this_path = selectorOutput + name + ".root"
    root_files[name] = TFile(this_path)

for hist_name in hist_names:
    this_params = params[hist_name]
    cvs_params = this_params["cvs_params"]
    hist_params = this_params["hist_params"]
    info_params = this_params["info_params"]

    hist_incl = None
    hists_binned = {}
    for file_name in file_names:
        if file_name == "DYm50_012j_nlo_cp5_GridToNano":
            dir_name = "DYm50_cp5_GridToNano"
        else:
            dir_name = file_name
        
        scale = weights[file_name]*lumi*1000
        # combine ee and mm channel
        hist_path = dir_name + "/" + hist_name
        hist_ee = root_files[file_name].Get(hist_path + option + "_ee")
        hist_mm = root_files[file_name].Get(hist_path + option + "_mm")
        hist = hist_ee.Clone(file_name + option + "_clone")
        hist.Add(hist_mm)
        hist.Scale(scale)
        
        key = file_name
        if option == "":
            file_name += "_dressedLep"
        elif option == "_prefsr":
            file_name += "_prefsr"
        else:
            file_name += option

        if "012j" in file_name:
            hist_incl = hist
        else:
            hists_binned[key] = hist
        
    make_hist()

for name in file_names:
    root_files[name].Close()
