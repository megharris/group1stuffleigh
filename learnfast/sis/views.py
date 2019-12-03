from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from shopping_cart.models import Order
from .forms import UserRegistrationForm
from django.contrib.auth.models import Group


@login_required
def student_home(request):
    return render(request, 'sis/student_home.html', {'sis': student_home})

@login_required
def tutor_list(request):
    tutor = Tutor.objects.filter(created_date__lte=timezone.now())
    return render(request, 'sis/tutor_list.html', {'tutors': tutor})

@login_required
def course_list(request):
    course = Course.objects.filter(created_date__lte=timezone.now())
    return render(request, 'sis/course_list.html', {'courses': course})

@login_required
def schedule_list(request):
    object_list = Schedule.objects.all()
    filtered_orders = Order.objects.filter(owner=request.user.profile, is_ordered=False)
    current_order_schedules = []
    if filtered_orders.exists():
        user_order = filtered_orders[0]
        user_order_items = user_order.items.all()
        current_order_schedules = [schedule.schedule for schedule in user_order_items]

    context = {
        'object_list': object_list,
        'current_order_schedules': current_order_schedules
    }

    return render(request, "sis/schedule_list.html", context)

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            group = Group.objects.get(name='student')
            # Set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            new_user.groups.add(Group.objects.get(name='student'))
            return render(request,
                          'sis/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                  'sis/register.html',
                  {'user_form': user_form})

def my_profile(request):
    my_user_profile = Profile.objects.filter(user=request.user).first()
    my_orders = Order.objects.filter(is_ordered=True, owner=my_user_profile)
    context = {
        'my_orders':my_orders
    }
    return render(request, "profile.html", context)


now = timezone.now()
def about_us(request):
    return render(request, 'sis/about_us.html', {'sis': about_us})

now = timezone.now()
def contact_us(request):
    return render(request, 'sis/contact_us.html', {'sis': contact_us})

@login_required
def tutor_dashboard(request):
    schedule = Schedule.objects.filter(schedule_tutor_name=request.user)
    return render(request, 'sis/tutor_dashboard.html', {'schedules': schedule})


@login_required
def tutor_home(request):
    return render(request, 'sis/tutor_home.html')


@login_required
def tutor_profile(request):
    tutor = Profile.objects.filter(user=request.user)
    return render(request, 'sis/tutor_profile.html', {'tutors': tutor})


@login_required
def tutor_courses(request):
    course = Course.objects.filter(created_date__lte=timezone.now())
    return render(request, 'sis/tutor_courses.html', {'courses': course})


@login_required
def tutor_rosters(request):
    student = Student.objects.filter(created_date__lte=timezone.now())
    return render(request, 'sis/tutor_rosters.html', {'students': student})


@login_required
def tutor_wage(request):
    student = Student.objects.filter(created_date__lte=timezone.now())
    course = Course.objects.filter(created_date__lte=timezone.now())
    schedule = Schedule.objects.filter(created_date__lte=timezone.now())
    sum_stud_name = Student.objects.filter(created_date__lte=timezone.now()).aggregate(Sum('stud_name'))
    return render(request, 'sis/tutor_wage.html', {'students': student, 'tutors': tutor, 'courses': course,
                                                 'schedules': schedule, 'sum_stud_name': sum_stud_name})


now = timezone.now()
def landing_page(request):
    return render(request, 'sis/landing_page.html', {'sis': landing_page})