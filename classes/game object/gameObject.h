#ifndef GAMEOBJECT_H
#define GAMEOBJECT_H

#include <SDL.h>

class GameObject {
public:
    GameObject(int x, int y);
    virtual ~GameObject() {}

    virtual void draw(SDL_Renderer* renderer) const = 0;
    virtual void update() = 0;

protected:
    int x;
    int y;
};

#endif // GAMEOBJECT_H
