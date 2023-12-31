from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.forms.models import BaseModelForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LogoutView

# Create your views here.


class SignupView(CreateView):
    app_name = "accounts"
    form_class = UserCreationForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("top") # ここでエラー出る.

    def form_valid(self, form: BaseModelForm):
        user = form.save()
        login(self.request, user)
        messages.add_message(self.request, messages.SUCCESS,"ユーザー登録しました。")

        self.object = user
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self
                     , form):
        messages.add_message(self.request, messages.ERROR,"ユーザー登録に失敗しました。")
        return super().form_invalid(form)

class CustomLogoutView(LogoutView):
    # ログアウト後のリダイレクト先を指定するためのget_success_urlメソッドをオーバーライドします。
    def get_success_url(self):
        # ログアウト後にリダイレクトしたいURLを指定します。
        return reverse_lazy('top')  # このURLをカスタマイズしてください
