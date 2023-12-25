from django_unicorn.components import UnicornView
from django import forms
from myapp.models import practis

class SimpleView(UnicornView):  
    practis = practis.objects.none()
    def mount(self):
           self.practis = practis.objects.all()
    title = ""
    compony = ""
    address = ""
    pin = ""
    def save_book(self):
        book = practis(name=self.title, compony=self.compony, address=self.address, pin=self.pin)
        book.save()
        self.reset()
        return self.mount()
    
#delete the 
    def delete(self, book_to_delete=None):
        if book_to_delete is None:
            return
        practis_instance = practis.objects.get(pk=book_to_delete['pk'])
        practis_instance.delete()
        return self.mount()

    # def updation(self,)


