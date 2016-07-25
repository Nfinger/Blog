from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import View
from django.contrib.auth.hashers import make_password,check_password
from .models import (
	Members,
	Post,
	Comment
	)
# Create your views here.

class Login(View):
	template_name = "blog/login.html"

	def get(self,request):
		return render(request,self.template_name)

	def post(self,request):
		username = request.POST["username"]
		member = get_object_or_404(Members,username=username)
		if check_password(request.POST["password"],member.password):
			if member.is_active:
				request.session['member_id'] = member.id
				return redirect("start:home")

		else:
			return render(request,self.template_name,{"error":"Invalid username or password"})

class Logout(View):
	def get(self,request):
		del request.session['member_id']
		return redirect("start:login")


class NewUser(View):
	template_name = "blog/new_user.html"

	def get(self,request):
		return render(request,self.template_name)

	def post(self,request):
		first_name = request.POST["first_name"]
		last_name = request.POST["last_name"]
		username = request.POST["username"]
		password = make_password(request.POST["password"])
		Members.objects.create(first_name=first_name,last_name=last_name,username=username,password=password)
		member = get_object_or_404(Members,username=username)
		request.session['member_id'] = member.id
		return redirect("start:home")

class Home(View):
	template_name = "blog/home.html"

	def get(self,request):
		posts = Post.objects.filter(is_active=True)
		return render(request,self.template_name,{"posts":posts})

class NewPost(View):
	template_name = "blog/new_post.html"

	def get(self,request):
		return render(request,self.template_name)

	def post(self,request):
		title = request.POST["title"]
		content = request.POST["content"]
		member = get_object_or_404(Members,pk=request.session['member_id'])
		Post.objects.create(title=title,content=content,author=member.first_name,member=member)
		return redirect("start:home")

class Article(View):
	template_name = "blog/article.html"

	def get(self,request,pk):
		post = get_object_or_404(Post,pk=pk)
		comments = Comment.objects.filter(post=post)
		return render(request,self.template_name,{"post":post,"comments":comments})

class NewComment(View):

	def post(self,request,pk):
		member = get_object_or_404(Members,pk=request.session['member_id'])
		post = get_object_or_404(Post,pk=pk)
		Comment.objects.create(content=request.POST["comment"],author=member.first_name,member=member,post=post)
		return redirect("start:article",pk=pk)

class Delete(View):

	def get(self,request,pk):
		post = get_object_or_404(Post,pk=pk)
		member = get_object_or_404(Members,pk=request.session['member_id'])
		if post.member == member:
			post.is_active = False
			post.save()
			return redirect("start:home")
		else:
			template_name = "blog/home.html"
			posts = Post.objects.filter(is_active=True)
			return render(request,template_name,{"posts":posts,"error":"Unauthorized Access"})
		

class Update(View):
	template_name="blog/update.html"

	def get(self,request,pk):
		post = get_object_or_404(Post,pk=pk)
		member = get_object_or_404(Members,pk=request.session['member_id'])
		if post.member == member:
			return render(request,self.template_name,{"post":post})
		else:
			self.template_name = "blog/home.html"
			posts = Post.objects.filter(is_active=True)
			return render(request,self.template_name,{"posts":posts,"error":"Unauthorized Access"})

	def post(self,request,pk):
		post = get_object_or_404(Post,pk=pk)
		post.title = request.POST["title"]
		post.content = request.POST["content"]
		post.save()
		return redirect("start:article",pk=pk)		


class Profile(View):
	template_name="blog/profile.html"

	def get(self,request):
		member = get_object_or_404(Members,pk=request.session['member_id'])
		return render(request,self.template_name,{"member":member})









