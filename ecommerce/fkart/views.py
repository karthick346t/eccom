from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from .models import Product
from pymongo import MongoClient
import gridfs

def home(request):
    # Fetch products from Django DB
    products = Product.objects.all()

    # Fetch products from MongoDB
    mongo_products = mongo_collection.find()

    context = {
        'products': products,
        'mongo_products': mongo_products
    }

    return render(request, 'home.html', context)

def index(request):
    return render(request, "index.html")

# MongoDB setup
mongo_client = MongoClient('mongodb+srv://admin:admin@ecommerce.sznln.mongodb.net/?retryWrites=true&w=majority&appName=ecommerce')
mongo_db = mongo_client['ecom']  # MongoDB database
mongo_collection = mongo_db['product']  # MongoDB collection

def add_product(request):
    if request.method == 'POST':
        # Get data from the form (assuming you have a form in home.html)
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        stock = request.POST.get('stock')

        # Save to Django DB
        product = Product(name=name, description=description, price=price, stock=stock)
        product.save()

        # Save to MongoDB
        mongo_collection.insert_one({
            'name': name,
            'description': description,
            'price': float(price),
            'stock': int(stock)
        })

        return redirect('home')  # Redirect to the home page or some other page

    return render(request, 'add_product.html')
