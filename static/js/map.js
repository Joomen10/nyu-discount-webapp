function initMap() {
  // 지도 생성 (NYU 좌표)
  const nyuCoords = { lat: 40.7291, lng: -73.9965 };
  const map = new google.maps.Map(document.getElementById("map"), {
    center: nyuCoords,
    zoom: 13,
  });

  // /api/restaurants/ 엔드포인트에서 레스토랑 좌표 불러오기
  fetch("/api/restaurants/")
    .then((response) => response.json())
    .then((data) => {
      data.forEach((rest) => {
        if (rest.lat && rest.lng) {
          new google.maps.Marker({
            position: { lat: rest.lat, lng: rest.lng },
            map: map,
            title: rest.name,
          });
        }
      });
    })
    .catch((err) => console.error("Error fetching restaurants:", err));
}

// Google Maps 콜백에서 이 함수를 찾을 수 있도록 전역에 등록
window.initMap = initMap;
