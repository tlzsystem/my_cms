from sitesetting.models import SiteSetting

def siteinfo(request):
    return {'siteinfo': SiteSetting.objects.get(pk='app')}