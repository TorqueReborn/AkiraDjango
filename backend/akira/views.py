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

@api_view(['GET'])
def trending(request):
    QUERY = """
        query($type: VaildPopularTypeEnumType!, $size: Int!, $dateRange: Int!){
            queryPopular(type: $type, size: $size, dateRange: $dateRange) {
                recommendations {
                    anyCard {
                        _id,name,englishName,thumbnail,banner
                    }
                }
            }
        }
    """
    VARIABLES = {
        "type": "anime",
        "size": 20,
        "dateRange": 1
    }
    response = get_response_json(QUERY,VARIABLES)
    return Response(item['anyCard'] for item in response['data']['queryPopular']['recommendations'])

@api_view(['GET'])
def spotlight(request):
    QUERY = """
        query($type: VaildPopularTypeEnumType!, $size: Int!, $dateRange: Int!){
            queryPopular(type: $type, size: $size, dateRange: $dateRange) {
                recommendations {
                    anyCard {
                        _id
                    }
                }
            }
        }
    """
    VARIABLES = {
        "type": "anime",
        "size": 20,
        "dateRange": 1
    }
    response = get_response_json(QUERY,VARIABLES)
    recommendations = response['data']['queryPopular']['recommendations']
    ids = [recommendation['anyCard']['_id'] for recommendation in recommendations]
    QUERY = """
        query($ids: [String!]!){
            showsWithIds(ids: $ids) {
                _id,name,englishName,banner
            }
        }
    """
    VARIABLES = {
        "ids": ids
    }
    response = get_response_json(QUERY,VARIABLES)
    return Response(response)