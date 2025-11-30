from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import TemplateView


class GoogleOAuthLoginView(TemplateView):
	"""Display a single entry point for Google-based authentication."""

	template_name = "accounts/login.html"

	def dispatch(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect("core:home")
		return super().dispatch(request, *args, **kwargs)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		google_login_url = reverse("google_login")
		context.update(
			{
				"google_login_url": google_login_url,
				"google_signup_url": f"{google_login_url}?process=signup",
			}
		)
		return context


def signup_redirect(request):
	"""Send users straight into the Google OAuth signup flow."""

	if request.user.is_authenticated:
		return redirect("core:home")

	google_signup_url = f"{reverse('google_login')}?process=signup"
	return redirect(google_signup_url)
