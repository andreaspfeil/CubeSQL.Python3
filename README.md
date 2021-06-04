# cubeSQL Python3 client

Simple Python3 JSON client for the [cubeSQL](http://www.sqlabs.com/cubesql.php) database server.

## Usage example

See `Examples/simple.py` for a simple example.

```py
import cubesql

cube = cubesql.CubeSQL( 'localhost', "loginname", "password" )
cube.use( "test" )

cube.execute( "CREATE TABLE IF NOT EXISTS Users (FirstName TEXT, LastName TEXT, Address TEXT);" )

cube.execute( "INSERT INTO Users VALUES ( 'Some', 'One', 'Firststreet 2, 69000 Bettertown' );" )
cube.execute( "INSERT INTO Users VALUES ( 'Other', 'Guy', 'Onlystreet 1, 69001 Besttown' );" )

d = cube.select( "SELECT * FROM Users;" );
print( d )
```

## Installation

## Documentation

- [Wiki](https://github.com/andreaspfeil/CubeSQL.Python3/wiki)

## Video Tutorials

- [YouTube](https://www.youtube.com/channel/UCQF_wTmbR5aJZUcb7U1_0Fw)

## Donate

- [github](https://github.com/sponsors/andreaspfeil)
- [Patreon](https://www.patreon.com/andreas_pfeil)
- [PayPal](https://www.paypal.com/paypalme/PfeilAndreas/10.00EUR)

## Contributors

- [Marco Bambini](https://github.com/marcobambini) (Author of cubeSQL and the original PHP client)

## Acknowledgments

- [cubeSQL](https://sqlabs.com/cubesql)

## See also

- [cubeSQL for Python2](https://github.com/andreaspfeil/CubeSQL.Python2)
- [cubeSQL für .NET](https://github.com/andreaspfeil/CubeSQL.NET)

## License

[BEER license / MIT license](https://github.com/andreaspfeil/CubeSQL.Python3/blob/main/LICENSE) 

The BEER license is basically the same as the MIT license [(see link)](https://github.com/andreaspfeil/CubeSQL.Python3/blob/main/LICENSE), except 
that you should buy the author a beer [(see Donate)](https://github.com/andreaspfeil/CubeSQL.Python3#donate) if you use this software.

## Sponsors

none yet - YOU can still be number one in this list!!!