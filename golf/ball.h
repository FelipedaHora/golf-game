// Ball.h
#ifndef BALL_H
#define BALL_H

#include "gameObject.h"
#include <SDL.h>
#include "box2d/box2d.h"

class Ball : public GameObject {
public:
    Ball(int x, int y, int radius);

    void draw(SDL_Renderer* renderer) const override;
    void update() override;
    void move(int dx, int dy);

private:
    int radius;
};

#endif // BALL_H
