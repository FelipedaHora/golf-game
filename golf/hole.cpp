#include "Hole.h"

Hole::Hole(int x, int y, int size) : GameObject(x, y), size(size) {}

void Hole::draw(SDL_Renderer* renderer) const {
    // L�gica para desenhar o buraco no renderer
}

void Hole::update() {
    // L�gica para atualizar o estado do buraco, se necess�rio
}
