from ROOT import TCanvas, TLegend, TPad, TH1

class plotterBase:
    # constructor
    def __init__(self, cvs_type="normal", logy=False):
        # normal, ratio
        self.cvs_type = cvs_type
        if self.cvs_type == "normal":
            self.cvs = TCanvas("cvs", "", 500, 500)
            self.legend = TLegend(0.69, 0.65, 0.90, 0.90)
            self.logy = logy
        elif self.cvs_type == "ratio":
            self.cvs = TCanvas("cvs", "", 720, 800)
            self.pad_up = TPad("pad_up", "", 0, 0.25, 1, 1)
            self.pad_down = TPad("pad_down", "", 0, 0, 1, 0.25)
            self.legend = TLegend(0.69, 0.65, 0.95, 0.92)
        else:
            raise(NameError)
        
    def get_hists(self, hists_data={}, hists_exp={}, rebin=-1):
        self.hists_data = {}
        self.hists_exp = {}
        self.hists_data = hists_data
        self.hists_exp = hists_exp

        if rebin == -1:
            pass
        else:
            for name, hist in self.hists_data.items():
                hist.Rebin(rebin)
            for name, hist in self.hists_exp.items():
                hist.Rebin(rebin)

    def decorate(self, deco_type="none", x_title="", y_title="", x_max=-1.):
        # none, normalize, ratio
        self.decos_data = {}
        self.decos_exp = {}
        
        if deco_type == "none":
            # TODO: make function for default deco_type
            color = 2

            y_range = -1.
            for name, hist in self.hists_exp.items():
                this_y_range = hist.GetMaximum()
                if y_range < this_y_range:
                    y_range = this_y_range
            
            for name, hist in self.hists_exp.items():
                h = hist.Clone("clone_" + name)
                h.SetLineColor(color)
                color += 1

                if x_max == -1.:
                    pass
                else:
                    h.GetXaxis().SetRangeUser(0, x_max)
                
                #y_range = h.GetMaximum()
                h.GetYaxis().SetRangeUser(0, y_range*1.3)
                if self.logy:
                    h.GetYaxis().SetRangeUser(1, y_range*10)

                h.SetStats(0)

                self.decos_exp[name] = h
                self.legend.AddEntry(h, name, "lep")

        elif deco_type == "normalize":
            # TODO: hists_data decoration setup
            color = 2

            # get y_range
            y_range = -1.
            for name, hist in self.hists_exp.items():
                scale_factor = 1. / hist.Integral()
                hist.Scale(scale_factor)

                this_y_range = hist.GetMaximum()
                if y_range < this_y_range:
                    y_range = this_y_range

            for name, hist in self.hists_exp.items():
                #print(name, type(hist))
                h = hist.Clone("clone_" + name)
                
                # scale histogram
                #scale_factor = 1. / h.Integral()
                #h.Scale(scale_factor)

                # set color
                h.SetLineColor(color)
                color += 1
                
                # x range
                if x_max == -1.:
                    pass
                else:
                    h.GetXaxis().SetRangeUser(0, x_max)
                # y range
                #y_range = h.GetMaximum()
                h.GetYaxis().SetRangeUser(0, y_range*1.3)
                if self.logy:
                    h.GetYaxis().SetRangeUser(1, y_range*10)
                
                # StatBox
                h.SetStats(0)

                # set title
                h.GetXaxis().SetTitle(x_title)
                h.GetYaxis().SetTitle(y_title)
                h.GetYaxis().SetTitleOffset(0.8)
                
                self.decos_exp[name] = h
                self.legend.AddEntry(h, name, "lep")
                
        elif deco_type == "ratio":
            # TODO: ratio setup
            pass
        else:
            raise(NameError)

    def canvas(self, deco_type="normalize", x_title="", y_title="", x_max=-1.):
        self.decorate(deco_type, x_title, y_title, x_max)
        self.cvs.SetGrid(1)
        self.cvs.cd()
        if self.cvs_type == "normal":
            for name, hist in self.decos_data.items():
                # TO DO
                continue
            for name, hist in self.decos_exp.items():
                hist.Draw("hist&same")
            self.legend.Draw("same")
        elif self.cvs_type == "ratio":
            pass
        else:
            raise(NameError)

        return self.cvs