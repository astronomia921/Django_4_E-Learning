from django.shortcuts import render
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required


@login_required
def course_chat_room(request, course_id):
    try:
        course = request.user.courses_joined.get(id=course_id)
    except HttpResponseForbidden() as exc:
        return exc
    return render(request, 'chat/room.html', {'course': course})
