file_names = ["DYm50_012j_nlo_cp5_GridToNano",
              "DYm50_0j_nlo_cp5_GridToNano",
              "DYm50_1j_nlo_cp5_GridToNano",
              "DYm50_2j_nlo_cp5_GridToNano"]
option = "_prefsr"
observables = ["ZMass", "yZ", "ptZ", "phiZ", 
                "ptl1", "ptl2", "etal1", "etal2", "phil1", "phil2", "nLeptons",
                "ptj1", "ptj2", "etaj1", "etaj2", "phij1", "phij2", "nJets"]
lumi = 150. # fb^-1
weights = {
        "DYm50_012j_nlo_cp5_GridToNano" : 3.47162670E-03,
        "DYm50_0j_nlo_cp5_GridToNano" : 8.99246544E-04,
        "DYm50_1j_nlo_cp5_GridToNano" : 8.66583897E-04,
        "DYm50_2j_nlo_cp5_GridToNano" : 9.94959157E-04
}
output_path = "./test"
params = {
	# Z
    "ZMass": {
        "cvs_params": {
            "leg_size": "medium",
            "logy": False,
            "grid": False
        },
        "hist_params": {
            "rebin": 20,
            "x_title": "M(ll)",
            "y_title": "Events",
            "ratio_title": "x/Default",
            "error_range": [0.5, 1.5]
        },
        "info_params": {
            "info": "#it{L}_{int} = 150 fb^{-1}",
            "cms_text": "CMS",
            "extra_text": "Preliminary"
        }
    },
    "yZ": {
        "cvs_params": {
            "leg_size": "medium",
            "logy": False,
            "grid": False
        },
        "hist_params": {
            "rebin": -1,
            "x_title": "y^{Z}",
            "y_title": "Events", 
            "ratio_title" : "x/Default",
            "error_range": [0.5, 1.5],
        },
        "info_params": {
            "info": "#it{L}_{int} = 150 fb^{-1}",
            "cms_text": "CMS",
            "extra_text": "Preliminary"
        }
    },
	"ptZ": {
        "cvs_params": {
            "leg_size": "medium",
            "logy": False,
            "grid": False
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
            "info": "#it{L}_{int} = 150 fb^{-1}",
            "cms_text": "CMS",
            "extra_text": "Preliminary"
        }
    },
	"phiZ": {
        "cvs_params": {
            "leg_size": "medium",
            "logy": False,
            "grid": False
        },
        "hist_params": {
            "rebin": -1,
            "x_title": "#phi(Z)",
            "y_title": "Events",
            "ratio_title" : "x/Default",
            "error_range": [0.5, 1.5],
        },
        "info_params": {
            "info": "#it{L}_{int} = 150 fb^{-1}",
            "cms_text": "CMS",
            "extra_text": "Preliminary"
        }
    },
	# Leptons
	"ptl1": {
        "cvs_params": {
            "leg_size": "medium",
            "logy": False,
            "grid": False
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
            "info": "#it{L}_{int} = 150 fb^{-1}",
            "cms_text": "CMS",
            "extra_text": "Preliminary"
        }
    },
	"ptl2": {
        "cvs_params": {
            "leg_size": "medium",
            "logy": False,
            "grid": False
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
            "info": "#it{L}_{int} = 150 fb^{-1}",
            "cms_text": "CMS",
            "extra_text": "Preliminary"
        }
    },
	"etal1": {
        "cvs_params": {
            "leg_size": "medium",
            "logy": False,
            "grid": False
        },
        "hist_params": {
            "rebin": -1,
            "x_title": "#eta(l1)",
            "y_title": "Events",
            "ratio_title" : "x/Default",
            "error_range": [0.5, 1.5],
        },
        "info_params": {
            "info": "#it{L}_{int} = 150 fb^{-1}",
            "cms_text": "CMS",
            "extra_text": "Preliminary"
        }
    },
	"etal2": {
        "cvs_params": {
            "leg_size": "medium",
            "logy": False,
            "grid": False
        },
        "hist_params": {
            "rebin": -1,
            "x_title": "#eta(l2)",
            "y_title": "Events",
            "ratio_title" : "x/Default",
            "error_range": [0.5, 1.5],
        },
        "info_params": {
            "info": "#it{L}_{int} = 150 fb^{-1}",
            "cms_text": "CMS",
            "extra_text": "Preliminary"
        }
    },
	"phil1": {
        "cvs_params": {
            "leg_size": "medium",
            "logy": False,
            "grid": False
        },
        "hist_params": {
            "rebin": -1,
            "x_title": "#phi(l1)",
            "y_title": "Events",
            "ratio_title" : "x/Default",
            "error_range": [0.5, 1.5],
        },
        "info_params": {
            "info": "#it{L}_{int} = 150 fb^{-1}",
            "cms_text": "CMS",
            "extra_text": "Preliminary"
        }
    },
	"phil2": {
        "cvs_params": {
            "leg_size": "medium",
            "logy": False,
            "grid": False
        },
        "hist_params": {
            "rebin": -1,
            "x_title": "#phi(l2)",
            "y_title": "Events",
            "ratio_title" : "x/Default",
            "error_range": [0.5, 1.5],
        },
        "info_params": {
            "info": "#it{L}_{int} = 150 fb^{-1}",
            "cms_text": "CMS",
            "extra_text": "Preliminary"
        }
    },
	"nLeptons": {
        "cvs_params": {
            "leg_size": "medium",
            "logy": False,
            "grid": False
        },
        "hist_params": {
            "rebin": -1,
            "x_title": "N(l)",
            "y_title": "Events",
            "ratio_title" : "x/Default",
            "error_range": [0.5, 1.5],
        },
        "info_params": {
            "info": "#it{L}_{int} = 150 fb^{-1}",
            "cms_text": "CMS",
            "extra_text": "Preliminary"
        }
    },
    # Jets
    "ptj1": {
        "cvs_params": {
            "leg_size": "medium",
            "logy": False,
            "grid": False
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
            "info": "#it{L}_{int} = 150 fb^{-1}",
            "cms_text": "CMS",
            "extra_text": "Preliminary"
        }
    },
    "ptj2": {
        "cvs_params": {
            "leg_size": "medium",
            "logy": False,
            "grid": False
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
            "info": "#it{L}_{int} = 150 fb^{-1}",
            "cms_text": "CMS",
            "extra_text": "Preliminary"
        }
    },
    "etaj1": {
        "cvs_params": {
            "leg_size": "medium",
            "logy": False,
            "grid": False
        },
        "hist_params": {
            "rebin": -1,
            "x_title": "#eta(j1)",
            "y_title": "Events",
            "ratio_title" : "x/Default",
            "error_range": [0.5, 1.5],
        },
        "info_params": {
            "info": "#it{L}_{int} = 150 fb^{-1}",
            "cms_text": "CMS",
            "extra_text": "Preliminary"
        }
    },
    "etaj2": {
        "cvs_params": {
            "leg_size": "medium",
            "logy": False,
            "grid": False
        },
        "hist_params": {
            "rebin": -1,
            "x_title": "#eta(j2)",
            "y_title": "Events",
            "ratio_title" : "x/Default",
            "error_range": [0.5, 1.5],
        },
        "info_params": {
            "info": "#it{L}_{int} = 150 fb^{-1}",
            "cms_text": "CMS",
            "extra_text": "Preliminary"
        }
    },
    "phij1": {
        "cvs_params": {
            "leg_size": "medium",
            "logy": False,
            "grid": False
        },
        "hist_params": {
            "rebin": -1,
            "x_title": "#phi(j1)",
            "y_title": "Events",
            "ratio_title" : "x/Default",
            "error_range": [0.5, 1.5],
        },
        "info_params": {
            "info": "#it{L}_{int} = 150 fb^{-1}",
            "cms_text": "CMS",
            "extra_text": "Preliminary"
        }
    },
    "phij2": {
        "cvs_params": {
            "leg_size": "medium",
            "logy": False,
            "grid": False
        },
        "hist_params": {
            "rebin": -1,
            "x_title": "#phi(j2)",
            "y_title": "Events",
            "ratio_title" : "x/Default",
            "error_range": [0.5, 1.5],
        },
        "info_params": {
            "info": "#it{L}_{int} = 150 fb^{-1}",
            "cms_text": "CMS",
            "extra_text": "Preliminary"
        }
    },
    "nJets": {
        "cvs_params": {
            "leg_size": "medium",
            "logy": False,
            "grid": False
        },
        "hist_params": {
            "rebin": -1,
            "x_title": "N(j)",
            "y_title": "Events",
            "ratio_title" : "x/Default",
            "error_range": [0.5, 1.5],
        },
        "info_params": {
            "info": "#it{L}_{int} = 150 fb^{-1}",
            "cms_text": "CMS",
            "extra_text": "Preliminary"
        }
    },
}
