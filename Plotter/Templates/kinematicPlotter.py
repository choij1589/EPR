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

def make_hist(cvs_params, hist_params, info_params):
    canvas = Kinematics(cvs_params)
    canvas.get_hists(hists, hist_params)
    canvas.combine(info_params)
    path_to_store = plotterBaseDir + output_path + "/" + hist_name + ".pdf"
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
        else:
            dir_name = file_name

        # combine ee and mm channel
        for option in selectorArgs:
            hist_path = dir_name + "/" + hist_name
            hist_ee = root_files[file_name].Get(hist_path + option + "_ee")
            hist_mm = root_files[file_name].Get(hist_path + option + "_mm")
            hist = hist_ee.Clone(file_name + option + "_clone")
            hist.Add(hist_mm)

            if option == "":
                option = "_dressedLep"
            elif option == "_prefsr":
                option = "_matchedGenJet"
            else:
                pass
            
            key = file_name + option
            hists[key] = hist
    
    info = userinputs.params[hist_name]
    cvs_params = info["cvs_params"]
    hist_params = info["hist_params"]
    info_params = info["info_params"]
    make_hist(cvs_params, hist_params, info_params)

for name in file_names:
    root_files[name].Close()
