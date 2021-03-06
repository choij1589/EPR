from plotterBase import Kinematics
from ROOT import *
import os
import sys
import subprocess
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from PlotObjects import kinematicsInputs as userinputs

# get data
pwd = subprocess.check_output("echo $PWD", shell=True, encoding="utf-8")
pwd = pwd.rstrip("\n")

# set meta information
plotterBaseDir = pwd + "/"
selectorOutput = pwd + "/../SelectorOutput/DrellYan/"
file_names = userinputs.file_names
selectorArgs = userinputs.selectorArgs
hist_names = userinputs.observables
output_path = userinputs.output_path
base_hist = userinputs.base_hist

def make_hist(cvs_params, hist_params, info_params):
    canvas = Kinematics(cvs_params)
    canvas.get_hists(hists, hist_params)
    canvas.combine(info_params)
    path_to_store = output_path + "/" + hist_name + ".pdf"
    canvas.save(path_to_store)


root_files = {}
for name in file_names:
    this_path = selectorOutput + name + ".root"
    root_files[name] = TFile(this_path)

for hist_name in hist_names:
    hists = {}
    for file_name in file_names:
        if file_name == "DYm50_012j_nlo_cp5_GridToNano":
            dir_name = "DYm50_cp5_GridToNano"
        elif file_name == "DYm50_012j_nlo_cp5_MiniToNano":
            dir_name = "DYm50_cp5_MiniToNano"
        else:
            dir_name = file_name

        # combine ee and mm channel
        for option in selectorArgs:
            hist_path = dir_name + "/" + hist_name
            print(hist_path + option + "_ee")
            hist_ee = root_files[file_name].Get(hist_path + option + "_ee")
            hist_mm = root_files[file_name].Get(hist_path + option + "_mm")
            hist = hist_ee.Clone(file_name + option + "_clone")
            hist.Add(hist_mm)

            if option == "":
                key = file_name + "_dressedLep"
                option = "_dressedLep"
            elif option == "_prefsr":
                key = file_name + "_matchedGenJet"
            else:
                key = file_name + option
            print(key)
            hists[key] = hist
    
    info = userinputs.params[hist_name]
    info["hist_params"]["base_hist"] = base_hist
    cvs_params = info["cvs_params"]
    hist_params = info["hist_params"]
    info_params = info["info_params"]
    make_hist(cvs_params, hist_params, info_params)

for name in file_names:
    root_files[name].Close()
