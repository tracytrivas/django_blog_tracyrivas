from django.shortcuts import render
from django.http.response import HttpResponse, Http404
from blogging.models import Post
from django.template import loader


def stub_view(request, *args, **kwargs):
    body = "Stub View\n\n"
    if args:
        body += "Args: \n"
        body += "\n".join(["\t%s" % a for a in args])
    # else:
    if kwargs:
        body += "Kwargs:\n"
        body += "\n".join(["\t%s: %s" % a for a in kwargs.items()])
        return HttpResponse(body, content_type="text/plain")


def list_view(request):
    published = Post.objects.exclude(published_date__exact=None)
    # published = Post.title
    posts = published.order_by('published_date')
    # posts = published
    # template = loader.get_template("blogging/list.html")
    context = {'posts': posts}
    # body = template.render(context)
    # return HttpResponse(body, content_type="text/html")
    return render(request, 'blogging/list.html', context)


def detail_view(request, post_id):
    published = Post.objects.exclude(published_date__exact=None)
    try:
        post = published.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404
    context = {'post': post}
    return render(request, 'blogging/templates/detail.html', context)
