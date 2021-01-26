-- Урок 3. Домашнее задание. В нижней части скрипта 

-- ----------------------------------------------------------------
-- Скрипт MySQL, созданный DBeaver 7.3.3
-- База данных социальной сети "vk"
-- Версия 1.0
-- 23 января 2021 г.
-- ----------------------------------------------------------------


-- ----------------------------------------------------------------
-- База данных социальной сети "vk"
-- ----------------------------------------------------------------
drop DATABASE if exists vk;
create DATABASE vk;

USE vk;

-- -----------------------------------------------------------------
-- Таблица 1 - users - "пользователи"
-- -----------------------------------------------------------------
drop table if exists users;
create table users(
	id SERIAL primary key,
	firstname VARCHAR(100) COMMENT 'Имя',
	lastname VARCHAR(100) COMMENT 'Фамилия',
	email VARCHAR(120) unique,
	password_hash VARCHAR(100),
	phone BIGINT UNSIGNED,
	is_deleted BIT default 0,
	index users_firstname_lastname_idx(firstname, lastname)	
);

-- -----------------------------------------------------------------
-- Таблица 7 - media_types - "типы файлов медиа"
-- -----------------------------------------------------------------
drop table if exists media_types;
create table media_types(	
	id SERIAL primary key,
	name VARCHAR(255),
	created_at DATETIME default NOW(),
	updated_at DATETIME default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP
);

-- -----------------------------------------------------------------
-- Таблица 8 - media 
-- -----------------------------------------------------------------
drop table if exists media;
create table media(	
	id SERIAL primary key,
	user_id BIGINT  UNSIGNED not null,
	media_type_id BIGINT UNSIGNED not null,
	body TEXT,
	-- filename BLOB,   -------хранение данных файлов непосредственно в базе
	filename VARCHAR(255),
	`size` INT,                                         --     размер файлов
	metadata JSON,
	created_at DATETIME default NOW(),
	updated_at DATETIME default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP,
	
	foreign key (user_id) references users(id) on update cascade on delete cascade,
	foreign key (media_type_id) references media_types(id) on update cascade on delete cascade
);

-- -----------------------------------------------------------------
-- Таблица 2 - `profiles` - "профили" 
-- -----------------------------------------------------------------
drop table if exists `profiles`;
create table `profiles`(
	user_id SERIAL primary key,
	gender CHAR(1),
	birthday DATE,
	photo_id BIGINT UNSIGNED null,
	created_at DATETIME default NOW(),
	hometown VARCHAR(100),
	
	foreign key (photo_id) references media(id) on update cascade on delete cascade
);

-- Таблицы: users - `profiles` -------------------------------------
alter table `profiles` add constraint fk_user_id
foreign key (user_id) references users(id) on update cascade on delete cascade;

-- -----------------------------------------------------------------
-- Таблица 3 - messages - "сообщения"
-- -----------------------------------------------------------------
drop table if exists messages;
create table messages(
	id SERIAL primary key,
	from_user_id BIGINT UNSIGNED not null,
	to_user_id BIGINT UNSIGNED not null,
	body TEXT,
	created_at DATETIME default NOW(),
	
	foreign key (from_user_id) references users(id) on update cascade on delete cascade,	
	foreign key (to_user_id) references users(id) on update cascade on delete cascade
);

-- -----------------------------------------------------------------
-- Таблица 4 - friend_requests - "запросы на дружбу"
-- -----------------------------------------------------------------
drop table if exists friend_requests;
create table friend_requests(	
	initiator_user_id BIGINT UNSIGNED not null,
	target_user_id BIGINT UNSIGNED not null,
	`status` ENUM('requested', 'approved', 'declined', 'unfriended'),
	requested_at DATETIME default NOW(),
	update_at DATETIME on update NOW(), 
	
	primary key (initiator_user_id, target_user_id),
	foreign key (initiator_user_id) references users(id) on update cascade on delete cascade,			
	foreign key (target_user_id) references users(id) on update cascade on delete cascade
);

-- -----------------------------------------------------------------
-- Таблица 5 - communities - "сообщества"
-- -----------------------------------------------------------------
drop table if exists communities;
create table communities(	
	id SERIAL primary key,
	name VARCHAR(150),
	admin_user_id BIGINT UNSIGNED not null,
	index communities_name_idx(name),
	
	foreign key (admin_user_id) references users(id) on update cascade on delete cascade
);

-- -----------------------------------------------------------------
-- Таблица 6 - users_communities - "участники сообществ"
-- -----------------------------------------------------------------
drop table if exists users_communities;
create table users_communities(	
	user_id BIGINT UNSIGNED not null,
	community_id BIGINT UNSIGNED not null,
	primary key (user_id, community_id),
	
	foreign key (user_id) references users(id) on update cascade on delete cascade,
	foreign key (community_id) references communities(id) on update cascade on delete cascade
);

-- -----------------------------------------------------------------
-- Таблица 9 - likes
-- -----------------------------------------------------------------
drop table if exists likes;
create table likes(	
	id SERIAL primary key,
	user_id BIGINT  UNSIGNED not null,
	media_id BIGINT  UNSIGNED not null,
	created_at DATETIME default NOW(),
	
	foreign key (user_id) references users(id) on update cascade on delete cascade,	
	foreign key (media_id) references media(id) on update cascade on delete cascade
);

-- -----------------------------------------------------------------
-- Таблица 10 - `photo_albums`
-- -----------------------------------------------------------------
drop table if exists `photo_albums`;
create table `photo_albums`(	
	`id` SERIAL,
	`name` VARCHAR(255) default null,
	`user_id` BIGINT  UNSIGNED not null,
	
	foreign key (user_id) references users(id) on update cascade on delete cascade,
	primary key (`id`)
);

-- -----------------------------------------------------------------
-- Таблица 11 - `photo`
-- -----------------------------------------------------------------
drop table if exists `photo`;
create table `photo`(	
	id SERIAL primary key,
	`album_id` BIGINT  UNSIGNED not null,
	`media_id` BIGINT  UNSIGNED not null,
	
	foreign key (album_id) references photo_albums(id) on update cascade on delete cascade,
	foreign key (media_id) references media(id) on update cascade on delete cascade
);


-- =================================================================
/* Урок 3. Домашнее задание.
 * Написать cкрипт, добавляющий в БД vk, которую создали на 3 вебинаре, 3-4 новые таблицы 
 * (с перечнем полей, указанием индексов и внешних ключей).
 * 
 * Добавлены таблицы:
 * - подарки;
 * - черный список;
 * - подписка;
 * - анализ событий.
*/

-- -----------------------------------------------------------------
-- Таблица 12 (ДЗ - 1) - presents - "подарки"
-- -----------------------------------------------------------------
drop table if exists presents;
create table presents(	
	id SERIAL primary key,
	from_user_id BIGINT UNSIGNED not null,
	to_user_id BIGINT UNSIGNED not null,
	media_type_id BIGINT UNSIGNED not null,
	body TEXT,	
	filename VARCHAR(255),
	`size` INT,	
	presents_at DATETIME default NOW(),	 
	
	foreign key (media_type_id) references media_types(id) on update cascade on delete cascade,	
	foreign key (from_user_id) references users(id) on update cascade on delete cascade,
	foreign key (to_user_id) references users(id) on update cascade on delete cascade
	
);

-- -----------------------------------------------------------------
-- Таблица 13 (ДЗ - 2) - block_list - "черный список"
-- -----------------------------------------------------------------
drop table if exists block_list;
create table block_list(	
	initiator_user_id BIGINT UNSIGNED not null,
	target_user_id BIGINT UNSIGNED not null,
	`status` ENUM('locked', 'unlocked'),
	locked_at DATETIME default NOW(),	 
	unlocked_at DATETIME default NOW(),
	
	primary key (initiator_user_id, target_user_id),
	foreign key (initiator_user_id) references users(id) on update cascade on delete cascade,		
	foreign key (target_user_id) references users(id) on update cascade on delete cascade	
);

-- -----------------------------------------------------------------
-- Таблица 14 (ДЗ - 3) - subscribtion - "подписка"
-- -----------------------------------------------------------------
drop table if exists subscribtion;
create table subscription(
	id SERIAL primary key,
	who_to_user_id BIGINT UNSIGNED not null,
	from_user_id BIGINT UNSIGNED not null,
	`status` ENUM('subscribed', 'unsubscribed'),	
	subscribed_at DATETIME default NOW(),
	update_at DATETIME on update NOW(),
	
	foreign key (who_to_user_id) references users(id) on update cascade on delete cascade,
	foreign key (from_user_id) references users(id) on update cascade on delete cascade
	
);

-- -----------------------------------------------------------------
-- Таблица 15 (ДЗ - 4) - events_analytics - "анализ событий"
-- -----------------------------------------------------------------
drop table if exists events_analytics;
create table events_analytics(
	user_id BIGINT UNSIGNED not null primary key,	
	messages_id BIGINT UNSIGNED,
	messages_act ENUM('0', '1') not null,
	presents_id BIGINT UNSIGNED,
	presents_act ENUM('0', '1') not null,
	block_list_id BIGINT UNSIGNED,
	block_list_act ENUM('0', '1') not null,
	likes_id BIGINT UNSIGNED,
	likes_act ENUM('0', '1') not null,
	friend_requests_id BIGINT UNSIGNED,
	friend_requests_act ENUM('0', '1') not null,
	subscribtion_id BIGINT UNSIGNED,
	subscribtion_act ENUM('0', '1') not null,
	act_at DATETIME default NOW(),		
	
	foreign key (user_id) references users(id) on update cascade on delete cascade,
	foreign key (messages_id) references messages(to_user_id) on update cascade on delete cascade,
	foreign key (presents_id) references presents(to_user_id) on update cascade on delete cascade,
	foreign key (block_list_id) references block_list(initiator_user_id) on update cascade on delete cascade,
	foreign key (likes_id) references likes(id) on update cascade on delete cascade,
	foreign key (friend_requests_id) references friend_requests(initiator_user_id) on update cascade on delete cascade,
	foreign key (subscribtion_id) references subscription(who_to_user_id) on update cascade on delete cascade
);




























