#include "Particle.h"
using namespace std;

void test() {
	//TFile* f_ul = new TFile("DYm50_nlo_cp5_MiniToNano_UL.root");
	TFile* f_prune = new TFile("DYm50_012j_nlo_cp5_prune.root");
	TFile* f_out = new TFile("f_out_prune.root", "recreate");

	// histograms to store number of particles
	TH1D* h_nGens = new TH1D("h_nGens", "", 150, 0., 150.);
	TH1D* h_nElectrons = new TH1D("h_nElectrons", "", 20, 0., 20.);
	TH1D* h_nMuons = new TH1D("h_nMuons", "", 20, 0., 20.);
	TH1D* h_nPhotons = new TH1D("h_nPhotons", "", 20, 0., 20.);

	// Set branch address	
	auto tr = (TTree*)f_prune->Get("Events");
	unsigned int nEntry = tr->GetEntries();
	unsigned int nGenPart; tr->SetBranchAddress("nGenPart", &nGenPart);
	float GenPart_pt[28]; tr->SetBranchAddress("GenPart_pt", &GenPart_pt);
	float GenPart_eta[28]; tr->SetBranchAddress("GenPart_eta", &GenPart_eta);
	float GenPart_phi[28]; tr->SetBranchAddress("GenPart_phi", &GenPart_phi);
	float GenPart_mass[28]; tr->SetBranchAddress("GenPart_mass", &GenPart_mass);
	int GenPart_pdgId[28]; tr->SetBranchAddress("GenPart_pdgId", &GenPart_pdgId);
	int GenPart_genPartIdxMother[28]; tr->SetBranchAddress("GenPart_genPartIdxMother", &GenPart_genPartIdxMother);
	int GenPart_status[28]; tr->SetBranchAddress("GenPart_status", &GenPart_status);
	int GenPart_statusFlags[28]; tr->SetBranchAddress("GenPart_statusFlags", &GenPart_statusFlags);

	// Loop over entries
	vector<GenPart> gens;
	vector<GenPart> electrons, muons, photons;
	for (unsigned int entry = 0; entry < nEntry; entry++) {
		gens.clear();
		electrons.clear();
		muons.clear();
		photons.clear();

		tr->GetEntry(entry);
		
		//if (entry%1000 == 0)
		//	cout << "==== entry: " << entry << " ====" << endl;
		// make collections
		for (unsigned int i = 0; i < nGenPart; i++) {
			GenPart part = GenPart(GenPart_pt[i], GenPart_eta[i], GenPart_phi[i], GenPart_mass[i],
					GenPart_pdgId[i], GenPart_genPartIdxMother[i],
					GenPart_status[i], GenPart_statusFlags[i]);

			bool isElectron = abs(part.PdgId()) == 11;
			bool isMuon = abs(part.PdgId()) == 13;
			bool isPhoton = abs(part.PdgId()) == 22;

			gens.emplace_back(part);
			if (isElectron)
				electrons.emplace_back(part);
			if (isMuon)
				muons.emplace_back(part);
			if (isPhoton)
				photons.emplace_back(part);

			//if (entry%1000 == 0) {
			//	cout << gens.at(i).PdgId() << endl;
			//	cout << gens.at(i).Pt() << endl;
			//	cout << gens.at(i).Eta() << endl;
			//}
		}
		
		h_nGens->Fill(gens.size());
		h_nElectrons->Fill(electrons.size());
		h_nMuons->Fill(muons.size());
		h_nPhotons->Fill(photons.size());
		if (entry%1000 == 0) {
			cout << "==== entry: " << entry << " ====" << endl;
			cout << "All gens: " << gens.size() << endl;
			cout << "Electrons: " << electrons.size() << endl;
			cout << "Muons: " << muons.size() << endl;
			cout << "Photons: " << photons.size() << endl;
		}
	}

	f->Close();
	f_out->cd();
	h_nGens->Write();
	h_nElectrons->Write();
	h_nMuons->Write();
	h_nPhotons->Write();
	f_prune->Close();
	f_out->Close();
}
