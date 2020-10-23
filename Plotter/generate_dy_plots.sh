#!/bin/sh
export o_path="$PWD/../PlotterResult/drellyan"

python plotter.py --hist ZMass --xAxis "ZMass" --yAxis "A.U." --output $o_path --rebin 10
python plotter.py --hist yZ --xAxis "y^{Z}" --yAxis "A.U." --output $o_path
python plotter.py --hist ptZ --xAxis "p_{T} (Z)" --yAxis "A.U." --xRange 0. 200. --output $o_path
python plotter.py --hist phiZ --xAxis "#phi(Z)" --yAxis "A.U." --output $o_path

python plotter.py --hist ptl1 --xAxis "p_{T}(l1)" --yAxis "A.U." --xRange 0. 200. --output $o_path
python plotter.py --hist ptl2 --xAxis "p_{T}(l2)" --yAxis "A.U." --xRange 0. 200. --output $o_path
python plotter.py --hist etal1 --xAxis "#eta(l1)" --yAxis "A.U." --output $o_path
python plotter.py --hist etal2 --xAxis "#eta(l2)" --yAxis "A.U." --output $o_path
python plotter.py --hist phil1 --xAxis "#phi(l1)" --yAxis "A.U." --output $o_path
python plotter.py --hist phil2 --xAxis "#phi(l2)" --yAxis "A.U." --output $o_path
python plotter.py --hist phil2 --xAxis "#phi(l2)" --yAxis "A.U." --output $o_path

#python plotter.py --hist ZMass_prefsr --xAxis "mZ_prefsr" --yAxis "A.U." --rebin 10
#python plotter.py --hist yZ_prefsr --xAxis "yZ_prefsr" --yAxis "A.U."
#python plotter.py --hist ptZ_prefsr --xAxis "ptZ_prefsr" --yAxis "A.U." --xRange 0. 200.
#python plotter.py --hist phiZ_prefsr --xAxis "phiZ_prefsr" --yAxis "A.U."
