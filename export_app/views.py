from django.contrib.auth.models import User 
from django.http import HttpResponse 
from django.core.mail import EmailMessage 
from django.utils import timezone 
from datetime import timedelta 
import csv 
from io import StringIO 

def export_users(request): 
  days = int(request.GET.get('days', 7))   
  order = request.GET.get('order', 'asc')   
  
  date_threshold = timezone.now( ) - timedelta(days=days) 
  users = User.objects.filter(date_joined__gte=date_threshold) 

  if order == 'desc': 
    users = users.order_by('-username') 
  else: 
    users = users.order_by('username') 

  csv_buffer = StringIO( ) 
  writer = csv.writer(csv_buffer) 
  writer.writerow(['Username', 'Email', 'Date Joined']) 

  for user in users: 
     writer.writerow([user.username, user.email, user.date_joined]) 
   
  subject = f"User Export - Last {days} Days" 
  message = f"Attached is the list of users created in the last {days} days." 
  admin_email = 'admin@example.com'   

  email = EmailMessage(subject, message, to=[admin_email]) 
  email.attach(f"user_export_{days}days.csv", csv_buffer.getvalue(), 'text/csv') 
  email.send( ) 

  response = HttpResponse(csv_buffer.getvalue( ), content_type='text/csv') 
  response['Content-Disposition'] = f'attachment; filename="user_export_{days}days.csv"' 
  return response
