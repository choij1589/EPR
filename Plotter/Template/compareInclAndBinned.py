from plotterBase import CompareBinnedAndIncl
from ROOT import *
import compare_input
import subprocess

# get root files
pwd = subprocess.check_output("echo $PWD", shell=True, encoding="utf-8")
pwd = pwd.rstrip("\n")
path_selectorOutput = pwd + "/../../SelectorOutput/DrellYan/"
# inclusive first
file_names = compare_input.file_names
option = compare_input.option
hist_names = compare_input.observables
lumi = compare_input.lumi
output_path = compare_input.output_path

weights = compare_input.weights
params = compare_input.params
cvs_params = {
        "leg_size" : "medium",
        "logy" : True,
        "grid" : False
}
hist_params = {
        "rebin" : -1,
        "x_title" : "p_{T}(j1)",
        "y_title" : "Events",
        "error_range" : [0., 2.0]
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
        print(hist_path + option + "_ee")
        hist_ee = root_files[file_name].Get(hist_path + option + "_ee")
        hist_mm = root_files[file_name].Get(hist_path + option + "_mm")
        hist = hist_ee.Clone(file_name + option + "_clone")
        hist.Add(hist_mm)
        hist.Scale(scale)

        key = file_name + option
        if "012j" in file_name:
            hist_incl = hist
        else:
            hists_binned[key] = hist

    make_hist()

for name in file_names:
    root_files[name].Close()
