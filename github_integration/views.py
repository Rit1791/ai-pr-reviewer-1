from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def github_webhook(request):
    if request.method == "POST":

        event = request.headers.get("X-GitHub-Event")

        print(f"GitHub Event: {event}")

        if event == "pull_request":
            print("PULL REQUEST EVENT RECEIVED")

        return JsonResponse({"status": "success"})

    return JsonResponse({"status": "invalid request"})

