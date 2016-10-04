#coding=utf-8
class App(object):

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def image(self):
    	return self._image

    @image.setter
    def image(self, value):
    	self._image = value

    @property
    def summary(self):
    	return self._summary

    @summary.setter
    def summary(self, value):
    	self._summary = value

    @property
    def link(self):
    	return self._link

    @link.setter
    def link(self, value):
    	self._link = value


    @property
    def bundleId(self):
    	return self._bundleId

    @bundleId.setter
    def bundleId(self, value):
    	self._bundleId = value


    @property
    def category(self):
    	return self._category

    @category.setter
    def category(self, value):
    	self._category = value


    @property
    def releaseDate(self):
    	return self._releaseDate

    @releaseDate.setter
    def releaseDate(self, value):
    	self._releaseDate = value


    @property
    def rank(self):
    	return self._rank

    @rank.setter
    def rank(self, value):
    	self._rank = value