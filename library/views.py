#coding:utf-8
from django.shortcuts import render
from library.models import Book
from library.models import Author

page = 0

def show(request):
    global page
    i = 0
    book_lists = []
    for book_list in Book.objects.all():
        i += 1
        if i > page * 10:
            book_dict = {}
            book_dict["id"] = book_list.id
            book_dict["ISBN"] = book_list.ISBN
            book_dict["Title"] = book_list.Title
            book_dict["AuthorID"] = book_list.AuthorID
            book_dict["Publisher"] = book_list.Publisher
            book_dict["PublishDate"] = book_list.PublishDate
            book_dict["Price"] = book_list.Price
            book_lists.append(book_dict)
        if i >= (page + 1) * 10:
            break
    return render(request, 'library.html', {"book_lists": book_lists})

def main(request):
    global page
    if request.method == 'POST':
        if request.POST.has_key('add'):
            return render(request, 'add_book.html')
        elif request.POST.has_key('search'):
            book_lists = []
            if (len(Author.objects.filter(Name=request.POST['author'])) != 0):
                for book_list in Book.objects.filter(AuthorID=Author.objects.get(Name=request.POST['author']).AuthorID):
                    book_dict = {}
                    book_dict["ISBN"] = book_list.ISBN
                    book_dict["Title"] = book_list.Title
                    book_dict["AuthorID"] = book_list.AuthorID
                    book_dict["Publisher"] = book_list.Publisher
                    book_dict["PublishDate"] = book_list.PublishDate
                    book_dict["Price"] = book_list.Price
                    book_lists.append(book_dict)
                return render(request, 'library.html', {"book_lists": book_lists})
            else:
                return render(request, 'library.html', {"book_lists": []})
        elif request.POST.has_key('author'):
            AuthorID = request.POST['AuthorID']
            Name = request.POST['Name']
            Age = request.POST['Age']
            Country = request.POST['Country']
            Author.objects.create(
                AuthorID=AuthorID,
                Name=Name,
                Age=Age,
                Country=Country,
            )
            return show(request)
        elif request.POST.has_key('updata'):
            book = Book.objects.get(id=request.POST['id'])
            book.AuthorID=request.POST['AuthorID']
            book.Publisher=request.POST['Publisher']
            book.PublishDate=request.POST['PublishDate']
            book.Price=request.POST['Price']
            book.save()
            if (len(Author.objects.filter(AuthorID=request.POST['AuthorID'])) == 0):
                return render(request, 'add_author.html', {"AuthorID": request.POST['AuthorID']})
            return show(request)
        else:
            ISBN = request.POST['ISBN']
            Title = request.POST['Title']
            AuthorID = request.POST['AuthorID']
            Publisher = request.POST['Publisher']
            PublishDate = request.POST['PublishDate']
            Price = request.POST['Price']
            Book.objects.create(
                ISBN=ISBN,
                Title=Title,
                AuthorID=AuthorID,
                Publisher=Publisher,
                PublishDate=PublishDate,
                Price=Price,
            )
            if (len(Author.objects.filter(AuthorID=request.POST['AuthorID'])) == 0):
                return render(request, 'add_author.html', {"AuthorID": request.POST['AuthorID']})
            return show(request)
    else:

        if request.GET.get('up') == "1" and page > 0:
            page -= 1
        elif request.GET.get('up') == "2" and page < len(Book.objects.all()) / 10:
            page += 1
        return show(request)

def add_book(request):
    return render(request, 'add_book.html')

def delete(request):
    Book.objects.get(id=request.GET.get('id')).delete()
    return show(request)

def author(request):
    book = Book.objects.get(id=request.GET.get('id'))
    author = Author.objects.get(AuthorID=book.AuthorID)
    author_dict = {}
    author_dict["AuthorID"] = author.AuthorID
    author_dict["Name"] = author.Name
    author_dict["Age"] = author.Age
    author_dict["Country"] = author.Country
    return render(request, 'author.html', {"author_dict": author_dict})

def updata(request):
    book = Book.objects.get(id=request.GET.get('id'))
    book_dict = {}
    book_dict["id"] = book.id
    book_dict["AuthorID"] = book.AuthorID
    book_dict["Publisher"] = book.Publisher
    book_dict["PublishDate"] = book.PublishDate
    book_dict["Price"] = book.Price
    return render(request, 'updata.html', {"book_dict": book_dict})