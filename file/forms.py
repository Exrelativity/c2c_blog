from django.forms import ModelForm, ModelChoiceField, ClearableFileInput
from .models import File, FilePost, FileCategory, FileSubCategory, FileProfile

class FileForm(ModelForm):
    class Meta:
        model = File
        fields = ("source", "userId", "fileType")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['userId'] = ModelChoiceField(
            queryset=Users.objects.all(),
            widget=ModelChoiceField(attrs={
                "placeholder": "User",
                "class": "form-control"
            })
        )
        self.fields['source'].widget = ClearableFileInput(attrs={
            "placeholder": "File",
            "class": "form-control"
        })

class FileRelationForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['postId'] = ModelChoiceField(
            queryset=Post.objects.all(),
            widget=ModelChoiceField(attrs={"placeholder": "Post", "class": "form-control"})
        )
        self.fields['fileId'] = ModelChoiceField(
            queryset=File.objects.all(),
            widget=ModelChoiceField(attrs={"placeholder": "File", "class": "form-control"})
        )

class FilePostForm(FileRelationForm):
    class Meta:
        model = FilePost
        fields = ("postId", "fileId")

class FileCategoryForm(FileRelationForm):
    class Meta:
        model = FileCategory
        fields = ("categoryId", "fileId")

class FileSubCategoryForm(FileRelationForm):
    class Meta:
        model = FileSubCategory
        fields = ("subCategoryId", "fileId")

class FileProfileForm(FileRelationForm):
    class Meta:
        model = FileProfile
        fields = ("profileId", "fileId")
