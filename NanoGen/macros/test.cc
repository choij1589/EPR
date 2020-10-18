#include "Particle.h"
#include "LHEPart.h"

void test() {
	// Initialize
	TString path_mc = "${PWD}/../dyellell01j_4f_NLO_FXFX.root";
	TFile f(path_mc);
	TFile f_out("out.root", "recreate");
	
	// ttree
	auto tr = (TTree*)f.Get("Events");
	unsigned int nEntry = tr->GetEntries();
	unsigned int nGenJet = 0; tr->SetBranchAddress("nGenJet", &nGenJet);
	unsigned int nGenJetAK8 = 0; tr->SetBranchAddress("nGenJetAK8", &nGenJetAK8);
	unsigned int nLHEPart = 0; tr->SetBranchAddress("nLHEPart", &nLHEPart);
	float GenJet_pt[28]; tr->SetBranchAddress("GenJet_pt", &GenJet_pt);
	float GenJet_eta[28]; tr->SetBranchAddress("GenJet_eta", &GenJet_eta);
	float GenJet_phi[28]; tr->SetBranchAddress("GenJet_phi", &GenJet_phi);
	float GenJet_mass[28]; tr->SetBranchAddress("GenJet_mass", &GenJet_mass);
	float LHEPart_pt[28]; tr->SetBranchAddress("LHEPart_pt", &LHEPart_pt);
	float LHEPart_eta[28]; tr->SetBranchAddress("LHEPart_eta", &LHEPart_eta);
	float LHEPart_phi[28]; tr->SetBranchAddress("LHEPart_phi", &LHEPart_phi);
	float LHEPart_mass[28]; tr->SetBranchAddress("LHEPart_mass", &LHEPart_mass);
	int LHEPart_pdgId[28]; tr->SetBranchAddress("LHEPart_pdgId", &LHEPart_pdgId);
	
	// histograms
	TH1D* h_mass = new TH1D("Z_mass", "", 200, 0., 200.);
	TH1D* h_pt = new TH1D("Z_pt", "", 200, 0., 200.);
	TH1D* h_leading_l_pt = new TH1D("leading_l_pt", "", 200, 0., 200.);
	TH1D* h_leading_l_eta = new TH1D("leading_l_eta", "", 160, -8., 8.);

	// Loop for entries
	for (int entry = 0; entry < nEntry; entry++) {
		if (entry%1000 == 0)
			cout << "entry: " << entry << endl;
		tr->GetEntry(entry);
		
		// now make a jet collection
		vector<Particle> genjets;
		vector<LHEPart> LHEParts;
		for (unsigned int i = 0; i < nGenJet; i++) {
			genjets.push_back(Particle(GenJet_pt[i], GenJet_eta[i], GenJet_phi[i], GenJet_mass[i]));
			//cout << genjets.at(i).Pt() << endl;
		}

		// and LHE collection
		for (unsigned int i = 0; i < nLHEPart; i++) {
			LHEParts.push_back(LHEPart(LHEPart_pt[i], LHEPart_eta[i], LHEPart_phi[i], LHEPart_mass[i], LHEPart_pdgId[i]));
			//cout << LHEParts.at(i).Pt() << endl;
		}

		// match GenJets to LHE particles
		vector<Particle> matched_jets;
		for (const auto& genjet: genjets) {
			for (const auto& lhe : LHEParts) {
				float dR = genjet.DeltaR(lhe);
				bool isLepton = false;
				if (abs(lhe.Pdgid()) == 11 || abs(lhe.Pdgid()) == 13)
					isLepton = true;
				if (dR < 0.4 && isLepton)
					matched_jets.push_back(genjet);
			}
		}
		if (matched_jets.size() != 2) continue;
		auto ZCand = matched_jets.at(0).P4() + matched_jets.at(1).P4();
		auto ZMass = ZCand.M();
		auto ZPt = ZCand.Pt();
		//if (!(60. < mass && mass < 120.))
		//	cout << mass << endl;
		h_mass->Fill(ZMass);
		h_pt->Fill(ZPt);
		h_leading_l_pt->Fill(matched_jets.at(0).Pt());
		h_leading_l_eta->Fill(matched_jets.at(0).Eta());
		
	}

	// finalize
	f_out.cd();
	h_mass->Write();
	h_pt->Write();
	h_leading_l_pt->Write();
	h_leading_l_eta->Write();
	f_out.Close();
}
