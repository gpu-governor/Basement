### Displaying Images and 2D Textures in Raylib

When creating games or graphical applications, one essential aspect is rendering images and 2D textures on the screen.

#### Images vs. Textures

Before diving into code, it's crucial to distinguish between images and textures in Raylib:

Image: This refers to data stored in CPU memory (RAM). It's used for manipulating pixel data (e.g., loading, modifying, or saving).

Texture: This represents data uploaded to GPU memory (VRAM), optimized for fast rendering. While you can’t modify a texture directly on the GPU, it allows for efficient drawing.
---
Raylib provides two primary ways to do this, each serving different needs depending on how you want to handle the image data. These methods are:

1. Loading an image first, then converting it to a texture.


2. Directly loading a texture.



Let's dive into both methods, understand how they work, and when to use each approach.


---

#### Method 1: Load an Image First, Then Convert to a Texture

Raylib gives you the flexibility to load an image using the LoadImage() function, which loads the image into CPU memory. This is useful when you want to modify the image before displaying it. Once your image is ready, you can convert it into a GPU texture using LoadTextureFromImage() for rendering.

Here’s an example:
<pre>
<code class="language-c">
#include "raylib.h"

int main() {
    InitWindow(800, 600, "Raylib - Load Image then Texture");
    
    // Step 1: Load an image (in CPU memory)
    Image img = LoadImage("file_path/my_image.png");

    // Optional: Modify the image before using it as a texture
    ImageFlipVertical(&img);  // Example: Flip the image vertically

    // Step 2: Convert the image to a texture (in GPU memory)
    Texture2D texture = LoadTextureFromImage(img);

    // Unload the image from CPU memory (we no longer need it)
    UnloadImage(img);
    
    while (!WindowShouldClose()) {
        BeginDrawing();
        ClearBackground(RAYWHITE);

        // Draw the texture
        DrawTexture(texture, 100, 100, WHITE);

        EndDrawing();
    }

    // Clean up resources
    UnloadTexture(texture);
    CloseWindow();
    
    return 0;
}
</code>
</pre>
##### Why Use This Method?

This approach is ideal when you need to manipulate or process the image before rendering it. Some possible operations include:

* Flipping (as shown in the example),

* Resizing the image,

* Drawing onto the image using functions like ImageDraw().


The key takeaway is that you load the image in CPU memory, perform modifications, and then upload it to the GPU as a texture when ready. Once it's uploaded, you can render the texture as usual, which benefits from GPU acceleration.

##### Pros:

Flexibility to edit the image before rendering.

Useful for procedural generation or image processing.


##### Cons:

Slower if no image modifications are needed because of the additional CPU memory step.

Takes up more memory briefly since the image is stored both on CPU and GPU memory during the process.



---

#### Method 2: Load a Texture Directly

The simpler and faster option for most use cases is to load an image directly as a texture using LoadTexture(). This skips the intermediate step of loading the image into CPU memory and sends it straight to the GPU, ready to be rendered.

Here’s how you do it:
<pre>
<code class="language-c">
#include "raylib.h"

int main() {
    InitWindow(800, 600, "Raylib - Load Texture Directly");

    // Load the texture directly (in GPU memory)
    Texture2D texture = LoadTexture("file_path/my_image.png");
    
    while (!WindowShouldClose()) {
        BeginDrawing();
        ClearBackground(RAYWHITE);

        // Draw the texture
        DrawTexture(texture, 100, 100, WHITE);

        EndDrawing();
    }

    // Clean up resources
    UnloadTexture(texture);
    CloseWindow();
    
    return 0;
}
</code>
</pre>
##### Why Use This Method?

This method is the most efficient way to load and display images if you don’t need to modify the image data. Since it goes straight to GPU memory, you skip any intermediate steps and can begin drawing the texture right away. For static images where no manipulation is required, this is the preferred approach.

##### Pros:

Faster since it loads directly into GPU memory.

Simpler for static images that don’t need processing.


##### Cons:

You cannot modify the image data once it's loaded as a texture.

Less flexibility for procedural manipulation or real-time changes.



---

#### Comparison: When to Use Each Method

Modifying Images: If your application needs to modify the image data (e.g., applying filters, resizing, flipping, etc.), use Method 1 (load as an image first).

Fast Rendering: If you just need to display an image without any processing, use Method 2 (load directly as a texture). This saves you the step of handling CPU memory and goes straight to GPU for optimal performance.



---

#### Conclusion

Raylib provides you with flexible options for displaying images and textures in your 2D games or applications. If you need to modify an image before rendering, go with the Image + Texture approach. However, if you're looking for simplicity and performance, loading a texture directly is the way to go.

By understanding the differences between these methods, you can make informed choices about how to handle images in your projects, ensuring the best performance and functionality for your needs.
<br>

in the next page, we will look into them in more details
