# Create your views here.
from django.shortcuts import render, redirect  
from BlogApp.forms import BlogForm  
from BlogApp.models import Blog  
# Create your views here.  
def emp(request):  
    if request.method == "POST":  
        form = BlogForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = BlogForm()  
    return render(request,'index.html',{'form':form})  
def show(request):  
    theblog = Blog.objects.all()  
    return render(request,"show.html",{'theblog':theblog})  
def edit(request, id):  
    ablog = Blog.objects.get(id=id)  
    return render(request,'edit.html', {'ablog':ablog})  
def update(request, id):  
    ablog = Blog.objects.get(id=id)  
    # print("entered")
    if request.method == "POST":
        form = BlogForm(request.POST, instance=ablog)  
        if form.is_valid():
            # print("form is")  
            form.save()  
            return redirect("/show")
        else:
            print("form errors:",form.errors)
    else:
        form = BlogForm(instance=ablog)
    return render(request, 'edit.html', {'ablog': ablog, 'form': form})   
def destroy(request, id):  
    ablog = Blog.objects.get(id=id)  
    ablog.delete()  
    return redirect("/show")  