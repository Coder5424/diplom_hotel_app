import csv
import datetime
import xlwt
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, FormView
from .forms import CheckInForm, GetDataForm
from hotel.models import Booking
from userlogin.models import User
from .models import CheckIn
from .checkin.checkin_avail import check_checkin_avail
from datetime import date


def booking_list_view(request):
    firstname = request.GET.get('search_booking')
    booking_list = []
    bookings = Booking.objects.filter(firstname__iregex=firstname)
    for booking in bookings:
        booking_url = reverse('adminworkenv:CheckInView', kwargs={
            'firstname': booking.firstname,
            'lastname': booking.lastname,
            'email': booking.email,
            'phone_number': booking.phone_number,
            'room': booking.room.number,
            'check_in': booking.check_in,
            'check_out': booking.check_out,
        })
        booking_list.append((booking, booking_url))

    context = {'booking_list': booking_list}

    return render(request, 'adminworkenv/booking_list.html', context)


def admin_page_view(request):
    return render(request, 'adminworkenv/admin_page.html')


def search_bookings_view(request):
    return render(request, 'adminworkenv/search_bookings.html')


class CheckInView(FormView):
    form_class = CheckInForm
    template_name = 'adminworkenv/checkin.html'

    def get(self, request, *args, **kwargs):
        firstname = self.kwargs.get('firstname', None)
        lastname = self.kwargs.get('lastname', None)
        email = self.kwargs.get('email', None)
        phone_number = self.kwargs.get('phone_number', None)
        room = self.kwargs.get('room', None)
        check_in = self.kwargs.get('check_in', None)
        check_out = self.kwargs.get('check_out', None)

        booking = Booking.objects.get(
            email=email,
            phone_number=phone_number,
            room=room,
            check_in=check_in,
            check_out=check_out
        )

        context = {
            'firstname': firstname,
            'lastname': lastname,
            'email': email,
            'phone_number': phone_number,
            'room': room,
            'check_in': check_in,
            'check_out': check_out
        }

        try:
            user = User.objects.get(
                firstname=firstname,
                lastname=lastname,
                email=email,
                phone_number=phone_number,
            )
            user_passport = user.passport
            if user_passport:
                context['passport'] = user_passport

        except ObjectDoesNotExist:
            pass

        return render(request, 'adminworkenv/checkin.html', context)

    def form_valid(self, form):
        data = form.cleaned_data

        check_in = data['check_in']
        check_out = data['check_out']

        if (check_in <= check_out) and (check_in >= date.today()):
            if check_checkin_avail(data['room'], check_in, check_out):
                checkin = CheckIn.objects.create(
                    firstname=data['firstname'],
                    lastname=data['lastname'],
                    email=data['email'],
                    phone_number=data['phone_number'],
                    passport=data['passport'],
                    room=data['room'],
                    check_in=check_in,
                    check_out=check_out,
                )

                checkin.save()

                try:
                    user = User.objects.get(
                        email=data['email'],
                        phone_number=data['phone_number'],
                    )

                    if not user.passport:
                        user_passport = data['passport']
                        user.passport = user_passport
                        user.save()

                except ObjectDoesNotExist:
                    pass

                return HttpResponse(checkin)

            else:
                return HttpResponse('No')

        else:
            return HttpResponse('Date Error')


class GetDataView(FormView):
    form_class = GetDataForm
    template_name = 'adminworkenv/get_data.html'

    def form_valid(self, form):
        data = form.cleaned_data

        check_in_down = data['check_in_down']
        check_in_up = data['check_in_up']

        if check_in_down <= check_in_up:
            checkin_list = CheckIn.objects.filter(check_in__lte=check_in_up, check_in__gte=check_in_down).order_by('check_in')

            context = {'checkin_list': checkin_list}

            return render(self.request, 'adminworkenv/get_data_list.html', context)

        else:
            return HttpResponse('Date Error')


class GetExcelView(FormView):
    form_class = GetDataForm
    template_name = 'adminworkenv/get_excel.html'

    def form_valid(self, form):
        data = form.cleaned_data

        check_in_down = data['check_in_down']
        check_in_up = data['check_in_up']

        if check_in_down <= check_in_up:
            response = HttpResponse(content_type='application/ms-excel')
            response['Content-Disposition'] = "attachment; filename=export_" + \
                                              str(datetime.datetime.now()) + ".xls"

            wb = xlwt.Workbook(encoding='utf-8')
            ws = wb.add_sheet('CheckIn Data')

            row_num = 0

            font_style = xlwt.XFStyle()
            font_style.font.bold = True

            columns = ['First Name', 'Last Name', 'Email Address', ]

            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], font_style)

            font_style = xlwt.XFStyle()

            checkin_list = CheckIn.objects.filter(check_in__lte=check_in_up, check_in__gte=check_in_down).order_by(
                'check_in').values_list('firstname', 'lastname', 'email')

            for checkin in checkin_list:
                row_num += 1
                for col_num in range(len(checkin)):
                    ws.write(row_num, col_num, checkin[col_num], font_style)

            wb.save(response)

            return response

        else:
            return HttpResponse('Date Error')

