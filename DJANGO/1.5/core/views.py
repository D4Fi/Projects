from django.shortcuts import render
from core.models import Post
from . import forms



def home(request):

    if request.method == 'GET':

        pessoa = Post.objects.all()
        form = forms.UserPost()
        context ={'pessoa': pessoa,'form': form}
        return render(request, 'core/pages/index.html', context=context)

    elif request.method == 'POST':

        form = forms.UserPost(request.POST)
        if form.is_valid:

            form.save()
            pessoa = Post.objects.all()
            form = forms.UserPost()
            context ={'pessoa': pessoa,'form': form}
            return render(request, 'core/pages/index.html', context=context)

        else:
            pass
