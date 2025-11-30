from datetime import datetime

from django.shortcuts import render


def home(request):
    """Render the marketing home page for Specc."""
    context = {
        "current_year": datetime.utcnow().year,
    }
    return render(request, "core/home.html", context)
