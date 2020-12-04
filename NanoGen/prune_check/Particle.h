#ifndef Particle_h__
#define Particle_h__

class Particle {
private:
	TLorentzVector p4;
public:
	Particle(const float &pt, const float &eta, const float &phi, const float &mass) {
		p4.SetPtEtaPhiM(pt, eta, phi, mass);
	}
	~Particle() {};

	float Pt() const { return p4.Pt(); }
    float Eta() const { return p4.Eta(); }
    float Phi() const { return p4.Phi(); }
    float M() const { return p4.M(); }
    float E() const { return p4.E(); }
    TLorentzVector P4() const { return  p4; }

    float DeltaR(const Particle& part) const {
        return p4.DeltaR(part.P4());
    }
};

class GenPart : public Particle {
private:
	int __pdgid;
	int __motherIdx;
	int __status;
	int __statusFlag;
public:
	GenPart(const float &pt, const float &eta, const float &phi, const float &mass,
			const int &pid, const int &motherIdx, const int &status,
			const int &statusFlag) 
		: Particle(pt, eta, phi, mass), 
		__pdgid(pid), __motherIdx(motherIdx), __status(status), __statusFlag(statusFlag) {}
    int Pdgid() const { return __pdgid; }
	int MotherIdx() const { return __motherIdx; }
	int Status() const { return __status; }
	int StatusFlag() const { return __statusFlag; }
};

#endif
