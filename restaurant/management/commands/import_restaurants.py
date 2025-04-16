import time
import requests
from django.core.management.base import BaseCommand
from restaurant.models import Restaurants
import pprint

class Command(BaseCommand):
    help = "Import restaurants from Google Places API (NYU 중심 반경 15km 내 레스토랑 데이터 구축) using (New) Places API"

    def add_arguments(self, parser):
        parser.add_argument(
            '--location',
            type=str,
            help='검색 기준 위치 (예: "40.7291,-73.9965")',
            default="40.7291,-73.9965"
        )
        parser.add_argument(
            '--radius',
            type=int,
            help='검색 반경 (미터 단위, 기본 15000m = 15km)',
            default=15000
        )
        parser.add_argument(
            '--type',
            type=str,
            help='장소 타입 (기본값: restaurant)',
            default="restaurant"
        )

    def handle(self, *args, **options):
        # 실제 발급받은 (New) Places API 키로 교체하세요.
        API_KEY = "AIzaSyCGyCxqGwUDZACVf-GrppfQlpgbEHv9oIo"
        url = "https://places.googleapis.com/v1/places:searchNearby"
        headers = {
            "Content-Type": "application/json; charset=utf-8",
            "X-Goog-Api-Key": API_KEY,
            # 반환받을 필드를 지정 (필요에 따라 수정)
            "X-Goog-FieldMask": "places(id,displayName,formattedAddress,location,rating,types,photos)"
        }
        NYU_LAT, NYU_LNG = 40.7291, -73.9965
        body = {
            "locationRestriction": {
                "circle": {
                    "center": {"latitude": NYU_LAT, "longitude": NYU_LNG},
                    "radius": options["radius"]
                }
            },
            "includedTypes": [options["type"]],
            "maxResultCount": 20
        }

        self.stdout.write("Google Places API (New)로부터 식당 정보를 가져옵니다...")
        try:
            resp = requests.post(url, headers=headers, json=body)
            data = resp.json()
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"네트워크 오류: {e}"))
            return

        if "error" in data:
            self.stdout.write(self.style.ERROR(f"API 호출 실패: {data['error'].get('message', '알 수 없는 오류')}"))
            return

        places = data.get("places", [])
        restaurants_count = 0
        photo_width = 400
        photo_height = 400

        for i in places[0]['photos']:
            print(i)

        # image_urls = [photo['photoUri'] for photo in places[0]['photos']]
        # print(image_urls)
        for place in places:
            google_place_id = place.get("id")
            # print("\n WEEEE: ", google_place_id)
            google_place_photos = place.get("photos")
            # print("\n WAHHHH: ", place)
            displayName = place.get("displayName")
            if isinstance(displayName, dict):
                name = displayName.get("text")
            else:
                name = displayName
            address = place.get("formattedAddress")
            loc = place.get("location", {})
            latitude = loc.get("latitude")
            longitude = loc.get("longitude")
            rating = place.get("rating")
            types = place.get("types", [])
            cuisine = ",".join(types) if types else None

            Restaurants.objects.update_or_create(
                google_place_id=google_place_id,
                defaults={
                    "name": name,
                    "address": address,
                    "latitude": latitude,
                    "longitude": longitude,
                    "rating": rating,
                    "cuisine_type": cuisine,
                }
            )
            restaurants_count += 1

        self.stdout.write(self.style.SUCCESS(f"총 {restaurants_count} 개의 식당 정보를 추가/업데이트했습니다."))
