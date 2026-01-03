import requests

from rest_framework.decorators import api_view
from rest_framework.response import Response

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

@api_view(['GET'])
def test_api(request):
    QUERY = """
    query($showId: String!, $translationType: VaildTranslationTypeEnumType!, $episodeString: String!){
        episode(showId: $showId, translationType: $translationType, episodeString: $episodeString) {
            sourceUrls
        }
    }
    """
    VARIABLES = {
        "showId": "ReooPAxPMsHM4KPMY",
        "translationType": "sub",
        "episodeString": "1"
    }
    data = get_response_json(QUERY,VARIABLES)
    sourceUrls = data.get("data").get("episode").get("sourceUrls")
    sources = []
    for source in sourceUrls:
        if "--" in source.get("sourceUrl"):
            decryptedSource = decrypt(source.get("sourceUrl"))
            sources.append(f"{SERVER_END_POINT}{decryptedSource}".replace("clock", "clock.json") if "clock" in decryptedSource else decryptedSource)
    return Response({
        'data': sources
    })