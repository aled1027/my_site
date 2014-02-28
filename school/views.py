import time
from calendar import month_name

from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import get_object_or_404, render_to_response, render
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse

# for pdfs
from reportlab.pdfgen import canvas
from django.http import HttpResponse

# my stuff
from school.models import *
from school.forms import *

def school_home(request):
	return render(request, "school_home.html", {})

def course_list(request):
	coursees = Course.objects.all()
	return render(request, "course_list.html", {"course_list": coursees})

def course_detail(request, c_id):
	c = get_object_or_404(Course, pk=c_id)
	return render(request, "course_detail.html", {"course": c})

def course_delete(request, c_id):
	c = get_object_or_404(Course, pk=c_id)
	c.delete()
	return HttpResponseRedirect(reverse('school_course_list'))


def course_form(request, c_id=None):
	if c_id:
		c = Course.objects.get(pk=c_id)
	else:
		c = None
	if request.method == "POST":
		form = CourseForm(request.POST, request.FILES, instance=c)
		if form.is_valid():
			instance = form.save()
			return HttpResponseRedirect(reverse('school_course_detail', args=(instance.id,)))
	else:
		form = CourseForm(instance=c)
	return render(request, 'course_form.html', {'form': form})

def homework_detail(request, c_id, h_id):
	h = get_object_or_404(Homework, pk=h_id)
	return render(request, "homework_detail.html", {"homework": h})

def homework_delete(request, c_id, h_id):
	h = get_object_or_404(Homework, pk=h_id)
	h.delete()
	return HttpResponseRedirect(reverse('school_course_list'))

def homework_form(request, c_id=None, h_id=None):
	if h_id:
		homework = Homework.objects.get(pk=h_id)
	else:
		homework = None
	if request.method == "POST":
		form = HomeworkForm(request.POST, request.FILES, instance=homework)
		if form.is_valid():
			#instance = Homework(file_field=request.FILES['file'])
			instance = form.save()
			return HttpResponseRedirect(reverse('school_homework_detail', args=(c_id, instance.id,)))
	else:
		form = HomeworkForm(instance=homework)
	return render(request, 'homework_form.html', {'form': form})

def program_detail(request, c_id, h_id, p_id):
	program = get_object_or_404(Program, pk=p_id)
	return render(request, "program_detail.html", {"program": program})

def program_form(request, c_id=None, h_id=None, p_id=None):
	if p_id:
		program = Homework.objects.get(pk=p_id)
	else:
		program = None
	if request.method == "POST":
		form = ProgramForm(request.POST, request.FILES, instance=program)
		if form.is_valid():
			instance = form.save()
			return HttpResponseRedirect(reverse('school_program_detail', args=(c_id, h_id, instance.id)))
	else:
		form = ProgramForm(instance=program)
	return render(request, 'program_form.html', {'form': form})


def upload_file(request):
	if request.method == "POST":
		form = UploadFileForm(request.POST, request.FILES)
		if form.is_valid():
			handle_uploaded_file(request.FILES['file'])
			return HttpResponseRedirect(reverse('blog_home'))
	else:
		form = UploadFileForm()
	return render(request, 'upload_form.html', {'form': form})


def save_a_pdf(request):
	response = HttpResponse(mimetype='application/pdf')
	response['Content-Disposition'] = 'attachment; filename=hello.pdf'

	p = canvas.Canvas(response)
	p.drawString(100,100,"Hello world")
	p.showPage()
	p.save()
	return response


