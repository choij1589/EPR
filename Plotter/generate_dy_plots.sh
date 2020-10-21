#!/bin/sh

python plotter.py --hist ZMass_ee --xAxis "MassZ(ee) [GeV]" --yAxis "A.U."
python plotter.py --hist ZMass_mm --xAxis "MassZ(#mu#mu) [GeV]" --yAxis "A.U."
python plotter.py --hist yZ_ee --xAxis "y^{Z_{ee}}" --yAxis "A.U."
python plotter.py --hist yZ_mm --xAxis "y^{Z_{#mu#Mu}}" --yAxis "A.U."
python plotter.py --hist ptZ_ee --xAxis "p_{T} (Z_{ee})" --yAxis "A.U."
python plotter.py --hist ptZ_mm --xAixs "p_{T} (Z_{#mu#mu})" --yAxis "A.U."
python plotter.py --hist phiZ_ee --xAxis "#phi(Z_{ee})" --yAxis "A.U."
python plotter.py --hist phiZ_mm --xAxis "#phi(Z_{#mu#mu})" --yAxis "A.U."
