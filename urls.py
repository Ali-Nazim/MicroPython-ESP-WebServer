import views

# Defining URLs
URLS = {
    '/OPEN_DOOR': views.OPEN_DOOR,
}


# You can edit this only if you send parameters in the URL
def router(request):
    # Getting URL Path
    path = request.split()[1]
    path_parts = path.split('?')

    # Getting First Part
    url = path_parts[0]
    view_function = URLS.get(url, -1)

    # Check if URL is valid
    if view_function != -1:
        view_function()

    return views.WEB_PAGE()