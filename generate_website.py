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

    IndexFile.write( "        <h2>Regeln</h2>\n" )

    IndexFile.write( "            <p>Die Orte, die auf den ersten 10 Eiern abgebildet sind, müssen von euch erraten werden.</p>\n" )
    IndexFile.write( "            <p>Sendet eure Lösungen bitte per Ingame-Mail oder über Discord an einen der vier Gildenleiter (Imo, Setesh, DanonYumei oder TerrorHenri).</p>\n" )
    IndexFile.write( "            <p>Gebt dabei für jedes Ei folgende Informationen an:</p>\n" )

    IndexFile.write( "            <ul>\n" )
    IndexFile.write( "                <li>Nummer des Eis</li>\n" )
    IndexFile.write( "                <li>Name der Karte, auf der es gefunden wurde</li>\n" )
    IndexFile.write( "                <li>Koordinaten</li>\n" )
    IndexFile.write( "            </ul>\n" )

    IndexFile.write( "            <p>Einsendeschluss ist der 07. April 2026 um 00:00 Uhr.</p>\n" )
    IndexFile.write( "            <p>Für jedes korrekt erratene Ei erhält der jeweilige Spieler einen Punkt.</p>\n" )
    IndexFile.write( "            <p>Das Gesamt-Preisgeld von 355.600.000 Gelt wird anschließend durch die insgesamt erreichte Punktzahl aller Teilnehmer geteilt. Die Auszahlung erfolgt dann anteilig entsprechend der von jedem Spieler erzielten Punkte.</p>\n" )

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
