function initMap() {
  //Center London - as center of location
  //This would never change as it is center of map 
  console.log(p_ids)
  // var place_ids=document.getElementById('p_ids').innerHTML
  var all_place_ids = document.getElementsByClassName('p_ids');
  var all_destination_ids = document.getElementsByClassName('d_ids');

  console.log("all_place_ids.length", all_place_ids.length)
  

  // console.log("This is place_id from html",place_ids,typeof place_ids);
      var options = {
        zoom: 2,
        center: {
          lat: 51.509865,
          lng: -0.118092
        },

      }
  //Getting map from map api
  var map = new google.maps.Map(document.getElementById('map'), options);
  // var placeId = "ChIJ7cv00DwsDogRAMDACa2m4K8";
  // console.log(placeId)
  var service = new google.maps.places.PlacesService(map);

  // var names = [];
  // for (var i = 0; i < all_place_ids.length - 1; i++) {

  //   names[i] = all_place_ids[i].name;
  //   console.log("printing all place_ids&&&&&", names[i])

  // }

  for (var i = 0; i < all_place_ids.length; i++) {
    let destination_id=all_destination_ids[i].name
    let request_1 = {
      placeId: all_place_ids[i].name
    };
    placeId = all_place_ids[i].name
    console.log("this is place_id#####",placeId)

    service.getDetails(request_1, function (results, status) {
      console.log(status);
      console.log("inside getdeatils::::::::", request_1.placeId);

      if (status == google.maps.places.PlacesServiceStatus.OK) {
        console.log(results.name)
        console.log(results.geometry.location.lat())
        console.log("this is lng", results.geometry.location.lng())
        console.log("this is place_id((((", request_1.placeId)

        addMarker(results.geometry.location.lat(), results.geometry.location.lng(), map, request_1.placeId,destination_id)
        for (var item in results) {
          console.log("item : " + item);
        }
      }
    });
  }

}

function addMarker(x, y, map, placeId,destination_id) {
  var image = {
    url: 'https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png',
    // This marker is 20 pixels wide by 32 pixels high.
    size: new google.maps.Size(20, 32),
    // The origin for this image is (0, 0).
    origin: new google.maps.Point(0, 0),
    // The anchor for this image is the base of the flagpole at (0, 32).
    anchor: new google.maps.Point(0, 32)
  };

  //  var marker = new google.maps.Marker({
  //   map: map,
  //   place: {
  //     placeId: results[0].place_id,
  //     location: results[0].geometry.location
  //   }
  // });
  var marker = new google.maps.Marker({
    position: {
      lat: x,
      lng: y
    },
    placeId: placeId,
    animation: google.maps.Animation.DROP,
    icon: image,
    map: map
  });

  console.log("Marker created")
  marker.addListener('click', function () {
    console.log("inside AddListener$$$$$", placeId)
    console.log("This is marker test", marker.position.lat())
    console.log("this is  this test", this.position.lat())
    showDetails(map, marker, marker.placeId,destination_id);
  });

}

function showDetails(map, marker, place_id,destination_id) {
  console.log("marker*******", marker);
  console.log("place_id", marker.placeId, place_id)

  // var placeService = new google.maps.places.PlacesService(map)
  var contentStringChicago = '';
  var service = new google.maps.places.PlacesService(map);

  var request_1 = {
    placeId: place_id
  };

  service.getDetails(request_1, function (results, status) {
    console.log(status);
    contentStringChicago = '<div id="x">' + '<h1>' + results.name + '</h1>' + '<img class="photo" src="' + results.photos[0].getUrl() + '" alt="chicago">' +
      '</div>' + '<div id="y"><p><b>' + results.formatted_address + '</b></p> <p><a href='+ results.website + '>places to visit</a></P><a href=/myGallery/'+ destination_id+'> My Gallery</a></div>';
    if (status == google.maps.places.PlacesServiceStatus.OK) {
      console.log("contentStringChicago** :" + contentStringChicago);
      for (var item in results) {
        console.log("item : " + item);

      }

    }
    var infowindow = new google.maps.InfoWindow({
      content: contentStringChicago
    });

    infowindow.open(map, marker);

  });

}