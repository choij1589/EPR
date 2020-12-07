#include "Particle.h"
using namespace std;

void test() {
	TFile* f = new TFile("DYm50_nlo_cp5_MiniToNano_UL.root");
	// Set branch address	
	auto tr = (TTree*)f->Get("Events");
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
		for (unsigned int i = 0; i < nGenPart; i++) {
			gens.push_back(GenPart(GenPart_pt[i], GenPart_eta[i], GenPart_phi[i], GenPart_mass[i],
						GenPart_pdgId[i], GenPart_genPartIdxMother[i],
						GenPart_status[i], GenPart_statusFlags[i]));
			if (entry%1000 == 0) {
				cout << gens.at(i).Pt() << endl;
				cout << gens.at(i).Eta() << endl;
			}
		}
	}

	f->Close();
}
