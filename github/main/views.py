# views.py file
from django.http import HttpResponse

from .models import PullRequest


def index(request):
    if request.method == 'POST':
        # Process the webhook payload
        payload = request.POST

        # Extract pull request details from the payload
        title = payload['pull_request']['title']
        url = payload['pull_request']['url']

        # Save the pull request details to the database
        pull_request = PullRequest.objects.create(title=title, url=url)

        # Return a success response
        return HttpResponse('Webhook received and processed successfully.')
    else:
        # Return a 405 Method Not Allowed response for other HTTP methods
        return HttpResponse("tech with team")

