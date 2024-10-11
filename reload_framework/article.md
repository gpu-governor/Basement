### Getting started with Raylib
create a `main.c` or `main.cpp` file, and copy the code below :
<pre>
<code class="language-c">
#include "raylib.h"

// Determing the Game Window Width and Height
const int screenWidth = 640;
const int screenHeight = 480;

int main() {

    // Initialize the Window
    InitWindow(screenWidth, screenHeight, "my first raylib window");

    // Setting the Frames Per Second
    SetTargetFPS(60);

    // The Game Loop
    while (!WindowShouldClose()) {

        // Setup renderer
        BeginDrawing();
        // Clear renderer to a specific color to avoid flicker
        ClearBackground(RAYWHITE);

        // Here goes all the Game Logic

        // teardown renderer
        EndDrawing();
    }
    CloseWindow();
    return 0;
}
</code>
</pre>

the above program is a basic structure of all raylib programs, it creates a window of resolution 640x480 with a title that says "my first raylib window". then we set the target fps to 60 so that it aims to run at the same frame rates regardless of the computer with run it on.
if you run the program you would see :
![my first raylib window](files/img/02_00_my_first_window.png). 

---
we have created a window but it's empty, so let's draw to it
to write a simple text to a window we use the `DrawText()` function in our while loop of our program :
<pre>
<code class="language-c">
 while(!WindowShouldClose()){
        BeginDrawing();
        ClearBackground(RAYWHITE);
        // draw text function
        DrawText("haha hi, 'I'm GPU governor", 100, 100, 30, RED);
        EndDrawing();
    }
</code>
</pre>

as you can see above, the DrawText() recieves 5 parameters, the first parameter is the text we want to write and i personally choose to write "haha hi, i am GPU Governor".
then he 