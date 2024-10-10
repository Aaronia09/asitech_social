from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    content = models.TextField()  
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f"Post by {self.user.username} at {self.created_at}"


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  
    content = models.TextField()  
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"Comment by {self.user.username} on post {self.post.id}"


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  

    class Meta:
        unique_together = ('user', 'post')  

    def __str__(self):
        return f"{self.user.username} likes {self.post.id}"


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)  
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"Notification for {self.user.username} on comment {self.comment.id}"
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  
    bio = models.TextField(blank=True, null=True) 
    avatar = models.ImageField(upload_to='profiles/', blank=True, null=True)  
    

    def __str__(self):
        return f"{self.user.username}'s Profile"