def get_agent(request):
    agent = request.META.get('HTTP_USER_AGENT', 'Anonymous')
        
    if "Android" in agent:
        agent = "Android"
    elif "Windows" in agent:
        agent = "Windows"
    elif "Linux" in agent:
        agent = "Linux"
    elif "Mac" in agent:
        agent = "macOS"
    else:
        agent = "Anonynous"
    
    return agent