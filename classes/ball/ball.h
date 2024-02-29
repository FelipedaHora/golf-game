#ifndef BALL_H
#define BALL_H

#include "gameObject.h"

class Ball : public GameObject {
public:
    Ball(int x, int y, int radius);

    void draw(SDL_Renderer* renderer) const override;
    void update() override;

private:
    int radius;
};

#endif // BALL_H
