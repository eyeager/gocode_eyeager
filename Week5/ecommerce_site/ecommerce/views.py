from django.shortcuts import render, redirect
from ecommerce.models import Product, Order, Customer, State, OrderProduct
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q,F,Sum
from django.core import serializers
from django.contrib.auth.models import User

from django.http import HttpResponse

# Create your views here.
def index(request):
	all_products = Product.objects.all()

	search = request.GET.get('search')
	if search:
		all_products = all_products.filter(Q(name__icontains=search) | Q(description__icontains=search))

	filters = {}
	filters["1"] = {"filter_data" : all_products.filter(price__lte=50), "text" : "$0 to $50"}
	filters["2"] = {"filter_data" : all_products.filter(price__gte=50, price__lte=100), "text" : "$50 to $100"}
	filters["3"] = {"filter_data" : all_products.filter(price__gte=100, price__lte=200), "text" : "$100 to $200"}
	filters["4"] = {"filter_data" : all_products.filter(price__gte=200), "text" : "$200 and up"}

	filter_query = request.GET.get('filter')
	if filter_query:
		all_products = filters[filter_query]["filter_data"]

	paginator = Paginator(all_products,10)
	page = request.GET.get('page')
	try:
		products = paginator.page(page)
	except PageNotAnInteger:
		products = paginator.page(1)
	except EmptyPage:
		products = paginator.page(paginator.num_pages)

	format_json = request.GET.get('format')
	if format_json == "json":
		json_data = serializers.serialize("json",all_products)
		return HttpResponse(json_data,content_type='application/json')

	return render(request, 'ecommerce/product_index.html',{"products" : products, "filters": filters ,"page_array": range(1,paginator.num_pages+1)})

def product(request,num):
	product_data = Product.objects.get(pk=num)

	return render(request, 'ecommerce/product_description.html',{"ID" : product_data.id ,"Name":product_data.name, "Description": product_data.description,"Price": "{0:.2f}".format(product_data.price)})

def add_to_cart(request,num):
	product_data = Product.objects.get(pk=num)

	quantity = int(request.POST["quantity"])
	open_order = Order.objects.filter(status__id = 1)
	open_order = open_order[0]

	open_orderproduct = OrderProduct.objects.filter(order = open_order, product = product_data)
	if open_orderproduct:
			open_orderproduct[0].quantity += quantity
			open_orderproduct[0].save()
	else:
		new_orderproduct = OrderProduct.objects.create(order = open_order, product = product_data, quantity = quantity)

	return redirect('cart')

def remove_from_cart(request,num):
	orderproduct_data = OrderProduct.objects.get(id = num)

	orderproduct_data.delete()

	return redirect('cart')

def cart(request):
	order = Order.objects.get(status__id = 1)
	cart_items = OrderProduct.objects.filter(order = order)

	total = cart_items.aggregate(total=Sum(F('product__price') * F('quantity')))['total']

	return render(request, 'ecommerce/cart.html',{"products" : cart_items, "total" : total})

def check_out(request):
	order = Order.objects.filter(status__id = 1)[0]
	order.status = State.objects.get(pk=2)
	order.save()

	order_state = State.objects.get(pk=1)
	order_customer = Customer.objects.get(pk=1)
	new_order = Order.objects.create(status=order_state, customer = order_customer)
	return redirect('index')

def signup(request):
	return render(request, 'ecommerce/signup.html',{})

def register(request):
	first_name = request.POST["first_name"]
	last_name = request.POST["last_name"]
	address = request.POST["address"]
	city = request.POST["city"]
	state_name = request.POST["state_name"]
	zip_code = request.POST["zip_code"]
	username = request.POST["username"]
	email = request.POST["email"]
	password = request.POST["password"]

	user = User.objects.create_user(first_name = first_name, last_name = last_name, username = username, email = email, password = password, address = address, city = city, state = state_name, zip_code = zip_code)

	return redirect('index')

def login(request):
	return render(request, 'ecommerce/login.html',{})

def login_user(request):
	pass

def my_account(request):
	pass

def logout(request):
	return redirect('index')
