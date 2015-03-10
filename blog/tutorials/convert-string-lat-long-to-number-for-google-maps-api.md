Convert string Lat/Long to number for Google Maps API
=====================================================

By [Chris Keller](https://github.com/chrislkeller)

When sending [Lat/Long](https://developers.google.com/maps/documentation/javascript/reference#LatLng) values to the [Google Maps API](https://developers.google.com/maps/documentation/javascript/) for something like setCenter(), it wants an number value. But the value we pull from an option menu like the one below is a string.

    <select id="searchString" onchange="zoomToAddress(this.value);">
    <option value="">--Select All--</option>
    <option value="43.138092,-89.747988">Luckenbooth Cafe</option>
    <option value="43.017218,-89.831479">Aunt Mary's Hooterville Inn</option>
    </select>

So we want to convert the above strings to numbers that the Maps API can use. We'll place the following inside a function called zoomToAddress.

First we get the value from the option menu as a string and set it to a variable.

    var searchString = document.getElementById('searchString').value;

Then we set a variable to find the position of the comma in the string.

    var commaPos = searchString.indexOf(',');

Use [parseFloat](http://www.javascripter.net/faq/convert2.htm) to conver the string to a number while parsing out the Latitude value.

    var coordinatesLat = parseFloat(searchString.substring(0, commaPos));

And we do the same for the Longitude.

    var coordinatesLong = parseFloat(searchString.substring(commaPos + 1, searchString.length));

Those variables are combined into a new google maps LatLng pair.

    var centerPoint = new google.maps.LatLng(coordinatesLat, coordinatesLong);

Then we can use the setCenter() method from the Maps API.

    map.setCenter(centerPoint);