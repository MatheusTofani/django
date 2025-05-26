import pytest
from blog.models import Post
from blog.tests.factories import PostFactory

@pytest.mark.django_db
def test_post_factory_creates_valid_post():
    post = PostFactory()
    assert isinstance(post, Post)
    assert post.title != ""
    assert post.author is not None
