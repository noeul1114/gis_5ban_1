from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView

from articleapp.models import Article
from likeapp.models import LikeRecord


@method_decorator(login_required(login_url=reverse_lazy('accountapp:login')), 'get')
class LikeArticleView(RedirectView):
    def get(self, request, *args, **kwargs):
        user = request.user
        article = Article.objects.get(pk=kwargs['article_pk'])
        like_record = LikeRecord.objects.filter(user=user,
                                                article=article)
        if like_record.exists():
            # 좋아요가 반영 X
            messages.add_message(request, messages.ERROR, '좋아요는 한번만 가능합니다.')
            return HttpResponseRedirect(reverse('articleapp:detail',
                                                kwargs={'pk': kwargs['article_pk']}))
        else:
            LikeRecord(user=user, article=article).save()
        article.like += 1
        article.save()
        # 좋아요가 반영 O
        messages.add_message(request, messages.SUCCESS, '좋아요가 반영되었습니다.')
        return super().get(request, *args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        return reverse('articleapp:detail', kwargs={'pk': kwargs['article_pk']})

