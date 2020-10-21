#!/bin/sh

python plotter.py --hist ZMass_ee --xAxis "MassZ(ee) [GeV]" --yAxis "A.U." --rebin 10
python plotter.py --hist ZMass_mm --xAxis "MassZ(#mu#mu) [GeV]" --yAxis "A.U." --rebin 10
python plotter.py --hist yZ_ee --xAxis "y^{Z_{ee}}" --yAxis "A.U."
python plotter.py --hist yZ_mm --xAxis "y^{Z_{#mu#Mu}}" --yAxis "A.U."
python plotter.py --hist ptZ_ee --xAxis "p_{T} (Z_{ee})" --yAxis "A.U." --xRange 0. 200.
python plotter.py --hist ptZ_mm --xAxis "p_{T} (Z_{#mu#mu})" --yAxis "A.U." --xRange 0. 200.
python plotter.py --hist phiZ_ee --xAxis "#phi(Z_{ee})" --yAxis "A.U."
python plotter.py --hist phiZ_mm --xAxis "#phi(Z_{#mu#mu})" --yAxis "A.U."

python plotter.py --hist ptl1_ee --xAxis "p_{T}(l1_{ee})" --yAxis "A.U." --xRange 0. 200.
python plotter.py --hist ptl1_mm --xAxis "p_{T}(l1_{mm})" --yAxis "A.U." --xRange 0. 200.
python plotter.py --hist ptl2_ee --xAxis "p_{T}(l2_{ee})" --yAxis "A.U." --xRange 0. 200.
python plotter.py --hist ptl2_mm --xAxis "p_{T}(l2_{mm})" --yAxis "A.U." --xRange 0. 200.
python plotter.py --hist etal1_ee --xAxis "#eta(l1_{ee})" --yAxis "A.U."
python plotter.py --hist etal1_mm --xAxis "#eta(l1_{mm})" --yAxis "A.U."
python plotter.py --hist etal2_ee --xAxis "#eta(l2_{ee})" --yAxis "A.U."
python plotter.py --hist etal2_mm --xAxis "#eta(l2_{mm})" --yAxis "A.U."
python plotter.py --hist phil1_ee --xAxis "#phi(l1_{ee})" --yAxis "A.U."
python plotter.py --hist phil1_mm --xAxis "#phi(l1_{mm})" --yAxis "A.U."
python plotter.py --hist phil2_ee --xAxis "#phi(l2_{ee})" --yAxis "A.U."
python plotter.py --hist phil2_mm --xAxis "#phi(l2_{mm})" --yAxis "A.U."
