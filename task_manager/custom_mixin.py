from django.contrib import messages
from django.shortcuts import redirect


class AuthenticationVerification:
    page_log = 'login'

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            messages.error(self.request, self.message_not_authenticated,)
            return redirect(self.redirect_url_not_authenticated)
        else:
            messages.error(self.request, self.memessage_not_login)
            return redirect(self.login_url)
