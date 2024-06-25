from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.views.decorators.http import require_GET


@require_GET
def add_messages(request: HttpRequest) -> HttpResponse:
    messages.info(request, "This is an info message.")
    messages.success(request, "This is a success message.")
    messages.warning(request, "This is a warning message.")
    messages.error(request, "This is an error message.")
    return HttpResponse()
