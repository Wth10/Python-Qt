import httpx

url_base = "https://covid19-brazil-api.vercel.app/api/report/v1"


def connectionApi(url):
    request = httpx.get(url)
    response = request.json()
    return response


class API:
    def getAll():
        return connectionApi(url_base)
