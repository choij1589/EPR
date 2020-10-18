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

#endif
