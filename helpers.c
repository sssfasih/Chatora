#include "helpers.h"
#include <math.h>

// FUNCTIONS Declaration
RGBTRIPLE avg4(RGBTRIPLE one, RGBTRIPLE two, RGBTRIPLE three, RGBTRIPLE four);
RGBTRIPLE avg6(RGBTRIPLE one, RGBTRIPLE two, RGBTRIPLE three, RGBTRIPLE four, RGBTRIPLE five, RGBTRIPLE six);
RGBTRIPLE avg9(RGBTRIPLE one, RGBTRIPLE two, RGBTRIPLE three, RGBTRIPLE four, RGBTRIPLE five, RGBTRIPLE six, RGBTRIPLE seven,
               RGBTRIPLE eight, RGBTRIPLE nine);


// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    // Simple Double For Looping for every pixel in image.
    for (int latitude = 0; latitude < height; latitude++)
    {
        for (int longitude = 0; longitude < width; longitude++)
        {
            float addition;
            addition = image[latitude][longitude].rgbtBlue + image[latitude][longitude].rgbtGreen + image[latitude][longitude].rgbtRed;
            addition = addition / 3;
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
    // Simple Double For Looping for every pixel in image.
    for (int latitude = 0; latitude < height; latitude++)
    {
        for (int longitude = 0; longitude < width; longitude++)
        {
            float sepiaRed, sepiaGreen, sepiaBlue;

            sepiaRed = .393 * image[latitude][longitude].rgbtRed + .769 * image[latitude][longitude].rgbtGreen + .189 *
                       image[latitude][longitude].rgbtBlue;
            sepiaGreen = .349 * image[latitude][longitude].rgbtRed + .686 * image[latitude][longitude].rgbtGreen + .168 *
                         image[latitude][longitude].rgbtBlue;
            sepiaBlue = .272 * image[latitude][longitude].rgbtRed + .534 * image[latitude][longitude].rgbtGreen + .131 *
                        image[latitude][longitude].rgbtBlue;

            //More than max values exception

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
    // For Loop that runs fully vertically but half horizontally
    for (int latitude = 0; latitude < height; latitude++)
    {
        int longitude = 0;

        if (width)
        {
            longitude = (width / 2);
        }
        for (int longitudeF = 0; longitudeF < longitude; longitudeF++)
        {

            //Swaping Algorithm used ,using Temporary variables
            int tempGreen, tempBlue, tempRed;
            tempRed = image[latitude][width - longitudeF - 1].rgbtRed;
            tempGreen = image[latitude][width - longitudeF - 1].rgbtGreen;
            tempBlue = image[latitude][width - longitudeF - 1].rgbtBlue;

            image[latitude][width - longitudeF - 1].rgbtRed = image[latitude][longitudeF].rgbtRed;
            image[latitude][width - longitudeF - 1].rgbtGreen = image[latitude][longitudeF].rgbtGreen;
            image[latitude][width - longitudeF - 1].rgbtBlue = image[latitude][longitudeF].rgbtBlue;

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
    // Making Copy of Image to get original pixels for filteration
    RGBTRIPLE copy[height][width];
    for (int h = 0; h < height; h++)
    {
        for (int w = 0; w < width; w++)
        {
            copy[h][w] = image[h][w];
        }
    }

    //Here the Conditions and filteration happens
    for (int latitude = 0; latitude < height; latitude++)
    {
        for (int longitude = 0; longitude < width; longitude++)
        {
            if ((latitude == 0) && (longitude == 0)) //top left corner
            {
                image[latitude][longitude] = avg4(copy[latitude][longitude], copy[latitude][longitude + 1], copy[latitude + 1][longitude],
                                                  copy[latitude + 1][longitude + 1]);
            }
            else if ((latitude == 0) && (longitude == width - 1)) //top right corner
            {
                image[latitude][longitude] = avg4(copy[latitude][longitude], copy[latitude][longitude - 1], copy[latitude + 1][longitude],
                                                  copy[latitude + 1][longitude - 1]);
            }
            else if ((latitude == height - 1) && (longitude == 0)) //bottom left corner
            {
                image[latitude][longitude] = avg4(copy[latitude][longitude], copy[latitude - 1][longitude], copy[latitude][longitude + 1],
                                                  copy[latitude - 1][longitude + 1]);
            }
            else if ((latitude == height - 1) && (longitude == width - 1)) //bottom right corner
            {
                image[latitude][longitude] = avg4(copy[latitude][longitude], copy[latitude - 1][longitude], copy[latitude][longitude - 1],
                                                  copy[latitude - 1][longitude - 1]);
            }
            else if (latitude == 0) //upper edge
            {
                image[latitude][longitude] = avg6(copy[latitude][longitude], copy[latitude][longitude - 1],
                                                  copy[latitude][longitude + 1], copy[latitude + 1][longitude - 1], copy[latitude + 1][longitude], copy[latitude + 1][longitude + 1]);
            }

            else if (longitude == 0) //left edge
            {
                image[latitude][longitude] = avg6(copy[latitude][longitude], copy[latitude - 1][longitude], copy[latitude + 1][longitude],
                                                  copy[latitude][longitude + 1], copy[latitude - 1][longitude + 1], copy[latitude + 1][longitude + 1]);
            }
            else if (longitude == width - 1) //right edge
            {
                image[latitude][longitude] = avg6(copy[latitude][longitude], copy[latitude - 1][longitude], copy[latitude + 1][longitude],
                                                  copy[latitude][longitude - 1], copy[latitude + 1][longitude - 1], copy[latitude - 1][longitude - 1]);
            }
            else if (latitude == height - 1)  //bottom edge
            {
                image[latitude][longitude] = avg6(copy[latitude][longitude], copy[latitude][longitude - 1], copy[latitude][longitude + 1],
                                                  copy[latitude - 1][longitude], copy[latitude - 1][longitude - 1], copy[latitude - 1][longitude + 1]);
            }
            else
            {
                image[latitude][longitude] = avg9(copy[latitude - 1][longitude - 1], copy[latitude - 1][longitude],
                                                  copy[latitude - 1][longitude + 1], copy[latitude][longitude - 1], copy[latitude][longitude], copy[latitude][longitude + 1],
                                                  copy[latitude + 1][longitude - 1], copy[latitude + 1][longitude], copy[latitude + 1][longitude + 1]);
            }

        }
    }
    return;
}

// Functions take take many RGBTRIPLEs and return single averaged RGBTRIPLE
RGBTRIPLE avg4(RGBTRIPLE one, RGBTRIPLE two, RGBTRIPLE three, RGBTRIPLE four)
{
    RGBTRIPLE temp;
    temp.rgbtRed = round((one.rgbtRed + two.rgbtRed + three.rgbtRed + four.rgbtRed) / 4.0);
    temp.rgbtBlue = round((one.rgbtBlue + two.rgbtBlue + three.rgbtBlue + four.rgbtBlue) / 4.0);
    temp.rgbtGreen = round((one.rgbtGreen + two.rgbtGreen + three.rgbtGreen + four.rgbtGreen) / 4.0);

    return temp;
}

RGBTRIPLE avg6(RGBTRIPLE one, RGBTRIPLE two, RGBTRIPLE three, RGBTRIPLE four, RGBTRIPLE five, RGBTRIPLE six)
{
    RGBTRIPLE temp;
    temp.rgbtRed = round((one.rgbtRed + two.rgbtRed + three.rgbtRed + four.rgbtRed + five.rgbtRed + six.rgbtRed) / 6.0);
    temp.rgbtBlue = round((one.rgbtBlue + two.rgbtBlue + three.rgbtBlue + four.rgbtBlue + five.rgbtBlue + six.rgbtBlue) / 6.0);
    temp.rgbtGreen = round((one.rgbtGreen + two.rgbtGreen + three.rgbtGreen + four.rgbtGreen + five.rgbtGreen + six.rgbtGreen) / 6.0);

    return temp;
}

RGBTRIPLE avg9(RGBTRIPLE one, RGBTRIPLE two, RGBTRIPLE three, RGBTRIPLE four, RGBTRIPLE five, RGBTRIPLE six, RGBTRIPLE seven,
               RGBTRIPLE eight, RGBTRIPLE nine)
{
    RGBTRIPLE temp;
    temp.rgbtRed = round((one.rgbtRed + two.rgbtRed + three.rgbtRed + four.rgbtRed + five.rgbtRed + six.rgbtRed + seven.rgbtRed +
                          eight.rgbtRed + nine.rgbtRed) / 9.0);
    temp.rgbtBlue = round((one.rgbtBlue + two.rgbtBlue + three.rgbtBlue + four.rgbtBlue + five.rgbtBlue + six.rgbtBlue + seven.rgbtBlue
                           + eight.rgbtBlue + nine.rgbtBlue) / 9.0);
    temp.rgbtGreen = round((one.rgbtGreen + two.rgbtGreen + three.rgbtGreen + four.rgbtGreen + five.rgbtGreen + six.rgbtGreen +
                            seven.rgbtGreen + eight.rgbtGreen + nine.rgbtGreen) / 9.0);

    return temp;

}