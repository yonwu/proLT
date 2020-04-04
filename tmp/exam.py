class Blog:
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def output_with_comments(self):
        title = f'{self.name} (by {self.owner})'
        print(title)
        print('=' * len(title))
        print()
        for p in self.posts:
            p.output_with_comments()
        print()

    def posts_with_text(self, text):
        blog_list = []
        for post in self.posts:
            title = post.title
            post_txt = post.text
            if text in title or text in post_txt:
                blog_list.append(post)
        return blog_list


class BlogPost:
    def __init__(self, title, text=''):
        self.title = title
        self.text = text
        self.comments = []

    def add_comment(self, comment):
        self.comments.append(comment)

    def output_with_comments(self):
        print(self.title)
        print('-' * len(self.title))
        print(self.text)
        print()
        for c in self.comments:
            c.output_with_comments(level=1)
        print()


class Comment:
    indent_marker = '> '

    def __init__(self, author, text=''):
        self.author = author
        self.text = text
        self.comments = []

    def add_comment(self, comment):
        self.comments.append(comment)

    def output_with_comments(self, level=0):
        indent = self.indent_marker * level
        print(f'{indent}[Comment by {self.author}:]')
        print(f'{indent}{self.text}')
        for c in self.comments:
            c.output_with_comments(level=level + 1)


class BlogPostForbiddingComments(BlogPost):
    def __init__(self, title, text=''):
        super().__init__(title, text)

    def add_comment(self, comment):
        raise TypeError


class Node:
    def __init__(self, data, skip, next):
        self.next = next
        self.data = data
        self.skip = skip


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data, skip):
        self.head = Node(data, skip, self.head)

    def printSkip(self):
        current = self.head
        while current:
            skip = current.skip
            print(current.data)
            for i in range(0, skip):
                current = current.next

    def removeValue(self, value):
        current = self.head
        previous = None
        while current:
            if current.data == value:
                if previous is None:
                    self.head = current.next
                    current = self.head
                else:
                    previous.next = current.next
                    current = previous.next
            else:
                previous = current
                current = current.next


import time
import matplotlib.pyplot as plt

# Imports for pytorch
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim






