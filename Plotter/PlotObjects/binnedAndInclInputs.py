file_names = ["DYm50_012j_nlo_cp5", "DYm50_0j_nlo_cp5", "DYm50_1j_nlo_cp5", "DYm50_2j_nlo_cp5"]
#file_names = ["DYm50_012j_nlo_cuep5m1", "DYm50_0j_nlo_cuep5m1", "DYm50_1j_nlo_cuep5m1", "DYm50_2j_nlo_cuep5m1"]
option = "_barelep"
observables = ["ZMass", "yZ", "ptZ", "phiZ", 
                "ptl1", "ptl2", "etal1", "etal2", "phil1", "phil2", "nLeptons",
                "ptj1", "ptj2", "etaj1", "etaj2", "phij1", "phij2", "nJets"]
lumi = 150. # fb^-1
weights = {
        "DYm50_012j_nlo_cp5" : 2.99030301E-03,
        "DYm50_0j_nlo_cp5" : 8.43901018E-04,
        "DYm50_1j_nlo_cp5" : 7.35992842E-04,
        "DYm50_2j_nlo_cp5" : 4.39098262E-04,
        "DYm50_012j_nlo_cuep5m1" : 2.73003549E-03,
        "DYm50_0j_nlo_cuep5m1" : 9.57783732E-04,
        "DYm50_1j_nlo_cuep5m1" : 7.61277377E-04,
        "DYm50_2j_nlo_cuep5m1" : 3.93164481E-04
}
#output_path = "/home/choij/Workspace/EPR/PlotterResult/drellyan/cp5/BinnedAndIncl/matchedGenJet"
output_path = "/home/choij/Workspace/www/VGenStudies"
params = {
	# Z
    "ZMass": {
        "cvs_params": {
            "leg_size": "medium",
            "logy": False,
            "grid": True
        },
        "hist_params": {
            "rebin": 20,
            "x_title": "M(ll)",
            "y_title": "Events",
            "ratio_title": "x/Default",
            "error_range": [0.5, 1.5]
        },
        "info_params": {
            "info": "Normed to #it{L}_{int} = 150 fb^{-1}",
            "cms_text": "CMS",
            "extra_text": "Preliminary"
        }
    },
    "yZ": {
        "cvs_params": {
            "leg_size": "medium",
            "logy": False,
            "grid": True
        },
        "hist_params": {
            "rebin": -1,
            "x_title": "y^{Z}",
            "y_title": "Events", 
            "ratio_title" : "x/Default",
            "error_range": [0.5, 1.5],
        },
        "info_params": {
            "info": "Normed to #it{L}_{int} = 150 fb^{-1}",
            "cms_text": "CMS",
            "extra_text": "Preliminary"
        }
    },
	"ptZ": {
        "cvs_params": {
            "leg_size": "medium",
            "logy": True,
            "grid": True
        },
        "hist_params": {
            "rebin": 2,
            "x_title": "p_{T}(Z)",
            "y_title": "Events",
            "ratio_title" : "x/Default",
            "x_range": [0., 200.],
            "error_range": [0.5, 1.5],
        },
        "info_params": {
            "info": "Normed to #it{L}_{int} = 150 fb^{-1}",
            "cms_text": "CMS",
            "extra_text": "Preliminary"
        }
    },
	"phiZ": {
        "cvs_params": {
            "leg_size": "medium",
            "logy": False,
            "grid": True
        },
        "hist_params": {
            "rebin": -1,
            "x_title": "#phi(Z)",
            "y_title": "Events",
            "ratio_title" : "x/Default",
            "error_range": [0.5, 1.5],
        },
        "info_params": {
            "info": "Normed to #it{L}_{int} = 150 fb^{-1}",
            "cms_text": "CMS",
            "extra_text": "Preliminary"
        }
    },
	# Leptons
	"ptl1": {
        "cvs_params": {
            "leg_size": "medium",
            "logy": True,
            "grid": True
        },
        "hist_params": {
            "rebin": 2,
            "x_title": "p_{T}(l1)",
            "y_title": "Events",
            "ratio_title" : "x/Default",
			"x_range" : [0., 200.],
            "error_range": [0.5, 1.5],
        },
        "info_params": {
            "info": "Normed to #it{L}_{int} = 150 fb^{-1}",
            "cms_text": "CMS",
            "extra_text": "Preliminary"
        }
    },
	"ptl2": {
        "cvs_params": {
            "leg_size": "medium",
            "logy": True,
            "grid": True
        },
        "hist_params": {
            "rebin": 2,
            "x_title": "p_{T}(l2)",
            "y_title": "Events",
            "ratio_title" : "x/Default",
			"x_range" : [0., 200.],
            "error_range": [0.5, 1.5],
        },
        "info_params": {
            "info": "Normed to #it{L}_{int} = 150 fb^{-1}",
            "cms_text": "CMS",
            "extra_text": "Preliminary"
        }
    },
	"etal1": {
        "cvs_params": {
            "leg_size": "medium",
            "logy": False,
            "grid": True
        },
        "hist_params": {
            "rebin": -1,
            "x_title": "#eta(l1)",
            "y_title": "Events",
            "ratio_title" : "x/Default",
            "error_range": [0.5, 1.5],
        },
        "info_params": {
            "info": "Normed to #it{L}_{int} = 150 fb^{-1}",
            "cms_text": "CMS",
            "extra_text": "Preliminary"
        }
    },
	"etal2": {
        "cvs_params": {
            "leg_size": "medium",
            "logy": False,
            "grid": True
        },
        "hist_params": {
            "rebin": -1,
            "x_title": "#eta(l2)",
            "y_title": "Events",
            "ratio_title" : "x/Default",
            "error_range": [0.5, 1.5],
        },
        "info_params": {
            "info": "Normed to #it{L}_{int} = 150 fb^{-1}",
            "cms_text": "CMS",
            "extra_text": "Preliminary"
        }
    },
	"phil1": {
        "cvs_params": {
            "leg_size": "medium",
            "logy": False,
            "grid": True
        },
        "hist_params": {
            "rebin": -1,
            "x_title": "#phi(l1)",
            "y_title": "Events",
            "ratio_title" : "x/Default",
            "error_range": [0.5, 1.5],
        },
        "info_params": {
            "info": "Normed to #it{L}_{int} = 150 fb^{-1}",
            "cms_text": "CMS",
            "extra_text": "Preliminary"
        }
    },
	"phil2": {
        "cvs_params": {
            "leg_size": "medium",
            "logy": False,
            "grid": True
        },
        "hist_params": {
            "rebin": -1,
            "x_title": "#phi(l2)",
            "y_title": "Events",
            "ratio_title" : "x/Default",
            "error_range": [0.5, 1.5],
        },
        "info_params": {
            "info": "Normed to #it{L}_{int} = 150 fb^{-1}",
            "cms_text": "CMS",
            "extra_text": "Preliminary"
        }
    },
	"nLeptons": {
        "cvs_params": {
            "leg_size": "medium",
            "logy": False,
            "grid": True
        },
        "hist_params": {
            "rebin": -1,
            "x_title": "N(l)",
            "y_title": "Events",
            "ratio_title" : "x/Default",
            "error_range": [0.5, 1.5],
        },
        "info_params": {
            "info": "Normed to #it{L}_{int} = 150 fb^{-1}",
            "cms_text": "CMS",
            "extra_text": "Preliminary"
        }
    },
    # Jets
    "ptj1": {
        "cvs_params": {
            "leg_size": "medium",
            "logy": True,
            "grid": True
        },
        "hist_params": {
            "rebin": -1,
            "x_title": "p_{T}(j1)",
            "y_title": "Events",
            "ratio_title" : "x/Default",
            "x_range" : [0., 200.],
            "error_range": [0.5, 1.5],
        },
        "info_params": {
            "info": "Normed to #it{L}_{int} = 150 fb^{-1}",
            "cms_text": "CMS",
            "extra_text": "Preliminary"
        }
    },
    "ptj2": {
        "cvs_params": {
            "leg_size": "medium",
            "logy": True,
            "grid": True
        },
        "hist_params": {
            "rebin": -1,
            "x_title": "p_{T}(j2)",
            "y_title": "Events",
            "ratio_title" : "x/Default",
            "x_range" : [0., 200.],
            "error_range": [0.5, 1.5],
        },
        "info_params": {
            "info": "Normed to #it{L}_{int} = 150 fb^{-1}",
            "cms_text": "CMS",
            "extra_text": "Preliminary"
        }
    },
    "etaj1": {
        "cvs_params": {
            "leg_size": "medium",
            "logy": False,
            "grid": True
        },
        "hist_params": {
            "rebin": -1,
            "x_title": "#eta(j1)",
            "y_title": "Events",
            "ratio_title" : "x/Default",
            "error_range": [0.5, 1.5],
        },
        "info_params": {
            "info": "Normed to #it{L}_{int} = 150 fb^{-1}",
            "cms_text": "CMS",
            "extra_text": "Preliminary"
        }
    },
    "etaj2": {
        "cvs_params": {
            "leg_size": "medium",
            "logy": False,
            "grid": True
        },
        "hist_params": {
            "rebin": -1,
            "x_title": "#eta(j2)",
            "y_title": "Events",
            "ratio_title" : "x/Default",
            "error_range": [0.5, 1.5],
        },
        "info_params": {
            "info": "Normed to #it{L}_{int} = 150 fb^{-1}",
            "cms_text": "CMS",
            "extra_text": "Preliminary"
        }
    },
    "phij1": {
        "cvs_params": {
            "leg_size": "medium",
            "logy": False,
            "grid": True
        },
        "hist_params": {
            "rebin": -1,
            "x_title": "#phi(j1)",
            "y_title": "Events",
            "ratio_title" : "x/Default",
            "error_range": [0.5, 1.5],
        },
        "info_params": {
            "info": "Normed to #it{L}_{int} = 150 fb^{-1}",
            "cms_text": "CMS",
            "extra_text": "Preliminary"
        }
    },
    "phij2": {
        "cvs_params": {
            "leg_size": "medium",
            "logy": False,
            "grid": True
        },
        "hist_params": {
            "rebin": -1,
            "x_title": "#phi(j2)",
            "y_title": "Events",
            "ratio_title" : "x/Default",
            "error_range": [0.5, 1.5],
        },
        "info_params": {
            "info": "Normed to #it{L}_{int} = 150 fb^{-1}",
            "cms_text": "CMS",
            "extra_text": "Preliminary"
        }
    },
    "nJets": {
        "cvs_params": {
            "leg_size": "medium",
            "logy": False,
            "grid": True
        },
        "hist_params": {
            "rebin": -1,
            "x_title": "N(j)",
            "y_title": "Events",
            "ratio_title" : "x/Default",
            "error_range": [0.5, 1.5],
        },
        "info_params": {
            "info": "Normed to #it{L}_{int} = 150 fb^{-1}",
            "cms_text": "CMS",
            "extra_text": "Preliminary"
        }
    },
}
