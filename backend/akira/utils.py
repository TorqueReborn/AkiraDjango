import requests

SERVER_END_POINT = "https://allanime.day"
API_END_POINT = "https://api.allanime.day/api"

def decrypt(hex_str: str) -> str:
    result = ""
    for i in range(2, len(hex_str), 2):
        byte = int(hex_str[i:i+2], 16) ^ 56
        result += chr(byte)
    return result

def get_response_json(query: str, variables: dict):
    response = requests.post(
        API_END_POINT,
        headers={"Content-Type": "application/json"},
        json={
            "query": query,
            "variables": variables
        }
    )
    return response.json()