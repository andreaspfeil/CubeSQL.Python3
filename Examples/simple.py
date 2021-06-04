#
#         ___              __                        ____  ____     _ __
#        /   |  ____  ____/ /_______  ____ ______   / __ \/ __/__  (_) /
#       / /| | / __ \/ __  / ___/ _ \/ __ `/ ___/  / /_/ / /_/ _ \/ / / 
#      / ___ |/ / / / /_/ / /  /  __/ /_/ (__  )  / ____/ __/  __/ / /  
#     /_/  |_/_/ /_/\__,_/_/   \___/\__,_/____/  /_/   /_/  \___/_/_/
#                                                          
#  Product:     CubeSQL.Python3 - Demo App for the Python3 JSON driver
#  Version:     Revision: 1.0.0, Build: 1
#  Date:        2021/06/03 21:58:48
#  Author:      Andreas Pfeil <patreon@familie-pfeil.com>
#
#  Description: Opens a CubeSQL database connection with the JSON protocoll
#               Creates a table and inserts some rows, then selects the
#               values and prints it on the screen
#
#  Usage:       python3 simple.py
#
#  License:     BEER license / MIT license
#
#  Copyright (C) 2021 by Andreas Pfeil
#
# -----------------------------------------------------------------------TAB=2

import cubesql

print( "            _          ____   ___  _     " )
print( "  ___ _   _| |__   ___/ ___| / _ \| |    " )
print( " / __| | | | '_ \ / _ \___ \| | | | |    " )
print( "| (__| |_| | |_) |  __/___) | |_| | |___ " )
print( " \___|\__,_|_.__/ \___|____/ \__\_\_____|" )
print( "" )
print( "Demo App for the Python JSON driver, v1.0" )
print( "(c) 2021 by Andreas Pfeil" )
print( "" )
print( "" )

print( "Opening database server connection..." )
cube = cubesql.CubeSQL( 'localhost', "loginname", "password" )

print( "Selecting database..." )
cube.use( "test" )

print( "Creation table..." )
cube.execute( "CREATE TABLE IF NOT EXISTS Users (FirstName TEXT, LastName TEXT, Address TEXT);" )

print( "Inserting data..." )
cube.execute( "INSERT INTO Users VALUES ( 'Some', 'One', 'Firststreet 2, 69000 Bettertown' );" )
cube.execute( "INSERT INTO Users VALUES ( 'Other', 'Guy', 'Onlystreet 1, 69001 Besttown' );" )

print( "Selecting data..." )
d = cube.select( "SELECT * FROM Users;" );

print( "Printing data..." )
print( d )

print( "" )
print( "Done." )