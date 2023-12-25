from django.shortcuts import redirect
from django_unicorn.components import UnicornView
from myapp.models import practis

class SampleView(UnicornView):
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

    



























































































































'''
from django.shortcuts import redirect
from django_unicorn.components import UnicornView
from myapp.models import practis

class SampleView(UnicornView):
    title = ""
    compony = ""
    address = ""
    pin = ""

    def save_book(self):
        # Create a new practis instance
        book = practis(name=self.title, compony=self.compony, address=self.address, pin=self.pin)
        
        # Save the new practis instance to the database
        book.save()

        # Reset form fields (if you have a reset method defined)
        self.update()

        # Redirect to the detail page of the newly created practis
        # return redirect(f"/book/{book.id}")
    def delete(self, book_to_delete):
        # Retrieve the practis object using the provided ID
        practis_instance = practis.objects.get(pk=book_to_delete['pk'])

        # Delete the practis object
        practis_instance.delete()

        # Optionally, you can update the page after deletion
        self.update()'''
