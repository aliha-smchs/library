# library_app/admin.py
from django.contrib import admin
# from .models import Book, BookCopy, Student, Staff, Borrow
#
# @admin.register(Book)
# class BookAdmin(admin.ModelAdmin):
#     list_display = ('name', 'isbn', 'rack', 'row', 'column')
#
# @admin.register(BookCopy)
# class BookCopyAdmin(admin.ModelAdmin):
#     list_display = ('book', 'copy_number', 'is_available')
#
# @admin.register(Student)
# class StudentAdmin(admin.ModelAdmin):
#     list_display = ('student_id', 'first_name', 'last_name', 'year_group', 'section')
#
# @admin.register(Staff)
# class StaffAdmin(admin.ModelAdmin):
#     list_display = ('staff_id', 'name')
#
# @admin.register(Borrow)
# class BorrowAdmin(admin.ModelAdmin):
#     list_display = ('book_copy', 'student', 'staff', 'borrowed_date', 'due_date', 'returned_date', 'fine_amount')
