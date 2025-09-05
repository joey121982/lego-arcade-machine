/**
 * @name Brickman Map Generator
 * @author joey
 * @brief external tool made to aid in quickly building maps
 * @version 1.0
 */


#include <iostream>
#include <fstream>
#include <vector>
#include <GLFW/glfw3.h>

#include "json.hpp" // json.hpp by nlohmann: https://github.com/nlohmann/json
#include "imgui.h" // https://github.com/ocornut/imgui
#include "backends/imgui_impl_glfw.h"
#include "backends/imgui_impl_opengl3.h"

const int rows = 9;
const int cols = 16;
std::vector<std::vector<int>> maze(rows, std::vector<int>(cols, 0));

int player_x = 0;
int player_y = 0;
char filename[256];

int main() {
    glfwInit();
    GLFWwindow* window = glfwCreateWindow(1280, 720, "Brickman Map Generator", nullptr, nullptr);
    glfwMakeContextCurrent(window);
    glfwSwapInterval(1);

    IMGUI_CHECKVERSION();
    ImGui::CreateContext();
    ImGuiIO& io = ImGui::GetIO();
    (void)io;
    ImGui::StyleColorsDark();

    ImGui_ImplGlfw_InitForOpenGL(window, true);
    ImGui_ImplOpenGL3_Init("#version 130");

    while (!glfwWindowShouldClose(window)) {
        glfwPollEvents();

        ImGui_ImplOpenGL3_NewFrame();
        ImGui_ImplGlfw_NewFrame();
        ImGui::NewFrame();

        ImGui::Begin("Brickman Map Generator");
        for (int y = 0; y < rows; y++) {
            for (int x = 0; x < cols; x++) {
                std::string label = std::to_string(y) + "," + std::to_string(x);

                if (maze[y][x] == 0) ImGui::PushStyleColor(ImGuiCol_Button, IM_COL32(200,200,200,255)); // empty
                if (maze[y][x] == 1) ImGui::PushStyleColor(ImGuiCol_Button, IM_COL32(50,50,200,255));   // wall
                if (maze[y][x] == 2) ImGui::PushStyleColor(ImGuiCol_Button, IM_COL32(200,50,50,255));   // fruit

                if (ImGui::Button(label.c_str(), ImVec2(20,20))) {
                    maze[y][x] = (maze[y][x] + 1) % 3;
                }

                ImGui::PopStyleColor();

                if (x < cols - 1) ImGui::SameLine();
            }
        }

        ImGui::InputInt("Start Position X", &player_x);
        ImGui::InputInt("Start Position Y", &player_y);
        ImGui::InputText("File Name", filename, 256);

        if (ImGui::Button("Save Maze")) {
            nlohmann::json data;
            data["maze"] = maze;
            data["player_start"] = { player_y, player_x };

            const std::string filepath = "maps/" + std::string(filename) + ".json";
            std::ofstream file(filepath);
            file << data.dump(4);
        }

        ImGui::End();
        ImGui::Render();

        int display_w, display_h;
        glfwGetFramebufferSize(window, &display_w, &display_h);
        glViewport(0, 0, display_w, display_h);
        glClear(GL_COLOR_BUFFER_BIT);
        ImGui_ImplOpenGL3_RenderDrawData(ImGui::GetDrawData());
        glfwSwapBuffers(window);
    }

    ImGui_ImplOpenGL3_Shutdown();
    ImGui_ImplGlfw_Shutdown();
    ImGui::DestroyContext();
    glfwDestroyWindow(window);
    glfwTerminate();
}
