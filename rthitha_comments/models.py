from django.contrib.comments.models import Comment
from mptt.models import MPTTModel, TreeForeignKey
from zmovies.models import UserProfile
from django.contrib.auth.models import User 

class MPTTComment(MPTTModel, Comment):
	parent = TreeForeignKey('self', null=True, blank=True, related_name='children')		

	class MPTTMeta:
		order_insertion_by=['-submit_date']

	class Meta:
		ordering=['tree_id','lft']

	def __unicode__(self):
	 	return '%s %s: %s %s %s' % \
	 					(
	 						self.user.id, 
	 						self.user.last_name,
	 						self.content_type,
	 						self.object_pk,
							self.comment,
	 					)		