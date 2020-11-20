from plotterBase import plotterBase, KinematicDistribution
from ROOT import *
import subprocess

# get data
pwd = subprocess.check_output("echo $PWD", shell=True, encoding="utf-8")
pwd = pwd.rstrip("\n")

path_selectorOutput = pwd + "/../SelectorOutput/DrellYan/"
file_names = ["DYm50_012j_nlo_cp5_GridToNano",
              "DYm50_0j_nlo_cp5_GridToNano",
              "DYm50_1j_nlo_cp5_GridToNano",
              "DYm50_2j_nlo_cp5_GridToNano"]

# Set meta information
# decalre the histogram you want to put
hist_name = "ZMass"
#selectorArgs = ["_lhe", "_born", "_barelep", "_prefsr", ""]
selectorArgs = ["_barelep", "_prefsr"]
cvs_params = {
        "leg_size" : "medium",
        "logy" : False,
        "grid" : False
        }

hist_params = {
        "base_hist" : "DYm50_012j_nlo_cp5_GridToNano_barelep",
        "rebin" : 20,
        "x_title": "M(ll)",
        "y_title": "Events",
        "ratio_title": "x/Default",
        "error_range": [0.5, 1.5],
        }

info_params = {
        #"info": "#it{L}_{int} = 35.9 fb^{-1}"
        "info": "Normed to unit",
        "cms_text" : "CMS",
        "extra_text" : "Preliminary"
        }

root_files = {}
for name in file_names:
    this_path = path_selectorOutput + name + ".root"
    root_files[name] = TFile(this_path)
    # root_files[name].ls()

# now get histograms from the root file
hists = {}
for file_name in file_names:
    for option in selectorArgs:
        if file_name == "DYm50_012j_nlo_cp5_GridToNano":
            dir_name = "DYm50_cp5_GridToNano";
        else:
            dir_name = file_name

        # combine ee and mm channel
        hist_path = dir_name + "/" + hist_name
        hist_ee = root_files[file_name].Get(hist_path + option + "_ee")
        hist_mm = root_files[file_name].Get(hist_path + option + "_mm")
        hist = hist_ee.Clone(file_name + option + "_clone")
        hist.Add(hist_mm)
        hists[file_name + option] = hist

canvas = KinematicDistribution(cvs_params)
canvas.get_hists(hists, hist_params)
canvas.combine(info_params)
canvas.save("test.png")
