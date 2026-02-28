import os


def MakeImageFiles():
    """generates the individual <number>.html files for the images"""

    subfolder = "img"

    filenames = [
    f.split(".")[0] for f in os.listdir(subfolder)
    if os.path.isfile(os.path.join(subfolder, f))
    ]

    for name in filenames:
        ImgFile = open( name + ".html", "w" )

        ImgFile.write( "<!DOCTYPE html>\n" )
        ImgFile.write( "<html>\n" )
        ImgFile.write( "<head>\n" )
        ImgFile.write( "    <title></title>\n" )
        ImgFile.write( "    <meta charset=\"UTF-8\">\n" )
        ImgFile.write( "</head>\n" )
        ImgFile.write( "<body style=\"margin:0; padding:0;\">\n" )
        ImgFile.write( "    <img src=\"" + subfolder + "/" + name + ".png\" style=\"display:block; width:auto; height:100%;\">\n" )
        ImgFile.write( "</body>\n" )
        ImgFile.write( "</html>\n" )

        ImgFile.close()


def MakeIndex( ImgNumber ):
    """generates the index.html file
    ImgNumber: the number of the image called by default"""

    IndexFile = open( "index.html", "w" )

    IndexFile.write( "<!DOCTYPE html>\n" )
    IndexFile.write( "<html>\n" )
    IndexFile.write( "<head>\n" )
    IndexFile.write( "    <meta http-equiv=\"refresh\" content=\"0; url=" + str( ImgNumber ) + "\">\n" )
    IndexFile.write( "</head>\n" )
    IndexFile.write( "<body>\n" )
    IndexFile.write( "</body>\n" )
    IndexFile.write( "</html>\n" )

    IndexFile.close()


if __name__ == "__main__":
    MakeImageFiles()
    MakeIndex( "741357" )
