from tracker.models import GoogleAddress
import requests

from tracker_api.settings import API_KEY


def get_address(latitude, longitude):
    address = GoogleAddress.objects.filter(latitude=latitude, longitude=longitude).last()
    if not address:
        URL = "https://maps.googleapis.com/maps/api/geocode/json?"
        params = f"latlng={latitude},{longitude}&key={API_KEY}"
        response = requests.get(URL + params)
        result = response.json()["results"]
        place_id = ""
        for item in result:
            formatted_address = item.get("formatted_address")
            if formatted_address and len(formatted_address) > len(address or ""):
                address = formatted_address
                place_id = item.get("place_id")
        GoogleAddress.objects.create(
            latitude=latitude,
            longitude=longitude,
            place_id=place_id,
            formatted_address=address
        )
        return address
    return address.formatted_address
