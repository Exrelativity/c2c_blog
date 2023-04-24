from graphene import relay, ObjectType, Field, List, Int, Schema
from graphene_django.forms.mutation import DjangoModelFormMutation
from graphene_django import DjangoObjectType
from authentication.models import Users
from post.models import *
from file.models import *
from userprofile.models import * 
from authentication.forms import *
from post.forms import *
from file.forms import *
from userprofile.forms import * 

class UsersType(DjangoObjectType):
    class Meta:
        model = Users
        interfaces = (relay.Node,)  # make sure you add this
        fields = "__all__"
        

class UsersConnection(relay.Connection):
    class Meta:
        node = UsersType


class UsersMutation(DjangoModelFormMutation):
    users = Field(UsersType)
    class Meta:
        form_class = UsersMutationForm 


class FileType(DjangoObjectType):
    class Meta:
        model = File
        interfaces = (relay.Node,)  # make sure you add this
        fields = "__all__"

class FileConnection(relay.Connection):
    class Meta:
        node = FileType


class FileMutation(DjangoModelFormMutation):
    File = Field(FileType)
    class Meta:
        form_class =FileForm 


class PostType(DjangoObjectType):
    
    class Meta:
        model = Post
        interfaces = (relay.Node,)  # make sure you add this
        fields = "__all__"

class PostConnection(relay.Connection):
    class Meta:
        node = PostType


class PostMutation(DjangoModelFormMutation):
    post = Field(PostType)
    class Meta:
        form_class = PostForm 



class ProfileType(DjangoObjectType):
    class Meta:
        model = UsersProfile
        interfaces = (relay.Node,)  # make sure you add this
        fields = "__all__"

class UsersProfileConnection(relay.Connection):
    class Meta:
        node = ProfileType

class UsersProfileMutation(DjangoModelFormMutation):
    usersProfiles = Field(ProfileType)
    class Meta:
        form_class = UsersProfileForm




class Query(ObjectType):
    all_users = List(UsersType)
    all_files = List(FileType)
    all_posts = List(PostType)
    all_usersprofile = List(ProfileType)
    users = relay.ConnectionField(UsersConnection)
    files = relay.ConnectionField(FileConnection)
    posts = relay.ConnectionField(PostConnection)
    usersprofile = relay.ConnectionField(UsersProfileConnection)
    usersById = Field(UsersType, id=Int(required=True))
    fileById = Field(FileType, id=Int(required=True))
    postsById = Field(PostType, id=Int(required=True))
    usersprofileById = Field(ProfileType, id=Int(required=True))


    def resolve_all_users(root, info):
        return Users.objects.all()

    def resolve_all_file(root, info):
        return File.objects.all()


    def resolve_all_posts(root, info):
        return Post.objects.all()


    def resolve_all_usersprofile(root, info):
        return UsersProfile.objects.all()


    def resolve_users(root, info, **kwargs):
        return Users.objects.all()


    def resolve_file(root, info, **kwargs):
        return File.objects.all()


    def resolve_posts(root, info, **kwargs):
        return Post.objects.all()


    def resolve_usersprofile(root, info, **kwargs):
        return UsersProfile.objects.all()
    
    # resolver for by ids
    def resolve_usersById(root, info, id):
        try:
            return Users.object.get(id=id)
        except Users.DoesNotExist:
            return None
        
    def resolve_fileById(root, info, id):
        try:
            return File.object.get(id=id)
        except File.DoesNotExist:
            return None

    def resolve_postsById(root, info, id):
        try:
            return Post.object.get(id=id)
        except Post.DoesNotExist:
            return None

    def resolve_usersprofileById(root, info, id):
        try:
            return UsersProfile.object.get(id=id)
        except UsersProfile.DoesNotExist:
            return None



class Mutation(ObjectType):
    users = UsersMutation.Field()
    file = FileMutation.Field()
    posts = PostMutation.Field()
    usersprofile = UsersProfileMutation.Field()



schema = Schema(query=Query, mutation=Mutation)