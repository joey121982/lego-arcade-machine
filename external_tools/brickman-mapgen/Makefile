build:
	g++ main.cpp imgui/*.cpp imgui/backends/*.cpp -Iimgui -Ibackends -lglfw -lGL -ldl -lpthread -lX11 -lXrandr -lXi -o bin/bmmgen

clean:
	rm -rf bin/* imgui.ini

run:
	./bin/bmmgen

brun:
	make clean
	make build
	./bin/bmmgen