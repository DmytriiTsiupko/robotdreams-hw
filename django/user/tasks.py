from celery import shared_task
from .models import User


@shared_task
def print_text_task(text):
    print(text)


@shared_task
def print_user_purchases(user_id):
    try:
        user = User.objects.get(id=user_id)
        purchases_count = user.purchases.count()
        print(f"User {user_id} has {purchases_count} purchases.")
    except User.DoesNotExist:
        print(f"User with ID {user_id} does not exist.")


@shared_task
def print_user_count():
    user_count = User.objects.count()
    print(f"Number of users in the database: {user_count}")

