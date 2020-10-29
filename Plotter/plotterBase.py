from ROOT import TCanvas, TLegend, TPad, TLatex


class plotterBase:
    def __init__(self, cvs_type, leg_size,  logy):
        self.make_canvas(cvs_type, leg_size, logy)

    # getter
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

    # methods
    def make_canvas(self, cvs_type="default", leg_size="medium", logy=False):
        # default, ratio, ROC...?
        self.info = TLatex()
        self.logo = TLatex()
        self.extra_logo = TLatex()

        # set information
        self.info.SetTextSize(0.035)
        self.info.SetTextFont(42)
        self.logo.SetTextSize(0.04)
        self.logo.SetTextFont(61)
        self.extra_logo.SetTextSize(0.035)
        self.extra_logo.SetTextFont(52)

        if cvs_type == "default":
            self.cvs = TCanvas("cvs", "", 500, 500)
            self.cvs.SetGrid(1)
            self.legend = TLegend(0.69, 0.65, 0.90, 0.90)
            if logy:
                self.cvs.SetLogy()

        elif cvs_type == "ratio":
            self.cvs = TCanvas("cvs", "", 504, 560)
            self.pad_up = TPad("pad_up", "", 0, 0.25, 1, 1)
            self.pad_up.SetBottomMargin(0.02)
            self.pad_up.SetGrid(1)
            if logy:
                self.pad_up.SetLogy()

            self.pad_down = TPad("pad_down", "", 0, 0, 1, 0.25)
            self.pad_down.SetGrid(1)
            self.pad_down.SetTopMargin(0.08)
            self.pad_down.SetBottomMargin(0.3)
            
			# leg size
            if leg_size == "small":
                self.legend = TLegend(0.69, 0.70, 0.90, 0.90)
            elif leg_size == "medium":
                self.legend = TLegend(0.69, 0.60, 0.90, 0.90)
            elif leg_size == "large":
                self.legend = TLegend(0.50, 0.60, 0.90, 0.90)
            else:
                print("wrong legend size...modify leg_size")
                raise(RuntimeError)

        else:
            raise(NameError)

    def save(self, path):
        self.cvs.SaveAs(path)


class kDistributions(plotterBase):
    def __init__(self, leg_size="medium", logy=False):
        super().__init__("ratio", leg_size, logy)
        self.logy = logy
        self.hists = {}
        self.ratio_hists = {}

    def get_hists(self, hists={}, scale="none", rebin=-1, x_axis_range=[0., -1.], y_axis_range=[0., -1.]):
        for name, hist in hists.items():
            h = hist.Clone("temp_" + name)
            self.hists[name] = h

        for name, hist in self.hists.items():
            if scale == "none":
                pass
            elif scale == "normalize":
                s = hist.Integral()
                if s != 0:
                    hist.Scale(1. / s)
                else:
                    print("total integral is 0... normalization will not work")
            else:
                raise(SyntaxError)

            if rebin == -1:
                pass
            else:
                hist.Rebin(rebin)
        
        y_range_max = self.automatic_y_range()
        for name, hist in self.hists.items():
            if x_axis_range[1] == -1.:
                pass
            else:
                hist.GetXaxis().SetRangeUser(x_axis_range[0], x_axis_range[1])

            if y_axis_range[1] == -1.:
                if self.logy:
                    hist.GetYaxis().SetRangeUser(1, y_range_max*10)
                else:
                    hist.GetYaxis().SetRangeUser(0, y_range_max*1.4)
            else:
                hist.GetYaxis().SetRangeUser(y_axis_range[0], y_axis_range[1])

    def automatic_y_range(self):
        out = -1.
        for name, hist in self.hists.items():
            this_max = hist.GetMaximum()
            if out < this_max:
                out = this_max
        return out
        
    def generate_ratio(self, base_name):
        for name, hist in self.hists.items():
            ratio = hist.Clone("ratio_" + name)
            ratio.Divide(self.hists[base_name])
            self.ratio_hists[name] = ratio

    def deco_hists(self, deco_type="central", scale_factor=1., y_title=""):
        # deco type: syst, central
        if deco_type == "central":
            color = 2

            for name, hist in self.hists.items():
                hist.SetStats(0)

            # decorate
            for name, hist in self.hists.items():
                hist.SetLineColor(color)
                color += 1

                # x axis
                hist.GetXaxis().SetLabelSize(0)

                # y axis
                hist.GetYaxis().SetTitle(y_title)
                hist.GetYaxis().SetTitleSize(0.05)
                hist.GetYaxis().SetTitleOffset(0.8)
                hist.GetYaxis().SetTitleSize(0.05)
                hist.GetYaxis().SetLabelSize(0.03)

                super().legend().AddEntry(hist, name, "lep")

    def deco_ratio(self, deco_type="central", error_range="medium", x_title="", y_title=""):
        if deco_type == "central":
            color = 2

            for name, ratio in self.ratio_hists.items():
                ratio.SetStats(0)
                ratio.SetLineColor(color)
                ratio.SetTitleSize(0.)
                ratio.SetTitle("")
                color += 1

                if error_range == "small":
                    ratio.GetYaxis().SetRangeUser(0.8, 1.2)
                elif error_range == "medium":
                    ratio.GetYaxis().SetRangeUser(0.5, 1.5)
                elif error_range == "large":
                    ratio.GetYaxis().SetRangeUser(0., 2.0)
                else:
                    raise(SyntaxError)

                # Xaxis
                ratio.GetXaxis().SetTitle(x_title)
                ratio.GetXaxis().SetTitleSize(0.1)
                ratio.GetXaxis().SetTitleOffset(1.)
                ratio.GetXaxis().SetLabelSize(0.08)
                ratio.GetXaxis().SetLabelOffset(0.02)

                # Yaxis
                ratio.GetYaxis().SetTitle(y_title)
                ratio.GetYaxis().SetTitleSize(0.09)
                ratio.GetYaxis().SetTitleOffset(0.5)
                ratio.GetYaxis().SetLabelSize(0.08)
                # ratio.GetXaxis().SetLable

    def combine(self, info="#it{L}_{int} = 35.9 fb^{-1}", cmsText="CMS", extraText="Preliminary"):
        super().pad_up().cd()
        for name, hist in self.hists.items():
            hist.Draw("same")
        super().legend().Draw()
        super().info().DrawLatexNDC(0.68, 0.92, info)
        super().logo().DrawLatexNDC(0.15, 0.83, cmsText)
        super().extra_logo().DrawLatexNDC(0.15, 0.78, extraText)

        super().pad_down().cd()
        for name, hist in self.ratio_hists.items():
            hist.Draw("same")

        super().cvs().cd()
        super().pad_up().Draw()
        super().pad_down().Draw()

    def draw(self):
        super().cvs().Draw()

# TO DO: make templates


class DataAndMC(plotterBase):
    pass


class Efficiency(plotterBase):
    pass


class ROC(plotterBase):
    pass
