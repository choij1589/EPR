from plotterBase import CompareBinnedAndIncl
from ROOT import *
import userinputs
import subprocess

# get root files
pwd = subprocess.check_output("echo $PWD", shell=True, encoding="utf-8")
pwd = pwd.rstrip("\n")
path_selectorOutput = pwd + "/../SelectorOutput/DrellYan/"
# inclusive first
file_names = ["DYm50_012j_nlo_cp5_GridToNano", "DYm50_0j_nlo_cp5_GridToNano", "DYm50_1j_nlo_cp5_GridToNano", "DYm50_2j_nlo_cp5_GridToNano"]
option = "_prefsr"
hist_names = ["ZMass"]
output_path = "./test_binIncl"

cvs_params = {
        "leg_size" : "medium",
        "logy" : False,
        "grid" : False
}
hist_params = {
        "rebin" : 20,
        "x_title" : "M(ll)",
        "y_title" : "Events",
        "error_range" : [0.5, 1.5]
}
info_params = {
        "info": "#it{L}_{int} = 150 fb^{-1}",
        "cms_text" : "CMS",
        "extra_text" : "Preliminary"
}

def make_hist():
    canvas = CompareBinnedAndIncl(cvs_params)
    canvas.get_hists(hist_incl, hists_binned, hist_params)
    canvas.combine(info_params)
    canvas.save(output_path + "/" + hist_name + ".pdf")

root_files = {}
for name in file_names:
    this_path = path_selectorOutput + name + ".root"
    root_files[name] = TFile(this_path)

for hist_name in hist_names:
    hist_incl = None
    hists_binned = {}
    for file_name in file_names:
        if file_name == "DYm50_012j_nlo_cp5_GridToNano":
            dir_name = "DYm50_cp5_GridToNano"
        else:
            dir_name = file_name

        # combine ee and mm channel
        hist_path = dir_name + "/" + hist_name
        print(hist_path + option + "_ee")
        hist_ee = root_files[file_name].Get(hist_path + option + "_ee")
        hist_mm = root_files[file_name].Get(hist_path + option + "_mm")
        hist = hist_ee.Clone(file_name + option + "_clone")
        hist.Add(hist_mm)

        key = file_name + option
        if "012j" in file_name:
            hist_incl = hist
        else:
            hists_binned[key] = hist

    make_hist()

for name in file_names:
    root_files[name].Close()



