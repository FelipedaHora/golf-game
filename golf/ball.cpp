// Ball.cpp
#include "Ball.h"

Ball::Ball(int x, int y, int radius) : GameObject(x, y), radius(radius) {}

void Ball::draw(SDL_Renderer* renderer) const {
    SDL_SetRenderDrawColor(renderer, 0xFF, 0xFF, 0xFF, 0xFF);

    for (int dy = -radius; dy <= radius; dy++) {
        for (int dx = -radius; dx <= radius; dx++) {
            if (dx * dx + dy * dy <= radius * radius) {
                SDL_RenderDrawPoint(renderer, x + dx, y + dy);
            }
        }
    }
}

void Ball::update() {
    
}

void Ball::move(int dx, int dy) {
    x += dx;
    y += dy;
}
