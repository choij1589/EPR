from ROOT import TCanvas, TLegend, TPad, THStack, TLatex


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
    def draw(self):
        self.cvs.Draw()

    def save(self, path):
        self.cvs.SaveAs(path)
        self.cvs.Close()

# Comparing binned-samples and inclusive samples
class BinnedAndIncl(plotterBase):
    def __init__(self, cvs_params):
        leg_size = cvs_params["leg_size"]
        logy = cvs_params["logy"]
        grid = cvs_params["grid"]
        super().__init__(cvs_type="ratio", leg_size=leg_size, logy=logy, grid=grid)

    def get_hists(self, hist_incl, hists_binned, hist_params):
        rebin = hist_params["rebin"]
        self.hist_incl = None
        self.hists_binned = {}
        self.stack = THStack("stack", "")
        self.syst = None
        self.ratio = None
        self.ratio_syst = None

        # Store histograms
        print("INFO: Storing histograms...")
        print("INFO: histograms automatically normalized to L = 150 fb^-1")
        self.hist_incl = self.__rebin(hist_incl, hist_params)
        for name, hist in hists_binned.items():
            self.hists_binned[name] = self.__rebin(hist, hist_params)

        self.__decorate_hists(hist_params)
        self.__make_stack_and_syst()
        self.__make_ratio(hist_params)

    def combine(self, info_params):
        info = info_params["info"]
        cmsText = info_params["cms_text"]
        extraText = info_params["extra_text"]

        super().pad_up().cd()
        self.hist_incl.Draw("p&hist")
        self.stack.Draw("hist & pfc & same")
        self.syst.Draw("e2 & f & same")
        self.hist_incl.Draw("p&hist&same")
        self.hist_incl.Draw("e1 & same")

        super().legend().Draw()
        super().info().DrawLatexNDC(0.63, 0.91, info)
        super().logo().DrawLatexNDC(0.15, 0.83, cmsText)
        super().extra_logo().DrawLatexNDC(0.15, 0.78, extraText)

        super().pad_down().cd()
        self.ratio.Draw("p & hist")
        self.ratio_syst.Draw("e2&f&same")

        super().cvs().cd()
        super().pad_up().Draw()
        super().pad_down().Draw()

    def __rebin(self, hist, hist_params):
        rebin = hist_params["rebin"]
        if rebin == -1:
            pass
        else:
            hist.Rebin(rebin)
        if "x_range" in hist_params.keys():
            x_range = hist_params["x_range"]
            hist.GetXaxis().SetRangeUser(x_range[0], x_range[1])
        return hist

    def __decorate_hists(self, hist_params):
        y_title = hist_params["y_title"]

        # y axis scale is just the Maximum of inclusive sample
        print("INFO: y axis range set to be maximum of inclusive plot...")
        y_range = self.hist_incl.GetMaximum()

        # decorate self.hist_incl
        self.hist_incl.SetStats(0)
        self.hist_incl.SetMarkerStyle(8)
        self.hist_incl.SetMarkerSize(0.5)
        self.hist_incl.SetMarkerColor(1)

        # X axis
        self.hist_incl.GetXaxis().SetLabelSize(0)

        # Y axis
        self.hist_incl.GetYaxis().SetTitle(y_title)
        self.hist_incl.GetYaxis().SetRangeUser(0., y_range*1.2)
        if self.logy:
            self.hist_incl.GetYaxis().SetRangeUser(1., y_range*100.)

        for name, hist in self.hists_binned.items():
            hist.GetXaxis().SetLabelSize(0)

        # add to legend
        super().legend().AddEntry(self.hist_incl, "Incl", "lep")

    def __make_stack_and_syst(self):
        print("WARNING: Make sure that histograms are properly scaled")
        for name, hist in self.hists_binned.items():
            hist.GetXaxis().SetLabelSize(0)
            self.stack.Add(hist)
            super().legend().AddEntry(hist, name, "f")

            if self.syst == None:
                self.syst = hist.Clone("syst")
            else:
                self.syst.Add(hist)

        self.stack.Draw()
        self.stack.GetHistogram().GetXaxis().SetLabelSize(0)
        self.syst.SetStats(0)
        self.syst.SetFillColorAlpha(12, 0.6)
        self.syst.SetFillStyle(3144)
        self.syst.GetXaxis().SetLabelSize(0)
        super().legend().AddEntry(self.syst, "stat err", "f")

    def __make_ratio(self, hist_params):
        error_range = hist_params["error_range"]
        x_title = hist_params["x_title"]

        self.ratio = self.hist_incl.Clone("ratio")
        self.ratio.Divide(self.syst)
        self.ratio_syst = self.ratio.Clone("ratio_syst")

        self.ratio.SetStats(0)
        self.ratio.SetTitle("")
        # y axis
        self.ratio.GetYaxis().SetRangeUser(error_range[0], error_range[1])
        self.ratio.GetYaxis().SetTitle("Incl / binned")
        self.ratio.GetYaxis().SetTitleSize(0.08)
        self.ratio.GetYaxis().SetTitleOffset(0.5)
        self.ratio.GetYaxis().SetLabelSize(0.08)
        # x axis
        self.ratio.GetXaxis().SetTitle(x_title)
        self.ratio.GetXaxis().SetTitleSize(0.1)
        self.ratio.GetXaxis().SetTitleOffset(0.8)
        self.ratio.GetXaxis().SetLabelSize(0.08)

        self.ratio_syst.SetStats(0)
        self.ratio_syst.SetFillColorAlpha(12, 0.6)
        self.ratio_syst.SetFillStyle(3144)


# Comparing normalized distributions b/w observables
# e.g samples with different setup (e.g. years...)
class Kinematics(plotterBase):
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

            if "x_range" in hist_params.keys():
                x_range = hist_params["x_range"]
                hist.GetXaxis().SetRangeUser(x_range[0], x_range[1])
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
            hist.Draw("same&plc")
        super().legend().Draw()
        super().info().DrawLatexNDC(0.72, 0.91, info)
        super().logo().DrawLatexNDC(0.15, 0.83, cmsText)
        super().extra_logo().DrawLatexNDC(0.15, 0.78, extraText)

        super().pad_down().cd()
        for name, ratio in self.ratio.items():
            ratio.Draw("same&plc")

        super().cvs().cd()
        super().pad_up().Draw()
        super().pad_down().Draw()

    def draw(self):
        super().cvs().Draw()

    # private methods
    def __decorate_hists(self, hist_params):
        y_title = hist_params["y_title"]

        # get y axis scale
        y_range = -1.
        for name, hist in self.hists.items():
            this_max = hist.GetMaximum()
            if y_range < this_max:
                y_range = this_max

        for name, hist in self.hists.items():
            hist.SetStats(0)

            # line color
            hist.SetLineWidth(2)

            # x axis
            hist.GetXaxis().SetLabelSize(0)

            # y axis
            hist.GetYaxis().SetTitle(y_title)
            hist.GetYaxis().SetTitleSize(0.05)
            hist.GetYaxis().SetTitleOffset(0.8)
            hist.GetYaxis().SetTitleSize(0.05)
            hist.GetYaxis().SetLabelSize(0.03)
            if self.logy:
                hist.GetYaxis().SetRangeUser(1., y_range*100.)
            else:
                hist.GetYaxis().SetRangeUser(0., y_range*1.3)

            super().legend().AddEntry(hist, name, "lep")

    def __decorate_ratio(self, hist_params):
        error_range = hist_params["error_range"]
        x_title = hist_params["x_title"]
        ratio_title = hist_params["ratio_title"]

        for name, ratio in self.ratio.items():
            ratio.SetStats(0)
            ratio.SetTitleSize(0.)
            ratio.SetTitle("")

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
