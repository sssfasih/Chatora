#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
typedef uint8_t BYTE;
int main(int argc, char *argv[])
{
    //If less then 2 arguments exception
    if (argc != 2)
    {
        printf("Usage: ./recover [FILENAME]\n");
        return 1;
    }
    //opening given file in read-only mode
    FILE *f = fopen(argv[1], "r");
    if (f == NULL)
    {
        printf("File Not Accessable");
        return 1;
    }
    BYTE *buffer = malloc(512); //allocated buffer that is released in line 75
    int byteRead;
    int found;
    int counter = 0;
    char Filename[8];
    FILE *img;

    while (1) // while true read 512 bytes and if 512 bytes are there;
    {
        byteRead = fread(buffer, 1, 512, f);
        if (byteRead == 512)
        {
            //if new image detected
            if ((buffer[0] == 0xff) && (buffer[1] == 0xd8) && (buffer[2] == 0xff) && ((buffer[3] & 0xf0) == 0xe0))
            {
                //if it is first new image
                if (found == 0)
                {
                    //printf("First Image has been found!");
                    found = 1;
                    sprintf(Filename, "%03i.jpg", counter);
                    img = fopen(Filename, "w");
                    fwrite(buffer, 512, 1, img);

                }
                else
                {
                    //close the previous image and create new one
                    fclose(img);
                    counter++;
                    sprintf(Filename, "%03i.jpg", counter);
                    img = fopen(Filename, "w");
                    fwrite(buffer, 512, 1, img);

                }


            }
            else
            {
                //if any image is already found but this byte is not new image
                // then append to already opened image
                if (found == 1)
                {

                    fwrite(buffer, 512, 1, img);
                }

            }


        }

        // if raw file is out of bytes.
        else
        {
            printf("Could Not Read 512 Bytes. Read: %i\n", byteRead);
            break;
        }
    }
    fclose(img);
    free(buffer);
}
