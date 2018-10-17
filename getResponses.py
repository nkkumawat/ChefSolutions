from customer.models import Customers, Address
from cart.models import Cart


def getResponse(request):
    data = {}
    if 'customer_id' in request.session:
        data['customer'] = Customers.objects.filter(
            id=request.session['customer_id'])[0]
        data['cart'] = Cart.objects.filter(
            customer_id=request.session['customer_id'])
    return data
