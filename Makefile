all:
	g++ -I./src/include -L./src/lib -o golf2 main.cpp classes/ball/ball.cpp classes/hole/hole.cpp -lmingw32 -lSDL2main -lSDL2
