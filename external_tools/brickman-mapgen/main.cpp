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

const int winwidth = 985;
const int winheight = 690;

const int rows = 9;
const int cols = 16;
std::vector<std::vector<int>> maze(rows, std::vector<int>(cols, 0));

constexpr int tilesize = 1280 / 24;

int player_x = 0;
int player_y = 0;
char savefile[256];
char loadfile[256];

int main() {
    glfwInit();
    GLFWwindow* window = glfwCreateWindow(winwidth, winheight, "Brickman Map Generator", nullptr, nullptr);
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
        ImGui::SetNextWindowPos(ImVec2(0, 0), ImGuiCond_Always);
        ImGui::SetNextWindowSize(ImVec2(winwidth, winheight), ImGuiCond_Always);

        ImGui::Begin("Brickman Map Generator", nullptr, ImGuiWindowFlags_NoTitleBar | ImGuiWindowFlags_NoResize | ImGuiWindowFlags_NoMove | ImGuiWindowFlags_NoCollapse);

        if (ImGui::BeginPopupModal("Controls Info", nullptr, ImGuiWindowFlags_AlwaysAutoResize)) {
            ImGui::Text(
                "Controls:\n\n\n"
                "To use this program, you have the following available controls:\n\n"
                "Left Click on a grid item - changes state:\n"
                "  - white: empty space\n"
                "  - purple: wall\n"
                "  - red: fruit\n"
                "Right Click on a grid item - sets player start to this position.\n\n"
                "To save/load map files, fill in the file names into the corresponding fields\n"
                "And then press the respective buttons."
            );
            if (ImGui::Button("Close")) {
                ImGui::CloseCurrentPopup();
            }
            ImGui::EndPopup();
        }

        for (int y = 0; y < rows; y++) {
            for (int x = 0; x < cols; x++) {
                std::string label = std::to_string(y) + "," + std::to_string(x);

                if (maze[y][x] == 0) ImGui::PushStyleColor(ImGuiCol_Button, IM_COL32(200,200,200,255)); // empty
                if (maze[y][x] == 1) ImGui::PushStyleColor(ImGuiCol_Button, IM_COL32(50,50,200,255));   // wall
                if (maze[y][x] == 2) ImGui::PushStyleColor(ImGuiCol_Button, IM_COL32(200,50,50,255));   // fruit

                ImGui::PushID((y * cols) + x); // Ensure unique ID for each button
                bool button_clicked = ImGui::Button(label.c_str(), ImVec2(tilesize, tilesize));
                bool right_clicked = ImGui::IsItemHovered() && ImGui::IsMouseClicked(ImGuiMouseButton_Right);
                if (button_clicked) {
                    maze[y][x] = (maze[y][x] + 1) % 3;
                }
                if (right_clicked) {
                    player_x = x;
                    player_y = y;
                }

                // Draw yellow border if this is the player start position
                if (player_x == x && player_y == y) {
                    ImDrawList* draw_list = ImGui::GetWindowDrawList();
                    ImVec2 p_min = ImGui::GetItemRectMin();
                    ImVec2 p_max = ImGui::GetItemRectMax();
                    draw_list->AddRect(p_min, p_max, IM_COL32(255, 255, 0, 255), 0.0f, 0, 3.0f);
                }
                ImGui::PopID();

                ImGui::PopStyleColor();

                if (x < cols - 1) ImGui::SameLine();
            }
        }

        ImGui::InputInt("Start Position X", &player_x);
        ImGui::InputInt("Start Position Y", &player_y);
        
        ImGui::InputText("Save File Name", savefile, 256);
        if (ImGui::Button("Save Maze")) {
            nlohmann::json data;
            data["maze"] = maze;
            data["player_start"] = { player_y, player_x };

            const std::string filepath = "maps/" + std::string(savefile) + ".json";
            std::ofstream file(filepath);
            if (file) {
                file << data.dump(4);
            } else {
                std::cerr << "Failed to open file: " << filepath << std::endl;
            }
        }

        ImGui::InputText("Load File Name", loadfile, 256);
        if (ImGui::Button("Load Maze")) {
            const std::string filepath = "maps/" + std::string(loadfile) + ".json";
            std::ifstream file(filepath);
            if (file) {
                nlohmann::json data;
                file >> data;
                if (data.contains("maze")) {
                    maze = data["maze"].get<std::vector<std::vector<int>>>();
                }
                if (data.contains("player_start")) {
                    player_y = data["player_start"][0].get<int>();
                    player_x = data["player_start"][1].get<int>();
                }
            } else {
                std::cerr << "Failed to open file: " << filepath << std::endl;
            }
        }

        if (ImGui::Button("Controls")) {
            ImGui::OpenPopup("Controls Info");
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
