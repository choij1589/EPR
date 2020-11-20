from ROOT import TCanvas, TLegend, TPad, TLatex


class plotterBase:
    def __init__(self, cvs_type="default", leg_size="medium", logy=False, grid=False):
        # store information
        self.cvs_type = cvs_type
        self.leg_size = leg_size
        self.logy = logy
        self.grid = grid

        # set info and logo
        self.__set_info()
        self.__set_logo()

        # set canvas and legend
        self.__set_canvas(cvs_type, logy, grid)
        self.__set_legend(leg_size)

    # getter
    # this will be
    def cvs(self):
        return self.cvs

    def pad_up(self):
        return self.pad_up

    def pad_down(self):
        return self.pad_down

    def legend(self):
        return self.legend

    def info(self):
        return self.info

    def logo(self):
        return self.logo

    def extra_logo(self):
        return self.extra_logo

    # private methods
    def __set_info(self):
        self.info = TLatex()
        self.info.SetTextSize(0.035)
        self.info.SetTextFont(42)

    def __set_logo(self):
        self.logo = TLatex()
        self.extra_logo = TLatex()
        self.logo.SetTextSize(0.04)
        self.logo.SetTextFont(61)
        self.extra_logo.SetTextSize(0.035)
        self.extra_logo.SetTextFont(52)

    def __set_canvas(self, cvs_type="default", logy=False, grid=False):
        if cvs_type == "default":
            self.cvs = TCanvas("cvs", "", 500, 500)
            if grid:
                self.cvs.SetGrid()
            if logy:
                self.cvs.SetLogy()
        elif cvs_type == "ratio":
            self.cvs = TCanvas("cvs", "", 504, 560)
            self.pad_up = TPad("pad_up", "", 0, 0.25, 1, 1)
            self.pad_up.SetBottomMargin(0.02)
            if grid:
                self.pad_up.SetGrid()
            if logy:
                self.pad_up.SetLogy()

            self.pad_down = TPad("pad_down", "", 0, 0, 1, 0.25)
            self.pad_down.SetGrid(1)
            self.pad_down.SetTopMargin(0.08)
            self.pad_down.SetBottomMargin(0.3)
        else:
            print("WARNING: No matched canvas type %s", cvs_type)
            print("Set the canvas type as default")
            self.__set_canvas(self, cvs_type="default", logy=logy)

    def __set_legend(self, leg_size="medium"):
        if leg_size == "small":
            self.legend = TLegend(0.69, 0.70, 0.90, 0.90)
        elif leg_size == "medium":
            self.legend = TLegend(0.69, 0.60, 0.90, 0.90)
        elif leg_size == "large":
            self.legend = TLegend(0.50, 0.60, 0.90, 0.90)
        else:
            print("wrong legend size...modify leg_size")
            #print("Set the legend size as medium")
            #self.__legend(self, leg_size="medium")

    # methods
    def save(self, path):
        self.cvs.SaveAs(path)

# HOWTO
### dist = KinematicDistribution()
# dist


class KinematicDistribution(plotterBase):
    def __init__(self, cvs_params={}):
        leg_size = cvs_params["leg_size"]
        logy = cvs_params["logy"]
        grid = cvs_params["grid"]
        super().__init__(cvs_type="ratio", leg_size=leg_size, logy=logy, grid=grid)

    def get_hists(self, hists={}, hist_params={}):
        base_hist = hist_params["base_hist"]
        rebin = hist_params["rebin"]

        self.hists = {}
        self.ratio = {}

        print("INFO: Scale of histograms are normalizaed automatically")

        # store histograms first
        for name, hist in hists.items():
            scale = hist.Integral()
            hist.Scale(1./scale)
            if rebin == -1:
                pass
            else:
                hist.Rebin(rebin)
            self.hists[name] = hist

        # now make ratio plots
        for name, hist in self.hists.items():
            ratio = hist.Clone("ratio_" + name)
            if base_hist is None:
                print("INFO: No base histogram is set")
                ratio.Divide(self.hists[name])
            else:
                ratio.Divide(self.hists[base_hist])
            self.ratio[name] = ratio

        # now decorate the plots
        self.__decorate_hists(hist_params)
        self.__decorate_ratio(hist_params)

    def combine(self, info_params):
        info = info_params["info"]
        cmsText = info_params["cms_text"]
        extraText = info_params["extra_text"]

        super().pad_up().cd()
        for name, hist in self.hists.items():
            hist.Draw("same")
        super().legend().Draw()
        super().info().DrawLatexNDC(0.72, 0.91, info)
        super().logo().DrawLatexNDC(0.15, 0.83, cmsText)
        super().extra_logo().DrawLatexNDC(0.15, 0.78, extraText)

        super().pad_down().cd()
        for name, ratio in self.ratio.items():
            ratio.Draw("same")

        super().cvs().cd()
        super().pad_up().Draw()
        super().pad_down().Draw()

    def draw(self):
        super().cvs().Draw()

    # private methods
    def __decorate_hists(self, hist_params):
        y_title = hist_params["y_title"]
        __color = 2

        # get y axis scale
        y_range = -1.
        for name, hist in self.hists.items():
            this_max = hist.GetMaximum()
            if y_range < this_max:
                y_range = this_max

        for name, hist in self.hists.items():
            hist.SetStats(0)

            # line color
            hist.SetLineColor(__color)
            hist.SetLineWidth(2)
            __color += 1

            # x axis
            hist.GetXaxis().SetLabelSize(0)

            # y axis
            hist.GetYaxis().SetTitle(y_title)
            hist.GetYaxis().SetTitleSize(0.05)
            hist.GetYaxis().SetTitleOffset(0.8)
            hist.GetYaxis().SetTitleSize(0.05)
            hist.GetYaxis().SetLabelSize(0.03)
            if self.logy:
                hist.GetYaxis().SetRangeUser(1., y_range*10.)
            else:
                hist.GetYaxis().SetRangeUser(0., y_range*1.3)

            super().legend().AddEntry(hist, name, "lep")

    def __decorate_ratio(self, hist_params):
        error_range = hist_params["error_range"]
        x_title = hist_params["x_title"]
        ratio_title = hist_params["ratio_title"]
        __color = 2

        for name, ratio in self.ratio.items():
            ratio.SetStats(0)
            ratio.SetLineColor(__color)
            ratio.SetTitleSize(0.)
            ratio.SetTitle("")
            __color += 1

            # x axis
            ratio.GetXaxis().SetTitle(x_title)
            ratio.GetXaxis().SetTitleSize(0.1)
            ratio.GetXaxis().SetTitleOffset(1.)
            ratio.GetXaxis().SetLabelSize(0.08)
            ratio.GetXaxis().SetLabelOffset(0.02)

            # y axis
            ratio.GetYaxis().SetRangeUser(error_range[0], error_range[1])
            ratio.GetYaxis().SetTitle(ratio_title)
            ratio.GetYaxis().SetTitleSize(0.09)
            ratio.GetYaxis().SetTitleOffset(0.5)
            ratio.GetYaxis().SetLabelSize(0.08)
