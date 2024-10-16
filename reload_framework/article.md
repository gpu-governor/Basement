### How to Load Images in Raylib Using Image

Raylib simplifies image handling by offering a straightforward API to load, process, and draw images. In this tutorial, we will cover how to load an image using the Image structure, and how to manipulate it before rendering it on the screen.

#### What is an Image in Raylib?

In Raylib, an Image is a 2D bitmap data structure used for manipulation and loading purposes. It stores the image's pixel data in CPU memory, which allows you to perform operations like resizing, cropping, or even pixel-by-pixel modifications before converting it into a texture for GPU rendering.

> Note: An Image is different from a Texture2D. Once an Image is loaded and processed, it can be converted into a Texture2D for rendering on the screen, which resides in GPU memory.


---
#### Basic Steps to Load an Image

To load and display an image in Raylib, you need to follow these basic steps:

1. Initialize Raylib.


2. Load the Image from a file.


3. Convert the Image to a Texture.


4. Render the Texture on the screen.


5. Unload resources after use.



Let’s walk through an example step-by-step.

Step 1: Initialize Raylib

Before loading any images, you need to initialize Raylib with the proper window size and other settings. You can do this by calling InitWindow() and setting the dimensions of your game window.

<pre>
<code class="language-c">
#include "raylib.h"

int main() {
    // Initialize the window
    InitWindow(800, 600, "Image Loading Example");

    // Set the target FPS (frames per second)
    SetTargetFPS(60);

    // Main game loop
    while (!WindowShouldClose()) {
        // Update and draw the game
        BeginDrawing();
        ClearBackground(RAYWHITE);
        
        // TODO : image drawing
        
        EndDrawing();
    }

    // Close window and OpenGL context
    CloseWindow();

    return 0;
}
</code>
</pre>

Step 2: Load an Image from a File

To load an image, use the LoadImage() function, which takes a file path as its argument and returns an Image struct. In this example, let’s assume we have an image called image.png located in the same directory as our executable.

<pre>
<code class="language-c">
// Load the image from a file
Image my_image = LoadImage("image.png");
</code>
</pre>
Step 3: Convert the Image to a Texture

Since Raylib renders using OpenGL, it’s necessary to convert the Image into a Texture2D before rendering. This is done using LoadTextureFromImage().

<pre>
<code class="language-c">
// Convert the image to a texture for rendering
Texture2D texture = LoadTextureFromImage(my_image);

// Once converted, you no longer need the Image object in CPU memory
UnloadImage(my_image);
</code>
</pre>
Step 4: Draw the Texture

Now that we have the texture ready, we can render it on the screen using the DrawTexture() function.
<pre>
<code class="language-c">
// In the game loop, render the texture
while (!WindowShouldClose()) {
    BeginDrawing();
    ClearBackground(RAYWHITE);

    // Draw the texture at position (200, 150)
    DrawTexture(texture, 200, 150, WHITE);

    EndDrawing();
}
</code>
</pre>
Step 5: Unload Resources

Once you’re done with the texture, make sure to unload it to free up GPU memory. This is done with the UnloadTexture() function.
<pre>
<code class="language-c">
// Before closing the window, unload the texture
UnloadTexture(texture);
</code>
</pre>
Full Example Code

Here’s the complete code for loading and displaying an image:
<pre>
<code class="language-c">
#include "raylib.h"

int main() {
    // Initialize window
    InitWindow(800, 600, "Image Loading Example");

    // Load an image and convert it to a texture
    Image my_image = LoadImage("image.png");
    Texture2D texture = LoadTextureFromImage(my_image);
    UnloadImage(my_image);  // We no longer need the CPU-side image data

    // Set target FPS
    SetTargetFPS(60);

    // Main game loop
    while (!WindowShouldClose()) {
        // Update and draw
        BeginDrawing();
        ClearBackground(RAYWHITE);

        // Draw the texture on the screen
        DrawTexture(texture, 200, 150, WHITE);

        EndDrawing();
    }

    // Unload the texture when done
    UnloadTexture(texture);

    // Close window and OpenGL context
    CloseWindow();

    return 0;
}
</code>
</pre>
Conclusion

Raylib makes image loading and rendering simple with its Image and Texture2D types. The steps are straightforward:

1. Load an Image using LoadImage().


2. Convert it to a Texture2D with LoadTextureFromImage().


3. Render it using DrawTexture().


4. Unload your resources to prevent memory leaks.



Using these tools, you can easily integrate 2D images into your game, whether for backgrounds, characters, or UI elements. Once you grasp these basics, you can start exploring other powerful features Raylib offers for image manipulation.


---

Feel free to adjust or expand this article based on your blog’s style!

