### Working with 2D Textures in Raylib

In previous tutorials we first created an image then convert it to a texture, which is cool but however it is more faster to load it as texture directly by skipping the image function. In this tutorial, we’ll show you how to load and display a 2D texture in Raylib. Along the way, we’ll also mention some other useful functions for drawing textures in different ways.

#### Step 1: Loading a Texture

The first step is loading an image as a texture using Raylib’s LoadTexture() function.
<pre>
<code class="language-c">
#include "raylib.h"

int main(void) {
    InitWindow(640, 480, "Raylib - 2D Textures Tutorial");

    // Load texture from file
    Texture2D texture = LoadTexture("resources/image.png");

    while (!WindowShouldClose()) {
        BeginDrawing();
        ClearBackground(RAYWHITE);

        // Draw the texture at position (200, 200)
        DrawTexture(texture, 200, 200, WHITE);

        EndDrawing();
    }

    // Unload texture and close window
    UnloadTexture(texture);
    CloseWindow();

    return 0;
}
</code>
</pre>

#### Step 2: Drawing the Texture

In this example, we load an image called image.png and draw it on the screen using DrawTexture() at coordinates (200, 200). The function is simple and perfect for when you want to display a full image on the screen without any transformations.

#### Step 3: Other Useful DrawTexture Functions

While DrawTexture() is the most basic way to display a texture, Raylib offers a few more advanced functions that can come in handy:

DrawTextureEx(): This function allows you to scale and rotate textures easily. If you want to make a texture bigger or rotate it around a point, use DrawTextureEx(). It's useful for basic transformations without needing extra code.

DrawTexturePro(): If you need more control over how your texture is displayed, such as changing its size, flipping it, or applying complex transformations, DrawTexturePro() is the way to go. This function is more flexible but requires you to set up source and destination rectangles, so it’s more advanced.

DrawTextureRec(): Use this function when you want to draw only a part of the texture. This is great for sprite sheets, where you have multiple images stored in one file and need to pick specific sections to display.

DrawTextureTiled(): If you want to create repeating patterns using your texture, DrawTextureTiled() can be useful. It’s a quick way to fill an area with the same image repeated over and over.


Each of these functions is designed to give you more control over how textures are displayed on the screen. You won’t need them for simple drawings, but as your projects get more complex (like animations or tiled backgrounds), they will become very helpful.

#### Step 4: Unloading the Texture

When you're done, remember to unload the texture from memory with UnloadTexture() to prevent memory leaks.

### Conclusion

In this tutorial, you learned how to load and display a texture in Raylib using DrawTexture(). We also briefly mentioned more advanced functions like DrawTextureEx(), DrawTexturePro(), and others, which you'll find useful as you get deeper into graphics programming.

In the next tutorial, we’ll cover animations and sprite sheets in more detail!
