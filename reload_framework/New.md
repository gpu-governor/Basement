Working with Images in Raylib

Images are a key component when creating games or graphical applications. In Raylib, images are stored in CPU memory (RAM), making them easy to manipulate before sending them to the GPU as textures. This tutorial will focus on practical uses of images, without converting them into textures.

Loading an Image

To start working with an image, you first need to load it into CPU memory using the LoadImage() function. In this example, we'll work with a file named image.png located in the same directory as our program.

#include "raylib.h"

int main() {
    InitWindow(800, 600, "Raylib - Image Example");

    // Load the image from file (stored in CPU memory)
    Image image = LoadImage("image.png");

    // Now we can work with the image data before converting it to a texture (if needed)

    // Once you're done with the image, make sure to unload it to free memory
    UnloadImage(image);

    CloseWindow();
    
    return 0;
}

Displaying Image Information

After loading an image, you might want to gather some information, such as its dimensions or color format. Raylib provides functions to extract these details.

#include "raylib.h"
#include <stdio.h>  // For printing to console

int main() {
    InitWindow(800, 600, "Raylib - Image Info");

    Image image = LoadImage("image.png");

    // Displaying basic information about the image
    printf("Image Width: %d\n", image.width);
    printf("Image Height: %d\n", image.height);
    printf("Image Format: %d\n", image.format);  // Format is usually PIXELFORMAT_UNCOMPRESSED_R8G8B8A8

    UnloadImage(image);
    CloseWindow();
    
    return 0;
}

Modifying the Image

One of the main advantages of working with images in CPU memory is the ability to modify them. Raylib provides several functions for manipulating images. Let’s look at some common operations:

1. Flipping the Image Vertically

You can flip an image vertically with ImageFlipVertical(). This is useful, for example, when correcting image orientation issues.

#include "raylib.h"

int main() {
    InitWindow(800, 600, "Raylib - Flip Image");

    Image image = LoadImage("image.png");

    // Flip the image vertically
    ImageFlipVertical(&image);

    // You could convert it to a texture and display it here if needed (not in this tutorial)

    UnloadImage(image);
    CloseWindow();
    
    return 0;
}

2. Resizing the Image

If you want to resize an image, Raylib provides the ImageResize() function. This is useful when you need to adjust the resolution of an image.

#include "raylib.h"

int main() {
    InitWindow(800, 600, "Raylib - Resize Image");

    Image image = LoadImage("image.png");

    // Resize the image to 400x300
    ImageResize(&image, 400, 300);

    UnloadImage(image);
    CloseWindow();
    
    return 0;
}

3. Drawing on the Image

Raylib allows you to draw onto an image using functions like ImageDraw(). In this example, we’ll draw a red rectangle onto the image:

#include "raylib.h"

int main() {
    InitWindow(800, 600, "Raylib - Draw on Image");

    Image image = LoadImage("image.png");

    // Create a new image to use as a brush (a simple red rectangle)
    Image brush = GenImageColor(100, 50, RED);

    // Draw the brush onto the original image at position (200, 100)
    ImageDraw(&image, brush, (Rectangle){ 0, 0, 100, 50 }, (Rectangle){ 200, 100, 100, 50 });

    UnloadImage(brush);  // Free the brush image
    UnloadImage(image);
    CloseWindow();
    
    return 0;
}

Saving the Modified Image

Once you’ve made modifications to an image, you may want to save it back to disk. Raylib makes this easy with the ExportImage() function:

#include "raylib.h"

int main() {
    InitWindow(800, 600, "Raylib - Save Image");

    Image image = LoadImage("image.png");

    // Modify the image (e.g., flip vertically)
    ImageFlipVertical(&image);

    // Save the modified image as a new file
    ExportImage(image, "flipped_image.png");

    UnloadImage(image);
    CloseWindow();
    
    return 0;
}

Conclusion

In this tutorial, we’ve covered the basics of loading, modifying, and saving images in Raylib, all without converting them into textures. This approach gives you maximum flexibility for processing images in your application. You can flip, resize, and draw onto images, then save them for later use or convert them into textures when ready for rendering.

Next, we'll explore more advanced manipulation techniques and how to work with multiple images in a scene!

