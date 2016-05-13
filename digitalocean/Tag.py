# -*- coding: utf-8 -*-
from .baseapi import BaseAPI, GET, POST, DELETE, PUT


class Tag(BaseAPI):
    def __init__(self, *args, **kwargs):
        self.name = None
        self.resources = {}
        super(Tag, self).__init__(*args, **kwargs)

    @classmethod
    def get_object(cls, api_token, name):
        """
            Class method that will return a Tag object by name.
        """
        tag = cls(token=api_token, name=name)
        tag.load()
        return tag

    def load(self):
        """
            Load the Tag object from DigitalOcean.

            Requires either self.name to be set.
        """
        data = self.get_data("tags/%s" % self.name, type=GET)

        self.name = data['tag']['name']
        self.resources = data['tag']['resources']

    def create(self):
        """
            Create the Tag
        """
        input_params = {
            "name": self.name
        }

        data = self.get_data("tags/", type=POST, params=input_params)

        self.name = data['tag']['name']
        self.resources = data['tag']['resources']
        return self

    def edit(self, name):
        """
            Edit the Tag
        """
        input_params = {
            "name": name,
        }

        if input_params['name'] == self.name:
            return

        data = self.get_data(
            "tags/%s" % self.name,
            type=PUT,
            params=input_params
        )

        if data:
            self.name = data['name']
            self.resources = data['resources']

    def destroy(self):
        """
            Destroy the Tag
        """
        return self.get_data("keys/%s" % self.name, type=DELETE)

    def add_resource(self, resources):
        input_params = {
            "resources": resources,
        }

        return self.get_data(
            "tags/%s/resources" % self.name,
            type=POST,
            params=input_params
        )

    def remove_resource(self, resources):
        input_params = {
            "resources": resources,
        }

        return self.get_data(
            "tags/%s/resources" % self.name,
            type=DELETE,
            params=input_params
        )

    def __str__(self):
        return "%s" % (self.name)
