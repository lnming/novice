-- 删除重复命名表
drop table if exists 'image';
drop table if exists 'tag';
drop table if exists 'relationship';

/* 创建图片信息表 */
create table image (
  id integer primary key autoincrement,
  title text,
  uri text unique,
  author text,
  'date' date
);

/* 创建分类表 */
create table tag (
  id integer primary key autoincrement,
  name text unique
);

/* 创建图片分类关联表 */
create table relationship (
  id integer primary key autoincrement,
  img int,
  tag int,
  foreign key(img) references image(id),
  foreign key(tag) references tag(id)
);
