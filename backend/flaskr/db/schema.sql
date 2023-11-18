DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS groups;
DROP TABLE IF EXISTS group_leaders;
DROP TABLE IF EXISTS group_moderators;
DROP TABLE IF EXISTS collect_sessions;
DROP TABLE IF EXISTS collect_session_entries;

CREATE TABLE users (
    username TEXT PRIMARY KEY NOT NULL UNIQUE,
    password TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    date_joined TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE groups (
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    date_created TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    creator TEXT NOT NULL,
    FOREIGN KEY (creator) REFERENCES users (username)
    PRIMARY KEY (name, creator)
);

CREATE TABLE group_moderators (
    group_name TEXT NOT NULL,
    group_creator TEXT NOT NULL,
    moderator TEXT NOT NULL,
    date_added TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (moderator) REFERENCES users (username),
    FOREIGN KEY (group_name, group_creator) REFERENCES groups (name, creator),
    PRIMARY KEY (group_name, group_creator, moderator)
);

CREATE TABLE collect_sessions (
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    date_created TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    due_date TEXT NOT NULL,
    group_name TEXT NOT NULL,
    group_creator TEXT NOT NULL,
    FOREIGN KEY (group_creator) REFERENCES users (username),
    FOREIGN KEY (group_name, group_creator) REFERENCES groups (name, creator),
    PRIMARY KEY (name, group_name, group_creator)
);

CREATE TABLE collect_session_entries (
    group_name TEXT NOT NULL,
    group_creator TEXT NOT NULL,
    session_name TEXT NOT NULL,
    member TEXT NOT NULL,
    paid BOOLEAN NOT NULL DEFAULT FALSE,
    date_paid TEXT,
    FOREIGN KEY (group_name, group_creator) REFERENCES groups (name, creator),
    FOREIGN KEY (group_name, group_creator, session_name) REFERENCES collect_sessions (group_name, group_creator, name),
    PRIMARY KEY (group_name, group_creator, session_name, member)
);

