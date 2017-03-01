from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.views.generic.edit import View
from .forms import PostForm
from .models import Post

class Welcome(View):
      def get(self, request):
          """
          Fetch all posts and render full index page with form
          """
          context = {
              'posts': Post.objects.all(),
              'new_post_form' : PostForm()
          }
          return render(request, 'ajax_posts/index.html', context)

class Posts(View):
      def get(self, request):
          context = {
              'posts': Post.objects.all()
          }
          print "I'm in Posts>get"
          return render(request, 'ajax_posts/posts_index.html', context)

      def post(self, request):
          form = PostForm(request.POST)

          if form.is_valid():
              Post.objects.create(
                  description=request.POST['description']
                )
          return redirect(reverse('ajax_posts:posts'))
