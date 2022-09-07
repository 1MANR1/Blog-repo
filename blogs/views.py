from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import BlogPost

from .forms import BlogForm

def check_blog_owner(blog, request):
   """Make sure the topic blongs to the current topic."""
   if blog.owner != request.user:
        raise Http404

def blogs(request):
    """Show all blogs."""
    blogs = BlogPost.objects.filter(owner=request.user.id).order_by('date_added')
    context = {'blogs': blogs}
    return render(request, 'blogs/blogs.html', context)

@login_required
def new_blog(request):
	"""Creating new Blog"""

	if request.method != 'POST':
		# No data submitted; create a blank form.
		form = BlogForm()
	else:
		# POST data submitted; process data.
		form = BlogForm(data=request.POST)
		if form.is_valid():
			new_blog = form.save(commit=False)
			new_blog.save()
			return redirect('blogs:blogs')

	# Display a blank or invalid form.
	context = {'form': form}
	return render(request, 'blogs/new_blog.html', context)

@login_required
def edit_blog(request, blog_id):
	"""Edit an existing Blog."""
	blog = BlogPost.objects.get(id=blog_id)
	check_blog_owner(blog, request)

	if request.method != 'POST':
		# Initial request; pre-fill form with the current entry.
		form = BlogForm(instance=blog)
	else:
		# POST data submitted; process data.
		form = BlogForm(instance=blog, data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('blogs:blogs')
	
	context = {'blog': blog, 'form': form}
	return render(request, 'blogs/edit_blog.html', context)


