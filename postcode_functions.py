"""Functions that interact with the Postcode API."""

import requests as req
import os
import json

CACHE_FILE = "./postcode_cache.json"

def load_cache() -> dict:
    """Loads the cache from a file and converts it from JSON to a dictionary."""
    # This function is used in Task 3, you can ignore it for now.
    ...


def save_cache(cache: dict):
    """Saves the cache to a file as JSON"""
    # This function is used in Task 3, you can ignore it for now.
    ...



def validate_postcode(postcode: str) -> bool:
    if not isinstance(postcode, str):
        raise TypeError("Function expects a string.")
    response = req.get(
        f"https://api.postcodes.io/postcodes/{postcode}/validate")
    if response.status_code == 500:
        raise req.RequestException('Unable to access API.', 500)
    return response.json()["result"]


def get_postcode_for_location(lat: float, long: float) -> str:
    if not isinstance(lat, float):
            raise TypeError("Function expects two floats.")
    if not isinstance(long, float):
            raise TypeError("Function expects two floats.")
    response = req.get(
        f"https://api.postcodes.io/postcodes?lon={long}&lat={lat}")
    if response.status_code == 500:
        raise req.RequestException('Unable to access API.', 500)
    location = response.json()
    if location["result"] is None:
         if response.status_code == 200:
            raise ValueError("No relevant postcode found.")      
    return location["result"][0]["postcode"]

    


def get_postcode_completions(postcode_start: str) -> list[str]:
    if not isinstance(postcode_start, str):
            raise TypeError("Function expects a string.")
    response = req.get(
        f"https://api.postcodes.io/postcodes/{postcode_start}/autocomplete")
    if response.status_code == 500:
        raise req.RequestException('Unable to access API.', 500)
    filled = response.json()
    return filled["result"]


def get_postcodes_details(postcodes: list[str]) -> dict:
    if not isinstance(postcodes, list) or not all(isinstance(p, str) for p in postcodes):
        raise TypeError("Function expects a list of strings.")
    response = req.post(
        f"https://api.postcodes.io/postcodes")
    if response.status_code == 500:
        raise req.RequestException('Unable to access API.', 500)
    details =response.json()
    return details["result"]