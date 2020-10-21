from plotterBase import plotterBase, kDistributions
from ROOT import *
import subprocess
import argparse

# input for argparse
parser = argparse.ArgumentParser(description="test")
parser.add_argument("--hist", required=True, help="histogram name")
parser.add_argument("--xAxis", required=True, help="x axis name")
parser.add_argument("--yAxis", required=True, help="y axis name")
parser.add_argument("--rebin", default=-1, help="rebin factor")

args = parser.parse_args()

# get data
pwd = subprocess.check_output("echo $PWD", shell=True, encoding="utf-8")
pwd = pwd.rstrip("\n")

path_selOutput = pwd + "/../SelectorOutput/DrellYan/"
file_names = ["DYtest",
              "DY_inclusive_0j_nlo",
              "DY_inclusive_012j_nlo"]

# TFiles and hists
files = {}
for name in file_names:
    this_path = path_selOutput + name + ".root"
    files[name] = TFile(this_path)

hists = {}
hist_name = str(args.hist)
x_axis = str(args.xAxis)
y_axis = str(args.yAxis)
rebin = int(args.rebin)
#hist_name = "ZMass_ee"
#x_axis = "M(ee)"
#y_axis = "A.U."

for file_name in file_names:
    if file_name == "DYtest":
        hist_path = "DYm50/" + hist_name
        hist = files[file_name].Get(hist_path)
        hists[file_name] = hist
    elif file_name == "DY_inclusive_0j_nlo":
        hist_path = file_name + "/" + hist_name
        hist = files[file_name].Get(hist_path)
        hists[file_name] = hist
    elif file_name == "DY_inclusive_012j_nlo":
        hist_path = file_name + "/" + hist_name
        hist = files[file_name].Get(hist_path)
        hists[file_name] = hist
    else:
        raise(NameError)

kDist = kDistributions()
kDist.get_hists(hists=hists, scale="normalize", rebin=rebin)
kDist.generate_ratio(base_name="DYtest")
kDist.deco_hists(y_title=y_axis)
kDist.deco_ratio(x_title=x_axis, y_title="x/DYtest")
kDist.combine(info="Normed to unit")
kDist.save(pwd + "/../PlotterResult/drellyan/" + hist_name + ".png")
