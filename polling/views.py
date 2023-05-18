from django.shortcuts import render
from polling.models import Poll
from django.http import Http404


def list_view(request):
    context = {'polls': Poll.objects.all()}
    return render(request, 'polling/list.html', context)
    # we are using list.html, and pass the context as well
    # for all elements returned by db query above pass to the list.html template
    # how you pass variables to your templates
    # when we look at list template we have an element called polls
    # what is the name this context will see for this element? called polls


# Create your views here.


def detail_view(request, poll_id):
    try:
        poll = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist:
        raise Http404

    if request.method == "POST":
        if request.POST.get("vote") == "Yes":
            poll.score += 1
        else:
            poll.score -= 1
        poll.save()

    context = {'poll': poll}
    return render(request, 'polling/detail.html', context)
