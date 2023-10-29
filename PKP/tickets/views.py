from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views import generic
from django.utils import timezone

from .models import Ticket

def check_ticket_to_delete(ticket):
    if ticket.ticket_ulgowy <= 0 and ticket.ticket_szybki <= 0 and ticket.ticket_dzieci <= 0:
        return True
    if ticket.start < timezone.now():
        return True
    return False

def index(request):
    return render(request, 'pages/index.html')

class IndexView(generic.ListView):
    template_name = 'tickets/index.html'
    context_object_name = 'tickets'

    def post(self, *args):
        queryset = Ticket.objects.order_by('start')
        przyjazd_place_lock = False
        odjazd_place_lock = False
        przyjazd_date_lock = False
        odjazd_date_lock = False

        przyjazd_place = self.request.POST.get('przyjazd-place').capitalize() 
        odjazd_place = self.request.POST.get('odjazd-place').capitalize() 
        przyjazd_date = self.request.POST.get('date-time-przyjazd')
        odjazd_date = self.request.POST.get('date-time-odjazd')

        # Helpful if statemant for Ticekt Sorter
        if przyjazd_place == '':
            przyjazd_place_lock = True
        if odjazd_place == '':
            odjazd_place_lock = True
        if odjazd_date == '':
            odjazd_date_lock = True
        if przyjazd_date == '':
            przyjazd_date_lock = True

        # Check if the przyjazd or odjazd is valid
        if przyjazd_date == '' and odjazd_date == '' and przyjazd_place == '' and odjazd_place == '':
            messages.add_message(self.request, messages.ERROR, 'You have not entried any values to search')
            return HttpResponseRedirect(self.request.META.get('HTTP_REFERER','/'))

        elif ((odjazd_date < timezone.now().isoformat() and odjazd_date_lock == False) or
        (przyjazd_date < timezone.now().isoformat() and przyjazd_date_lock == False) or 
        (przyjazd_date < odjazd_date and przyjazd_date_lock == False) or
        (odjazd_date == przyjazd_date and (przyjazd_date_lock == False or odjazd_date_lock == False)) or 
        (przyjazd_place == odjazd_place and (przyjazd_place_lock == False or odjazd_place_lock == False))):
            messages.add_message(self.request, messages.ERROR, 'You have entried incorrect values')
            return HttpResponseRedirect(self.request.META.get('HTTP_REFERER','/'))

        # Ticket Sorter
        for ticket in queryset:
            if check_ticket_to_delete(ticket):
                ticket.delete()

            if odjazd_place_lock == False and not(ticket.from_place == odjazd_place):
                queryset = queryset.exclude(from_place=str(ticket.from_place))
            if  przyjazd_place_lock == False and not(ticket.to_place == przyjazd_place):
                queryset = queryset.exclude(to_place=str(ticket.to_place))
            if przyjazd_date_lock == False and ticket.end.isoformat() > przyjazd_date:
                queryset = queryset.exclude(end=str(ticket.end))
            if odjazd_date_lock == False and ticket.start.isoformat() < odjazd_date:
                queryset = queryset.exclude(start=str(ticket.start))

        return render(self.request, 'tickets/index.html', context={ 'tickets': queryset })

    def get_queryset(self):
        queryset = Ticket.objects.order_by('start')
        for ticket in queryset:
            if check_ticket_to_delete(ticket):
                ticket.delete()
        return queryset

class DetailView(generic.DetailView):
    template_name = 'tickets/detail.html'

    def get_object(self):
        id = self.kwargs.get('id')
        return get_object_or_404(Ticket, id=id)

class BuyView(generic.View):
    template_name = 'tickets/buyTicket.html'
    model = Ticket
    lookup = 'id'

    def get_object(self):
        lookup = self.kwargs.get(self.lookup)
        obj = None
        if lookup is not None:
            obj = get_object_or_404(self.model, id=lookup)
        return obj

    def get(self, request, id=None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            context['ticket'] = obj
        return render(request, self.template_name, context)

@login_required
def buy(request, id):
    ticket = get_object_or_404(Ticket, id=id)
    user = request.user
    if request.method == 'POST':
        ticket_ulgowy = request.POST.get('ulgowy')
        ticket_szybki = request.POST.get('szybki')
        ticket_dzieci = request.POST.get('dzieci')
        if (ticket_ulgowy == None): ticket_ulgowy = '0'
        if (ticket_szybki == None): ticket_szybki = '0'
        if (ticket_dzieci == None): ticket_dzieci = '0'

        if ticket_ulgowy == '0' and ticket_szybki == '0' and ticket_dzieci == '0':
            messages.add_message(request, messages.ERROR, 'To buy some tickets you have to choose some of them')
        else:
            # Sum price of tickets what a user wants to buy
            bought_tickets_price = (int(ticket_ulgowy)* ticket.ticket_ulgowy_price) + (int(ticket_szybki)* ticket.ticket_szybki_price) + (int(ticket_dzieci)* ticket.ticket_dzieci_price)
    
            if user.wallet < bought_tickets_price:
                messages.add_message(request, messages.ERROR, f'You do not possess enough money to buy this ticket. Your wallet: {str(user.wallet)}, and tickets price: {str(bought_tickets_price)}')
            else:
                user.wallet -= bought_tickets_price

                messages.add_message(request, messages.SUCCESS, 'Sccessfully you bought your tickets')
                messages.add_message(request, messages.SUCCESS, f'Price you have spent: {bought_tickets_price}. Your wallet: {user.wallet}')
                ticket.ticket_ulgowy -= int(ticket_ulgowy)
                ticket.ticket_szybki -= int(ticket_szybki)
                ticket.ticket_dzieci -= int(ticket_dzieci)
                ticket.save()
                user.save()
                if check_ticket_to_delete(ticket):
                    ticket.delete()
                    messages.add_message(request, messages.INFO, 'That ticket has been just deleted')
                    return HttpResponseRedirect(reverse('tickets:index'))

                return redirect('../../') 
    return redirect('../')