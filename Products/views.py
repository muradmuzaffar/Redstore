from django.shortcuts import render,HttpResponse,get_object_or_404,redirect,reverse

from .models import Product,Category,Comment

from .forms import AddProduct,CommentForm

from django.contrib.auth.decorators import login_required

from django.contrib import messages

from django.views.generic import UpdateView,CreateView

# Create your views here..

def index(request):
    product = Product.objects.all().order_by('-id')
    query = request.GET.get('q')
    if query:
        product = Product.objects.filter(name__icontains = query)

    return render(request , 'index.html' , {'product' : product})

def addproduct(request):
    form = AddProduct(request.POST or None,request.FILES or None)
    if form.is_valid():
        product = form.save(commit = False)
        product.user = request.user
        product.save()
        return redirect('index')
    return render(request , 'addproduct.html' , {'form' :form})

def detail(request , id):
    product = get_object_or_404(Product , id=id)
    comments = product.comments.all()
    return render(request,'detail.html',{'product' : product , 'comments':comments})


def dashboard(request):
    product = Product.objects.filter(user=request.user)
    # messages.error(request , 'There is no product. Click the Add Product button to add the product')
    return render(request , 'dashboard.html'  , {'product' : product})

def delete(request , id):
    product = get_object_or_404(Product,id=id)
    product.delete()
    
    return redirect('dashboard')

class update(UpdateView):
    model = Product
    fields = ['name' , 'describtion' ,'category' , 'price', 'image']
    template_name = 'update.html'

class AddCategoryView(CreateView):
    model = Category
    template_name = 'addcategory.html'
    fields = '__all__'

def CategoryView(request,cats):
    product = Product.objects.all().filter(category = cats)
    return render(request , 'categories.html' , {'product' : product , 'cats' :cats})
    
def comment(request,id):
    product = get_object_or_404(Product,id=id)
    if request.method == 'POST':
        name = request.POST.get('comment_author')
        text = request.POST.get('comment_text')

        product = get_object_or_404(Product,id=id)
        newComment = Comment(comment_author = name, comment_text = text)
        newComment.product = product
        newComment.save()    
        

    return redirect(reverse('detail' , kwargs={'id' : id}))



