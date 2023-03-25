create database smart_vocab_notebook;
use smart_vocab_notebook;
-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/mwOJxJ
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/mwOJxJ
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE `users` (
    `user_id` int auto_increment,
    `username` varchar(15)  NOT NULL unique,
    -- `passw` varchar(30)  NOT NULL ,
    PRIMARY KEY (
        `user_id`
    )
);

CREATE TABLE `lists` (
    `list_id` int  auto_increment ,
    `listname` varchar(20)  NOT NULL ,
    `user_id` int  NOT NULL ,
    PRIMARY KEY (
        `list_id`
    )
);

CREATE TABLE `sentences` (
    `sentences_id` int  auto_increment ,
    `sentences` varchar(200)  NOT NULL ,
    `meaning` varchar(50),
    `note` varchar(200),
    `word_start_pos` int  NOT NULL ,
    `word_end_pos` int  NOT NULL ,
    `list_id` int  NOT NULL ,
    PRIMARY KEY (
        `sentences_id`
    )
);

CREATE TABLE `classes` (
    `class_id` int  auto_increment ,
    `user_id` int  NOT NULL ,
    `classname` varchar(50)  NOT NULL ,
    PRIMARY KEY (
        `class_id`
    )
);

CREATE TABLE `teaching` (
    `class_id` int  NOT NULL ,
    `list_id` int  NOT NULL ,
    PRIMARY KEY (
        `class_id`,`list_id`
    )
);

CREATE TABLE `enrolment` (
    `user_id` int  NOT NULL ,
    `class_id` int  NOT NULL ,
    PRIMARY KEY (
        `user_id`,`class_id`
    )
);

ALTER TABLE `lists` ADD CONSTRAINT `fk_lists_user_id` FOREIGN KEY(`user_id`)
REFERENCES `users` (`user_id`);

ALTER TABLE `sentences` ADD CONSTRAINT `fk_sentences_list_id` FOREIGN KEY(`list_id`)
REFERENCES `lists` (`list_id`) on DELETE cascade;

ALTER TABLE `classes` ADD CONSTRAINT `fk_classes_user_id` FOREIGN KEY(`user_id`)
REFERENCES `users` (`user_id`);

ALTER TABLE `teaching` ADD CONSTRAINT `fk_teaching_class_id` FOREIGN KEY(`class_id`)
REFERENCES `classes` (`class_id`);

ALTER TABLE `teaching` ADD CONSTRAINT `fk_teaching_list_id` FOREIGN KEY(`list_id`)
REFERENCES `lists` (`list_id`);

ALTER TABLE `enrolment` ADD CONSTRAINT `fk_enrolment_user_id` FOREIGN KEY(`user_id`)
REFERENCES `users` (`user_id`);

ALTER TABLE `enrolment` ADD CONSTRAINT `fk_enrolment_class_id` FOREIGN KEY(`class_id`)
REFERENCES `classes` (`class_id`);

DELIMITER $$
CREATE TRIGGER Create_user_miror_and_intial_list
    AFTER INSERT ON auth_user FOR EACH ROW    
        BEGIN    
        	INSERT INTO users(user_id, username)
            VALUES(new.id, new.username);
           INSERT INTO lists(listname, user_id)
            VALUES('Danh sách đầu tiên', new.id);
        END;$$
DELIMITER ;