from .models import Article, Comment
from .forms import CreateCommentForm, UpdateCommentForm
from django.views.generic import RedirectView, FormView, CreateView, UpdateView, DeleteView, DetailView, ListView


class MainPage(ListView):
    template_name = 'main_page.html'
    model = Article
    paginate_by = 3
    queryset = model.objects.filter().order_by('id')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        return context


class ArticleDetail(DetailView):
    template_name = 'article_detail.html'
    success_url = '/'
    model = Article





class CreateComment(CreateView):
    success_url = '/'
    form_class = CreateCommentForm
    template_name = 'create_comment.html'


class UpdateComment(UpdateView):
    template_name = 'update_comment.html'
    form_class = UpdateCommentForm
    success_url = '/'
    model = Comment


class DeleteComment(DeleteView):
    template_name = 'delete_comment.html'
    success_url = '/'
    queryset = Comment.objects.filter(is_active=True)


class DetailComment(DetailView):
    template_name = 'detail_comment.html'
    success_url = '/'
    model = Comment


class CommentsListView(ListView):
    template_name = 'comments_list.html'
    model = Comment
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context.update(
            {'comment_create_form': CreateCommentForm,
             'comment_update_form': UpdateCommentForm})
        return context