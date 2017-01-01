from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from .models import Topic, Entry
from .forms import TopicForm, EntryForm


def index(request):
	topics=Topic.objects.order_by('-date_added')
	context={'topics':topics}
	return render(request, 'hems_blog/index.html', context)
def weather(request):
    return render(request, 'hems_blog/weather.html') 

def topics(request):
	topics=Topic.objects.order_by('-date_added')
	context={'topics':topics}
	return render(request, 'hems_blog/topics.html', context)

def topic(request, topic_id):
	topic=Topic.objects.get(id=topic_id)
	entries=topic.entry_set.order_by('-date_added')
	context={'topic':topic,'entries':entries}
	return render(request, 'hems_blog/topic.html', context)


def new_topic(request):
	if request.method !='POST':
		form=TopicForm()
	else:
		form=TopicForm(request.POST)
		if form.is_valid():
			new_topic=form.save(commit=False)
			new_topic.save()
			return HttpResponseRedirect(reverse('hems_blog:topics'))

	context = {'form': form}
	return render(request, 'hems_blog/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
	topic=Topic.objects.get(id=topic_id)
	entries=topic.entry_set.order_by('-date_added')
	if request.method != 'POST':
		form=EntryForm()
	else:
		form=EntryForm(data=request.POST)
		if form.is_valid():
			new_entry=form.save(commit=False)
			new_entry.topic=topic
			new_entry.owner = request.user
			new_entry.save()
			return HttpResponseRedirect(reverse('hems_blog:topic', args=[topic_id]))

	context = {'topic': topic, 'form': form, 'entries':entries}
	return render(request, 'hems_blog/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
	entry=Entry.objects.get(id=entry_id)
	topic=entry.topic
	if entry.owner != request.user:
		raise Http404

	if request.method != 'POST':
		form=EntryForm(instance=entry)
	else:
		form=EntryForm(instance=entry, data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('hems_blog:topic', args=[topic.id]))

	context={'entry': entry, 'topic': topic, 'form': form}
	return render(request, 'hems_blog/edit_entry.html', context)
