from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def github_webhook(request):

    if request.method == "POST":

        event = request.headers.get("X-GitHub-Event")

        if event == "pull_request":

            payload = json.loads(request.body)

            action = payload["action"]

            repository_name = payload["repository"]["name"]

            pr_number = payload["pull_request"]["number"]

            pr_title = payload["pull_request"]["title"]

            print("\n===== PULL REQUEST =====")
            print(f"Repository: {repository_name}")
            print(f"PR Number: {pr_number}")
            print(f"Title: {pr_title}")
            print(f"Action: {action}")
            print("========================\n")

        return JsonResponse({"status": "success"})

    return JsonResponse({"status": "invalid request"})


