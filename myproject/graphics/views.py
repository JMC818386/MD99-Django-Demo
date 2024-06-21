# graphics/views.py
from django.http import JsonResponse, HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from .models import Graphic
import json
# import jmcauth
# import settings
from myproject import settings
from . import jmcauth



@csrf_exempt
def create_graphic(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            api_key = data.get('api_key')
            graphic_data = data.get('graphic_data')

            graphic = Graphic(api_key=api_key, graphic_data=graphic_data)
            graphic.save()
            return JsonResponse({"message": "Graphic created successfully."}, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Invalid request method."}, status=405)

def get_graphic(request, graphic_id, value):
    try:
        graphic = Graphic.objects.get(id=graphic_id)
        # Example: Render a dynamic graphic based on `value` and `graphic.graphic_data`
        # Placeholder response for dynamic rendering
        return JsonResponse({"graphic_id": graphic_id, "value": value, "graphic_data": graphic.graphic_data})
    except Graphic.DoesNotExist:
        raise Http404("Graphic not found")

def processUserRequest(userName):
    assetName = "Student Score"

    if userName == "Betty":
        bettyValue = 90

        url = jmcauth.getImageURL (settings.D99_PUBLIC_KEY, settings.D99_SECRET_KEY, bettyValue, assetName)
        return JsonResponse({"full_name": "Betty Smith", "url": url}, status=201)

    if userName == "Billy":
        billyValue = 50

        url = jmcauth.getImageURL (settings.D99_PUBLIC_KEY, settings.D99_SECRET_KEY, billyValue, assetName)

        return JsonResponse({"full_name": "Billy Johnson", "url": url}, status=201)

    return JsonResponse({"error": "(TIM) Invalid user name."}, status=405)

#--------------------------------------------------------------------

@csrf_exempt
def getImageUrl(request):
    if request.method == "POST":
        try:
            allData = json.loads(request.body)
            # return JsonResponse({"JSON": str(allData)}, status=201)
            # if 'data' not in allData:
                # return JsonResponse({"error":"Data(1) not found"}, status=405)

            # ourData = allData['data']
            if 'user_name' not in allData:
                return JsonResponse({"error":"(TIM) user_name not found"}, status=405)
            user_name = allData['user_name']
            
            return processUserRequest(user_name)

        except Exception as e:
            return JsonResponse({"error(in exception)": str(e)}, status=400)

    return JsonResponse({"error": "(TIM) Invalid request method."}, status=405)
