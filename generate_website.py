def AddEgg( IndexFile, Number ):
    """adds the image of an egg
    IndexFile: the file the egg shall be added to
    Number: the number of the egg"""

    IndexFile.write( "            <section class=\"card\">\n" )

    IndexFile.write( "                <p>Egg " + str( Number ) + ":</p>\n" )
    IndexFile.write( "                <img src=\"img/egg" + str( Number ).zfill( 2 ) + ".png\">\n" )

    IndexFile.write( "            </section>\n" )


def MakeIndex(  ):
    """generates the index.html file"""

    IndexFile = open( "index.html", "w" )

    IndexFile.write( "<!DOCTYPE html>\n" )
    IndexFile.write( "<html>\n" )
    IndexFile.write( "<head>\n" )
    IndexFile.write( "    <link rel=\"stylesheet\" href=\"style.css\">" )
    IndexFile.write( "</head>\n" )

    IndexFile.write( "<body>\n" )

    IndexFile.write( "    <header class=\"banner\">\n" )
    IndexFile.write( "        <h1>Aurora Easter Event</h1>\n" )
    IndexFile.write( "    </header>\n" )

    IndexFile.write( "    <main class=\"scroll-area\">\n" )

    IndexFile.write( "        <h2>Easter Challenge</h2>\n" )

    for nImg in range( 1,11 ):
        AddEgg( IndexFile, nImg )

    IndexFile.write( "        <h2>Bonus eggs (no points)</h2>\n" )

    for nImg in range( 11,62 ):
        AddEgg( IndexFile, nImg )

    IndexFile.write( "    </main>\n" )

    IndexFile.write( "</body>\n" )
    IndexFile.write( "</html>\n" )

    IndexFile.close()


if __name__ == "__main__":
    MakeIndex()
