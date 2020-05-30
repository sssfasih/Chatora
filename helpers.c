#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int latitude=0;latitude<height;latitude++)
    {
        for (int longitude=0;longitude<width;longitude++)
        {
            float addition;
            addition = image[latitude][longitude].rgbtBlue + image[latitude][longitude].rgbtGreen + image[latitude][longitude].rgbtRed;
            addition = addition/3;
            int add = round(addition);
            image[latitude][longitude].rgbtBlue = add;
            image[latitude][longitude].rgbtGreen = add;
            image[latitude][longitude].rgbtRed = add;

        }

    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{

    for (int latitude=0;latitude<height;latitude++)
    {
        for (int longitude=0;longitude<width;longitude++)
        {
            float sepiaRed,sepiaGreen,sepiaBlue;

            sepiaRed = .393 * image[latitude][longitude].rgbtRed + .769 * image[latitude][longitude].rgbtGreen + .189 * image[latitude][longitude].rgbtBlue;
            sepiaGreen = .349 * image[latitude][longitude].rgbtRed + .686 * image[latitude][longitude].rgbtGreen + .168 * image[latitude][longitude].rgbtBlue;
            sepiaBlue = .272 * image[latitude][longitude].rgbtRed + .534 * image[latitude][longitude].rgbtGreen + .131 * image[latitude][longitude].rgbtBlue;

            if (sepiaBlue > 255)
            {
                sepiaBlue = 255;
            }
            if (sepiaGreen > 255)
            {
                sepiaGreen = 255;
            }
            if (sepiaRed > 255)
            {
                sepiaRed = 255;
            }

            image[latitude][longitude].rgbtBlue = round(sepiaBlue);
            image[latitude][longitude].rgbtGreen = round(sepiaGreen);
            image[latitude][longitude].rgbtRed = round(sepiaRed);
        }
    }
    return;

}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int latitude = 0;latitude<height;latitude++)
    {
        int longitude;
        if (width%2 == 0)
        {
            longitude=round(width/2);
        }
        else
        {
            longitude = round(width/2);
        }
        for (int longitudeF=1;longitudeF<longitude;longitudeF++)
        {
            int tempGreen,tempBlue,tempRed;

            tempRed = image[latitude][width-longitudeF].rgbtRed;
            tempGreen = image[latitude][width-longitudeF].rgbtGreen;
            tempBlue = image[latitude][width-longitudeF].rgbtBlue;

            image[latitude][width-longitudeF].rgbtRed = image[latitude][longitudeF].rgbtRed;
            image[latitude][width-longitudeF].rgbtGreen = image[latitude][longitudeF].rgbtGreen;
            image[latitude][width-longitudeF].rgbtBlue = image[latitude][longitudeF].rgbtBlue;

            image[latitude][longitudeF].rgbtRed = tempRed;
            image[latitude][longitudeF].rgbtGreen = tempGreen;
            image[latitude][longitudeF].rgbtBlue = tempBlue;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}
