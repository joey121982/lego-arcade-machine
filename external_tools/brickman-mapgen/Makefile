build:
	rm -rf bin
	mkdir bin
	g++ main.cpp \
		imgui/*.cpp \
		imgui/backends/imgui_impl_glfw.cpp \
		imgui/backends/imgui_impl_opengl3.cpp \
		-Iimgui -Ibackends -lglfw -lGL -ldl -lpthread -lX11 -lXrandr -lXi -o bin/bmmgen
	mkdir maps

clean:
	rm -rf bin/* imgui.ini

run:
	./bin/bmmgen

brun:
	make clean
	make build
	make run