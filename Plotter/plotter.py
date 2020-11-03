from plotterBase import plotterBase, kDistributions
from ROOT import *
import subprocess
import argparse

# input for argparse
parser = argparse.ArgumentParser(description="test")
parser.add_argument("--hist", required=True, help="histogram name")
parser.add_argument("--xAxis", required=True, help="x axis name")
parser.add_argument("--xRange", nargs=2, type=float, default=[0., -1.], help="x axis range")
parser.add_argument("--yAxis", required=True, help="y axis name")
parser.add_argument("--yRange", nargs=2, type=float, default=[0., -1.], help="y axis range")
parser.add_argument("--error", type=str, default="medium", help="error range")
parser.add_argument("--rebin", default=-1, type=int, help="rebin factor")
parser.add_argument("--output", default=".", type=str, help="output path")
parser.add_argument("--combine", default=False, type=bool, help="combine ee and mm channel")
args = parser.parse_args()

# get data
pwd = subprocess.check_output("echo $PWD", shell=True, encoding="utf-8")
pwd = pwd.rstrip("\n")

path_selOutput = pwd + "/../SelectorOutput/DrellYan/"
file_names = ["DYm50_MiniToNano",
              "DY_incl_0j_nlo",
              "DY_incl_012j_nlo"]

# TFiles and hists
files = {}
for name in file_names:
    this_path = path_selOutput + name + ".root"
    files[name] = TFile(this_path)

hists = {}
hist_name = str(args.hist)
x_axis = str(args.xAxis)
x_axis_range = args.xRange
y_axis = str(args.yAxis)
y_axis_range = args.yRange
rebin = int(args.rebin)
error_range = str(args.error)
output_path = str(args.output)
combine = args.combine

#hist_name = "ZMass_ee"
#x_axis = "M(ee)"
#y_axis = "A.U."
options = ["_lhe", "_born"]
for file_name in file_names:
    for option in options:
        if file_name == "DY_incl_012j_nlo":
            dir_name = "DY_inclusive_012j_nlo"
        elif file_name == "DY_incl_0j_nlo":
            dir_name = "DY_inclusive_0j_nlo"
        else:
            dir_name = file_name
            
        if combine:
            hist_path = dir_name + "/" +  hist_name
            hist_ee = files[file_name].Get(hist_path + option + "_ee")
            hist_mm = files[file_name].Get(hist_path + option + "_mm")
            hist = hist_ee.Clone(file_name + option + "_clone")
            hist.Add(hist_mm)
            hists[file_name + option] = hist
        else:
            print("without combine option is not set yet")
            raise(TypeError)

kDist = kDistributions(leg_size="medium")
kDist.get_hists(hists=hists, scale="normalize", rebin=rebin, x_axis_range=x_axis_range, y_axis_range=y_axis_range)
kDist.generate_ratio(base_name="DYm50_MiniToNano_lhe")
kDist.deco_hists(y_title=y_axis)
kDist.deco_ratio(x_title=x_axis, error_range=error_range, y_title="x/DYm50")
kDist.combine(info="Normed to unit")
#kDist.save(pwd + "/../PlotterResult/drellyan/" + hist_name + ".png")
kDist.save(output_path + "/lhe_born/" + hist_name + "_lhe_born.pdf")
