from django.shortcuts import render, redirect

# Create your views here.
from .models import CouponCodes

def checkCoupon(request):
    if 'customer_id' in request.session:
        if request.method== "POST":
            coupon_code_number = request.POST['coupon_code']
            coupon_code = CouponCodes.objects.filter(coupon_code=coupon_code_number, is_applied=False)
            if coupon_code:
                request.session['coupon_code_id'] = coupon_code[0].id
                coupon_code.update(is_applied = True)
            return redirect("cart:cart")
        else:
            return redirect("error:error")
    else:
        return redirect("error:error")
def removeCoupon(request):
    if 'customer_id' in request.session:
        if request.method == "POST":
            coupon_code_number = request.POST['coupon_code_id']
            if 'coupon_code_id' in request.session:
                if int(request.session['coupon_code_id']) == int(coupon_code_number):
                    print("nk")
                    coupon_code = CouponCodes.objects.filter(id=request.session['coupon_code_id'])
                    if coupon_code:
                        print("kk")
                        del request.session['coupon_code_id']
                        coupon_code.update(is_applied=False)
                return redirect("cart:cart")
        else:
            return redirect("error:error")
    else:
        return redirect("error:error")