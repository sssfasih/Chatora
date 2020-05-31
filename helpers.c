#include "helpers.h"
#include <math.h>

RGBTRIPLE avg4(RGBTRIPLE one, RGBTRIPLE two , RGBTRIPLE three,RGBTRIPLE four);

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
        int longitude = 0;

        if (width)
        {
        longitude = (width/2);
        }
        for (int longitudeF=0;longitudeF<longitude;longitudeF++)
        {

            int tempGreen,tempBlue,tempRed;
            tempRed = image[latitude][width-longitudeF-1].rgbtRed;
            tempGreen = image[latitude][width-longitudeF-1].rgbtGreen;
            tempBlue = image[latitude][width-longitudeF-1].rgbtBlue;

            image[latitude][width-longitudeF-1].rgbtRed = image[latitude][longitudeF].rgbtRed;
            image[latitude][width-longitudeF-1].rgbtGreen = image[latitude][longitudeF].rgbtGreen;
            image[latitude][width-longitudeF-1].rgbtBlue = image[latitude][longitudeF].rgbtBlue;

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
    for (int latitude=0;latitude<height;latitude++)
    {
        for (int longitude=0;longitude<width;longitude++)
        {
            if ((latitude == 0) && (longitude == 0)) //top left corner
            {
                image[latitude][longitude] = avg4(image[latitude][longitude],image[latitude][longitude+1] , image[latitude+1][longitude] , image[latitude+1][longitude+1] );
            }
            else if ((latitude == 0) && (longitude == width-1)) //top right corner
            {
                image[latitude][longitude] = avg4(image[latitude][longitude],image[latitude][longitude-1],image[latitude+1][longitude],image[latitude+1][longitude-1]);
            }
            else if ((latitude==height-1) && (longitude == 0)) //bottom left corner
            {
                image[latitude][longitude] = avg4(image[latitude][longitude],image[latitude-1][longitude],image[latitude][longitude+1],image[latitude-1][longitude+1]);
            }
            else if ((latitude==height-1) && (longitude == width-1)) //bottom right corner
            {
                image[latitude][longitude] = avg4(image[latitude][longitude],image[latitude-1][longitude],image[latitude][longitude-1],image[latitude-1][longitude-1]);
            }

        }
    }
    return;
}

RGBTRIPLE avg4(RGBTRIPLE one, RGBTRIPLE two , RGBTRIPLE three,RGBTRIPLE four)
{
    RGBTRIPLE temp;
    temp.rgbtRed = (one.rgbtRed+two.rgbtRed+three.rgbtRed+four.rgbtRed)/4;
    temp.rgbtBlue = (one.rgbtBlue+two.rgbtBlue+three.rgbtBlue+four.rgbtBlue)/4;
    temp.rgbtGreen = (one.rgbtGreen+two.rgbtGreen+three.rgbtGreen+four.rgbtGreen)/4;

    return temp;
}