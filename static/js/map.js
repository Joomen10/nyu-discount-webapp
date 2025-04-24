
async function initMap() {

  // 지도 생성 (NYU 좌표)
  const nyuCoords = { lat: 40.7291, lng: -73.9965 };
  const map = new google.maps.Map(document.getElementById("map"), {
    center: nyuCoords,
    zoom: 13,
    map_id: Map.DEMO_MAP_ID
  });

  const { PinElement } = await google.maps.importLibrary("marker");

  let pin = new PinElement({
    scale: 1.25,
    background: "#57068C",
    glyph: "",

  });

  // /api/restaurants/ 엔드포인트에서 레스토랑 좌표 불러오기
  try {
    // Await the response and handle it correctly
    const response = await fetch("/api/restaurants/");
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }

    const data = await response.json();

    data.forEach((rest) => {
      if (rest["longitude"] && rest["latitude"]) {
        const lat = parseFloat(rest["latitude"]);
        const lng = parseFloat(rest["longitude"]);

        var marker = new google.maps.Marker({
          position: { lat: lat, lng: lng },
          map: map,
          title: rest.name,
          content: pin.element,
          gmpClickable: true,
        });

        const infowindow = new google.maps.InfoWindow({
          content: `
            <h1>Name: ${rest.name}</h1>
            <p>Restaurant ID: ${rest.restaurant_id}</p>
            <p>Address: ${rest.address}</p>
            <p>Latitude: ${rest.latitude}</p>
            <p>Longitude: ${rest.longitude}</p>
            <p>Rating: ${rest.rating || "Not Available"}</p>
            <p>Cuisine Type: ${rest.cuisine_type || "Not Available"}</p>
            <p>Open Hours: ${rest.open_hours || "Not Available"}</p>
            <p>Google Place ID: ${rest.google_place_id}</p>
            <p>Discount ID: ${rest.discounts_id || "Not Available"}</p>
            `,
        });

        google.maps.event.addListener(marker, "click", () => {
          infowindow.open(map, marker);
        });
      }
    });
  } catch (err) {
    console.error("Error fetching restaurants:", err);
  }
}

// Google Maps 콜백에서 이 함수를 찾을 수 있도록 전역에 등록
window.initMap = initMap;
