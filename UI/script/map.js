  function myMap() {
            var latitude = 	0.32850; // YOUR LATITUDE VALUE
            var longitude = 32.59187; // YOUR LONGITUDE VALUE

            var myLatLng = {lat: latitude, lng: longitude};

            map = new google.maps.Map(document.getElementById('googleMap'), {
              center: myLatLng,
              zoom: 10,
              disableDoubleClickZoom: true
            });
            
            
            
            var marker = new google.maps.Marker({
              position: myLatLng,
              map: map,
              //title: 'Hello World'

              // setting latitude & longitude as title of the marker
              // title is shown when you hover over the marker
              title: latitude + ', ' + longitude 
            });
            
                     
            // Update lat/long value of div when the marker is clicked
            marker.addListener('click', function(event) {              
              document.getElementById('late').innerHTML = event.latLng.lat();
              document.getElementById('long').innerHTML =  event.latLng.lng();
            });
            
            // Update lat/long value of div when anywhere in the map is clicked 
            google.maps.event.addListener(map,'click',function(event) {                
                document.getElementById('late').innerHTML = event.latLng.lat();
                document.getElementById('long').innerHTML =  event.latLng.lng();
            });
      
        }