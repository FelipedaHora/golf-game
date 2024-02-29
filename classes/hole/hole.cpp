#include "hole.h"

Hole::Hole(int x, int y, int size) : GameObject(x, y), size(size) {}

void Hole::draw(SDL_Renderer* renderer) const {
    // Lógica para desenhar o buraco no renderer
}

void Hole::update() {
    // Lógica para atualizar o estado do buraco, se necessário
}
