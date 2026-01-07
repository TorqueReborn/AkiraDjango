from .utils import decrypt, get_response_json
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def recent(request):
    QUERY = """
    query($search: SearchInput!){
        shows(search: $search) {
            edges {
                _id,name,englishName,thumbnail
            }
        }
    }
    """
    VARIABLES = {
        "search": {
            "sortBy": "Recent"
        }
    }
    response = get_response_json(QUERY,VARIABLES)
    edges = response["data"]["shows"]["edges"]

    fixed_thumbnails = [
        {
            **edge,
            "englishName": edge["englishName"] or edge["name"],
            "thumbnail": edge["thumbnail"]
            if edge["thumbnail"].startswith("http")
            else f"https://wp.youtube-anime.com/aln.youtube-anime.com/{edge['thumbnail']}"
        }
        for edge in edges
    ]
    return Response(fixed_thumbnails)