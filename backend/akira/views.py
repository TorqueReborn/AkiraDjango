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
    response = response['data']['showsWithIds']
    filtered_data = [item for item in response if item.get("banner")]
    return Response(filtered_data)

@api_view(['GET'])
def details(request):
    QUERY = """
        query($id: String!){
            show(_id: $id) {
                _id,name,englishName,thumbnail,description,availableEpisodesDetail
            }
        }
        """
    VARIABLES = {
        "id": request.GET.get('id')
    }
    response = get_response_json(QUERY,VARIABLES)
    return Response(response['data']['show'])

@api_view(['GET'])
def watch(request):
    QUERY = """
    query($showId: String!, $translationType: VaildTranslationTypeEnumType!, $episodeString: String!){
        episode(showId: $showId, translationType: $translationType, episodeString: $episodeString) {
            episodeString,
            sourceUrls,
            episodeInfo{
                thumbnails,
                description,
                vidInforssub,
                vidInforsdub
            },
        }
    }
    """
    VARIABLES = {
        "showId": request.GET.get('id'),
        "translationType": 'sub',
        "episodeString": '1'
    }
    response = get_response_json(QUERY,VARIABLES)
    sourceUrls = response['data']['episode']['sourceUrls']
    sources = []
    for source in sourceUrls:
        if "--" in source['sourceUrl']:
            decrypted = decrypt(source['sourceUrl'])
            if not "https" in decrypted:
                sources.append("https://allanime.day" + decrypt(source['sourceUrl']).replace("clock", "clock.json"))
    return Response(sources)