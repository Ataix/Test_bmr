# from django.contrib.auth import get_user_model
# from django.test import TestCase
#
# from ..models import Product, Review
#
#
# User = get_user_model()
#
#
# class TestProductReviewModel(TestCase):
#     """
#     Test product's model
#     """
#     def setUp(self):
#         self.product_1 = Product.objects.create(
#             name='Test Product 1',
#             description='Test Description 1',
#             category='Test Category 1',
#             price=322.0,
#             quantity=10,
#         )
#         self.product_2 = Product.objects.create(
#             name='Test Product 2',
#             description='Test Description 2',
#             category='Test Category 2',
#             price=109.0,
#             quantity=9,
#         )
#         self.user_1 = User.objects.create(
#             username='user1',
#             password='<PASSWORD>'
#         )
#         self.review_1 = Review.objects.create(
#             product=self.product_1,
#             text='Test Review 1',
#             author=self.user_1,
#             rate=5
#         )
#         self.review_2 = Review.objects.create(
#             product=self.product_2,
#             text='Test Review 2',
#             author=self.user_1,
#             rate=5
#         )
#
#     def test_product_creation(self):
#         product_1 = Product.objects.get(name='Test Product 1')
#         product_2 = Product.objects.get(name='Test Product 2')
#         self.assertEqual(self.product_1.name, product_1.name)
#         self.assertEqual(self.product_1.description, product_1.description)
#         self.assertEqual(self.product_1.category, product_1.category)
#         self.assertEqual(self.product_1.price, product_1.price)
#         self.assertEqual(self.product_1.quantity, product_1.quantity)
#         self.assertEqual(self.product_2.name, product_2.name)
#         self.assertEqual(self.product_2.description, product_2.description)
#         self.assertEqual(self.product_2.category, product_2.category)
#         self.assertEqual(self.product_2.price, product_2.price)
#         self.assertEqual(self.product_2.quantity, product_2.quantity)
#
#         review_1 = Review.objects.get(id=self.review_1.id)
#         review_2 = Review.objects.get(id=self.review_2.id)
#         self.assertEqual(self.review_1.product, review_1.product)
#         self.assertEqual(self.review_1.author, review_1.author)
#         self.assertEqual(self.review_1.rate, review_1.rate)
#         self.assertEqual(self.review_1.text, review_1.text)
#         self.assertEqual(self.review_2.product, review_2.product)
#         self.assertEqual(self.review_2.author, review_2.author)
#         self.assertEqual(self.review_2.rate, review_2.rate)
#         self.assertEqual(self.review_2.text, review_2.text)
