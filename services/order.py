from datetime import datetime

from django.contrib.auth import get_user_model
from django.db import transaction

from db.models import Order, Ticket


@transaction.atomic()
def create_order(
        tickets: list[dict],
        username: str,
        date: datetime = None) -> Order:

    user = get_user_model().objects.get(username=username)

    order = Order.objects.create(user=user)

    if date:
        order.created_at = date
        order.save()

    for ticket_data in tickets:
        movie_session = ticket_data.get("movie_session")
        row = ticket_data.get("row")
        seat = ticket_data.get("seat")

        ticket = Ticket(
            movie_session_id=movie_session,
            order=order,
            row=row,
            seat=seat
        )

        ticket.full_clean()
        ticket.save()

    return order


def get_orders(username: str = None) -> Order:
    if username:
        user = get_user_model().objects.get(username=username)

        return Order.objects.filter(user=user)
    return Order.objects.all()
