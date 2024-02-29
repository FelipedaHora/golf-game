#ifndef HOLE_H
#define HOLE_H

#include <gameObject.h>

class Hole : public GameObject {
public:
    Hole(int x, int y, int size);

    void draw(SDL_Renderer* renderer) const override;
    void update() override;

private:
    int size;
};

#endif // HOLE_H
