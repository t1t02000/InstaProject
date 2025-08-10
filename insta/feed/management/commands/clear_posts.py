from django.core.management.base import BaseCommand
from django.conf import settings
from feed.models import Post
import os
import shutil

class Command(BaseCommand):
    help = 'Elimina todas las publicaciones y borra las imágenes del directorio MEDIA_ROOT/posts/'

    def handle(self, *args, **options):
        count = Post.objects.count()
        self.stdout.write(self.style.WARNING(f'Eliminando {count} posts...'))
        # Borrar archivos de imágenes y luego los registros
        for post in Post.objects.all():
            if post.image and hasattr(post.image, 'path') and os.path.exists(post.image.path):
                try:
                    os.remove(post.image.path)
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f'No se pudo borrar {post.image.path}: {e}'))
        Post.objects.all().delete()
        # Borrar la carpeta posts/ completa si existe
        posts_dir = os.path.join(settings.MEDIA_ROOT, 'posts')
        if os.path.isdir(posts_dir):
            try:
                shutil.rmtree(posts_dir)
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'No se pudo borrar la carpeta {posts_dir}: {e}'))
        self.stdout.write(self.style.SUCCESS('Publicaciones e imágenes eliminadas.'))
