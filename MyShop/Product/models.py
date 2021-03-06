from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


# Create your models here.

class Product(models.Model):
    brand = models.ForeignKey('Product.Brand', verbose_name=_("Brand"), related_name='Product',
                              related_query_name='Product', on_delete=models.CASCADE)
    slug = models.SlugField(_("Slug"), db_index=True, unique=True)
    category = models.ForeignKey('Product.Category', verbose_name=_("Category"), related_name='Product',
                                 related_query_name='Product', on_delete=models.CASCADE)
    name = models.CharField(_('Name'), max_length=150)
    image = models.ImageField(_('Image'), upload_to='product/image/', max_length=100)
    detail = models.CharField(_('Detail'), max_length=150)
    description = models.CharField(_('Description'), max_length=2000,)


    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'pro_slug': self.slug})


class ShopProduct(models.Model):
    shop = models.ForeignKey('Account.Shop', verbose_name=_('Shop'), related_name='ShopProduct',
                             related_query_name='ShopProduct', on_delete=models.CASCADE, null=True)
    product = models.ForeignKey('Product.Product', verbose_name=_('Product'), related_name='ShopProduct',
                                related_query_name='ShopProduct', on_delete=models.CASCADE, null=True)
    price = models.CharField(_('Price'), max_length=50, default=0)
    quantity = models.CharField(_('Quantity'), max_length=50, default=0)

    class Meta:
        verbose_name = _('shop_product')
        verbose_name_plural = _('shops_products')

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('shop_product_detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    content = models.TextField(_("Content"), )
    create_at = models.DateTimeField(_("Create at"), auto_now_add=True)
    update_at = models.DateTimeField(_("Update at"), auto_now=True)
    product = models.ForeignKey("Product.Product", verbose_name=_("product"), related_name="comments",
                                related_query_name="comments", on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("Author"), on_delete=models.CASCADE,
                               related_name='comment', related_query_name='comment')
    is_confirmed = models.BooleanField(_("Confirm"), default=True)

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")
        ordering = ["-create_at"]

    def __str__(self):
        return self.product.name

    def get_absolute_url(self):
        return reverse('comment_detail', kwargs={'pk': self.pk})

    @property
    def like_count(self):
        q = Likes.objects.filter(comment=self, condition=True)
        return q.count()

    @property
    def dislike_count(self):
        q = Likes.objects.filter(comment=self, condition=False)
        return q.count()


class Image(models.Model):
    product = models.ForeignKey("Product.Product", verbose_name=_("Product"), related_name='Image',
                                related_query_name='Image', on_delete=models.CASCADE)
    image = models.ImageField(_('Image'), upload_to='image/image/', max_length=100)

    class Meta:
        verbose_name = _('image')
        verbose_name_plural = _('images')

    def get_absolute_url(self):
        return reverse('image_detail', kwargs={'pk': self.pk})


class Brand(models.Model):
    name = models.CharField(_('Name'), max_length=50)
    detail = models.TextField(_('Detail'), blank=False, help_text="Enter Your Brand Detail")
    image = models.ImageField(_('Image'), upload_to='brand/image/', max_length=100)
    slug = models.SlugField(_("Slug"), db_index=True, unique=True)

    class Meta:
        verbose_name = _('brand')
        verbose_name_plural = _('brands')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('brand_detail', kwargs={'pk': self.pk})


class Category(models.Model):
    name = models.CharField(_('Name'), max_length=50)
    slug = models.SlugField(_("Slug"), db_index=True, unique=True)
    detail = models.TextField(_('Detail'), blank=True, help_text="Enter Your Category Detail")
    image = models.ImageField(_('Image'), upload_to='category/image/', max_length=100)
    parent = models.ForeignKey('self', verbose_name=_("Parent"), on_delete=models.SET_NULL, null=True, blank=True
                               , related_name='children', related_query_name='children')

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'cat_slug': self.slug})


class ProductMeta(models.Model):
    product = models.ForeignKey("Product.Product", verbose_name=_("Product"), related_name='ProductMeta',
                                related_query_name='ProductMeta', on_delete=models.CASCADE)
    label = models.CharField(_('Label'), max_length=50)
    value = models.DecimalField(max_digits=4, decimal_places=2)

    class Meta:
        verbose_name = _('product_meta')
        verbose_name_plural = _('product_metas')

    def __str__(self):
        return self.label

    def get_absolute_url(self):
        return reverse('product_meta_detail', kwargs={'pk': self.pk})


class Likes(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("user"), on_delete=models.CASCADE,
                             related_name='like', related_query_name='like')
    product = models.ForeignKey('Product.Product', verbose_name=_("product"), on_delete=models.CASCADE,
                                related_name='product', related_query_name='product')
    condition = models.BooleanField(_("Condition"))

    class Meta:
        verbose_name = _('like')
        verbose_name_plural = _('likes')

    def __str__(self):
        return self.product.name

    def get_absolute_url(self):
        return reverse('like_detail', kwargs={'pk': self.pk})
