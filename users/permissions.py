from rest_framework.permissions import BasePermission

from materials.models import Course, Lesson


class ModeratorPermission(BasePermission):
    """ Кастомное разрешение для модераторов """
    def has_permission(self, request, view):
        # Проверить, является ли пользователь модератором
        if request.user and request.user.groups.filter(name='moderator_training').exists():
            # Разрешить доступ к просмотру и изменению
            return request.method in ['GET', 'PUT', 'PATCH']

        # Запретить доступ для всех остальных
        return False


class IsCourseOwner(BasePermission):
    """ Кастомное разрешение для владельцев курса """
    def has_permission(self, request, view):
        course_id = view.kwargs.get('id')
        if course_id:
            try:
                course = Course.objects.get(id=course_id)  # Предполагаем, что у вас есть модель Course
                # Проверяем, является ли пользователь владельцем
                return request.user == course.owner and request.method in ['GET', 'PUT', 'PATCH', 'DELETE']
            except Course.DoesNotExist:
                return False
        return False


class IsLessonOwner(BasePermission):
    """ Кастомное разрешение для владельцев урока """
    def has_permission(self, request, view):
        lesson_id = view.kwargs.get('id')
        if lesson_id:
            try:
                lesson = Lesson.objects.get(id=lesson_id)  # Предполагаем, что у вас есть модель Course
                # Проверяем, является ли пользователь владельцем
                return request.user == lesson.owner and request.method in ['GET', 'PUT', 'PATCH', 'DELETE']
            except Lesson.DoesNotExist:
                return False
        return False
