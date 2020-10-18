#ifndef LHEPart_h__
#define LHEPart_h__
#include "Particle.h"

class LHEPart : public Particle {
private:
	int pdgid;
public:
	LHEPart(const float &pt, const float &eta, const float &phi, const float &mass, const unsigned int &pid) : Particle(pt, eta, phi, mass), pdgid(pid) {
	}
	int Pdgid() const { return pdgid; };
};

#endif
