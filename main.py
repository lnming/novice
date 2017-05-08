# -*- coding: UTF-8 -*-
"""download webpage and parse then store info"""
import sqlite3
import json

import requests
import peewee
from bs4 import BeautifulSoup

from haopic import Image, Tag, Relationship


def get_imgs(url):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'lxml')
    return soup.find_all('li', class_='item_box')


def parse_imgs_info(imgs):
    result = []
    for img in imgs:
        title = img.div.a['title']
        uri = img.div.a.img['src']
        author = img.find('a', rel='author').get_text()
        date = img.find('div', 'byline').get_text().split()[-1].strip()
        tags = [tag.text for tag in img.find_all(rel='category tag')]

        result.append({
            'title': title,
            'uri': uri,
            'author': author,
            'date': date,
            'tags': tags,
        })
    return result


def store_imgs_info(imgs):
    for img in imgs:
        item = Image(author=img['author'], date=img['date'], title=img['title'], uri=img['uri'])
        item.save()
        img_id = item.id

        tag_ids = []
        tags = img['tags']
        for tag in tags:
            entry = Tag(name=tag)
            try:
                entry.save()
                tag_ids.append(entry.id)
            except peewee.IntegrityError:
                tag_ids.append(Tag.get(Tag.name == tag).id)

        for _id in tag_ids:
            rel = Relationship(img=img_id, tag=_id)
            rel.save()

        # print 'img_id:', img_id,'tag_ids:', tag_ids


def _main():
    import json
    url = 'http://www.haopic.me'
    imgs = parse_imgs_info(get_imgs(url))
    # print json.dumps(imgs, ensure_ascii=False)

    print 'start...'
    store_imgs_info(imgs)
    print 'done...'


if __name__ == '__main__':
    _main()
