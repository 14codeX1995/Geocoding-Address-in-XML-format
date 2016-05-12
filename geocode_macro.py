#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
import time
from bs4 import BeautifulSoup
from xml.dom import minidom
import re
import unicodedata
class Geo:
	def __init__(self):
		self.subloc_1=" "
		self.subloc_2=" "
		self.subloc_3=" "
		self.admin_1=" "
		self.admin_2=" "
		self.locality=" "
		self.country=" "
		self.pin=" "
		self.premise=" "
		self.route=" "
		self.street_number=" "
		self.lat=" "
		self.lng=" "
	def split_address(self,addr_loc):
		url="https://maps.googleapis.com/maps/api/geocode/xml?address=%s&key=AIzaSyCNUZZcsmT3cDI3DVPNt0FVJ9WGWjKsHcQ"%addr_loc
		xml_distant = urllib.urlopen(url)
		time.sleep(5)
		xmldoc = minidom.parse(xml_distant)
		xml_distant.close()
		data= xmldoc.toxml()
		bs_ex=BeautifulSoup(data)
		try:
			self.lat=bs_ex.find('lat').text
		except Exception as e:
			self.lat=" "
			pass
		try:
			self.lng=bs_ex.find('lng').text
		except Exception as e:
			self.lat=" "
			pass
		for tag_ex in bs_ex.find_all('address_component'):
			try:
				type_loc=tag_ex.find('type').text
			except Exception as e:
				type_loc=" "
				pass
			try:
				if type_loc=='sublocality_level_1':
					self.subloc_1=tag_ex.find('long_name').text
			except Exception as e:
				self.subloc_1=" "
				pass
			try:
				if type_loc=='sublocality_level_2':
					self.subloc_2=tag_ex.find('long_name').text
			except Exception as e:
				self.subloc_2=" "
				pass
			try:
				if type_loc=='sublocality_level_3':
					self.subloc_3=tag_ex.find('long_name').text
			except Exception as e:
				self.subloc_3=" "
				pass
			try:
				if type_loc=='administrative_area_level_1':
					self.admin_1=tag_ex.find('long_name').text
			except Exception as e:
				self.admin_1=" "
				pass
			try:
				if type_loc=='administrative_area_level_2':
					self.admin_2=tag_ex.find('long_name').text
			except Exception as e:
				self.admin_2=" "
				pass
			try:
				if type_loc=='locality':
					self.locality=tag_ex.find('long_name').text
			except Exception as e:
				self.locality=" "
				pass
			try:
				if type_loc=='country':
					self.country=tag_ex.find('long_name').text
			except Exception as e:
				self.country=" "
				pass
			try:
				if type_loc=='postal_code':
					self.pin=tag_ex.find('long_name').text
			except Exception as e:
				self.pin=" "
				pass
			try:
				if type_loc=='premise':
					self.premise=tag_ex.find('long_name').text
			except Exception as e:
				self.premise=" "
				pass
			try:
				if type_loc=='street_number':
					self.street_number=tag_ex.find('long_name').text
			except Exception as e:
				self.street_number=" "
				pass
			try:
				if type_loc=='route':
					self.route=tag_ex.find('long_name').text
			except Exception as e:
				self.route=" "
				pass
	
	def print_addr(self):
		print "subloc1 : "+self.subloc_1
		print "subloc2 : "+self.subloc_2
		print "subloc3 : "+self.subloc_3
		print "premise : "+self.premise
		print "street_number : "+self.street_number
		print "route : "+self.route
		print "administrative_area_level_1 : "+self.admin_1
		print "administrative_area_level_2 : "+self.admin_2
		print "locality : "+self.locality
		print "country : "+self.country
		print "postal_code : "+self.pin
		print "Lat : "+self.lat
		print "Lng : "+self.lng

'''
geo1=Geo()
addr='T28, 3rd Floor, Center One Mall,\xa0Vashi, Navi Mumbai'
unicodedata.normalize('NFKD', addr).encode('ascii','ignore')
geo1.split_address(addr)
geo1.print_addr()

'''

		
