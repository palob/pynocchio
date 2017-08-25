# -*- coding: utf-8 -*-

from unittest import TestCase

from pynocchio.comic import Comic
from pynocchio.comic_page_handler_factory import ComicPageHandlerFactory
from pynocchio.comic_page_handler import ComicPageHandlerSinglePage
from pynocchio.comic_page_handler import ComicPageHandlerDoublePage


class TestComicPageHandlerFactory(TestCase):

    def setUp(self):
        self.hq = Comic('Teste', '/opt/teste')

    def test_create_handler(self):
        handler = ComicPageHandlerFactory.create_handler(True, self.hq)
        self.assertIsInstance(handler, ComicPageHandlerDoublePage)

        handler = ComicPageHandlerFactory.create_handler(False, self.hq)
        self.assertIsInstance(handler, ComicPageHandlerSinglePage)
