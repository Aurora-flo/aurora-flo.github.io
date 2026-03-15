def AddEgg( IndexFile, Number ):
    """adds the image of an egg
    IndexFile: the file the egg shall be added to
    Number: the number of the egg"""

    IndexFile.write( "            <section class=\"card\">" )

    IndexFile.write( "                <p>Egg " + str( Number ) + ":</p>" )
    IndexFile.write( "                <img src=\"img/egg" + str( Number ).zfill( 2 ) + ".png\" style=\"display:block; max-width:100%; height:auto;\">" )

    IndexFile.write( "            </section>" )


def MakeIndex(  ):
    """generates the index.html file"""

    IndexFile = open( "index.html", "w" )

    IndexFile.write( "<!DOCTYPE html>\n" )
    IndexFile.write( "<html>\n" )
    IndexFile.write( "<head>\n" )
    IndexFile.write( "</head>\n" )

    IndexFile.write( "<body>\n" )

    IndexFile.write( "    <header class=\"banner\">" )
    IndexFile.write( "        <h1>Aurora Easter Event</h1>" )
    IndexFile.write( "    </header>" )

    IndexFile.write( "    <main class=\"scroll-area\">" )

    IndexFile.write( "        <h2>Easter Challenge</h2>" )

    for nImg in range( 1,10 ):
        AddEgg( IndexFile, nImg )

    IndexFile.write( "        <h2>Bloopers/Outtakes</h2>" )

    for nImg in range( 11,58 ):
        AddEgg( IndexFile, nImg )

    IndexFile.write( "    </main>" )

    IndexFile.write( "</body>\n" )
    IndexFile.write( "</html>\n" )

    IndexFile.close()


if __name__ == "__main__":
    MakeIndex()
