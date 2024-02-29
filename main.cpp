#include <iostream>
#include <SDL2/SDL.h>
#include <hole.h>
#include <ball.h>

const int SCREEN_WIDTH = 800;
const int SCREEN_HEIGHT = 600;

SDL_Window* gWindow = nullptr;
SDL_Renderer* gRenderer = nullptr;

bool initializeSDL() {
    if (SDL_Init(SDL_INIT_VIDEO) < 0) {
        std::cerr << "SDL could not initialize! SDL_Error: " << SDL_GetError() << std::endl;
        return false;
    }

    gWindow = SDL_CreateWindow("Golf Game", SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED, SCREEN_WIDTH, SCREEN_HEIGHT, SDL_WINDOW_SHOWN);
    if (gWindow == nullptr) {
        std::cerr << "Window could not be created! SDL_Error: " << SDL_GetError() << std::endl;
        return false;
    }

    gRenderer = SDL_CreateRenderer(gWindow, -1, SDL_RENDERER_ACCELERATED);
    if (gRenderer == nullptr) {
        std::cerr << "Renderer could not be created! SDL_Error: " << SDL_GetError() << std::endl;
        return false;
    }

    SDL_SetRenderDrawColor(gRenderer, 255, 255, 255, 255);
    SDL_RenderClear(gRenderer);

    return true;
}

void closeSDL() {
    SDL_DestroyRenderer(gRenderer);
    SDL_DestroyWindow(gWindow);
    SDL_Quit();
}

int main() {
    if (!initializeSDL()) {
        return 1;
    }

    Ball ball(50, 50, 10);
    Hole hole(200, 200, 15);

    bool isRunning = true;
    SDL_Event event;

    while (isRunning) {
        while (SDL_PollEvent(&event) != 0) {
            if (event.type == SDL_QUIT) {
                isRunning = false;
            }
        }

        ball.update();
        hole.update();

        SDL_SetRenderDrawColor(gRenderer, 255, 255, 255, 255);
        SDL_RenderClear(gRenderer);

        ball.draw(gRenderer);
        hole.draw(gRenderer);

        SDL_RenderPresent(gRenderer);
    }

    closeSDL();
    return 0;
}
